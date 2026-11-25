---
name: thc-presentaciones
description: "Cómo hacer presentaciones de formación y charlas de The Hero Camp (16:9) con el tema Slidev de Course-Builder, y cómo aplicar la marca a materiales de sesión, documentos y otras piezas que no sean webs ni carruseles."
---

# Presentaciones y materiales · The Hero Camp

Las slides de THC **no** heredan el estilo web de `thc-marca` (bordes de 2 px, sombras sólidas, titulares de 700 apretados): ese estilo es de la web. Las slides siguen el tema de Slidev del repo Course-Builder (`ferguirao/Course-Builder`): `slides/tema/` (layouts y estilos), `compartido/marca/marca.md` (guía de marca de slides) y las skills del repo `elegir-slide`, `maquetacion-thc`, `garabatos-thc`, `imagenes-thc` y `revisar-slides`. De `thc-marca` solo se toman los colores y las fuentes.

## Presentaciones de formación y charlas (16:9)

**Cómo se hacen:** en Slidev, dentro de Course-Builder, con `theme: thc` (`canvasWidth: 980`). Si el repo no está en la sesión, añádelo antes de maquetar; no reconstruyas el tema a mano en HTML.

1. Plan slide a slide con `elegir-slide` (forma del contenido, recurso, layout, receta, garabato).
2. Maqueta con `maquetacion-thc`: layouts del tema (`portada`, `separador`, `mensaje`, `contenido`, `figura`, `caso`, `comparar`, `lado-foto`, `foto-mensaje`, `pregunta`, `cita`, `ponente`…) y la capa de patrones `p-*` de `slides/tema/styles/patrones.css`.
3. Exporta con `npm run exportar -- <ruta>/slides.md`, revisa hojas de contacto con `revisar-slides` y entrega el PDF.

**Charlas (fuera de los cursos):** van en `charlas/<nombre>/` con su propio `slides.md` (solo headmatter + `src:` a `secciones/N-bloque.md`), `style.css` de la charla, `components/` con un `.vue` por cada visual dibujado y `public/img/`. Las imágenes se ponen con `<Im f="archivo.png" />` (respeta la ruta base del build) y los logos de empresa con `<MarcaLogo nombre="…" />` (SVG de `logos/`) o el icono oficial como imagen.

**Cómo se trabaja con Fer una charla:**

- Fer itera slide a slide y manda notas "en feo" (número de slide + texto o captura). Procesa todos los mensajes aunque lleguen mientras trabajas.
- Los números de slide pueden desfasarse en uno cuando has insertado slides: identifica cada slide por su contenido (lista las slides con `@slidev/parser`) antes de tocarla.
- Si Fer da el texto literal, úsalo tal cual. Si das tú la vuelta al texto: frases que explican qué pasó o qué muestra el dato, nunca eslóganes.
- Todo lo que aportes tú (ejemplos, etiquetas, cifras, frases, imágenes que quitas o añades) se dice explícitamente al final de la respuesta.
- Tras cada cambio, exporta a PNG solo las slides tocadas (`slidev export --format png --range N`) y míralas antes de publicar: desbordes, solapes, títulos que parten una expresión (arréglalo con `<span class="nb">`).
- Se publica como artifact: `slidev build --base ./`, quitar `404.html` y `_redirects`, y subir solo lo que cambia respecto al build anterior. Un artifact admite como mucho 512 archivos: borra los assets de builds antiguos antes de subir el nuevo (nunca los del build que está en vivo).
- PDF cuando lo pidan: PNG de cada slide unidos en un PDF de imágenes, sin números de página.

### Charlas: patrones visuales probados (deck Voltron, nov 2026)

- **Sin marca THC en las slides de contenido:** se oculta el símbolo de arriba a la derecha y la cabecera vacía, y el contenido va centrado en vertical. Sin kicker gris en mono: el contexto lo da el logo.
- **Logo de la empresa del caso arriba a la izquierda, encima del título:** icono de app a 34 px con esquinas de 9 px, o wordmark a 24 px. Nunca en la esquina derecha ni con texto debajo.
- **Título de contenido fino (peso 400) con negrita solo en la expresión clave.** Slides de "solo una frase" a 2,6 rem peso 400, máximo 85 % de ancho.
- **Permanent Marker en rosa** para preguntas al público ("¿Es un caso para multiproducto?"), transiciones ("Veamos otro ejemplo") y anotaciones sobre un visual ("← Acción"). En lima o blanco sobre fondo oscuro. Recto por defecto, sin inclinar; uno por slide.
- **Pasos de un método numerados en el título** con un círculo rosa y el número en Permanent Marker blanco (`.paso-n`). El subtítulo de la slide que abre el método dice cuántos pasos son.
- **Stickies** rectangulares `#fff3b0`, sombra suave y giro de ±1°, para barreras, soluciones o ideas sueltas. Un hueco sin resolver es un sticky con "?" en rosa y más grande.
- **Caso en dos slides, problema → solución.** Problema: `lado-foto` con una captura real del producto, logo arriba a la izquierda, el problema en una frase y una pregunta en marker. Solución: un visual dibujado (pasos + una comparación antes/después con cifra), no una lista.
- **Visuales dibujados como componentes Vue**, uno por idea: loops con una bola que recorre el ciclo, árboles de crecimiento, journeys con una barra por producto sobre las etapas, comparaciones con monedas o fichas. Lo que el ponente cuenta en dos tiempos se revela con clicks (`$clicks` de `useSlideContext` y `clicks: N` en el frontmatter).
- **Cajas de dato** sobre gris sutil, en rosa claro (`#fde6ee`, texto `#a3134f`) para el problema y en verde claro con borde lima para la solución.
- **Separadores** con hilos o garabatos de colores de marca (lima, rosa, amarillo) que se separan o se cruzan según la idea del bloque.
- **Fotos personales del equipo** como polaroid pegada al tablón: marco blanco, cinta amarilla translúcida, giro de 3° y el logo de la empresa como pegatina redonda.
- **Cierre:** foto a sangre con velo degradado desde la izquierda y el texto en blanco encima.
- **Logos reales siempre** (SVG oficial o icono de la app), no nombres escritos. Nada de fotos de personajes públicos descargadas de la web.

**Cómo se ven** (de `diseno-elegante.md`):

- Títulos de contenido pequeños y finos (1,5–1,7 rem, peso 400) con negrita solo en la parte clave. Los títulos grandes y en negrita, solo en portada, separadores, mensajes y preguntas.
- Mucho blanco. Elementos repetidos sobre gris sutil (`#F4F6F5`) con esquinas de 18 px, sin bordes gruesos ni sombras.
- Jerarquía dentro de cada tarjeta: etiqueta en DM Mono → título en negrita → texto en gris.
- Verde claro solo para un elemento activo o un fondo de pregunta; verde oscuro para mensajes y separadores; lima para separadores y cifras.
- Permanent Marker en kicker de portada, preguntas, citas, callouts, números de paso y anotaciones sobre visuales (máx. 20 % de la slide). Si se cambian las `fonts` del headmatter, incluye `serif: Permanent Marker`, y carga la fuente en local (`@font-face` con el `.woff2`) para que el PDF no la pierda.
- Imágenes reales (capturas, logos, fotos) por slot (`::foto::`, `::pantalla::`, `::cuerpo::`); visuales dibujados cuando el contenido tiene forma.
- Historias, citas largas y fuentes de la persona ponente, en las notas del orador.

### Tipos de slide de la marca (piezas fuera de Slidev)

Para piezas sueltas que no salen de Slidev (una imagen para un post, una slide en Google Slides). Pocos elementos por slide, mucho aire. Margen de 100 px a 1920 × 1080:

| Tipo | Cómo es |
| --- | --- |
| Portada | Fondo blanco o verde oscuro. Logo THC arriba a la derecha (unos 200 px de alto). Abajo a la izquierda, frase manuscrita ("SESIÓN ESTRATÉGICA:") y debajo el título en DM Sans SemiBold, 110–140 px, en una o dos líneas. Una flecha doodle lima que baja hacia la frase manuscrita. |
| Sección | Fondo rosa (o lima, o verde oscuro). Número y nombre de sección abajo a la izquierda, grande. Un grupo de doodles en negro o blanco ocupando la mitad derecha. Isotipo pequeño y translúcido abajo a la derecha. |
| Idea | Una frase grande centrada, 90–130 px, en negro sobre blanco o en blanco sobre verde oscuro. Una palabra en lima o subrayada con doodle. Nada más. |
| Contenido | Titular arriba a la izquierda, 70–80 px. Debajo, el esquema o la imagen que lo explica. Si hay texto, como mucho tres bloques cortos. |
| Persona | Fondo verde oscuro o negro. Foto en blanco y negro a la derecha con esquinas redondeadas y doodles lima encima. A la izquierda: frase manuscrita lima ("NOS ACOMPAÑARÁ"), nombre grande en blanco y cargo debajo. |
| Ejercicio | Fondo verde oscuro. "EJERCICIO:" manuscrito en lima y el nombre del ejercicio en blanco. Las instrucciones como post-its (amarillo, lima, rosa), una por post-it. |
| Cierre | Fondo verde oscuro, logo lima grande, una frase de despedida y el contacto. |

Reglas:

- Una idea por slide. Si un slide necesita más de tres bloques de texto, son dos slides.
- La frase manuscrita es Permanent Marker en MAYÚSCULAS y va encima del titular, nunca sola.
- Alterna fondos (blanco, verde oscuro, rosa para secciones) para marcar ritmo.
- Las fotos de sesión siguen el estilo "learning in action" de `thc-marca`.
- Nada de chips, etiquetas, badges, degradados ni iconos decorativos de UI.

`plantillas/presentacion.html` tiene estos tipos maquetados a 1920 × 1080; úsala solo para piezas sueltas, nunca para una presentación completa.

Si piden la presentación en otra herramienta (Google Slides, PowerPoint, un tipo de artifact de slides), aplica allí el estilo de Course-Builder descrito arriba (títulos finos, tarjetas grises, mucho blanco), no el estilo web de `thc-marca`.

## Otros materiales

- **Fichas de ejercicio y plantillas para alumnos** (A4 o pantalla): fondo blanco, cabecera con "EJERCICIO:" manuscrito en verde oscuro y título en DM Sans, campos con líneas finas gris claro y etiquetas en DM Sans SemiBold mayúsculas pequeñas. Logo verde oscuro pequeño abajo.
- **Documentos y propuestas**: fondo blanco, títulos en DM Sans SemiBold verde oscuro, texto en negro a 11–12 pt, un único acento lima en subrayados o separadores. Portada en verde oscuro con logo blanco.
- **Posts de una sola imagen**: mismas reglas que un slide de carrusel (ver `thc-carrusel-caso`), 1080 × 1350 o 1080 × 1080.
- **Webs, landings y emails**: usa la skill `thc-web`.

## Contenido

Las mismas reglas de escritura que en `thc-carrusel-caso`: titulares concretos, sin palabras huecas ni enumeraciones de tres por defecto, y nada inventado. Si aportas algo que no viene del material, dilo.