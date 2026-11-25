# Garabatos en slides

Los garabatos acompañan un título o señalan algo; nunca dominan la slide.

## Qué hay

`slides/tema/ilustraciones/`: 93 garabatos y 12 figuras de confeti (`confeti/`), todos de un color (`currentColor`), recoloreables. `indice.json` da de cada uno su `significado` (palabras clave), sus `roles` (acento, separador, cierre, portada, conector, enfasis, decoracion, callout) y su `tamano`. `_hoja-principal.png` y `_hoja-confeti.png` los muestran todos. Se elige por significado, no a ojo. No se inventan garabatos nuevos.

## Dónde van

| Slide | Garabato | Color |
|---|---|---|
| `portada` | Uno grande arriba a la derecha (rol `portada`: constelación, estrella fugaz, avión de papel, flecha) | lima |
| `separador`, `separador-fase` | Siempre, grande, en la esquina opuesta al título, y que diga el tema de la sección | verde oscuro sobre lima; lima sobre oscuro |
| `mensaje` | Opcional, uno cada 3 o 4 mensajes | lima |
| `hands-on` | Opcional, pequeño e inclinado (flecha, rayo, estrella) | lima |
| `callout` | El rayo por defecto | lima |
| `portada-modulo` | La flecha por defecto | lima |
| Cierre y `pausa` | Opcional: corazón, xoxo, carita | lima |
| `contenido`, `figura`, `comparar`, `caso`, `cita`, `pasos`, `lado-foto`, `foto-mensaje` | No: ya tienen foto, dato o diagrama | — |

## Cuál elegir

1. Saca la idea del título (avanzar, riesgo, atasco, idea, lanzamiento, valor, cierre…).
2. Búscala en `indice.json`. Ejemplos: lanzar o MVP → `avion-de-papel`; visión o roadmap → `constelacion`; riesgo → `calavera`; atasco → `nube-con-lluvia`; ciclo → `espiral-grande`, `bucles-grandes`; liderazgo → `corona`; feedback → `bocadillo-con-corazon`; observar → `ojo-con-pestanas`; cierre → `corazon-cometa`, `xoxo`, `carita-sonriente`.
3. Si ninguno encaja, ninguno, o uno neutro de rol `acento` (estrella, destello, flecha). Uno que contradice el mensaje es peor que ninguno.
4. No repitas el mismo en una sesión, salvo el cierre que responde a la portada. Alterna la esquina en separadores seguidos.

## Reglas visuales

- Uno por slide. El confeti es textura: como mucho una vez cada pocas slides y con poca opacidad.
- Tamaño: portada y separador, 30–35 % del ancho; mensaje, 20–25 %; hands on y callout, 12–18 %. Nunca más del 40 % ni encima del título.
- Color: sobre lima, verde oscuro; sobre verde oscuro, lima; sobre blanco, lima o verde oscuro. Rosa y amarillo solo como acento puntual en una o dos slides, siempre con el mismo criterio.
- Rotación de -10 a 10 grados.
- En una sesión: todos los separadores, la portada, el cierre y los callouts; en el resto, uno cada 4 o 5 slides como mucho.

## Cómo se pone

En el frontmatter de `portada`, `separador`, `separador-fase`, `mensaje`, `hands-on`, `callout` y `portada-modulo`:

```yaml
garabato: avion-de-papel
garabatoPos: sup-der   # sup-der | sup-izq | inf-der | inf-izq
```

En cualquier otro sitio, el componente:

```html
<Garabato nombre="corona" color="lima" pos="inf-der" ancho="22%" rotar="-6" sangrado="2rem" />
```

Colores: `verde-oscuro`, `lima`, `blanco`, `rosa`, `amarillo`, `gris`, `actual`.
