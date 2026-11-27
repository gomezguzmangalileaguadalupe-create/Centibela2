"""Estilos de la interfaz de CENTINELA IA."""

CSS = """
/* CENTINELA IA 2.13 — tema de sistema. Gradio aplica .dark según el dispositivo. */
:root {
    --cent-bg: #f7f7f2;
    --cent-surface: #ffffff;
    --cent-ink: #17324d;
    --cent-body: #334b55;
    --cent-muted: #526775;
    --cent-line: #dfe6e0;
    --cent-green: #245a51;
    --cent-green-hover: #19443c;
    --cent-accent: #d9aa73;
    --cent-mark-bg: #dcece6;
    --cent-hero: #e9f1ed;
    --cent-hero-line: #d5e8de;
    --cent-hero-ink: #183d37;
    --cent-tag: #e8f2ed;
    --cent-tag-ink: #204e45;
    --cent-warning: #fff0d4;
    --cent-warning-ink: #744500;
    --cent-success: #e5f2e5;
    --cent-success-ink: #215b30;
    --cent-help: #fff4f1;
    --cent-help-line: #ecd4ca;
    --cent-help-ink: #73322a;
    --cent-disclaimer: #fffdf7;
    --cent-disclaimer-line: #eee0be;
    --cent-disclaimer-ink: #664d26;
    --cent-camera-note: #fff5e7;
    --cent-camera-line: #ab6a32;
    --cent-camera-ink: #633d1a;
    --cent-camera-on: #e9f7ef;
    --cent-camera-on-line: #27755a;
    --cent-camera-on-ink: #1d4f3b;
    --cent-shadow: rgba(33,61,54,.055);
}
/* La clase .dark es añadida por Gradio cuando el navegador/sistema prefiere el modo oscuro.
   Este selector también sirve al forzar el tema mediante ?__theme=dark en las pruebas. */
:root.dark, .dark {
    --cent-bg: #101b24;
    --cent-surface: #1c2b35;
    --cent-ink: #f0f5f5;
    --cent-body: #d8e3e7;
    --cent-muted: #b8cbd1;
    --cent-line: #425564;
    --cent-green: #337d70;
    --cent-green-hover: #3c9484;
    --cent-accent: #ffcf92;
    --cent-mark-bg: #25463f;
    --cent-hero: #1c3937;
    --cent-hero-line: #3a6258;
    --cent-hero-ink: #f0f8f5;
    --cent-tag: #254d45;
    --cent-tag-ink: #e0faf2;
    --cent-warning: #55401e;
    --cent-warning-ink: #ffdeb3;
    --cent-success: #1d4936;
    --cent-success-ink: #c1f3d4;
    --cent-help: #452c2b;
    --cent-help-line: #95635b;
    --cent-help-ink: #ffe5df;
    --cent-disclaimer: #39351f;
    --cent-disclaimer-line: #82764e;
    --cent-disclaimer-ink: #fff0c9;
    --cent-camera-note: #3f3221;
    --cent-camera-line: #ac8751;
    --cent-camera-ink: #ffe6c2;
    --cent-camera-on: #1d4438;
    --cent-camera-on-line: #66b18b;
    --cent-camera-on-ink: #d3f7e2;
    --cent-shadow: rgba(0,0,0,.20);
}
.gradio-container {box-sizing:border-box; width:100% !important; min-width:0 !important;
    max-width:min(100%,1150px) !important; margin-inline:auto !important; font-size:18px !important;}
.gradio-container, body {background:var(--cent-bg) !important; color:var(--cent-ink) !important;}
.gradio-container label, .gradio-container input, .gradio-container textarea {font-size:1rem !important;}
.gradio-container button {min-height:54px !important; border-radius:14px !important; font-size:1rem !important; font-weight:650 !important;}
.gradio-container button.primary {background:var(--cent-green) !important; color:white !important; border-color:var(--cent-green) !important;}
.gradio-container button.primary:hover {background:var(--cent-green-hover) !important;}
.gradio-container [role="tab"] {min-height:53px; font-size:1rem !important;}
.gradio-container :focus-visible {outline:3px solid var(--cent-accent) !important; outline-offset:3px;}
.cent-brand {display:flex;align-items:center;gap:14px;padding:12px 0 14px;}
.cent-mark {display:grid;place-items:center;background:var(--cent-mark-bg);border-radius:18px;min-width:62px;height:62px;font-size:32px;}
.cent-brand h1 {font-size:2rem;line-height:1.15;margin:0;color:var(--cent-ink);}
.cent-brand p {font-size:1rem;color:var(--cent-muted);margin:2px 0;}
.cent-hero {border-radius:20px;background:var(--cent-hero);padding:24px;border:1px solid var(--cent-hero-line);margin:4px 0 14px;}
.cent-hero h2 {font-size:1.8rem;line-height:1.2;color:var(--cent-hero-ink);margin:0 0 10px;}
.cent-hero p {font-size:1.05rem;margin:0;line-height:1.5;color:var(--cent-body);}
.cent-grid {display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin:12px 0;}
.cent-card {background:var(--cent-surface);padding:22px;border:1px solid var(--cent-line);border-radius:18px;box-shadow:0 2px 5px var(--cent-shadow);color:var(--cent-body);}
.cent-card h3 {font-size:1.16rem;color:var(--cent-ink);margin:0 0 10px;}
.cent-card p {font-size:1rem;margin:8px 0;color:var(--cent-body);line-height:1.5;}
.cent-card strong {color:var(--cent-ink);}
.cent-card .cent-big {font-size:1.6rem;font-weight:750;color:var(--cent-ink);}
.cent-tag {font-size:.93rem;border-radius:999px;padding:5px 12px;background:var(--cent-tag);color:var(--cent-tag-ink);display:inline-block;font-weight:650;}
.cent-tag.warning {background:var(--cent-warning);color:var(--cent-warning-ink);}
.cent-tag.done {background:var(--cent-success);color:var(--cent-success-ink);}
.cent-muted {font-size:.94rem;color:var(--cent-muted);line-height:1.5;}
.cent-dose {display:flex;justify-content:space-between;align-items:center;gap:15px;padding:13px 0;border-bottom:1px solid var(--cent-line);}
.cent-dose:last-child {border-bottom:0;}
.cent-help {padding:12px 18px;background:var(--cent-help);border-radius:14px;border:1px solid var(--cent-help-line);color:var(--cent-help-ink);}
.cent-disclaimer {background:var(--cent-disclaimer);border:1px solid var(--cent-disclaimer-line);padding:14px 17px;border-radius:14px;color:var(--cent-disclaimer-ink);font-size:.92rem;line-height:1.5;}
.cent-section {padding-top:8px;font-size:1.35rem;color:var(--cent-ink);font-weight:750;}
.cent-video-shell {border-radius:18px;border:1px solid var(--cent-line);overflow:hidden;background:#142632;min-height:230px;display:grid;place-items:center;color:#eaf2f3;}
.cent-video-shell img {width:100%;height:auto;max-height:470px;display:block;object-fit:contain;background:#142632;}
.cent-video-placeholder {text-align:center;padding:54px 24px;line-height:1.6;font-size:1.08rem;}
.cent-video-placeholder strong {font-size:1.35rem;display:block;margin:8px 0;color:white;}
.cent-camera-note {padding:16px;border:2px solid var(--cent-camera-line);background:var(--cent-camera-note);color:var(--cent-camera-ink);border-radius:14px;line-height:1.5;}
.cent-camera-on {border:2px solid var(--cent-camera-on-line);background:var(--cent-camera-on);padding:12px;border-radius:14px;color:var(--cent-camera-on-ink);font-weight:700;}
.cent-session-bar {margin-bottom:8px;align-items:center;}
.cent-session-caption {font-weight:650;color:var(--cent-muted);margin:0;}
.gradio-container button.cent-logout {min-height:48px !important;}
@media(max-width:690px){.cent-grid{grid-template-columns:1fr}.cent-hero{padding:18px}.cent-brand h1{font-size:1.7rem}.cent-dose{align-items:start;flex-direction:column}.gradio-container{font-size:17px !important;}}

:root {--cent-bg:#faf6ee;--cent-green:#6b3543;--cent-green-hover:#542634;--cent-accent:#8c3547;}
.dark {--cent-bg:#171b25;--cent-green:#71394b;--cent-green-hover:#814356;--cent-accent:#ffc489;}
#adult-space {font-family:system-ui,sans-serif;}
#adult-space button,#adult-space label,#adult-space input,#adult-space textarea {font-size:1.125rem !important;}
#adult-space .cent-card {margin:.6rem 0;}
#adult-space .cent-card p,#adult-space .day-now p {font-size:1.16rem;line-height:1.55;}
#adult-space .day-next {font-weight:700;}
.day-now {display:flex;align-items:center;gap:1.25rem;padding:1.4rem;border-radius:1.2rem;}
.day-now.morning {background:#fff0cd;color:#392b15;}
.day-now.afternoon {background:#ffdfce;color:#48281d;}
.day-now.night {background:#302f4d;color:#fff5e4;}
.dark .day-now.morning {background:#453a27;color:#fff0cd;}
.dark .day-now.afternoon {background:#4c342f;color:#ffdfce;}
.dark .day-now.night {background:#34344e;color:#fff5e4;}
.day-now h2,.day-now p,.day-now strong {color:inherit !important;margin:.2rem 0;}
.day-now h2 {font-size:clamp(1.6rem,4vw,2.3rem);line-height:1.18;}
.day-now strong {font-size:1.45rem;}
.day-icon {font-size:clamp(2.4rem,7vw,4.5rem);line-height:1;}
.day-section {font-size:1.25rem;margin:1.2rem 0 .35rem;color:var(--cent-ink);}
@media(max-width:600px){.day-now{padding:1rem;gap:.8rem;}#adult-space .cent-card{padding:1rem;}}

#easy-tools {position:sticky;top:0;z-index:12;background:var(--cent-bg);padding:.25rem;}
#easy-tools button {min-width:0!important;flex:1 1 0!important;}
#adult-space.large-type :is(p,label,input,textarea,button,span,h3,legend) {font-size:1.45rem!important;line-height:1.45!important;}
#adult-space.large-type h2 {font-size:2rem!important;}
#single-mic {min-height:68px!important;}
#adult-tabs [role="tablist"], #adult-tabs .tab-wrapper {display:none!important;}
#adult-space button.menu-boton {min-height:96px!important;font-size:1.35rem!important;white-space:normal;}
@media(max-width:620px){#easy-tools {display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr));}#easy-tools button {white-space:normal;overflow-wrap:anywhere;padding:.3rem!important;}}

.weekly-table {overflow-x:auto; width:100%; max-width:100%; min-width:0; contain:inline-size; margin:1rem 0;}
.weekly-table table {width:100%; border-collapse:collapse; font-variant-numeric:tabular-nums;}
.weekly-table caption {text-align:left; padding:.35rem 0; font-weight:600;}
.weekly-table th,.weekly-table td {padding:.45rem .6rem; border-bottom:1px solid var(--cent-line); text-align:left;}
#detalle-evolucion .detalle-categoria {border-top:1px solid var(--cent-line);padding:.4rem 0;}
#detalle-evolucion summary {font-weight:700;cursor:pointer;color:var(--cent-ink);padding:.5rem .2rem;}
#detalle-evolucion caption {color:var(--cent-ink);font-size:1.05rem;margin:.35rem 0;}
#detalle-evolucion thead {background:var(--cent-mark-bg);color:var(--cent-ink);}
#detalle-evolucion td,#detalle-evolucion th {vertical-align:top;}
#resumen-evolucion h3 {font-size:1.4rem;margin:.25rem 0;}
#resumen-evolucion p {margin:.3rem 0;color:var(--cent-body);}
#resumen-evolucion .pista-deslizar {display:none;}
@media(max-width:640px){
    #resumen-evolucion .pista-deslizar {display:block;font-size:.95rem;}
    .weekly-chart .matplotlib {display:block!important;overflow-x:auto;overscroll-behavior-x:contain;}
    .weekly-chart .matplotlib img {display:block;width:690px!important;min-width:690px;max-width:none!important;height:auto!important;}
}
.weekly-chart > label.float {position:static !important; display:flex; width:fit-content; max-width:100%;
    margin:.55rem .75rem .2rem; background:transparent !important; color:var(--cent-ink) !important;
    box-shadow:none; font-weight:700;}
.cent-review {border-inline-start:5px solid var(--cent-accent); padding:.8rem 1rem; background:var(--cent-surface);}
.cent-review p {margin:.3rem 0 0; line-height:1.5;}
#perfil-portada {margin:clamp(.8rem,3vw,2.4rem) auto; width:100%; max-width:56rem;}
#perfil-portada h2 {font-size:clamp(1.7rem,4vw,2.45rem);line-height:1.16;margin:0 0 .45rem;color:var(--cent-ink);}
#perfil-portada p {color:var(--cent-body);line-height:1.5;}
#perfil-portada .perfil-opcion {box-sizing:border-box;border:1px solid var(--cent-line);border-radius:18px;
    background:var(--cent-surface);padding:clamp(1rem,3vw,1.5rem);justify-content:space-between;}
#perfil-portada h3 {margin:0 0 .35rem;font-size:1.28rem;color:var(--cent-ink);}
#perfil-portada .perfil-opcion button {min-height:58px !important;}
@media(max-width:640px){#perfil-portada .perfil-fila {flex-direction:column;}}
.aviso-principal,.aviso-contexto {color:var(--cent-body);background:var(--cent-surface);border:1px solid var(--cent-line);border-radius:14px;}
.aviso-principal {padding:clamp(.8rem,2vw,1.2rem);margin:.2rem 0 .3rem;}
.aviso-principal p,.aviso-contexto p {margin:.2rem 0;line-height:1.5;}
.aviso-principal strong,.aviso-contexto strong,.aviso-principal h2,.aviso-principal h3 {color:var(--cent-ink);}
.aviso-acciones {display:flex;flex-wrap:wrap;gap:.5rem;margin:.6rem 0 0;}
.aviso-acciones button {background:var(--cent-surface);color:var(--cent-ink);border:1px solid var(--cent-muted);
    padding:.45rem .9rem;border-radius:10px;font-weight:600;min-height:44px;cursor:pointer;}
.aviso-acciones button:focus-visible,.aviso-principal a:focus-visible {outline:3px solid var(--cent-accent);outline-offset:2px;}
.aviso-principal [hidden] {display:none !important;}
#aviso-reproductor audio {width:min(100%,30rem);margin-top:.7rem;}
#aviso-integral {max-width:76ch;margin:1rem 0 .2rem;overflow-wrap:anywhere;}
#aviso-integral h2 {margin:.6rem 0;font-size:1.4rem;}
#aviso-integral h3 {margin:.8rem 0 .2rem;font-size:1.1rem;}
#aviso-integral dt {font-weight:650;} #aviso-integral dd {margin:0 0 .4rem;}
#aviso-integral a {color:var(--cent-ink);text-decoration:underline;}
.aviso-contexto {padding:.65rem 1rem;border-inline-start:4px solid var(--cent-accent);margin:.25rem 0;}
#perfil-portada {margin:clamp(.35rem,1.2vw,1rem) auto;}
@media(max-width:640px){
    .aviso-principal{padding:.65rem .8rem;font-size:1rem;}
    .aviso-acciones{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);}
    .aviso-acciones button{padding:.25rem .4rem;line-height:1.25;}
    #perfil-portada .perfil-opcion{padding:0;border:0;background:transparent;min-width:0!important;}
    #perfil-portada .descripcion-perfil{display:none;}
    #perfil-portada .perfil-fila{gap:.55rem;}
    #perfil-portada .perfil-opcion button{width:100%;}
}

"""


