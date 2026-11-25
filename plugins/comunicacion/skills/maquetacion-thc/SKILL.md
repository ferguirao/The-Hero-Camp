---
name: maquetacion-thc
description: Qué tipo de slide usar y cómo maquetarlo en Slidev con el tema thc de The Hero Camp: layouts, cuándo usar cada uno, formatos, variedad, densidad, imágenes y trampas técnicas. Úsala al maquetar o rehacer slides, elegir un layout, añadir imágenes o diagramas, o escribir un layout nuevo. Se apoya en la skill slidev para la sintaxis general.
---

# Maquetación con el tema thc

Marca en `compartido/marca/marca.md`; tipos de slide con su layout en `cursos/ai-delivery/sesiones/dpm/catalogo-slides.md`; código en `slides/tema/`. Sintaxis general de Slidev: skill `slidev`.

> Qué slide usar en cada caso y cómo variarlas lo decide la skill `elegir-slide` (plan slide a slide, con reglas de diversidad). Esta skill explica cómo se construye cada una.

## Antes de maquetar: diseño elegante y patrones a evitar

Lee `referencias/diseno-elegante.md`. Las recetas están como clases `p-*` en `slides/tema/styles/patrones.css` (capa aditiva: **úsala siempre en slides nuevas y no toques los estilos antiguos del tema** — `.tarjeta`, `.cadena`, `.cascada` — porque lo usan decks ya hechos). Resumen:

- **Título de contenido pequeño y fino:** 1,5 a 1,7 rem, peso 400, negrita solo en la frase clave. Los títulos grandes en negrita son solo para portadas, separadores, mensajes y preguntas.
- **Jerarquía dentro de cada grupo:** etiqueta mono → icono de trazo → título en negrita → texto regular en gris. La negrita solo funciona si hay texto más ligero cerca.
- **Color:** el fondo de los elementos repetidos es el **gris sutil**; el verde claro es un acento puntual (un elemento activo, una conclusión o un fondo de slide entero). Sin gris dentro de verde. Fondos oscuros siempre `--thc-verde-oscuro`.
- **Formato:** alterna. Cada 8 slides, al menos una a sangre (foto al lado, foto con frase, pregunta con fondo), un visual dibujado y un grupo de tarjetas con jerarquía; nunca más de 2 seguidas con la estructura «título + un bloque».
- **Visual:** si el contenido tiene forma (camino, embudo, escalera, matriz, árbol), se dibuja; uno cada 3 o 4 slides.
- **Proceso de varias slides:** `pasos` con menú persistente a la izquierda.

## Elegir layout por intención

| Quiero… | Layout | Notas |
|---|---|---|
| Abrir el deck | `portada` | kicker y subtítulo |
| Presentar a quien imparte, o despedirme | `ponente` (`cierre: true` al final) | retrato por `::foto::` |
| Fijar normas | `iconos` | 4 iconos con una línea |
| Mostrar el programa y dónde estamos | `ruta` | `actual` y `marca` |
| Abrir una sección | `separador` | `numero`, `subtitulo`, `color: lima|oscuro|claro`; el título, a la derecha del número y en negrita (lo pone el layout) |
| Plantear la meta o definir con foto | `lado-foto` | `lado`, `ancho`, `fondo`, `ajuste` |
| Lanzar una pregunta o frase sobre una foto | `foto-mensaje` | `velo`, `caja`; sin foto, `mensaje` |
| Dejar una idea sola | `mensaje` | fondo oscuro, lo clave en negrita (sale en lima) |
| Explicar con tarjetas, tablas o listas | `contenido` | clases `.tres`, `.cinco`, `.tarjeta`, `.checklist`, `.numerada`, `.formula` |
| Enseñar un diagrama o captura | `figura` | título afirma; imagen en `::cuerpo::`, extras en `::pie::`, `fuente` |
| Citar a alguien | `cita` | `autor`, `rol`, `::retrato::` |
| Seguir un proceso por pasos | `pasos` | `actual`, y `agenda`/`agendaTitulo` en el headmatter |
| Enseñar un caso real | `caso` | `marca`, `anio`, `lugar`, `cifra`, `::pantalla::` |
| Contrastar dos cosas | `comparar` | `izq`, `der`, `::izq::`, `::der::` |
| Lanzar una dinámica | `hands-on` | `duracion`, `herramienta`, `codigo`, `plantilla` |
| Parar | `pausa` | `vuelta`, `duracion`, foto por `::foto::` |
| Resumir | `contenido` con 3 tarjetas oscuras (`.tarjeta.oscura`) | 3 ideas |
| Módulo del macrocurso | `apertura-bloque`, `separador-fase`, `portada-modulo`, `pregunta`, `callout` | ver `slides/tema/muestra.md` |

## Variedad y ritmo

- Nunca más de 3 slides seguidas con el mismo layout, salvo `pasos` (es la agenda y se repite a propósito).
- Alterna densidad: tras 2 o 3 slides de contenido, una de foto, una pregunta o un caso.
- Una slide, un foco: o una figura, o tarjetas, o una tabla, o una cita; no dos a la vez.
- Una pausa visual (foto con una frase) cada 8 a 12 slides de contenido.
- Slide de pregunta o foto después de cada bloque ("¿Preguntas?").

## Densidad por tipo

Portada y separador, 1 frase. Mensaje, 1 idea. Tarjetas, 3 a 6 de 1 a 2 líneas. Tabla, hasta 7 filas. Figura, solo el título más la imagen. Lista, 3 a 6 puntos. Nada por debajo de 0,7 rem en pantalla; si no cabe, se divide.

## Marca

- Colores: lima `#98DA01`, verde oscuro `#003133`, verde claro `#EAFFBF`, acentos rosa `#E83B83` y amarillo `#FFDA23`, neutros. El rosa solo para marcas de "no" o interrogación.
- Tipografía: DM Sans para todo; DM Mono para kickers y fuentes; Permanent Marker solo en callouts, citas, preguntas, "Hands on" y kicker de portada (máx. 20 % de la slide).
- Garabatos: ya existen (`compartido/marca/ilustraciones`, índice en `indice.json`). Qué poner y dónde lo decide la skill `garabatos-thc`; en los layouts es la prop `garabato`. No inventes ilustraciones nuevas.
- El logo se pone como símbolo en una esquina; nunca recolorear fuera de lima, verde oscuro o blanco.

## Imágenes y diagramas

- Rutas relativas a la sección y **siempre por slot** dentro de layouts (`::foto::`, `::cuerpo::`, `::pantalla::`, `::retrato::`); como atributo de frontmatter no se resuelven.
- Foto de fondo: `foto-mensaje` con velo oscuro; sin velo solo si la foto ya es oscura o muy limpia.
- Diagramas de terceros: se acreditan en `fuente`. Siempre que se pueda, **reconstruir** los sencillos (cascadas, cadenas, tablas) en HTML y tokens de marca en vez de pegar la captura.
- Fotos nuevas: de bibliotecas libres (skill `imagenes-thc`: Pexels, Unsplash, Pixabay), con su crédito en `assets/ORIGEN.md`. Las imágenes de terceros ya extraídas valen solo para uso interno de formación.
- Máximo 1600 px de lado en assets.

## Trampas técnicas

- **Atributos de fuente en SVG:** Slidev los convierte en clases enormes. El tamaño y el peso del texto de un SVG van en `style="…"` (más en `referencias/diseno-elegante.md`).
- Un `</div>` indentado detrás de una lista Markdown se traga el cierre; cierra los `<div>` sin indentación y deja línea en blanco entre HTML y listas.
- Contenido extra tras `::cuerpo::` en `figura` hay que ponerlo en `::pie::`.
- La clave `pasos` en un headmatter choca con la prop del layout `ruta`; para la agenda lateral se usa `agenda`.
- `src:` del primer slide va en el headmatter para no generar una slide vacía.
- Cada archivo `src` se compone de slides separadas por `---`; el primero no necesita línea previa.
- `slidev build` falla (minificador de v53); se previsualiza y se exporta.

## Espacios y ritmo vertical

El fallo más común al maquetar es apelotonar: título pegado al contenido, tarjetas pegadas a la nota de abajo, un párrafo sin aire sobre la lista. El tema ya fija el ritmo (en `base.css`); no lo encojas por meter más.

- **Título → contenido:** al menos 1,5 rem. Los márgenes entre bloques se colapsan, así que un `margin-top` pequeño en línea no lo reduce.
- **Entre bloques:** 1 a 1,3 rem. **Entre tarjetas:** 0,8 a 1 rem. **Notas y fuentes (`thc-footnote`):** 1,3 rem sobre lo anterior.
- **Dentro de una tarjeta:** relleno de 1 a 1,2 rem; el título de la tarjeta y su texto, 0,35 rem.
- **Mensaje sobre foto:** título y subtexto separados 1,1 rem, y la caja con relleno amplio (2 × 2,8 rem).
- **Mucho texto:** no aprietes los espacios. Usa `class="denso"` (baja el cuerpo un punto), divide en dos slides o pasa a tarjetas. Si no cabe con aire, sobra contenido.
- **Alineación:** en filas de iconos o tarjetas, los elementos arrancan a la misma altura (`align-items: flex-start`), no centrados con alturas desiguales.
- **Margen inferior:** deja al menos 2,5 rem libres abajo; nada pegado al borde ni al logo.

Se comprueba mirando la hoja de contacto: si algo "respira poco", sube el espacio en vez de bajar el texto.

## Saltos de línea en títulos

El tema ya equilibra las líneas de títulos y mensajes (`text-wrap: balance`), así que no queda una palabra suelta. Equilibrar no entiende el sentido, y a veces parte por un sitio raro. Cuando una frase tiene dos partes (afirmación y pregunta, por ejemplo), usa:

- `<span class="linea">¿Y el valor?</span>`: la segunda parte empieza en línea nueva y va entera.
- `<span class="nb">¿Y el valor?</span>`: la expresión no se parte nunca, pero el salto lo decide el navegador.

Se mira en la hoja de contacto, no a ojo en el código: depende del ancho. No uses `<br>` ni espacios duros; rompen al cambiar de layout. Con negritas en Markdown, mete el `**…**` dentro del span.

## Flujo de maquetación

1. Esqueleto aprobado (skill `arquitectura-de-contenido`).
2. Una sección por archivo en `secciones/`, la sesión importa las secciones con `src`.
3. Exportar a PNG, montar hojas de contacto de 6 slides y revisarlas con la skill `revisar-slides`.
4. Arreglar y repetir hasta que no haya desbordes ni huecos.
