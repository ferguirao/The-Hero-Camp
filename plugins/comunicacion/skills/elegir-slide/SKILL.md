---
name: elegir-slide
description: Decide qué tipo de slide y qué forma de contarlo usa cada slide de una sesión de The Hero Camp, antes de maquetar. Úsala siempre que haya un esqueleto aprobado y toque pasar a slides: produce un plan slide a slide (forma del contenido, recurso narrativo, layout, patrón, densidad) que garantiza diversidad. Basada en la variedad del deck DPM61. Después se maqueta con maquetacion-thc.
---

# Elegir la slide

`maquetacion-thc` dice **cómo** se construye cada layout. Esta skill decide **cuál** y **cómo se cuenta**, para que el deck no salga con cuatro layouts y tarjetas por todas partes. Se hace antes de escribir una sola slide, y el plan se aprueba.

## Procedimiento

1. **Parte del esqueleto aprobado** (`arquitectura-de-contenido`): un título que afirma por slide.
2. **Por cada slide, responde tres preguntas** y escríbelas:
   - **Forma del contenido:** ¿qué tiene realmente? (una cifra, un proceso, dos cosas que contrastar, niveles, una lista de pocas cosas, un caso, una cita, una opinión, un reto para el público, una imagen que lo explica…)
   - **Recurso narrativo:** ¿cómo lo cuento? (pregunta que provoca, cifra que impacta, caso real, contraste, metáfora visual, cita de un referente, definición con ejemplo, dinámica, resumen…)
   - **Layout y patrón** según las tablas de abajo.
   - **Garabato** (solo portada, separadores, mensajes, hands on, callouts y cierre): lo decide la skill `garabatos-thc`, según la idea de la slide.
3. **Comprueba la diversidad** (reglas abajo) y rehaz las slides que fallan.
4. **Escribe el plan** en `cursos/<curso>/sesiones/<sesion>/plan-slides.md` y pásalo a aprobación junto al esqueleto.
5. Maqueta con `maquetacion-thc`, escribe con `voz-thc` y revisa con `revisar-slides`.

## Forma del contenido → layout y patrón

| Si el contenido es… | Usa | Patrón (ver `referencias/patrones.md`) |
|---|---|---|
| Una cifra o dos que sorprenden | `contenido` | `.cifras` + `.cifra` |
| Un proceso lineal o una cadena causal | `contenido` | `.cadena` (con `.roto` donde falla) |
| Niveles que bajan de lo general a lo concreto | `contenido` | `.cascada` |
| Un proceso de pasos que dura varias slides | `pasos` | agenda lateral |
| Tres a seis conceptos paralelos | `contenido` | `.tres` / `.cinco` + `.tarjeta` |
| Tres a cuatro ideas cortas con símbolo | `iconos` | 3 o 4 `items` |
| Una técnica con "qué es / ejemplo / cuándo" | `contenido` | `.tres` con tres tarjetas |
| Datos comparables por filas | `contenido` | `<table>` |
| Dos cosas contrastadas | `comparar` | listas ✓ / × |
| Una definición | `lado-foto` | foto, frase, 3 a 5 puntos |
| Un caso real de marca | `caso` | datos, cifra, captura |
| Una cita de un referente | `cita` | frase, firma, retrato |
| Un diagrama o captura ajena | `figura` | título que afirma + figura + fuente |
| Una idea que se debe grabar | `mensaje` | una frase con lo clave en negrita |
| Una pregunta o un chiste | `foto-mensaje` | foto con velo |
| Un reto al público | `hands-on` | título, duración, herramienta |
| Un cambio de tema | `separador` | número y frase que provoca |
| Un descanso | `pausa` | foto y hora de vuelta |
| Cómo encaja con lo anterior | `contenido` | `.cascada` o `ruta` |
| Resumen | `contenido` | 3 tarjetas oscuras |

## Recursos narrativos que usa el deck (variar de uno a otro)

Pregunta que provoca · cifra que impacta · caso real con nombre · contraste "es / no es" · metáfora en foto · cita de un referente · meme que alivia · definición con ejemplo · dinámica de activación · "¿Os apetece un ejemplo real?" · resumen en tres ideas · gancho hacia lo siguiente. Un bloque no repite el mismo recurso dos veces seguidas.

## Reglas de diversidad (se comprueban sobre el plan)

- Cada 10 slides, **al menos 5 layouts distintos** y 3 recursos narrativos distintos.
- **Nunca 3 slides seguidas** con el mismo layout (excepto `pasos`).
- `contenido` con tarjetas: **máximo la mitad** de las slides de contenido; el resto usa cifras, cadena, cascada, tabla, comparar, figura o iconos.
- `foto-mensaje` y `mensaje` no suman más de **un tercio** del deck.
- Una slide con foto cada 3 o 4, una de pregunta o reto cada bloque, una de caso o cifra cada bloque.
- Si dos slides seguidas tienen la misma forma de contenido, **combínalas** o cambia una de recurso.
- Cada patrón del catálogo se usa **al menos una vez** por sesión de 40 slides o más.

## Ritmo y elegancia (se comprueban sobre el plan)

Lee `../maquetacion-thc/referencias/diseno-elegante.md`. Además de las reglas de diversidad:

- **Alterna formatos sin que te lo pidan.** Cada 8 slides, mínimo: una a sangre (`lado-foto`, `foto-mensaje`, `pregunta` o `mensaje` con fondo), un visual dibujado (forma → metáfora espacial) y un grupo de tarjetas grises con icono. Si el plan es una sucesión de `contenido` y `figura` de título + una cosa, rehazlo.
- **Lado de la foto:** alterna `izq` y `der` en los `lado-foto`.
- **Visual:** una slide con dibujo cada 3 o 4, no todas. Un dibujo cuando el contenido tiene **forma** (proceso, evolución, tamaño, jerarquía, matriz); si es una definición, un argumento o una lista, texto bien jerarquizado.
- **Método de varias slides** (más de 3): `pasos` con menú persistente y el mismo nombre de paso en la agenda y en la slide-índice.
- **Preguntas:** `pregunta` sobre fondo de acento (verde claro) con una expresión subrayada, no siempre sobre foto.
- **Recuerda los patrones a evitar** al decidir el layout: texto todo en negrita sin apoyo, verde claro en muchos elementos, elementos con solo un título y títulos grandes fuera de portadas, separadores, mensajes y preguntas.

Añade al plan una columna **«Receta»** con la receta de `diseno-elegante.md` que se usa (1 tarjetas grises, 3 pregunta con fondo, 4 visual, 5 menú, 6 imagen lateral) o «—».

## Formato del plan

```
| # | Título (afirma) | Forma del contenido | Recurso | Layout / patrón | Receta | Garabato | Notas (foto, datos, TODO) |
```
Al final, la tabla de recuento: layouts usados, recursos usados, ¿cumple las reglas? Si no cumple, se corrige antes de pasar al maquetado.

## Qué no hace

No inventa contenido para llenar un patrón: si la fuente no tiene una cifra, no hay slide de cifras. La diversidad sale de elegir bien la forma de lo que ya hay, no de añadir material.
