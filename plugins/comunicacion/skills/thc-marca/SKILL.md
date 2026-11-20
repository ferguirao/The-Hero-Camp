---
name: thc-marca
description: Sistema visual completo de The Hero Camp (color por fondo, tipografía y pesos, botones, líneas, espaciado, doodles, fotos, logo). Úsala SIEMPRE antes de diseñar cualquier pieza con la marca THC: web, landing, email, carrusel, presentación, documento o post.
---

# The Hero Camp · sistema visual

Esta skill es la fuente de verdad. Aplica sus reglas al pie de la letra: casi todo lo que hace que algo "parezca THC" está en los detalles (pesos, botones sin redondeo, doodles, qué color va sobre qué fondo). Ante la duda, mira `referencias/si/` y evita lo que hay en `referencias/no/`.

Las demás skills de THC (`thc-carrusel-caso`, `thc-presentaciones`) parten de esta.

## 0. Antes de empezar: copia esto tal cual

No aproximes colores ni cambies fuentes. Pega este bloque al principio de cualquier HTML o CSS:

```css
@import url("https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600&family=Permanent+Marker&display=swap");

:root {
  /* marca */
  --verde-oscuro: #003133;   /* fondo oscuro principal y texto oscuro */
  --lima:         #98DA01;   /* acento y botón principal */
  --rosa:         #E83B83;   /* pastilla de palabra destacada, acentos */
  --amarillo:     #FFDA23;   /* post-its y cinta, nunca texto */
  --verde-claro:  #EAFFBF;   /* bloques de realce en claro */
  --verde-fondo:  #F4FAF1;   /* fondo claro por defecto de la web */
  /* neutros */
  --negro:        #1C2125;
  --gris-oscuro:  #5C7069;   /* texto de apoyo sobre claro */
  --gris-medio:   #9DAFA9;
  --gris-claro:   #C7D1CE;   /* texto de apoyo sobre oscuro, líneas sobre claro */
  --gris-sutil:   #F4F6F5;
  --blanco:       #FFFFFF;

  --font-sans: "DM Sans", system-ui, sans-serif;
  --font-mano: "Permanent Marker", cursive;
}
```

## 1. Color de texto según el fondo

Es la regla que más se rompe. Cada fondo tiene sus colores de texto permitidos y ninguno más.

| Fondo | Titular | Texto | Texto de apoyo | Acento | Manuscrito | Botón principal |
| --- | --- | --- | --- | --- | --- | --- |
| **Verde oscuro** `#003133` | blanco | blanco | gris claro `#C7D1CE` | lima | lima | lima con texto verde oscuro |
| **Verde fondo** `#F4FAF1` o blanco | verde oscuro `#003133` | negro `#1C2125` | gris oscuro `#5C7069` | rosa (pastilla) | verde oscuro o rosa | lima con texto verde oscuro |
| **Verde claro** `#EAFFBF` | verde oscuro | verde oscuro | gris oscuro | rosa | verde oscuro | verde oscuro con texto blanco |
| **Lima** `#98DA01` | verde oscuro | verde oscuro | verde oscuro | — | verde oscuro | verde oscuro con texto blanco |
| **Rosa** `#E83B83` | blanco (grande) | blanco | blanco | — | blanco | blanco con texto rosa |

Prohibido siempre:

- Texto negro, verde oscuro o gris oscuro sobre verde oscuro (no se lee).
- Lima como texto sobre fondo claro (1,9:1, no se lee).
- Amarillo como texto en cualquier fondo.
- Texto de apoyo con opacidad baja: usa el gris de la tabla.

## 2. Cuándo usar cada color

- **Verde oscuro** es la marca. Hero, cabecera, secciones de impacto, footer, cierres. Una pieza THC suele tener al menos una zona en verde oscuro.
- **Verde fondo `#F4FAF1`** es el fondo claro por defecto de la web, más que el blanco puro. Alterna con verde oscuro sección a sección.
- **Lima** es la acción y el subrayado de la marca: botones principales, una palabra o cifra destacada sobre oscuro, doodles de señalar. Como mucho dos usos por pantalla además del botón.
- **Rosa** es el guiño: la pastilla de la palabra destacada del titular, un sello, un detalle de doodle. Muy poco y nunca como fondo de grandes zonas en web (en slides de sección sí).
- **Amarillo**: post-its, cinta adhesiva sobre fotos, un detalle de ilustración.
- **Verde claro `#EAFFBF`**: bloques de realce sobre claro (una franja de cifras, un recuadro de regalo).
- Nunca rosa y amarillo protagonistas en la misma pieza. Nunca degradados. Nunca colores fuera de esta lista.

## 3. Tipografía

**DM Sans** para todo el texto. **Permanent Marker** solo para el manuscrito.

| Estilo | Tamaño / interlínea (px) | Peso | Tracking | Uso |
| --- | --- | --- | --- | --- |
| H1 | 66 / 74 | 600 SemiBold | -4 % (-2,6 px) | Titular de hero o portada |
| H2 | 40 / 46 | 500 Medium | -2 px | Titular de sección |
| H3 | 32 / 38 | 600 | -2 px | Subtítulo de bloque |
| H4 | 24 / 30 | 600 | 0 | Título de tarjeta |
| H5 | 20 / 28 | 600 | 0 | Título pequeño |
| Body L | 18 / 28 | 400 Regular | 0 | Entradilla bajo el titular |
| Body M | 16 / 26 | 400 | 0 | Texto normal |
| Body S | 14 / 20 | 400 | 0 | Notas, pies |
| Botón | 16 / 20 | 500 Medium | +1 % | Botones |

Reglas:

- Solo pesos **400, 500 y 600**. Nunca 700, 800 ni 900: la marca no es gritona.
- Titulares en **minúscula normal** (sentence case), nunca en mayúsculas. Tracking negativo en todo lo que pase de 30 px.
- Titulares de 1 a 3 líneas, cortos, con punto final si es una frase.
- Para redes y slides se escala todo (titulares de 80–130 px), con los mismos pesos y tracking proporcional.

**Manuscrito (Permanent Marker, siempre en MAYÚSCULAS).** Es una frase corta de entrada encima de un titular ("ELIGE TU PRÓXIMO PASO"), o el texto de un post-it. Una vez por sección como mucho. Nunca como etiqueta repetida en cada tarjeta, nunca en gris, nunca para párrafos.

**Palabra destacada en pastilla.** Es el gesto más reconocible de la marca. Dentro del titular, una palabra va en una pastilla rosa con texto blanco: radio 999 px, padding 6 px arriba, 12 px abajo y 14 px a los lados, girada -1°, con sombra suave (`0 5px 2.5px rgba(0,0,0,.15)`). Una por pieza como mucho.

```html
<h1>Somos la escuela líder en <span class="pastilla">producto</span> con IA</h1>
<style>
.pastilla{display:inline-block;background:var(--rosa);color:#fff;border-radius:999px;padding:6px 14px 12px;transform:rotate(-1deg);box-shadow:0 5px 2.5px rgba(0,0,0,.15);line-height:.8}
</style>
```

## 4. Botones

- **Esquinas rectas (radio 0).** Nunca redondeados, nunca en pastilla.
- Padding 14 px × 22 px. Texto 16 px Medium, tracking +1 %. Sin sombra.
- **Principal**: fondo lima, texto verde oscuro.
- **Secundario**: transparente, borde de 1 px del color del texto (blanco sobre oscuro, verde oscuro sobre claro). Lleva una flecha → de 20 px a la derecha del texto.
- Separación entre botones: 12 px. Como mucho dos botones juntos.
- Textos de botón concretos ("Ver todos los cursos", "Para empresas"), sin flechas ↗ ni emojis.

```css
.btn{display:inline-flex;align-items:center;gap:8px;padding:14px 22px;font:500 16px/20px var(--font-sans);letter-spacing:.01em;border-radius:0;text-decoration:none}
.btn-principal{background:var(--lima);color:var(--verde-oscuro)}
.btn-secundario{border:1px solid currentColor;color:#fff;background:transparent}
```

## 5. Líneas, bordes y formas

- Líneas y bordes **de 1 px**. Separadores: gris claro `#C7D1CE` sobre claro, blanco al 20 % sobre oscuro.
- Esquinas rectas por defecto en botones, tarjetas y bloques. Redondeo total (999 px) solo en la pastilla de palabra destacada y en los avatares. Las fotos de slides de persona pueden llevar 24–32 px. En carruseles y slides, los bloques dibujados (tarjetas de producto, pizarras, fichas) pueden llevar 16–28 px; los botones siguen siendo rectos.
- Sin sombras salvo la de la pastilla y la de fotos o post-its "pegados" (sombra suave y difusa).
- Nada de chips, badges ni etiquetas en cajita ("AHORRAS 1.190 €", "Nuevo", "Popular"). Si un dato importa, va como texto o como cifra grande.
- Nada de cajitas con flechas encadenadas ("A → B → C") para explicar recorridos. Eso se dibuja con un doodle o se cuenta en una frase.

## 6. Espaciado

Base de 8 px. Medidas de la web:

- Contenedor de 1440 px con márgenes laterales de 64–120 px.
- Secciones con mucho aire: 120–190 px de padding vertical en escritorio.
- Dentro de un bloque: 12 px entre titular y entradilla, 32 px hasta los botones, 48 px entre grupos.
- Titulares centrados en hero y cabeceras de sección. Contenido de lectura alineado a la izquierda.

Mejor una sección vacía que una llena. Si caben más de cuatro elementos en una fila, es demasiado.

## 7. Doodles

Son lo que más diferencia a THC de cualquier otra escuela. Trazo a mano alzada, sin relleno, extremos redondeados y grosor uniforme: coronas, calaveras, tréboles, rayos, espirales, flechas con lazo, sobres, corazones.

Tres usos:

1. **Textura de fondo** sobre verde oscuro: varios doodles en blanco al **10–20 % de opacidad**, girados y repartidos por los bordes del hero o la sección, sin tapar el texto.
2. **Señalar**: una flecha con lazo en lima al 100 %, apuntando a un botón o a una cifra. Una por sección.
3. **Ilustración**: un grupo de doodles en negro o blanco ocupando media pieza (slides de sección).

Dibújalos como SVG inline con `stroke-linecap="round"` y `stroke-linejoin="round"`, sin `fill`. Si no hay doodles, la pieza no es THC.

## 8. Fotografía

- Personas reales trabajando o aprendiendo: pizarras, post-its, mesas de trabajo, alguien explicando. Nada de stock posado.
- En la web, retratos y fotos de equipo **en blanco y negro**. Sobre fondo oscuro, con un **marco dibujado a mano** en blanco (rectángulo de trazo irregular, ligeramente desplazado) y, si es un alumno, el logo de su empresa en blanco encima.
- Avatares: círculos de 32 px con borde blanco de 1 px, solapados -5 px.
- En carruseles y slides: fotos clavadas en un tablón (marco blanco de 14 px, rotación entre -6° y 6°, cinta amarilla) o a sangre.

Cada sección importante lleva al menos una foto o un doodle. Una página solo de texto y tarjetas no es THC.

## 9. Logo

Isotipo de dos formas redondeadas (una M o corona) con HERO CAMP debajo en mayúsculas escalonadas. **Nunca escribas "The Hero Camp" con texto en lugar del logo.** Usa este SVG: `currentColor` toma el color del texto del contenedor.

- Blanco sobre verde oscuro, negro o rosa.
- Verde oscuro sobre fondos claros.
- Lima sobre verde oscuro cuando el logo es protagonista (portada, cierre).
- En cabeceras, unos 40–56 px de alto. Con otro logo (co-branding), los dos a la misma altura y separados por un "×" en lima.

```html
<svg class="logo-thc" width="52" height="56" viewBox="0 0 279 301" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The Hero Camp"><path d="M0 208.828H21.6045V190.594H43.8803V208.828H65.4849V160.211H43.8803V176.42H21.6045V160.211H0V208.828Z" fill="currentColor"/><path d="M186.251 210.181C190.981 210.181 197.188 208.694 200.017 206.607L197.188 198.301C196.444 198.91 194.823 199.313 193.811 199.313C191.787 199.313 190.506 198.642 189.494 197.423L186.117 193.301C184.971 191.885 183.618 190.801 182.275 190.47V190.408C191.188 188.445 196.176 183.383 196.176 176.089C196.176 165.893 188.544 160.221 174.778 160.221H132.044V208.838H153.648V193.983H159.38C162.685 193.983 165.731 195.067 167.889 197.826L170.389 201.069C173.631 205.315 177.752 210.181 186.251 210.181ZM153.648 182.495V172.37H167.817C172.134 172.37 174.571 174.199 174.571 177.432C174.571 180.666 172.144 182.495 167.755 182.495H153.648Z" fill="currentColor"/><path d="M72.652 236.06H125.982V223.229H93.5749V216.814H122.605V206.008H93.5749V200.264H125.3V187.433H72.652V236.05V236.06Z" fill="currentColor"/><path d="M242.555 237.744C264.563 237.744 279.01 227.475 279.01 211.741C279.01 196.007 264.563 185.739 242.555 185.739C220.548 185.739 206.1 196.007 206.1 211.741C206.1 227.475 220.538 237.744 242.555 237.744ZM242.555 222.888C233.571 222.888 227.705 218.498 227.705 211.741C227.705 204.985 233.571 200.594 242.555 200.594C251.54 200.594 257.406 204.985 257.406 211.741C257.406 218.498 251.53 222.888 242.555 222.888Z" fill="currentColor"/><path d="M33.8835 278.582C49.4053 278.582 61.3539 271.423 64.5967 260.141L55.8908 258.117C53.4639 266.154 45.0266 271.278 34.0178 271.278C19.508 271.278 10.2549 264.191 10.2549 253.116C10.2549 242.042 18.6922 234.955 31.9214 234.955C41.505 234.955 49.0026 239.48 51.2952 246.639L59.7945 244.139C56.2833 234.077 45.3467 227.661 31.7148 227.661C12.816 227.661 0.867432 237.589 0.867432 253.116C0.867432 268.644 13.6938 278.582 33.8732 278.582H33.8835Z" fill="currentColor"/><path d="M66.373 297.932H76.1632L81.6367 287.467H111.606L117.069 297.932H126.932L102.219 250.059H91.2823L66.373 297.932ZM84.394 280.917L96.6111 256.877H96.7454L108.901 280.917H84.394Z" fill="currentColor"/><path d="M131.92 277.063H140.966V238.984H141.101L161.9 277.063H171.277L191.942 238.984H192.076V277.063H201.122V229.19H187.966L166.568 268.623H166.495L144.963 229.19H131.94V277.063H131.92Z" fill="currentColor"/><path d="M215.653 301H225.03V284.45H250.342C262.559 284.45 269.375 278.706 269.447 268.923C269.447 258.922 262.631 253.116 250.414 253.116H215.653V300.99V301ZM225.03 277.973V259.677H248.049C255.743 259.677 260.06 263.055 260.06 268.861C260.06 274.667 255.743 277.973 248.049 277.973H225.03Z" fill="currentColor"/><path d="M236.566 72.533L202.95 9.6077C199.852 3.81209 193.842 0.1343 187.274 -1.57533e-06C187.16 -1.57533e-06 187.036 -1.57533e-06 186.923 -1.57533e-06C180.489 -1.57533e-06 174.509 3.41951 171.246 8.98785L139.5 63.2249L107.754 8.98785C104.429 3.31621 98.2738 -0.134303 91.7264 -1.57533e-06C85.1583 0.123969 79.1581 3.80176 76.06 9.59737L42.4346 72.533C39.6979 77.6571 40.0696 83.8866 43.4053 88.6388L64.4832 118.722C67.3645 122.834 72.0737 125.293 77.0927 125.293H201.918C206.937 125.293 211.646 122.844 214.527 118.722L235.605 88.6388C238.941 83.8866 239.313 77.6571 236.576 72.533H236.566ZM85.0963 94.4757L74.0565 78.7108L92.5732 44.0508L122.088 94.4757H85.0963ZM193.894 94.4757H156.901L186.417 44.0508L204.933 78.7108L193.894 94.4757Z" fill="currentColor"/></svg>
```

Los mismos SVG están en `logos/`.

## 10. Errores frecuentes (mira `referencias/no/`)

Estos fallos salieron al aplicar una versión anterior de esta skill:

- Titulares negros sobre verde oscuro, que no se leen.
- Descripciones en gris oscuro sobre verde oscuro, que no se leen.
- "THE HERO CAMP." escrito en texto en vez del logo.
- Lima más claro o amarillento que `#98DA01`.
- Tarjetas con borde, precio y badge "AHORRAS…", al estilo de cualquier SaaS.
- Cajitas encadenadas con flechas ("Digital PM → Mentoría 1:1 → AI Builder").
- Manuscrito repetido como etiqueta en todas las tarjetas.
- Ninguna foto y ningún doodle salvo una flecha.
- Botones con esquinas redondeadas.

## 11. Comprobación final

Antes de entregar, repasa:

- [ ] ¿Cada texto respeta la tabla de color por fondo?
- [ ] ¿Solo pesos 400, 500 y 600? ¿Titulares en minúscula con tracking negativo?
- [ ] ¿Botones rectos, lima o con borde de 1 px?
- [ ] ¿Logo en SVG, no en texto?
- [ ] ¿Hay doodles y fotos de personas?
- [ ] ¿Manuscrito como mucho una vez por sección?
- [ ] ¿Cero chips, badges, degradados y sombras duras?
- [ ] ¿Se parece a `referencias/si/` y no a `referencias/no/`?
