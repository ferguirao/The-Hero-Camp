# Plan slide a slide: qué slide usar y cómo variar

Antes de maquetar, se hace un plan y se aprueba. Sirve para que el deck no salga con cuatro layouts y tarjetas por todas partes.

## Procedimiento

1. Parte de un esqueleto: un título que afirma por slide.
2. Por cada slide, escribe:
   - **Forma del contenido:** qué tiene de verdad (una cifra, un proceso, dos cosas que contrastar, niveles, pocas cosas paralelas, un caso, una cita, un reto para el público, una imagen que lo explica…).
   - **Recurso narrativo:** cómo se cuenta (pregunta que provoca, cifra que impacta, caso real, contraste es / no es, metáfora visual, cita, definición con ejemplo, dinámica, resumen…).
   - **Layout y receta** (tablas de abajo y `layouts.md`).
   - **Garabato**, solo en portada, separadores, mensajes, hands on, callouts y cierre (`garabatos.md`).
3. Comprueba las reglas de diversidad y rehaz lo que falle.
4. Pasa el plan a aprobación con este formato:

```
| # | Título (afirma) | Forma del contenido | Recurso | Layout / patrón | Receta | Garabato | Notas (foto, datos, TODO) |
```

Al final, el recuento: layouts usados, recursos usados y si cumple las reglas.

No se inventa contenido para llenar un patrón: si la fuente no tiene una cifra, no hay slide de cifras.

## Forma del contenido → layout

| Si el contenido es… | Usa |
|---|---|
| Una o dos cifras que sorprenden | `contenido` + `.cifras` |
| Un proceso lineal o una cadena causal | `contenido` + `.cadena` (con `.roto` donde falla), o visual dibujado |
| Niveles de lo general a lo concreto | `contenido` + `.cascada` |
| Un proceso que dura varias slides | `pasos` |
| Tres a seis conceptos paralelos | receta 1 (tarjetas grises) |
| Tres o cuatro ideas cortas con símbolo | `iconos` |
| Una técnica (qué es / ejemplo / cuándo) | tres tarjetas |
| Datos comparables por filas | `contenido` + `<table>` |
| Dos cosas contrastadas | `comparar` |
| Una definición | `lado-foto` |
| Un caso real de empresa | `caso`, o dos slides problema → solución |
| Una cita | `cita` |
| Un diagrama o captura ajena | `figura` (mejor reconstruido con los colores de marca que pegado) |
| Una idea que hay que grabar | `mensaje` |
| Una pregunta al público | `pregunta` con fondo de acento, o `foto-mensaje` |
| Un reto | `hands-on` |
| Un cambio de tema | `separador` |
| Un descanso | `pausa` |
| Un resumen | 3 tarjetas oscuras |

## Reglas de diversidad

- Cada 10 slides, al menos 5 layouts distintos y 3 recursos narrativos distintos.
- Nunca 3 slides seguidas con el mismo layout (salvo `pasos`, que es la agenda).
- Tarjetas: como mucho la mitad de las slides de contenido.
- `foto-mensaje` y `mensaje` no pasan de un tercio del deck.
- Un mismo recurso narrativo no se repite dos veces seguidas en un bloque.
- Si dos slides seguidas tienen la misma forma de contenido, se combinan o una cambia de recurso.

## Ritmo

- Cada 8 slides, como mínimo: una a sangre (`lado-foto`, `foto-mensaje`, `pregunta` o `mensaje` con fondo), un visual dibujado y un grupo de tarjetas con jerarquía o cifras. Nunca más de 2 seguidas con «título + un bloque».
- Un visual cada 3 o 4 slides, no en todas.
- Tras 2 o 3 slides densas, una de foto, pregunta o caso. Una pausa visual cada 8 a 12 slides de contenido.
- Una pregunta o reto por bloque, y un caso o cifra por bloque.
- Alterna el lado de la foto en `lado-foto`.
