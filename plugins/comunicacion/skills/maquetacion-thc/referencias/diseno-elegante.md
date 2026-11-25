# Diseño elegante: lo que funciona y lo que se evita

Sacado de las slides de DPM63 que el autor señaló como buenas (y de la que señaló como regular). Antes de maquetar una slide nueva, busca aquí si ya existe una receta; copia la receta en vez de improvisar. Si una receta no encaja, di por qué y propón otra; no caigas en «título grande + tarjetas verdes».

Referencias en el deck `cursos/ai-delivery/sesiones/dpm/sesion-1` (numeración del export de octubre de 2026; si cambia, busca por título).

## Qué hace buenas a esas slides

| Slide | Qué es | Por qué funciona |
|---|---|---|
| **72** «Bien entendido, un MVP…» | `contenido` con título pequeño y dos tarjetas grises con icono | Título de 1,7 rem en **peso 400** y negrita solo en la frase que importa. Fondo de tarjeta **gris sutil** (nada de verde). Cada tarjeta tiene una jerarquía de cuatro niveles: etiqueta mono diminuta en gris → icono de trazo → título en negrita → texto en gris, regular. La negrita funciona porque debajo hay texto más ligero que la sostiene. Mucho aire, solo verde oscuro y grises. |
| **65** «Landbot quería reducir…» | `lado-foto`, `lado: der`, foto en blanco y negro a sangre | Rompe la monotonía: una foto a sangre al lado de una slide de texto. Kicker mono arriba, título de 2 líneas, checklist con **solo la etiqueta en negrita** y el resto en regular. |
| **59** «Tenemos un roadmap con prioridades…» | `pregunta` sobre **verde claro**, frase de 3 rem en peso normal | El acento se usa como **fondo completo**, no como cajita, y el verde claro + verde oscuro dan una slide distinta de las blancas y las oscuras. Una sola palabra (o dos) con **subrayado de rotulador lima** a media altura de las letras, en mitad de la frase. Pie diminuto con una raya. |
| **49** «¿Para qué sirve el mapa?» | `figura` con un SVG: camino con tramos, destino, ramas descartadas con ✕ y notas a mano | Cuenta con un dibujo lo que con palabras sería un párrafo («decidimos qué hacer, qué no y en qué orden»). Pocos elementos, una línea gruesa que manda, el rosa solo en lo descartado, texto a mano muy corto. |
| **27** (y todas las de `pasos`) | `pasos` con menú persistente a la izquierda | El alumno ve siempre **dónde está** en el método; el paso activo en negrita, los demás atenuados sobre una foto difuminada. El contenido de cada slide queda a la derecha con su kicker y el paso actual. |

## Capa `p-*` del tema (lo que se usa de aquí en adelante)

Las recetas buenas están como clases **nuevas y aditivas** en `slides/tema/styles/patrones.css`, todas con el prefijo `p-`. Ninguna slide anterior las usa, así que no cambian lo vigente. **Slides nuevas o rehechas usan `p-*`; `.tarjeta`, `.cadena .eslabon` y `.cascada` son los estilos antiguos y no se usan en slides nuevas** (siguen existiendo para no romper decks anteriores). Nunca edites los estilos antiguos del tema. Muestra viva: `slides/tema/muestra-patrones.md` (`npx slidev slides/tema/muestra-patrones.md`).

| Clase | Para qué |
|---|---|
| `class: p-titulo-fino` (en la slide) | Título de 1,7 rem en peso 400; `**…**` en lo clave. `p-titulo-1-5` lo baja a 1,5 rem |
| `.p-grupo.p-2/.p-3/.p-4` + `.p-tarjeta` | Grupo de tarjetas grises con jerarquía: `.p-k` (etiqueta mono), `.p-ico` (icono de trazo), `<strong>` y texto regular |
| `.p-tarjeta.p-activa` | La única tarjeta con acento (verde claro) entre grises |
| `.p-chips` + `.p-chip` / `.p-activo` | Filas de chips grises, con uno solo activo |
| `layout: pregunta` + `class: p-pregunta`, `.p-resalte`, `.p-pie` | Pregunta con fondo de acento y subrayado de rotulador |
| `class: p-visual` en `figura` + `.p-nota` | SVG dibujado y notas a mano (texto del SVG con `style`, no con atributos) |
| `.p-sub`, `.p-aviso`, `.p-ico-s` | Subtítulo gris, aviso discreto, icono pequeño |

## Recetas

### 1. Tarjetas grises con icono (slide 72)

```html
---
layout: contenido
class: p-titulo-fino
kicker: "MVP · La idea central"
---

# Bien entendido, un MVP es una de las herramientas más potentes para **acelerar la entrega de valor**

<div class="p-grupo p-2">
  <div class="p-tarjeta">
    <span class="p-k">Premisa 1</span>
    <svg viewBox="0 0 64 64" class="p-ico"><!-- trazo, sin relleno --></svg>
    <strong>Construir es incierto</strong>
    <span>Incluso un desarrollo aparentemente sencillo puede complicarse…</span>
  </div>
  <!-- segunda tarjeta igual; una sola con `p-activa` si hay que destacar -->
</div>
```

Receta general para **cualquier grupo de 2 a 4 conceptos**: etiqueta mono → icono de trazo → título en negrita → texto regular en gris. Sustituye a las `.tarjeta` verdes.

### 2. Título fino con negrita solo en lo clave

`class: p-titulo-fino` y `# Frase que afirma algo **lo importante**`. Funciona en `contenido` y `figura`. Los títulos grandes en negrita son para separadores, portadas, mensajes y preguntas (ver «Patrones a evitar»).

### 3. Pregunta con fondo de acento y subrayado (slide 59)

```html
---
layout: pregunta
class: p-pregunta
---

Tenemos un roadmap con prioridades. ¿Ya podemos empezar a escribir <span class="p-resalte">tickets para desarrollo</span>?

<p class="p-pie">¿Sí o no? ¿Por qué?</p>
```

Subraya **una expresión de 1 a 4 palabras**, nunca la frase entera. El `p-resalte` sigue el salto de línea.

### 4. Un visual que cuenta el concepto (slide 49)

`figura` con `class: p-titulo-fino p-visual`, `alto: "300px"` y un SVG propio con `viewBox` (texto con `style="font-size:…"`, jamás con atributos: ver «Trampas»). Reglas del visual:
- Una **metáfora espacial** por slide: camino y destino, embudo, escalera, matriz, árbol, balanza, espiral, escala.
- Pocos elementos (≤ 10), **una línea o forma que domina** (verde oscuro, trazo grueso) y el resto en gris. Lima solo para el destino o lo elegido; rosa solo para lo descartado o el error.
- Etiquetas de 14 a 22 px en DM Sans; notas a mano (`p-nota`, 15–22 px, rosa) de **3 a 6 palabras**.
- Si hay una secuencia, `v-click` en cada capa.
Cuándo: cuando el contenido tiene **forma** (proceso, comparación de tamaño, jerarquía, evolución). Si es una definición o una lista de razones, no. Frecuencia: **un visual cada 3 o 4 slides**.

### 5. Menú persistente (slide 27)

Para cualquier **método o proceso que ocupe varias slides** (más de 3): `pasos` con `agenda` y `agendaTitulo` en el headmatter y `actual: N` en cada slide. La lista de pasos se escribe **una vez**; el nombre del paso es el que aparece también en la slide-índice. En cada slide del paso, un kicker + «N. Nombre del paso» ya los pone el layout; el título propio de la slide va debajo, a 1,5 o 1,7 rem.

### 6. Imagen a un lado (slide 65)

`lado-foto` con `lado: der` (o `izq`), `ancho: 34–46%`, foto de `imagenes-thc` o un recurso propio; el texto, con kicker mono, título de 2 líneas y lista corta con **etiqueta: texto**. Se alterna `izq` y `der` entre slides. Con capturas de producto: `ajuste: contain` y `fondo: sutil`. Es el recurso estándar para **definir, contextualizar un caso o romper una racha de slides blancas**.

## Ritmo: cuándo cambiar de formato

Cuando maquetes sin que te lo pidan, no te quedes en `contenido` y `figura`. Sobre cada 8 slides seguidas debe haber, **como mínimo**:
- 1 slide a sangre (`lado-foto`, `foto-mensaje` o `pregunta`/`mensaje` con fondo),
- 1 con un visual dibujado (receta 4),
- 1 con tarjetas grises y jerarquía (receta 1) o cifras,
- y como máximo 2 seguidas con la misma estructura (título + bloque a todo el ancho).
Antes de dar un bloque por terminado, lee la columna de layouts del plan y comprueba que no es una sucesión de títulos con una cosa debajo.

## Patrones a evitar

1. **Todo en negrita.** Tarjetas, chips, «thumbs», eslabones o títulos con **todo** el texto en negrita y nada más a su lado quedan feos. La negrita funciona como **cabeza de una jerarquía**: debajo o al lado hay texto de menos peso. Un elemento suelto lleva peso 500 como mucho (o DM Mono en minúsculas). Una cadena de cajas con una palabra cada una va en peso 500 y sin relleno de color.
2. **Verde claro (`#EAFFBF`) en muchos elementos.** Diez chips verdes (slide 62) cansan y se ven de «plantilla». Para elementos repetidos usa el **gris sutil** (`.tarjeta.sutil`, `--thc-gris-sutil`). El verde claro es un **acento puntual**: el elemento activo entre varios grises, la caja de la conclusión, un fondo completo de slide (receta 3). Si hay verde, que haya otro color alrededor (grises, verde oscuro, blanco) y que no cubra más del 20 % de la slide.
3. **Gris dentro del verde.** El texto gris sobre verde claro se lee mal. Dentro de una caja verde, texto en verde oscuro.
4. **Elementos con solo un título.** Una tarjeta o una caja con una sola etiqueta y nada más se ve vacía. O le sobra el contenedor (texto suelto) o le falta la segunda línea (descripción o dato).
5. **Títulos grandes en slides de contenido.** Hasta 1,7 rem, peso 400 con negrita en lo clave. El tamaño del tema (2,4 rem, negrita) es para portadas, separadores, mensajes y preguntas, donde el título **es** el contenido.
6. **Verde oscuro sobre verde oscuro, rosa en todo, fondos inventados.** Los fondos oscuros son siempre `--thc-verde-oscuro` (nunca un negro nuevo); el rosa solo para lo descartado, el error o las notas a mano.
7. **Slides de «título + una cosa»** repetidas: ver «Ritmo».

## Trampas técnicas descubiertas

- **Atributos SVG de fuente:** Slidev (UnoCSS en modo atributos) interpreta `font-size="15"` como una clase y lo convierte en `3,75rem`. En un SVG, pon el tamaño y el peso en `style="font-size:15px;font-weight:700"`; `fill`, `stroke` y `text-anchor` sí valen como atributos.
- **`figura`:** lo que va tras `::cuerpo::` comparte fila con el resto del `marco`; el pie va con `::pie::` (se renderiza en `.resto`) y el marco con `alto` suficiente para no tapar el pie.
- **`hide: true`** en el frontmatter oculta una slide sin borrarla; el export no la numera.
- **Slidev (dev) se queda con la lista antigua de slides** cuando cambia su número. Tras añadir o quitar slides, reiniciar `npm run slides` y recargar; si no, se ven slides mezcladas.
- Los estilos de sesión se cargan solo desde `sesion-N/style.css` (el que está junto al `slides.md` que se ejecuta), no desde la carpeta superior.
