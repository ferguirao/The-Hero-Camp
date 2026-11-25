# Patrones de contenido (HTML dentro de `contenido`)

Clases en `slides/tema/styles/base.css`. Siempre con línea en blanco entre HTML y Markdown.

## Cifras (`.cifras`)
```html
<div class="cifras">
  <div class="cifra"><span class="thc-kicker">Equipos que usan IA</span><span class="num">99 %</span><p>en al menos un flujo de trabajo</p></div>
  <div class="cifra"><span class="thc-kicker">Dicen entregar más rápido</span><span class="num">80 %</span><p>pero el cliente no lo nota</p></div>
</div>
```
`.cifra.rosa` para el dato que preocupa. Fuente en `.thc-footnote` debajo.

## Cadena (`.cadena`)
```html
<div class="cadena">
  <div class="eslabon">Comercial</div><span class="flecha">→</span>
  <div class="eslabon">Producto</div><span class="flecha roto">→</span>
  <div class="eslabon roto">Decisión</div>
</div>
```
`.roto` marca el eslabón o la flecha donde el proceso falla. De 3 a 6 eslabones.

## Cascada (`.cascada`)
```html
<div class="cascada">
  <span class="et">Visión</span><div class="fila oscura">Entretener al mundo</div>
  <span class="et">Roadmap</span><div class="fila actual">Estamos aquí</div>
  <span class="et">Backlog</span><div class="fila">Corto plazo</div>
</div>
```
Niveles de lo general a lo concreto; `.actual` resalta el que toca; `.oscura` lo ya explicado.

## Tres columnas "qué es / ejemplo / cuándo"
```html
<div class="tres">
  <div class="tarjeta"><strong>¿Qué es?</strong>…</div>
  <div class="tarjeta sutil"><strong>Ejemplo</strong>…</div>
  <div class="tarjeta"><strong>¿Cuándo utilizarlo?</strong>…</div>
</div>
```

## Tarjetas numeradas / paralelas
`.tres` o `.cinco` con `.tarjeta`; `.tarjeta.oscura` para resúmenes; `.tarjeta.sutil` para lo secundario.

## Tabla
`<table>` con cabecera; hasta 7 filas; primera columna en negrita.

## Lista con marca
`<div class="checklist">` con una lista Markdown (✓), o `<div class="numerada">` con lista numerada.

## Fórmula
`<p class="formula">ICE = Impact × Confidence × Easiness</p>`

## Ejemplos reales en el repo
DPM: `cursos/ai-delivery/sesiones/dpm/secciones/` (cascada en `s1-01`, `s1-04`, `s2-01`; cadena en `s2-04`; tres columnas en `s2-03`; tabla en `s1-01`, `s2-01`).
