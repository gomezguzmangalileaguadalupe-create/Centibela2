"""Pruebas automáticas de CENTINELA IA. Usan una base temporal: no tocan el caso de demostración."""
import sqlite3
import tempfile
import unittest
from pathlib import Path

import app
import datos_demo_centinela as demo
import seguridad_centinela as seguridad


class Riesgo(unittest.TestCase):
    def test_crisis(self):
        for frase in ("me quiero morir", "Ya no quiero vivir.", "quisiera estar muerta",
                      "he pensado en suicidarme", "tengo ganas de morirme", "estarían mejor sin mí", "quiero desaparecer"):
            with self.subTest(frase=frase):
                self.assertEqual(seguridad.detectar_riesgo(frase), "crisis")

    def test_urgencia(self):
        for frase in ("me caí", "me duele mucho el pecho", "tengo dolor en el pecho", "no puedo respirar",
                      "me falta el aire", "me tomé muchas pastillas", "auxilio"):
            with self.subTest(frase=frase):
                self.assertEqual(seguridad.detectar_riesgo(frase), "urgencia")

    def test_sin_riesgo(self):
        for frase in ("me muero de risa", "quiero vivir en Coyoacán", "no quiero ver la tele",
                      "solo quiero saber el clima", "me gusta pintar", ""):
            with self.subTest(frase=frase):
                self.assertIsNone(seguridad.detectar_riesgo(frase))


class ConBase(unittest.TestCase):
    def setUp(self):
        self.carpeta = tempfile.TemporaryDirectory()
        self.anterior = app.DB_PATH
        self.addCleanup(self.carpeta.cleanup)
        self.addCleanup(setattr, app, "DB_PATH", self.anterior)
        entorno = demo.os.environ.get("CENTINELA_DB")
        self.addCleanup(lambda: demo.os.environ.__setitem__("CENTINELA_DB", entorno)
                        if entorno is not None else demo.os.environ.pop("CENTINELA_DB", None))
        demo.cargar_escenario("ana", Path(self.carpeta.name) / "centinela_demo_pruebas.sqlite3")
        # Se omite el control de perfil: estas pruebas no abren una sesión del navegador.
        original = app.guard
        app.guard = lambda *args: None
        self.addCleanup(setattr, app, "guard", original)


class Asistente(ConBase):
    def test_respuestas_de_riesgo(self):
        self.assertIn(seguridad.LINEA_DE_LA_VIDA, app.assistant_answer("me quiero morir"))
        self.assertIn("911", app.assistant_answer("no puedo respirar"))

    def test_seguimiento_despues_de_crisis(self):
        historial = [{"role": "user", "content": "me quiero morir"}, {"role": "assistant", "content": "..."}]
        self.assertEqual(app.assistant_answer("no hay nadie", historial), seguridad.texto_seguimiento())

    def test_palabras_completas(self):
        self.assertNotIn("Me gusta que quieras conversar", app.assistant_answer("solo quiero saber el clima"))
        self.assertNotIn("buscar lugares", app.assistant_answer("cuéntame acerca de las aves"))
        self.assertIn("Me gusta que quieras conversar", app.assistant_answer("me siento muy sola"))
        self.assertIn("buscar lugares", app.assistant_answer("hay algún parque cerca de mí"))


class Datos(ConBase):
    def test_la_conexion_se_cierra(self):
        with app.database() as conexion:
            conexion.execute("SELECT 1")
        with self.assertRaises(sqlite3.ProgrammingError):
            conexion.execute("SELECT 1")

    def test_un_error_revierte_los_cambios(self):
        with self.assertRaises(RuntimeError):
            with app.database() as conexion:
                conexion.execute("UPDATE person SET display_name='Otra' WHERE id=1")
                raise RuntimeError
        self.assertEqual(app.person()["display_name"], "Ana")

    def test_marcar_y_deshacer_actividad(self):
        meta = app.scheduled_goals(app.now().date())[0]
        veces = lambda: int(app.activity_counts().set_index("Actividad").loc[meta["title"], "Veces realizada"])
        antes = veces()
        app.mark_activity_done(str(meta["id"]), None)
        app.mark_activity_done(str(meta["id"]), None)
        self.assertEqual(veces(), antes + 1)
        app.undo_activity(str(meta["id"]), None)
        self.assertEqual(veces(), antes)

    def test_bitacora_no_se_comparte_sin_permiso(self):
        self.assertFalse(app.pref_enabled("Sintomas"))
        resultado = app.save_symptoms("Mal", ["Mareo"], "", "nota-privada", None)
        self.assertIn("Guardado", resultado[0])
        oculto, _ = app.informe_cuidador(app.evolucion.HOY)
        self.assertNotIn("nota-privada", oculto.detalle)
        self.assertNotIn("Sintomas", oculto.graficas)

    def test_compartir_y_retirar_permiso(self):
        app.save_symptoms("Bien", ["Tos"], "", "nota-compartida", None)
        app.save_prefs(["Sintomas"], None)
        visible, _ = app.informe_cuidador(app.evolucion.HOY)
        self.assertIn("nota-compartida", visible.detalle)
        self.assertIsNotNone(visible.graficas["Sintomas"])
        self.assertNotIn("Metas", visible.graficas)
        app.save_prefs([], None)
        oculto, _ = app.informe_cuidador(app.evolucion.HOY)
        self.assertNotIn("nota-compartida", oculto.detalle)

    def test_bitacora_avisa_si_hay_riesgo(self):
        resultado = app.save_symptoms("Muy mal", [], "", "ya no quiero vivir", None)
        self.assertIn(seguridad.LINEA_DE_LA_VIDA, resultado[0])


class BitacoraSimulada(ConBase):
    def test_cubre_mas_de_un_mes_sin_duplicar_ni_compartir(self):
        app.save_symptoms("Bien", [], "", "anotación propia", None)
        self.assertEqual(demo.sembrar_bitacora(app), 35)
        self.assertEqual(demo.sembrar_bitacora(app), 0)
        filas = app.sql_rows("SELECT stamp,note FROM symptom_log")
        simuladas = [f for f in filas if f["note"].startswith("(Dato simulado)")]
        self.assertEqual(len({f["stamp"][:10] for f in simuladas}), 35)
        self.assertLess(max(f["stamp"][:10] for f in simuladas), app.now().date().isoformat())
        self.assertEqual(len(filas), 36)
        self.assertFalse(app.pref_enabled("Sintomas"))


class Interfaz(ConBase):
    def test_la_interfaz_se_construye(self):
        self.assertIsNotNone(app.build_app())


if __name__ == "__main__":
    unittest.main()


