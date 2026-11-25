---
theme: thc
title: Muestra de patrones p-* del tema thc
layout: contenido
class: p-titulo-fino
kicker: "Patrones · tarjetas grises"
---

# Un grupo de tarjetas grises **con jerarquía**, sin verde y sin negrita total

<div class="p-grupo p-2">
  <div class="p-tarjeta">
    <span class="p-k">Premisa 1</span>
    <svg viewBox="0 0 64 64" class="p-ico"><rect x="10" y="10" width="44" height="44" rx="9"/><circle cx="24" cy="24" r="3" fill="currentColor"/><circle cx="40" cy="40" r="3" fill="currentColor"/></svg>
    <strong>Construir es incierto</strong>
    <span>Incluso un desarrollo aparentemente sencillo puede complicarse y alargarse.</span>
  </div>
  <div class="p-tarjeta p-activa">
    <span class="p-k">Premisa 2</span>
    <svg viewBox="0 0 64 64" class="p-ico"><circle cx="22" cy="22" r="9"/><circle cx="44" cy="26" r="7"/><path d="M6 54 C6 40 38 40 38 54"/></svg>
    <strong>Una tarjeta activa, la única verde</strong>
    <span>El verde claro es un acento puntual entre grises.</span>
  </div>
</div>

<div class="p-chips" style="margin-top:1.6rem"><span class="p-chip">Problema</span><span class="p-chip">Objetivos</span><span class="p-chip p-activo">Métricas</span><span class="p-chip">Alternativas</span></div>

---
layout: pregunta
class: p-pregunta
---

Tenemos un roadmap con prioridades. ¿Ya podemos empezar a escribir <span class="p-resalte">tickets para desarrollo</span>?

<p class="p-pie">¿Sí o no? ¿Por qué?</p>

---
layout: figura
class: p-titulo-fino p-visual
kicker: "Patrones · visual"
alto: "260px"
---

# Un visual cuenta lo que **tres frases** no

::cuerpo::

<svg viewBox="0 0 900 260" role="img" aria-label="Camino con dos tramos y un destino">
  <path d="M 60 200 C 260 200 300 100 480 100 C 640 100 700 60 820 50" fill="none" stroke="#003133" stroke-width="7" stroke-linecap="round"/>
  <path d="M 480 100 C 520 150 540 190 580 220" fill="none" stroke="#9dafa9" stroke-width="3.5" stroke-dasharray="3 9" stroke-linecap="round"/>
  <circle cx="60" cy="200" r="13" fill="#fff" stroke="#003133" stroke-width="5"/>
  <circle cx="820" cy="50" r="15" fill="#98da01" stroke="#003133" stroke-width="5"/>
  <text x="60" y="240" text-anchor="middle" fill="#003133" style="font-size:16px;font-weight:700">Estamos aquí</text>
  <text x="820" y="90" text-anchor="middle" fill="#003133" style="font-size:16px;font-weight:700">Objetivo</text>
  <text x="590" y="244" class="p-nota" style="font-size:18px" fill="#e83b83">esto no, ahora</text>
</svg>
