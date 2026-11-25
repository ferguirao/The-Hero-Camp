# Slidev con el tema thc: montaje, archivos y trampas

## Dónde está el tema

El tema es el paquete `slidev-theme-thc`, en `slides/tema/` del repo `ferguirao/The-Hero-Camp`:

- `layouts/`: un `.vue` por layout (ver `layouts.md`).
- `styles/base.css`: paleta, tipografías, escala y clases antiguas (`.tarjeta`, `.cifras`, `.cadena`, `.cascada`…).
- `styles/patrones.css`: la capa `p-*`, la que se usa en slides nuevas.
- `components/`: `<Garabato>`, `<Logo>` y `<LogoHerramienta>` (logos de Notion, Slack, OpenAI, Claude, Gmail…).
- `ilustraciones/`: los garabatos de marca, con `indice.json` (ver `garabatos.md`).
- `assets/`: logos de THC en PNG (símbolo, horizontal, apilado, símbolo arriba; en negro y blanco).
- `muestra.md` y `muestra-patrones.md`: todos los layouts y patrones en vivo. Ábrelos antes de maquetar algo que no hayas hecho nunca.

No reconstruyas el tema a mano en HTML. Si el repo no está en la sesión, añádelo.

## Arrancar

Node 20 o superior. En la raíz de The-Hero-Camp:

```bash
npm install
npm run muestra                                   # muestra de layouts
npx slidev ruta/slides.md                         # una presentación, con recarga en vivo
npx playwright install chromium                   # solo la primera vez, para exportar
npx slidev export ruta/slides.md                  # PDF
npx slidev export ruta/slides.md --format png --output carpeta   # PNG por slide
npx slidev build ruta/slides.md --base ./ --out carpeta          # web estática (artifact)
```

Desde otro proyecto: `npm install -D @slidev/cli slidev-theme-thc@file:<ruta>/slides/tema`.

## Headmatter

```yaml
---
theme: thc
title: Título de la sesión
# el tema ya fija: DM Sans / DM Mono / Permanent Marker, 16:9, canvasWidth 980, transición fade, modo claro
src: ./secciones/0-portada.md      # la primera slide se importa aquí para que no salga una vacía
agenda: [Descubrir, Priorizar, Construir]   # solo si usas el layout `pasos`
agendaTitulo: El método
---
```

Si cambias `fonts`, incluye `serif: Permanent Marker` (el tema usa `serif` para el manuscrito). Para que el PDF no pierda la fuente, cárgala en local con `@font-face` y el `.woff2`.

## Estructura de archivos

```
<presentacion>/
  slides.md            headmatter + `src:` a cada sección
  secciones/
    0-portada.md
    1-bloque.md        slides separadas por `---`; el primero no necesita línea previa
  style.css            estilos propios de la presentación (se cargan solo desde aquí, junto al slides.md que ejecutas)
  components/          un .vue por visual dibujado
  assets/              fotos, con ORIGEN.md (créditos)
  public/              lo que se sirve tal cual (img/)
```

Una sección por archivo; `slides.md` solo importa.

## Slots

Las imágenes y el contenido de las zonas de un layout van **por slot**, no como atributo del frontmatter (ahí las rutas no se resuelven):

```md
---
layout: lado-foto
lado: der
ancho: 40%
---

# Título

Texto

::foto::
<img src="../assets/equipo.jpg" />
```

Slots del tema: `::foto::`, `::cuerpo::`, `::pie::`, `::pantalla::`, `::retrato::`, `::izq::`, `::der::`. Rutas relativas a la sección.

## Clicks y visuales

- `v-click` en cada capa de un visual que se cuenta por partes.
- En un componente Vue propio: `const { $clicks } = useSlideContext()` y `clicks: N` en el frontmatter de la slide.
- `hide: true` oculta una slide sin borrarla; el export no la numera.
- Historias, citas largas y fuentes, en las notas del orador (comentario `<!-- -->` al final de la slide).

## Trampas técnicas

- **Texto de SVG gigante:** Slidev (UnoCSS en modo atributos) convierte `font-size="15"` en una clase de 3,75 rem. En SVG, tamaño y peso van en `style="font-size:15px;font-weight:700"`; `fill`, `stroke` y `text-anchor` sí valen como atributos.
- **`</div>` indentado tras una lista Markdown** se traga el cierre. Cierra los `<div>` sin indentar y deja línea en blanco entre HTML y Markdown.
- **`figura`:** lo que va después de `::cuerpo::` comparte fila con el marco; el pie va en `::pie::`, y `alto` tiene que dejar sitio para él.
- **`pasos` en el headmatter** choca con la prop del layout `ruta`; la agenda lateral va en `agenda`.
- **Slidev en modo dev se queda con la lista antigua** cuando cambia el número de slides. Reinicia y recarga; si no, se ven slides mezcladas.
- **Los números de slide se desfasan** al insertar slides. Identifica cada slide por su contenido antes de tocarla (se pueden listar con `@slidev/parser`).
- **`slidev build` falla con `[lightningcss minify] Invalid token in pseudo element`** con las versiones de Vite que trae `@slidev/cli` 53.0.0 en algunos lockfiles. Se arregla actualizando las dependencias (`npm update`); en The-Hero-Camp compila.
- **Artifact:** tras `slidev build --base ./`, quita `404.html` y `_redirects`. Un artifact admite 512 archivos como mucho: borra los assets de builds antiguos antes de subir el nuevo, nunca los del que está en vivo.
- **PDF de imágenes** (cuando lo piden así): PNG de cada slide unidos en un PDF, sin números de página.
- Assets de 1600 px de lado como mucho (2400 si es fondo a pantalla completa).

## Espacios y ritmo vertical

El fallo más común es apelotonar. El tema ya fija el ritmo en `base.css`; no lo encojas para meter más.

- **Título → contenido:** al menos 1,5 rem. Los márgenes se colapsan: un `margin-top` pequeño en línea no lo reduce.
- **Entre bloques:** 1 a 1,3 rem. **Entre tarjetas:** 0,8 a 1 rem. **Notas y fuentes (`.thc-footnote`):** 1,3 rem sobre lo anterior.
- **Dentro de una tarjeta:** relleno de 1 a 1,2 rem; título de tarjeta y texto, 0,35 rem.
- **Mensaje sobre foto:** título y subtexto a 1,1 rem; caja con relleno de 2 × 2,8 rem.
- **Mucho texto:** `class="denso"` baja el cuerpo un punto. Si sigue sin caber, divide en dos slides o pasa a tarjetas: sobra contenido.
- **Alineación:** en filas de iconos o tarjetas, todo arranca a la misma altura (`align-items: flex-start`).
- **Abajo:** al menos 2,5 rem libres; nada pegado al borde ni al logo.
- Nada por debajo de 0,7 rem en pantalla.

## Saltos de línea en títulos

El tema equilibra las líneas (`text-wrap: balance`), pero no entiende el sentido. Cuando una frase tiene dos partes:

- `<span class="linea">¿Y el valor?</span>`: la segunda parte empieza en línea nueva y va entera.
- `<span class="nb">¿Y el valor?</span>`: la expresión no se parte; el salto lo decide el navegador.

Nada de `<br>` ni espacios duros: rompen al cambiar de layout. Con negritas, el `**…**` va dentro del span. Se comprueba en el PNG, no en el código.
