# Layouts, patrones y recetas del tema thc

## Layout por intención

| Quiero… | Layout | Props y slots |
|---|---|---|
| Abrir el deck | `portada` | kicker, subtítulo, `garabato` |
| Presentar a quien imparte, o despedirme | `ponente` (`cierre: true` al final) | retrato en `::foto::` |
| Fijar normas | `iconos` | 3 o 4 `items` con una línea |
| Mostrar el programa y dónde estamos | `ruta` | `actual`, `marca` |
| Abrir una sección | `separador` | `numero`, `subtitulo`, `color: lima \| oscuro \| claro`, `garabato`, `garabatoPos` |
| Definir, plantear la meta o contextualizar un caso con foto | `lado-foto` | `lado: izq \| der`, `ancho` (34–46 %), `fondo: sutil`, `ajuste: contain` para capturas; `::foto::` |
| Pregunta o frase sobre una foto | `foto-mensaje` | `velo`, `caja: true`; `::foto::` |
| Dejar una idea sola | `mensaje` | fondo oscuro; lo clave en `**negrita**` sale en lima |
| Pregunta al público sin foto | `pregunta` | con `class: p-pregunta` (receta 3) |
| Tarjetas, tablas, listas, cifras | `contenido` | `kicker`; patrones abajo |
| Diagrama, captura o visual dibujado | `figura` | `alto`, `fuente`; `::cuerpo::`, `::pie::` |
| Citar a alguien | `cita` | `autor`, `rol`; `::retrato::` |
| Método o proceso de más de 3 slides | `pasos` | `actual: N`; `agenda` y `agendaTitulo` en el headmatter |
| Caso real de una empresa | `caso` | `marca`, `anio`, `lugar`, `cifra`; `::pantalla::` |
| Contrastar dos cosas | `comparar` | `izq`, `der`; `::izq::`, `::der::` |
| Lanzar una dinámica | `hands-on` | `duracion`, `herramienta`, `codigo`, `plantilla`, `garabato` |
| Parar | `pausa` | `vuelta`, `duracion`; `::foto::` |
| Llamada de atención | `callout` | `garabato` (rayo por defecto) |
| Bloques y módulos de un curso largo | `apertura-bloque`, `separador-fase`, `portada-modulo` | ver `slides/tema/muestra.md` |
| Resumir | `contenido` con 3 `.tarjeta.oscura` | 3 ideas |

## Capa `p-*` (slides nuevas)

En `slides/tema/styles/patrones.css`. Es aditiva: las slides nuevas o rehechas usan `p-*`. Las clases antiguas (`.tarjeta`, `.cadena`, `.cascada`) siguen ahí para no romper presentaciones hechas; no se editan.

| Clase | Para qué |
|---|---|
| `class: p-titulo-fino` (en la slide) | Título de 1,7 rem, peso 400, `**…**` en lo clave. `p-titulo-1-5` lo baja a 1,5 rem |
| `.p-grupo.p-2 / .p-3 / .p-4` + `.p-tarjeta` | Tarjetas grises con jerarquía: `.p-k` (etiqueta mono), `.p-ico` (icono de trazo), `<strong>`, texto regular |
| `.p-tarjeta.p-activa` | La única tarjeta con acento (verde claro) entre grises |
| `.p-chips` + `.p-chip` / `.p-activo` | Fila de chips grises, uno activo |
| `layout: pregunta` + `class: p-pregunta`, `.p-resalte`, `.p-pie` | Pregunta con fondo de acento y subrayado de rotulador |
| `class: p-visual` en `figura` + `.p-nota` | SVG dibujado y notas a mano |
| `.p-sub`, `.p-aviso`, `.p-ico-s` | Subtítulo gris, aviso discreto, icono pequeño |

## Recetas

### 1. Tarjetas grises con icono

Para cualquier grupo de 2 a 4 conceptos.

```html
---
layout: contenido
class: p-titulo-fino
kicker: "MVP · La idea central"
---

# Bien entendido, un MVP sirve para **acelerar la entrega de valor**

<div class="p-grupo p-2">
  <div class="p-tarjeta">
    <span class="p-k">Premisa 1</span>
    <svg viewBox="0 0 64 64" class="p-ico"><!-- trazo, sin relleno --></svg>
    <strong>Construir es incierto</strong>
    <span>Incluso un desarrollo sencillo puede complicarse.</span>
  </div>
  <!-- segunda tarjeta igual; `p-activa` solo en una si hay que destacar -->
</div>
```

### 2. Título fino con negrita en lo clave

`class: p-titulo-fino` y `# Frase que afirma algo **lo importante**`. En `contenido` y `figura`.

### 3. Pregunta con fondo de acento y subrayado

```html
---
layout: pregunta
class: p-pregunta
---

Tenemos un roadmap con prioridades. ¿Ya podemos escribir <span class="p-resalte">tickets para desarrollo</span>?

<p class="p-pie">¿Sí o no? ¿Por qué?</p>
```

Se subraya una expresión de 1 a 4 palabras, nunca la frase entera.

### 4. Visual que cuenta el concepto

`figura` con `class: p-titulo-fino p-visual`, `alto: "300px"` y un SVG propio con `viewBox` (o un componente Vue en `components/`).

- Una metáfora espacial por slide: camino y destino, embudo, escalera, matriz, árbol, balanza, espiral, loop.
- Diez elementos como mucho. Una línea o forma manda (verde oscuro, trazo grueso); el resto en gris. Lima solo para el destino o lo elegido; rosa solo para lo descartado o el error.
- Etiquetas de 14 a 22 px en DM Sans; notas a mano (`.p-nota`, 15–22 px, rosa) de 3 a 6 palabras.
- Secuencia: `v-click` por capa.

Cuándo: cuando el contenido tiene forma (proceso, tamaño, jerarquía, evolución). Una definición o una lista de razones no se dibujan.

### 5. Menú persistente

Para un método de más de 3 slides: `pasos` con `agenda` en el headmatter y `actual: N` en cada slide. El layout pone el kicker y «N. Nombre del paso»; el título propio va debajo, a 1,5 o 1,7 rem. El nombre del paso es el mismo en la agenda y en la slide-índice.

### 6. Imagen a un lado

`lado-foto`, alternando `izq` y `der` entre slides. Kicker mono, título de dos líneas y lista corta con **etiqueta:** texto. Con capturas de producto, `ajuste: contain` y `fondo: sutil`. Es el recurso para definir, contextualizar un caso o romper una racha de slides blancas.

## Patrones de contenido antiguos (siguen valiendo dentro de `contenido`)

Clases en `base.css`. Línea en blanco entre HTML y Markdown.

- **Cifras:** `<div class="cifras"><div class="cifra"><span class="thc-kicker">Equipos que usan IA</span><span class="num">99 %</span><p>en al menos un flujo</p></div>…</div>`. `.cifra.rosa` para el dato que preocupa; fuente en `.thc-footnote`.
- **Cadena:** `.cadena` con `.eslabon` y `<span class="flecha">→</span>`; `.roto` en el eslabón o la flecha donde falla. De 3 a 6 eslabones, en peso 500.
- **Cascada:** `.cascada` con `<span class="et">Visión</span><div class="fila">…</div>`; `.actual` resalta el nivel que toca, `.oscura` lo ya explicado.
- **Tabla:** `<table>` con cabecera, hasta 7 filas, primera columna en negrita.
- **Listas:** `<div class="checklist">` (✓) o `<div class="numerada">` con lista Markdown.
- **Fórmula:** `<p class="formula">ICE = Impact × Confidence × Easiness</p>`.
- **Tarjetas antiguas:** `.tres` / `.cinco` con `.tarjeta`; `.tarjeta.oscura` para resúmenes, `.tarjeta.sutil` para lo secundario. En slides nuevas, mejor la receta 1.

## Densidad por tipo

Portada y separador, 1 frase. Mensaje, 1 idea. Tarjetas, 3 a 6 de 1 a 2 líneas. Tabla, hasta 7 filas. Figura, título más imagen. Lista, 3 a 6 puntos. Una slide, un foco: o figura, o tarjetas, o tabla, o cita.

## Color de texto por fondo en slides

| Nivel | Fuente | Sobre blanco | Sobre verde oscuro | Sobre verde claro |
|---|---|---|---|---|
| Kicker | DM Mono pequeña, mayúsculas | gris medio `#9DAFA9` | gris medio | gris medio |
| Título | DM Sans | verde oscuro `#003133` | blanco | verde oscuro |
| Subtítulo | DM Sans regular | gris medio | gris medio | gris medio |
| Cuerpo | DM Sans | negro `#1C2125` | blanco | negro |
| Manuscrito | Permanent Marker | rosa `#E83B83` (o lima) | lima o blanco | verde oscuro |
| Notas y fuentes | DM Sans pequeña | gris medio | gris medio | gris medio |

Proporción de color, de más a menos: blanco → verde oscuro → verde claro → lima → rosa y amarillo (solo detalles). Gris sutil `#F4F6F5` para cajas. Fondos oscuros siempre `--thc-verde-oscuro`.

## Logo

`<Logo>` del tema usa los PNG de `assets/`: símbolo (esquina de slides de contenido), horizontal (pies o cabeceras anchas), símbolo arriba (portadas), apilado (portadas y cierres). En color (lima, rosa, verde oscuro) se usa el PNG como máscara CSS (`mask-image`) con el color de fondo; no hacen falta archivos por color. Nunca en otro color que lima, verde oscuro o blanco.

## Patrones a evitar

1. **Todo en negrita.** La negrita es la cabeza de una jerarquía: necesita texto más ligero cerca. Un elemento suelto lleva peso 500 como mucho.
2. **Verde claro en muchos elementos.** Para lo repetido, gris sutil. El verde claro es un acento: el elemento activo, la conclusión o un fondo de slide entero. Máximo un 20 % de la slide.
3. **Gris dentro de verde claro.** Se lee mal; dentro de una caja verde, texto en verde oscuro.
4. **Cajas con solo un título.** O sobra la caja o falta la segunda línea.
5. **Títulos grandes en slides de contenido.** Hasta 1,7 rem, peso 400. El tamaño grande en negrita es para portada, separador, mensaje y pregunta.
6. **Fondos inventados, rosa en todo.** Oscuro siempre verde oscuro; rosa solo para lo descartado, el error o las notas a mano.
7. **Slides de «título + una cosa» seguidas** (ver `plan.md`).
