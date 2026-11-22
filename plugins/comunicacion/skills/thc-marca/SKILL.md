---
name: thc-marca
description: "Sistema visual web de The Hero Camp con valores exactos (colores por fondo, tipografía y pesos, botones, bordes y sombras, espaciado, componentes, logo). Úsala antes de diseñar webs, landings, emails, carruseles y posts con la marca THC; para presentaciones, solo aporta colores y fuentes (el estilo está en thc-presentaciones)."
---

# The Hero Camp · sistema visual

Todo lo que hay aquí sale del CSS de la web de referencia (variante v2 de la portada). No es orientativo: usa estos valores tal cual en webs, landings, emails, carruseles y posts. **En presentaciones solo valen los colores y las fuentes**: bordes de 2 px, sombras sólidas y titulares de 700 apretados no van en slides; el estilo de slides está en `thc-presentaciones` (tema Slidev de Course-Builder). Lo que hace que algo "parezca THC" son los detalles: bordes de 2 px, sombras sólidas desplazadas, titulares en negrita apretados, el subrayado de rotulador lima y el manuscrito.

Las demás skills de THC (`thc-web`, `thc-carrusel-caso`, `thc-presentaciones`) parten de esta. `referencias/si/pagina-v2.png` es una página de ejemplo con todo aplicado (sale de `thc-web/plantillas/pagina.html`).

## 0. Copia esto tal cual

Pega este bloque al principio de cualquier HTML o CSS (también está en `tokens.css`). No aproximes colores ni cambies fuentes.

```css
@import url("https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700;9..40,900&family=Permanent+Marker&display=swap");

:root {
  --ink:    #003133;  /* verde oscuro: texto, bordes, fondos oscuros */
  --ink2:   #0B4648;  /* verde oscuro secundario */
  --lime:   #98DA01;  /* acción, subrayado, sombras de acento */
  --pink:   #E83B83;  /* manuscrito sobre claro, foco, recomendado */
  --yellow: #FFDA23;  /* pegatinas, aviso, manuscrito sobre oscuro */
  --paper:  #F4F6F5;  /* fondo por defecto */
  --pale:   #EAFFBF;  /* fondo de realce (contacto, FAQ abierta) */
  --gris:   #486461;  /* texto secundario sobre claro */
  --cuerpo: #19494B;  /* texto de párrafo sobre claro */
  --linea:  #C9D6D3;  /* líneas finas sobre claro */
  --sobre-oscuro: #C5D8D5;  /* texto secundario sobre verde oscuro */
  --sombra: 5px 5px 0 var(--ink);
}
body { background: var(--paper); color: var(--ink); font-family: "DM Sans", sans-serif; font-size: 18px; line-height: 1.55; }
```

## 1. Color de texto según el fondo

Cada fondo tiene sus colores permitidos y ninguno más.

| Fondo | Titular | Párrafo | Secundario | Manuscrito (eyebrow) | Palabra destacada | Botón |
| --- | --- | --- | --- | --- | --- | --- |
| **Papel** `#F4F6F5` o blanco | `--ink` | `--cuerpo` `#19494B` | `--gris` `#486461` | rosa `--pink` | subrayado de rotulador lima | lima, sombra `--ink` |
| **Verde oscuro** `#003133` | blanco | blanco | `#C5D8D5` | amarillo `--yellow` | texto en lima, sin subrayado | lima, sombra **blanca** |
| **Verde claro** `#EAFFBF` | `--ink` | `--cuerpo` | `--gris` | rosa | subrayado lima | verde oscuro con texto blanco y sombra lima |
| **Lima** `#98DA01` (banda de cifras) | `--ink` | `--ink` | `--ink` | — | — | — |
| **Amarillo** `#FFDA23` (aviso superior) | — | `--ink` | — | — | — | — |

Prohibido siempre:

- Cualquier texto oscuro (`--ink`, `--cuerpo`, `--gris`, negro) sobre verde oscuro. Ahí todo es blanco, `#C5D8D5`, lima o amarillo.
- Lima como color de texto sobre fondos claros (no se lee). Sobre claro el lima solo va detrás del texto, como subrayado.
- Grises genéricos (`#666`, `#999`…): usa `--gris`, `--cuerpo` o `--linea`.

## 2. Cuándo usar cada color

- **Papel `#F4F6F5`** es el fondo por defecto. La mayoría de secciones van en papel.
- **Verde oscuro `--ink`** marca las secciones de peso (la oferta de programas, servicios a empresa) y el footer. Alterna con papel, nunca dos oscuras seguidas.
- **Blanco** es para superficies: tarjetas, cabecera y alguna sección para cambiar de ritmo (preguntas frecuentes).
- **Lima** es la acción y el realce: botones, subrayado de rotulador, sombras de acento en tarjetas destacadas, la banda de cifras, la franja final del footer y el subrayado al pasar el ratón.
- **Rosa** es el manuscrito sobre claro, el contorno de foco, la pegatina "Para ti" y la sombra del elemento elegido. Nunca un fondo grande.
- **Amarillo** es para pegatinas, la barra de aviso y el manuscrito sobre oscuro.
- **Verde claro `--pale`** es el fondo de realce: caja de contacto y pregunta frecuente abierta.

## 3. Tipografía

**DM Sans** para todo. **Permanent Marker** solo para el manuscrito.

| Estilo | Tamaño | Peso | Interlínea | Tracking |
| --- | --- | --- | --- | --- |
| H1 | `clamp(42px, 5.4vw, 80px)` | **700** | 1.04 | -0.045em |
| H2 | `clamp(30px, 3.5vw, 50px)` | **700** | 1.08 | -0.04em |
| H3 | 24px (tarjetas 19–24) | **700** | 1.15 | -0.03em |
| Entradilla | 20px, color `#19494B`, máx. 44ch | 400 | 1.5 | 0 |
| Párrafo | 18px (16–17 en tarjetas) | 400 | 1.55 | 0 |
| Secundario | 14–15px, `--gris` | 400 | 1.45 | 0 |
| Botón | 17px | **700** | 1.2 | 0 |
| Navegación | 15.5px | 500 | — | 0 |
| Cifra grande | `clamp(40px, 4.6vw, 64px)`, números tabulares | 700 | 1 | -0.05em |
| Rótulo pequeño | 12.5px, MAYÚSCULAS, `#9FBAB6` sobre oscuro o `--gris` sobre claro | 700 | — | +0.08em |
| Número de paso | 54px, **contorno** de 2px `--ink`, relleno transparente | 900 | 1 | -0.05em |

Reglas:

- Titulares en minúscula normal (sentence case) y siempre con tracking negativo. `text-wrap: balance` en titulares.
- **Manuscrito (eyebrow)**: Permanent Marker, 19px, encima del H2, tal como se escribe ("Nuestro método", "Formaciones"). Rosa sobre claro y amarillo sobre oscuro. Uno por sección. También se usa en pegatinas, en avisos cortos como "20 plazas" (rosa, 15px) y en la etiqueta del boletín.
- **Palabra destacada (`.marca`)**: una o dos palabras del titular con un subrayado de rotulador lima detrás. Sobre oscuro, esas palabras van en lima sin subrayado. Una por titular.

```css
.marca { background: linear-gradient(transparent 62%, var(--lime) 62% 92%, transparent 92%); margin-inline: -.06em; padding-inline: .06em; }
.oscura .marca { color: var(--lime); background: none; }
```

- **Enlaces de texto**: negrita, subrayado lima de 3px con 5px de separación; al pasar el ratón, el subrayado pasa a rosa.

## 4. Bordes, sombras y formas

Es el rasgo más reconocible del sistema.

- **Bordes de 2px sólidos en `--ink`** en botones, tarjetas, imágenes dentro de tarjetas, cabecera, separadores de sección y cajas. Los elementos pequeños (pegatinas, etiquetas de empresa) van a 1.5px. Las líneas secundarias son de 1px en `--linea` `#C9D6D3` sobre claro, o blanco al 20 % sobre oscuro.
- **Sombra sólida desplazada, sin difuminado**: `5px 5px 0 var(--ink)` en tarjetas, `4px 4px 0` en botones y `3px 3px 0` en elementos pequeños. Para destacar, la sombra va en lima (`5px 5px 0 var(--lime)`); para lo elegido, en rosa. Sobre verde oscuro, la sombra de los botones es blanca.
- **Esquinas rectas (radio 0) en todo.** Las únicas excepciones son los chips de filtro (radio 99px) y los avatares (círculo).
- Nunca sombras difuminadas (`0 10px 30px rgba…`), degradados de color ni efectos de cristal.
- **Al pasar el ratón**, el elemento sube (`translate(-2px,-2px)`) y la sombra crece a 6px. Al pulsar, baja (`translate(3px,3px)`) y la sombra se queda en 1px. Transiciones de .15–.2s.

## 5. Botones

```css
.btn { display:inline-flex; align-items:center; gap:10px; padding:13px 22px; font-size:17px; font-weight:700; line-height:1.2;
       background:var(--lime); color:var(--ink); border:2px solid var(--ink); box-shadow:4px 4px 0 var(--ink);
       border-radius:0; text-decoration:none; white-space:nowrap; transition:transform .15s, box-shadow .15s; }
.btn:hover  { transform:translate(-2px,-2px); box-shadow:6px 6px 0 var(--ink); }
.btn:active { transform:translate(3px,3px);  box-shadow:1px 1px 0 var(--ink); }
.btn-claro  { background:#fff; }                                                   /* secundario */
.btn-oscuro { background:var(--ink); color:#fff; box-shadow:4px 4px 0 var(--lime); }  /* sobre verde claro */
.oscura .btn { box-shadow:4px 4px 0 #fff; }                                         /* sobre verde oscuro */
```

- Principal en lima y secundario en blanco, uno al lado del otro con 14px de separación.
- Una flecha (→ o ↓) dentro, a la derecha del texto, que se mueve 3px al pasar el ratón. Nada de ↗ ni de emojis.
- Textos cortos y concretos: "Ver programas", "Soy empresa", "Pedir información".

## 6. Componentes pequeños

- **Etiqueta de fecha**: fondo blanco, borde 2px `--ink`, padding 2px 9px, 13px peso 500. Va en la esquina de la imagen de una tarjeta.
- **Pegatina**: fondo amarillo, borde 1.5px `--ink`, sombra `2px 2px 0 var(--ink)`, Permanent Marker de 14px, padding 5px 11px, girada 4°. Una por tarjeta como mucho ("Nueva edición"). La variante rosa con texto blanco, girada -4°, es para "Para ti".
- **Novedad**: caja blanca con borde de 2px y una etiqueta interior en verde oscuro con texto blanco en mayúsculas de 12px ("NEW"), seguida del texto y una flecha.
- **Datos de programa**: etiquetas pequeñas con fondo papel, borde 1px `--linea` y texto de 12.5px ("70 horas", "Certificación incluida"). Solo para datos, nunca para precios ni ahorros.
- **Chip de filtro**: radio 99px, borde 1.5px blanco al 40 % sobre oscuro. Si está activo, fondo lima con texto verde oscuro en negrita.
- **Etiqueta de empresa** sobre una foto: fondo blanco, borde 1.5px, 12.5px peso 500, en la esquina superior izquierda.
- **Banda de cifras**: fondo lima, bordes de 2px arriba y abajo, cuatro columnas separadas por líneas de 2px `--ink`. Cifra grande en 700 y etiqueta debajo en 16px peso 500.

## 7. Espaciado y retícula

- Contenedor: `width: min(1240px, 100% - 64px)` (en móvil, `100% - 36px`).
- Secciones: `padding-block: clamp(64px, 8.5vw, 120px)`.
- Cabecera de sección en dos columnas (`1.25fr 1fr`, separación de 64px, alineadas abajo): a la izquierda el manuscrito y el H2, y a la derecha la entradilla en `--gris`, de 46ch como mucho. Margen inferior de `clamp(32px, 4vw, 56px)`.
- Rejillas de tarjetas con separación de 22–24px, cuatro columnas como mucho.
- Dentro de las tarjetas, padding de 18–22px.

## 8. Fotografía

- Fotos reales de profesores, alumnos y sesiones, en color, recortadas a proporciones fijas (3:4 en retratos, 16:10 en programas, 16:9 en eventos y 4:3 en pasos).
- Siempre dentro de un marco: borde de 2px `--ink`, y si es protagonista, sombra sólida.
- En el hero, un **muro** de retratos en tres columnas que se desplazan, separados por líneas de 2px en verde oscuro.
- Los logos de empresas van monocromos en `--gris` y pasan a `--ink` al pasar el ratón.

## 9. Logo

Cabecera y footer usan el isotipo con "The Hero / **Camp**" al lado, en dos líneas: 13px peso 500 arriba y 17px peso 700 abajo. Nunca escribas solo el nombre sin el isotipo.

```html
<a class="logo" href="/" aria-label="The Hero Camp, inicio" style="display:flex;align-items:center;gap:9px;color:inherit;text-decoration:none;font-size:13px;font-weight:500;line-height:1.05">
  <svg viewBox="0 0 40.778 25.486" width="42" aria-hidden="true"><path fill="currentColor" d="M 40.401 14.755 L 33.47 1.955 C 32.831 0.776 31.592 0.028 30.238 0.001 C 30.214 0.001 30.189 0.001 30.165 0.001 C 28.839 0.001 27.606 0.696 26.933 1.829 L 20.388 12.861 L 13.843 1.829 C 13.157 0.675 11.888 -0.027 10.538 0.001 C 9.184 0.026 7.947 0.774 7.308 1.953 L 0.375 14.755 C -0.189 15.797 -0.112 17.064 0.575 18.031 L 4.921 24.15 C 5.515 24.986 6.486 25.486 7.521 25.486 L 33.257 25.486 C 34.292 25.486 35.263 24.988 35.857 24.15 L 40.203 18.031 C 40.891 17.064 40.967 15.797 40.403 14.755 Z M 9.171 19.218 L 6.895 16.011 L 10.713 8.961 L 16.798 19.218 Z M 31.603 19.218 L 23.976 19.218 L 30.061 8.961 L 33.879 16.011 Z"/></svg>
  <span>The Hero<br><b style="font-size:17px;font-weight:700">Camp</b></span>
</a>
```

Para piezas grandes (portadas, cierres, carruseles) está el logo apilado con "HERO CAMP" debajo, en `logos/` (lima, verde oscuro, blanco y `currentColor`).

## 10. Errores frecuentes (mira `referencias/no/`)

Al aplicar una versión anterior de esta skill salieron estos fallos:

- Titulares negros o párrafos gris oscuro sobre verde oscuro, que no se leen.
- Solo el texto "THE HERO CAMP." en lugar del logo.
- Un lima más claro o amarillento que `#98DA01`.
- Tarjetas con borde fino de 1px gris, sin sombra sólida: parecen de cualquier SaaS. En THC el borde es de 2px `--ink` y la sombra es sólida.
- Badges de ahorro ("AHORRAS 1.190 €"). El descuento se muestra con el precio antiguo tachado en `--gris` encima del nuevo en 700.
- Cajitas encadenadas con flechas para explicar un recorrido.
- Botones sin borde ni sombra, o con esquinas redondeadas.
- Manuscrito gris o en cada tarjeta. Va en rosa o amarillo y una vez por sección.

## 11. Comprobación final

- [ ] ¿Respeta la tabla de color por fondo, sin ningún texto oscuro sobre verde oscuro?
- [ ] ¿Titulares en 700 con tracking negativo y una palabra con subrayado de rotulador?
- [ ] ¿Bordes de 2px `--ink` y sombras sólidas desplazadas, todo con esquinas rectas?
- [ ] ¿Botones lima con borde, sombra y flecha?
- [ ] ¿Manuscrito en Permanent Marker, rosa o amarillo, una vez por sección?
- [ ] ¿Logo con isotipo, no solo texto?
- [ ] ¿Cero sombras difuminadas, degradados de color y badges de ahorro?