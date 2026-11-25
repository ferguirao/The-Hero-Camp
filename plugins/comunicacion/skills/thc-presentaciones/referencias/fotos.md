# Fotos para slides

## De dónde

| Biblioteca | Licencia (comprobar la vigente) | Clave | Mejor para |
|---|---|---|---|
| Pexels | Uso comercial libre, sin atribución obligatoria | `PEXELS_API_KEY` | Trabajo, oficinas, personas |
| Unsplash | Uso libre, sin atribución obligatoria; la API exige registrar la descarga | `UNSPLASH_ACCESS_KEY` | Fotografía cuidada, paisajes, texturas |
| Pixabay | Uso libre | `PIXABAY_KEY` | Ilustraciones, vectores, genéricas |
| Wikimedia Commons | Mezcla de licencias: leer cada una | — | Fotos históricas |

No se usan fotos de Google Imágenes, capturas de decks ajenos ni fotos de personas reales reconocibles sin permiso o modelo liberado. Nada de fotos de personajes públicos descargadas de la web. Los retratos de ponentes, siempre propios.

## Qué foto según el formato

| Formato | Foto que funciona | Búsquedas que dan resultado |
|---|---|---|
| `foto-mensaje` | Horizontal, con zonas lisas o desenfocadas para el texto; tono oscuro o neutro | "audience raised hands dark", "empty auditorium", "city skyline dusk" |
| `lado-foto` | Vertical o cuadrada, un sujeto claro | "architecture minimal", "hands writing notebook" |
| `pausa` | Calmada, cálida | "coffee cup table", "empty chair window light" |
| `separador` | Normalmente sin foto; si la lleva, textura o abstracto | "paper texture" |
| `pasos` | Larga y suave; el velo claro la apaga | "road mountain", "path forest" |
| Cierre | A sangre, con velo degradado desde la izquierda y texto blanco | — |

## Criterios

- Auténtica, no de postal: nada de gente sonriendo a un portátil, apretones de manos ni bombillas.
- Aire para el texto. Si no lo hay: `velo: oscuro` y `caja: true`.
- Una sesión no mezcla blanco y negro con fotos saturadas; misma temperatura de color.
- Si la foto se puede quitar sin perder nada, sobra.
- Mira 4 a 6 candidatas, no la primera.

## Buscar y descargar

Con claves en el entorno o en un `.env` de la carpeta desde la que lo ejecutas (plantilla en `.env.example` de The-Hero-Camp; `.env` no se sube a Git):

```bash
python3 <skill>/scripts/buscar-imagen.py "audience raised hands" --fuente pexels --orientacion landscape --n 6
python3 <skill>/scripts/buscar-imagen.py --descargar pexels:12345 --a <presentacion>/assets/publico.jpg
```

Al descargar, el script añade la línea de crédito (autor, URL, licencia, fecha) en `assets/ORIGEN.md`. Sin claves, se busca en la web de la biblioteca y el crédito se anota a mano. Si no sabes la licencia exacta, no se usa. Nunca pegues una clave en un archivo que se suba ni en el chat.

Si la foto es protagonista, el crédito va también en el pie de la slide (`fuente`).
