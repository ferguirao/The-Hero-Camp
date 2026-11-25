---
name: imagenes-thc
description: Cómo elegir, descargar, acreditar y colocar fotos en las slides de The Hero Camp usando bibliotecas gratuitas (Pexels, Unsplash, Pixabay), en los formatos de foto del deck DPM61 (foto con mensaje, lado-foto, pausa, ponente, separadores). Úsala al buscar imágenes nuevas para un curso o al sustituir las fotos de archivo y de terceros por otras con licencia clara.
---

# Imágenes para slides

El deck de DPM61 usa fotos de archivo (la mente abierta en neón, las palomas en el cable, el público con las manos alzadas) y capturas de terceros. Para cursos nuevos, y para sustituir lo de terceros, usa bibliotecas con licencia clara. Mira los términos vigentes de cada una antes de depender de ellas.

## Dónde buscar

| Biblioteca | Licencia (resumen, comprobar vigente) | API | Mejor para |
|---|---|---|---|
| **Pexels** | Libre para uso comercial, sin atribución obligatoria | Gratis con clave (`PEXELS_API_KEY`) | Fotos y vídeos de trabajo, oficinas, personas; muy buena búsqueda por orientación y color |
| **Unsplash** | Licencia propia de Unsplash: uso libre, sin atribución obligatoria | Gratis con clave (`UNSPLASH_ACCESS_KEY`); exige registrar la descarga | Fotografía más cuidada y artística, paisajes, texturas |
| **Pixabay** | Licencia de contenido de Pixabay: uso libre | Gratis con clave (`PIXABAY_KEY`) | Ilustraciones, vectores, fotos genéricas |
| **Wikimedia Commons** | Mezcla de licencias; leer cada una | Sin clave | Retratos y fotos históricas (por ejemplo, de autores citados) |

Prohibido sin permiso: fotos sacadas de Google Imágenes, capturas de otros decks y retratos de personas reales sin permiso. Lo ya extraído del deck de David vale solo para uso interno (ver `assets/ORIGEN.md` de la sesión).

## Qué buscar según el formato

Los formatos son los del deck de David, ya en el tema `thc` (`maquetacion-thc`).

| Formato | Foto que funciona | Buscar |
|---|---|---|
| `foto-mensaje` (pregunta o frase sobre foto) | Horizontal, con zonas lisas o desenfocadas donde caiga el texto; tono oscuro o neutro, porque el velo la oscurece | "audience raised hands dark", "empty auditorium", "city skyline dusk", "whiteboard team blurred" |
| `lado-foto` (objetivo, definición) | Vertical o cuadrada, un solo sujeto claro | "architecture minimal", "person looking at horizon", "hands writing notebook" |
| `pausa` (descanso) | Calmada, cálida | "coffee cup table", "empty chair window light" |
| `separador` | Normalmente sin foto (color de marca); si la lleva, una textura o abstracto | "paper texture", "abstract gradient" |
| `pasos` (agenda lateral) | Una imagen larga y suave; el velo claro la apaga | "road mountain", "path forest" |
| `ponente` | Retrato propio de la persona; nunca de archivo | — |
| Metáfora de una frase | Un objeto o escena que lo diga sin texto | "rails workers" (siglo XX), "backpack traveler" (lo que llevamos) |

## Criterios de una buena foto

- **Auténtica, no postal.** Evita lo posado y genérico (gente sonriendo señalando un portátil, apretones de manos, manos con bombillas).
- **Aire para el texto.** Si va con mensaje, que haya una zona sin detalle. Si no la hay, `velo: oscuro` y `caja: true`.
- **Consistencia en una sesión.** Misma temperatura de color (cálida con cálida) y estilo. Una sesión no mezcla blanco y negro con fotos saturadas.
- **Que diga algo.** Si la foto se puede quitar sin perder nada, la slide necesita otra cosa, o ninguna foto.
- **Resolución:** 1600 px de lado largo es suficiente; 2400 para fondo a pantalla completa.
- **Personas reales reconocibles:** solo con permiso o con modelo liberado (las bibliotecas lo suelen indicar).

## Flujo

1. Decide el formato de la slide y qué idea debe sugerir la foto.
2. Busca con el script o a mano:
   ```bash
   python3 scripts/buscar-imagen.py "audience raised hands" --fuente pexels --orientacion landscape --n 6
   ```
   Devuelve una lista (id, autor, URL, tamaño). Mira 4 a 6 candidatas, no la primera.
3. Descarga la elegida a los assets del curso:
   ```bash
   python3 scripts/buscar-imagen.py --descargar <fuente>:<id> --a cursos/<curso>/sesiones/<sesion>/assets/nombre-claro.jpg
   ```
   Escribe también la línea de crédito en `assets/ORIGEN.md` (autor, URL, licencia, fecha).
4. Colócala por slot (`::foto::`) con el layout adecuado y comprueba el resultado en la hoja de contacto (`revisar-slides`).
5. Si cambias una foto de David por una nueva, deja la antigua fuera del deck, no la borres de `assets/` hasta que nadie la use.

## Dónde están las claves

En `.env` en la raíz del repo (ignorado por Git; plantilla en `.env.example`). El script lo lee solo. Nunca pegues una clave en un archivo que se suba, en un commit ni en el chat.

## Si no hay claves de API

Las tres APIs son gratuitas y piden registrarse. Sin claves, busca a mano en la web de la biblioteca, descarga el archivo y regístralo con la misma línea de `ORIGEN.md`. No inventes autores ni licencias: si no sabes la licencia exacta, no se usa.

## Crédito

Las licencias de Pexels, Unsplash y Pixabay no exigen atribución, pero se anota siempre en `ORIGEN.md` y, si la imagen es protagonista, en el pie de la slide (`fuente`).
