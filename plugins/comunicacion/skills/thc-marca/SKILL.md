---
name: thc-marca
description: Identidad visual de The Hero Camp (colores, tipografías, logos, doodles, fotografía). Úsala siempre que vayas a diseñar cualquier material con la marca THC: carruseles, presentaciones, posts, documentos, landings o piezas visuales.
---

# The Hero Camp · marca

Esta skill es la fuente de verdad del estilo visual de The Hero Camp. Las demás skills de THC (`thc-carrusel-caso`, `thc-presentaciones`) la usan.

Archivos de esta skill:

- `tokens.json`: colores y estilos de texto exactos.
- `tokens.css`: los mismos colores como variables CSS, listos para pegar.
- `logos/`: el logo en SVG en tres versiones (lima, verde oscuro, blanco).

## Cómo se ve la marca

Fondo verde muy oscuro o blanco, titulares grandes en DM Sans, un toque de lima y doodles hechos a mano (flechas con lazo, garabatos, coronas) que rompen la seriedad. Fotos documentales de equipos trabajando de verdad.

El concepto de marca tiene tres ideas:

- una hoja de ruta de crecimiento, no cursos sueltos;
- impacto real en la empresa, no temario;
- cercanía de mentor, no de escuela.

## Color

| Token | Hex | Uso |
| --- | --- | --- |
| verde-oscuro | `#003133` | Fondo oscuro por defecto. Encima: blanco y lima. |
| lima | `#98DA01` | Primario. Titulares cortos, palabras destacadas, doodles. Solo sobre verde oscuro o negro: sobre blanco no se lee. |
| verde-claro | `#EAFFBF` | Fondo claro de marca. Encima: verde oscuro o negro. |
| rosa | `#E83B83` | Acento. Fondos de slide de sección o de "problema", detalles. Texto blanco encima solo en tamaño grande. |
| amarillo | `#FFDA23` | Acento. Post-its, cinta adhesiva, detalles. Nunca como texto. |
| negro | `#1C2125` | Texto principal. |
| gris-oscuro | `#5C7069` | Texto de apoyo sobre blanco. |
| gris-medio | `#9DAFA9` | Texto de apoyo sobre oscuro. |
| gris-claro | `#C7D1CE` | Texto de apoyo sobre verde oscuro. |
| gris-sutil | `#F4F6F5` | Fondos secundarios. |
| blanco | `#FFFFFF` | Fondos y texto sobre oscuro o rosa. |

Rosa y amarillo nunca como color dominante de la misma pieza a la vez.

## Tipografía

- **DM Sans** (Google Fonts) para todo. Titulares en SemiBold 600 con tracking negativo (-3 o -4 px en tamaños grandes). Texto en Regular 400.
- **Permanent Marker** (Google Fonts), siempre en MAYÚSCULAS, para todo lo manuscrito: la frase corta encima del titular ("SESIÓN ESTRATÉGICA:", "EL RETO:"), los post-its, las notas a mano. Una frase manuscrita por pieza o slide, salvo en post-its.

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600&family=Permanent+Marker&display=swap">
```

Escala de la web (en px): H1 66/74, H2 40/46, H3 32/38, H4 24/30, Body L 18/28, Body M 16/26. Para piezas de redes los tamaños son mucho mayores: ver cada skill.

## Logo

Isotipo de dos formas redondeadas que dibujan una M/corona, con HERO CAMP debajo en mayúsculas escalonadas. Nunca lo redibujes: usa los SVG de `logos/`.

- `thc-logo-verde-oscuro.svg` sobre blanco, verde claro y gris sutil.
- `thc-logo-blanco.svg` sobre verde oscuro, negro y rosa.
- `thc-logo-lima.svg` sobre verde oscuro o negro, cuando el logo es protagonista (portadas, cierres).

Con el logo de otra empresa (co-branding): los dos a la misma altura, separados por un "×" en lima.

## Doodles

Trazo a mano, sin relleno, extremos redondeados: flechas con lazo, espirales, coronas, rayos, subrayados. En lima sobre oscuro, en verde oscuro o negro sobre claro, en blanco sobre rosa. Sirven para señalar, unir o dar ritmo, no para decorar por decorar. Se dibujan como SVG inline con `stroke-linecap="round"`.

## Fotografía

"Learning in action": fotos documentales de gente aprendiendo y construyendo. Pizarras, post-its, gente de pie explicando, equipos alrededor de una mesa. Luz natural, nada de banco de imágenes posado. Formatos:

- clavadas en un tablón: marco blanco de 14 px, rotación entre -6° y 6°, sombra suave, cinta amarilla semitransparente;
- a sangre, ocupando media pieza;
- con esquinas redondeadas.

## Lo que no es THC

Degradados, chips y etiquetas con mini textos, iconos de UI decorativos, emojis como viñetas, sombras duras, colores fuera de esta paleta, tipografías distintas de las dos de arriba.
