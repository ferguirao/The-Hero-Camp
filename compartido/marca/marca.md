# Marca The Hero Camp (rebranding)

> Extraído de las capturas del rebranding (`capturas/`), 6 oct 2026. Lo que no aparece de forma explícita está marcado como **(inferido)** o **(por confirmar)**.

## Concepto

**"Mismo ADN, nueva energía."** Une el dominio técnico del producto con la cercanía de quien sabe que las reglas están para entenderlas y luego romperlas con criterio. Una identidad de calidad para una comunidad que se atreve a **mancharse las manos** y liderar el cambio.

La combinación tipográfica busca **aportar criterio, reforzar la profesionalidad y equilibrar lo técnico con lo humano**. Los recursos visuales reflejan **el rastro del pensamiento creativo y la impronta humana** que transforma la estrategia en impacto real.

Encaja con el curso: el feedback de DPM valora justo "mancharse las manos y pensar".

## Color

### Marca

| Nombre | Hex | Rol | Uso |
|---|---|---|---|
| Verde Lima | `#98DA01` | Primario | Textos, ilustraciones |
| Verde oscuro | `#003133` | Marca oscuro | Fondos, textos, ilustraciones |
| Verde claro | `#EAFFBF` | Marca surface | Fondos |
| Rosa | `#E83B83` | Acento | Detalle de ilustraciones |
| Amarillo | `#FFDA23` | Acento | Detalle de ilustraciones |

### Neutros

| Nombre | Hex | Uso |
|---|---|---|
| Negro | `#1C2125` | Texto principal |
| Gris oscuro | `#5C7069` | Texto de apoyo |
| Gris medio | `#9DAFA9` | Texto de apoyo (subtítulos) |
| Gris claro | `#C7D1CE` | Texto de apoyo |
| Gris sutil | `#F4F6F5` | Fondo secundario (áreas o cajas) |
| Blanco | `#FFFFFF` | Fondos |

### Proporción

De más a menos presencia: **blanco** (dominante) → **verde oscuro** → **verde claro** → **verde lima** → **rosa** y **amarillo** (solo detalles) → neutros para texto y cajas.

### Variante morada (desconocida)

Los ejemplos de slides muestran una variante con fondo morado oscuro y acentos en rosa en lugar de lima. No está en la paleta y no se sabe cuándo se usa: no se aplica en el curso.

## Tipografía

| Fuente | Rol | Uso | Disponible en |
|---|---|---|---|
| **DM Sans** | Principal: rigor, legibilidad, estructura digital sólida | Títulos, subtítulos, body, links, labels | Google Fonts |
| **Permanent Marker** | Acento: dinámica y auténtica, trazo humano | Callouts: comentarios, tips, quotes, preguntas de reflexión | Google Fonts |
| **DM Mono** | Etiquetas técnicas | Kickers en mayúsculas ("CONCEPTO", "FOUNDATIONS"), numeración ("04."), roles ("Product Manager @ THC") | Google Fonts |

**Reglas de la fuente de acento:**
- En slides, **no más del 20 %** de la slide.
- Se puede girar **hasta 10°** en palabras o frases muy cortas.

### Escala

| Nivel | Fuente | Color sobre claro | Color sobre verde oscuro | Color sobre verde claro |
|---|---|---|---|---|
| Kicker | Mono pequeña | Gris medio | Gris medio | Gris medio |
| Headline | DM Sans negrita | Verde oscuro | Blanco | Verde oscuro |
| Sub | DM Sans regular | Gris medio | Gris medio | Gris medio |
| Large text | DM Sans | Negro o gris medio | Blanco o gris medio | Negro o gris medio |
| Body copy | DM Sans | Negro | Blanco | Negro |
| Callout | Acento | Verde lima | Verde lima | Verde oscuro |
| Footnotes | DM Sans pequeña | Gris medio | Gris medio | Gris medio |

## Recursos visuales

- **Doodles a mano:** flechas en espiral, rayos, corona, estrellas, destellos, nubes, corazones, remolinos, líneas que se enredan. En verde oscuro, con detalles puntuales en lima, amarillo o rosa. Acompañan títulos o señalan algo; nunca dominan la slide.
- **Ilustraciones de línea** en blanco y negro con un acento de color (persona saliendo de una caja, cohete con personas).
- **Fotos** con superposición verde oscuro para slides de concepto.
- **Retratos** en blanco y negro con marco dibujado a mano y un doodle (rayo) en el color de acento.
- **Logo:** símbolo (dos picos unidos) sobre el wordmark "HERO CAMP" con letras escalonadas; a veces con una corona dibujada encima. Versiones en blanco, lima, rosa y verde oscuro.

## Patrones de slide observados

| Patrón | Cómo es |
|---|---|
| Portada oscura | Fondo negro o verde oscuro; kicker en fuente de acento lima ("Sesión estratégica:"); título en DM Sans blanco; logo pequeño arriba o abajo a la derecha |
| Portada clara | Fondo blanco; doodle de flecha en lima; subtítulo gris; título DM Sans oscuro; logo arriba a la derecha |
| Portada con ilustración | Título grande DM Sans a la izquierda, ilustración de línea a la derecha |
| Separador de sección | Fondo lima (o rosa); garabato grande en verde oscuro en una esquina; "4. Título de la sección" abajo a la izquierda |
| Presentación de ponente | Fondo verde oscuro; "Nos acompañará"; nombre en acento lima; rol en mono; foto B/N con marco a mano y rayo |
| Contenido | Fondo blanco; título en acento con un trazo corto debajo; subtítulos DM Sans negrita y body pequeño; ilustración a la derecha; logo pequeño arriba a la derecha |
| Quote | Título DM Sans; texto; cita en acento lima; imagen de apoyo con destello |
| Kicker de sección | Etiqueta mono en mayúsculas arriba a la izquierda ("CONCEPTO", "RECURSOS VISUALES") |
| Apertura de capítulo | Fondo negro; número mono en gris + título DM Sans blanco abajo a la izquierda ("04. Recursos visuales") |

## Logo

Archivos en `logo/`, PNG con transparencia, en negro y en blanco:

| Archivo | Versión | Uso sugerido |
|---|---|---|
| `simbolo-*.png` | Solo el símbolo | Esquina de slides de contenido |
| `logo-horizontal-*.png` | Símbolo a la izquierda y "HERO CAMP" en una línea | Pies o cabeceras anchas |
| `logo-simbolo-arriba-*.png` | Símbolo encima de "HERO CAMP" en una línea | Portadas |
| `logo-apilado-*.png` | Símbolo encima de "HERO / CAMP" en dos líneas escalonadas | Portadas y cierres; esquina de portadas |

Para las versiones en color (lima, rosa, verde oscuro) se usa el PNG como máscara CSS (`mask-image`) con el color de marca de fondo; no hacen falta archivos por color.

## Lo que falta

- **Doodles** (SVG o PNG con transparencia) e **ilustraciones de línea**: solo hay capturas. Mientras no estén, los layouts dejan el hueco marcado.
