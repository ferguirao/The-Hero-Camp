---
name: garabatos-thc
description: Cómo elegir y colocar los garabatos de marca de The Hero Camp (compartido/marca/ilustraciones) en las slides, con sentido: qué slides los llevan, cuál elegir según lo que dice la slide, color, posición, tamaño y cuántos por sesión. Úsala dentro del plan de slides (elegir-slide) y al maquetar portadas, separadores, mensajes, hands on, callouts y cierres.
---

# Garabatos con sentido

Los garabatos son parte de la identidad: la guía de marca dice que **acompañan títulos o señalan algo y nunca dominan la slide**. Esta skill decide dónde ponerlos y cuál; el cómo técnico es el componente `<Garabato>` y la prop `garabato` de cada layout.

## Qué hay

`compartido/marca/ilustraciones/`: 93 garabatos y 12 figuras de confeti, todos de un solo color (`currentColor`), recoloreables. **`indice.json`** lista cada uno con su nombre, `significado` (palabras clave), `roles` (acento, separador, cierre, portada, conector, enfasis, decoracion, callout) y `tamano`. `_hoja-principal.png` y `_hoja-confeti.png` son las hojas para verlos. Se busca por significado, no por ojo.

## Dónde van (y dónde no)

| Slide | Garabato | Color | Notas |
|---|---|---|---|
| `portada` | Sí, uno grande arriba a la derecha (`garabato`) | lima | Rol `portada`: constelación, estrella fugaz, avión de papel, flecha |
| `separador`, `separador-fase` | **Siempre** uno grande en una esquina | verde oscuro sobre lima; lima sobre oscuro | Es el momento fuerte de la marca. Que diga el tema de la sección |
| `mensaje` | Opcional, solo si refuerza la idea | lima | Uno cada 3 o 4 mensajes, no en todos |
| `hands-on` | Opcional, pequeño, inclinado | lima | Una flecha, un rayo o una estrella: "hazlo" |
| `callout` | Sí, el rayo por defecto (cambiable) | lima | |
| `portada-modulo` | Sí, la flecha por defecto | lima | |
| `ponente` de cierre y `pausa` | Opcional | lima | Cierre: corazón, xoxo, carita |
| `contenido`, `figura`, `comparar`, `caso`, `cita`, `pasos`, `lado-foto`, `foto-mensaje` | **No** | | Ya tienen foto, dato o diagrama. Un garabato ahí compite |

## Cómo elegir cuál

1. Lee el título de la slide y saca la **idea** (avanzar, riesgo, atasco, idea, lanzamiento, valor, cierre…).
2. Busca en `indice.json` por `significado` y por `roles`. Ejemplos: lanzar o MVP → `avion-de-papel`; visión o roadmap → `constelacion`; riesgo o fallo → `calavera`; atasco o problema → `nube-con-lluvia`; ciclo o iteración → `espiral-grande`, `bucles-grandes`; liderazgo → `corona`; feedback → `bocadillo-con-corazon`; descubrir u observar → `ojo-con-pestanas`; cierre → `corazon-cometa`, `xoxo`, `carita-sonriente`.
3. Si ninguno encaja, **no pongas ninguno** o usa uno neutro de rol `acento` (estrella, destello, flecha). Un garabato que contradice el mensaje es peor que ninguno (por ejemplo, la calavera en una slide de logro).
4. Comprueba **variedad**: no repitas el mismo en una sesión salvo en el cierre que responde a la portada. Alterna esquina (arriba derecha, abajo derecha) en separadores consecutivos.

## Reglas visuales

- **Uno por slide.** El confeti (gotas, rayitas) es textura, no garabato; úsalo como máximo una vez cada pocas slides y con poca opacidad.
- **Tamaño por slide:** separador y portada, 30 a 35 % del ancho; mensaje, 20 a 25 %; hands on y callout, 12 a 18 % o ancho fijo pequeño. Nunca más del 40 % ni encima del título.
- **Color:** sobre fondo lima, verde oscuro; sobre verde oscuro, lima; sobre blanco o sutil, lima o verde oscuro. El rosa y el amarillo solo como acento puntual de una sesión, en una o dos slides, y con el mismo criterio siempre (por ejemplo: rosa para lo que no funciona).
- **Posición:** esquinas (`sup-der`, `inf-der`, `sup-izq`, `inf-izq`). En separadores, la esquina opuesta al título (el título va abajo a la izquierda, el garabato arriba a la derecha). Que no tape el texto ni el logo.
- **Rotación:** de -10 a 10 grados da vida; más, no.
- **Cantidad en una sesión:** todos los separadores, la portada, el cierre y los callouts; los demás, uno cada 4 o 5 slides como mucho.

## Cómo se usa

En el frontmatter del layout:

```yaml
---
layout: separador
numero: "2"
color: lima
garabato: avion-de-papel
garabatoPos: sup-der   # sup-der | sup-izq | inf-der | inf-izq
---
```
`portada`, `separador`, `separador-fase`, `mensaje`, `hands-on`, `callout` y `portada-modulo` aceptan `garabato`. En otros sitios, el componente directo: `<Garabato nombre="corona" color="lima" pos="inf-der" ancho="22%" rotar="-6" sangrado="2rem" />`. Colores: `verde-oscuro`, `lima`, `blanco`, `rosa`, `amarillo`, `gris`, `actual`.

## En el plan de slides

`elegir-slide` añade una columna **Garabato** al plan (nombre o "—" con el motivo). Se aprueba con el plan.

## Revisión

En `revisar-slides`: ningún separador sin garabato; ninguno repetido sin motivo; ninguno que contradiga el mensaje; ninguno dominando; color correcto sobre su fondo.
