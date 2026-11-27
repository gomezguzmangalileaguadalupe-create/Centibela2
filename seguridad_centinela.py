"""Detección de frases de riesgo y mensajes de ayuda.

Es una lista de patrones: reconoce expresiones frecuentes, NO todas las formas de
pedir ayuda. No sustituye la atención de una persona ni envía alertas.
"""
from __future__ import annotations

import re
import unicodedata

LINEA_DE_LA_VIDA = "800 911 2000"

# Los patrones se comparan con texto en minúsculas, sin acentos (ñ -> n) ni signos.
CRISIS = (
    r"\b(quiero|quisiera|deseo|prefiero|preferiria) (ya )?(morir(me)?|estar muert[oa])\b",
    r"\bme (quiero|quisiera) (ya )?morir\b",
    r"\bganas de (morir(me)?|matarme|no seguir viviendo)\b",
    r"\bno (quiero|deseo|quisiera) (ya )?(seguir )?(vivir|viviendo)\b",
    r"\bno (quiero|quisiera) (volver a )?despertar\b",
    r"\b(quitarme la vida|(acabar|terminar) con mi vida)\b",
    r"\b(suicid\w*|matarme|me voy a matar|me quiero matar)\b",
    r"\b(hacerme dano|lastimarme a proposito|autolesion\w*)\b",
    r"\b(la|mi) vida (ya )?no tiene sentido\b",
    r"\bno (le )?(veo|encuentro) sentido a (la|mi) vida\b",
    r"\b(estarian|estaran) mejor sin mi\b",
    r"\b(quiero|quisiera) desaparecer\b",
)

URGENCIA = (
    r"\bme (cai|he caido|acabo de caer)\b",
    r"\bno (me )?(puedo|logro) levantar(me)?\b",
    r"\b(dolor|duele|opresion|presion|aprieta)( \w+){0,3} pecho\b",
    r"\bpecho( \w+){0,2} (duele|aprieta)\b",
    r"\b(no puedo|no logro|me cuesta( mucho)?( trabajo)?) respirar\b",
    r"\b(dificultad para respirar|me falta (el )?aire|me estoy ahogando|me ahogo)\b",
    r"\b(emergencia|auxilio|socorro)\b",
    r"\b(me desmaye|perdi el conocimiento|convulsion\w*)\b",
    r"\b(sangrando mucho|sangro mucho|mucha sangre)\b",
    r"\bno puedo mover (el |un |la |una |mi )?(brazo|pierna|cara|mano)\b",
    r"\btome (demasiadas|muchas) (pastillas|medicinas)\b",
)


def normalizar(texto):
    base = unicodedata.normalize("NFD", str(texto or "").lower())
    base = "".join(c for c in base if unicodedata.category(c) != "Mn")
    return " ".join(re.sub(r"[^a-z0-9 ]+", " ", base).split())


def detectar_riesgo(texto):
    """Devuelve 'crisis', 'urgencia' o None. La crisis tiene prioridad."""
    t = normalizar(texto)
    if any(re.search(p, t) for p in CRISIS):
        return "crisis"
    if any(re.search(p, t) for p in URGENCIA):
        return "urgencia"
    return None


def texto_urgencia():
    return ("Si estás en peligro o necesitas atención inmediata, pide ayuda a alguien cercano. "
            "En México, llama directamente al 911. CENTINELA no llama ni envía alertas por sí solo.")


def texto_crisis():
    return ("Siento que estés pasando por algo tan difícil. No tienes que enfrentarlo a solas. "
            "Busca ahora a alguien de confianza que te acompañe, o llámale. "
            "Si estás en peligro o podrías hacerte daño, llama al 911. "
            f"También puedes llamar a la Línea de la Vida, {LINEA_DE_LA_VIDA}. "
            "CENTINELA no llama ni avisa a nadie. ¿Hay alguien que pueda estar contigo ahora?")


def texto_seguimiento():
    return ("Quiero insistir en que busques apoyo de una persona ahora. Llama a alguien de confianza. "
            f"Si hay peligro, llama al 911. La Línea de la Vida es el {LINEA_DE_LA_VIDA}. "
            "CENTINELA no llama ni avisa a nadie.")


def ayuda_para(riesgo):
    return {"crisis": texto_crisis(), "urgencia": texto_urgencia()}.get(riesgo, "")


