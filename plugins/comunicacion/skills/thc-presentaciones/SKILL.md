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

**Cómo se ven** (de `diseno-elegante.md`):

- Títulos de contenido pequeños y finos (1,5–1,7 rem, peso 400) con negrita solo en la parte clave. Los títulos grandes y en negrita, solo en portada, separadores, mensajes y preguntas.
- Mucho blanco. Elementos repetidos sobre gris sutil (`#F4F6F5`) con esquinas de 18 px, sin bordes gruesos ni sombras.
- Jerarquía dentro de cada tarjeta: etiqueta en DM Mono → título en negrita → texto en gris.
- Verde claro solo para un elemento activo o un fondo de pregunta; verde oscuro para mensajes y separadores; lima para separadores y cifras.
- Permanent Marker solo en kicker de portada, preguntas, citas y callouts (máx. 20 % de la slide). Si se cambian las `fonts` del headmatter, incluye `serif: Permanent Marker`.
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