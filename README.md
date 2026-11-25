# The Hero Camp · skills de Claude y tema de slides

Este repo tiene dos cosas:

1. **Skills de Claude** para que Claude trabaje con la marca, los formatos y el contenido de The Hero Camp (THC) sin tener que explicárselo cada vez: webs, emails, carruseles, presentaciones y materiales de sesión.
2. **El tema de slides de THC** para [Slidev](https://sli.dev), con sus layouts, la guía de marca de slides, los logos y los garabatos. Las skills de presentaciones lo usan.

## Qué incluye

Todas las skills están en el plugin `comunicacion`.

**Marca, web y redes**

| Skill | Para qué |
| --- | --- |
| `thc-marca` | Sistema visual con valores exactos: color de texto por fondo, pesos, bordes y sombras, botones, espaciado, componentes y logo, y qué colores y fuentes se heredan en slides. Incluye referencias de lo que sí y lo que no. La usan las demás. |
| `thc-web` | Webs, landings, campañas y emails con la estructura y los componentes de la web real. Incluye una página de ejemplo con todos los componentes. |
| `thc-carrusel-caso` | Carrusel de LinkedIn/Instagram y texto del post contando una formación in-company. Incluye plantilla HTML. |

**Presentaciones**

| Skill | Para qué |
| --- | --- |
| `thc-presentaciones` | Punto de entrada: cómo se hacen las presentaciones de formación y las charlas 16:9 con el tema de slides, y cómo aplicar la marca a fichas de ejercicio, documentos y piezas sueltas. Incluye plantilla HTML para piezas sueltas. |
| `elegir-slide` | Decide, antes de maquetar, qué tipo de slide y qué forma de contarlo lleva cada slide. |
| `maquetacion-thc` | Layouts del tema, cuándo usar cada uno, densidad, imágenes y trampas técnicas de Slidev. |
| `garabatos-thc` | Qué garabatos de marca poner en cada slide y dónde. |
| `imagenes-thc` | Buscar, descargar, acreditar y colocar fotos de bancos gratuitos (Pexels, Unsplash, Pixabay). |
| `revisar-slides` | Lista de revisión y comprobación visual antes de dar unas slides por buenas. |

Las cinco últimas necesitan el tema de slides y poder ejecutar comandos, así que funcionan mejor en Claude Code (ver abajo).

## Instalar las skills

### En Claude Code (recomendado)

```
/plugin marketplace add ferguirao/The-Hero-Camp
/plugin install comunicacion@the-hero-camp
```

Para tenerlas siempre en un proyecto, añade esto a su `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "the-hero-camp": { "source": { "source": "github", "repo": "ferguirao/The-Hero-Camp" } }
  },
  "enabledPlugins": { "comunicacion@the-hero-camp": true }
}
```

### En claude.ai

1. Descarga los `.zip` de la carpeta [`dist/`](dist).
2. En claude.ai, abre la configuración, ve a la sección de Skills y sube cada `.zip`. Sube siempre `thc-marca`, porque las demás dependen de ella.
3. Pídele a Claude, por ejemplo: "Haz el carrusel de la formación que hicimos en [empresa]" o "Maqueta esta landing con la marca de THC".

Cuando una skill cambia, hay que volver a subir su `.zip`.

## Usar el tema de slides

### Probarlo en este repo

Necesitas Node 20 o superior.

```
git clone https://github.com/ferguirao/The-Hero-Camp
cd The-Hero-Camp
npm install
npm run muestra        # abre slides/tema/muestra.md con todos los layouts
```

Para una presentación tuya, crea un `slides.md` con `theme: thc` en el encabezado y ábrelo con `npx slidev ruta/slides.md`. Para el PDF, `npx slidev export ruta/slides.md` (la primera vez, `npx playwright install chromium`).

### Usarlo desde otro proyecto

El tema no está publicado en npm. Lo más sencillo es traer este repo como submódulo e instalar el tema desde ahí:

```
git submodule add https://github.com/ferguirao/The-Hero-Camp vendor/the-hero-camp
npm install -D @slidev/cli slidev-theme-thc@file:vendor/the-hero-camp/slides/tema
```

Así lo usa el repo de cursos de THC (Course-Builder), que además enlaza `slides/tema`, `compartido/marca` y las skills de presentaciones a ese submódulo para que las rutas sean las mismas en los dos repos. Para actualizarlo: `git submodule update --remote vendor/the-hero-camp`.

### Fotos de bancos gratuitos

`imagenes-thc` usa `scripts/buscar-imagen.py`, que necesita claves gratuitas de Pexels, Unsplash o Pixabay. Copia `.env.example` a `.env` y rellénalas. `.env` no se sube a Git.

## Estructura

```
.claude-plugin/marketplace.json   lista de plugins del repo
plugins/
  comunicacion/                   un plugin por área
    .claude-plugin/plugin.json
    skills/<skill>/SKILL.md       una carpeta por skill, con sus plantillas y referencias
slides/tema/                      tema de Slidev (layouts, estilos, componentes, logos)
compartido/marca/                 guía de marca de slides, logos e ilustraciones (garabatos)
scripts/buscar-imagen.py          búsqueda y descarga de fotos para imagenes-thc
dist/                             un .zip por skill, para claude.ai
empaquetar.sh                     regenera dist/
```

## Añadir o cambiar una skill

1. Decide el área. Si encaja en un plugin que ya existe, crea la carpeta en `plugins/<area>/skills/<nombre-skill>/`. Si es un área nueva (por ejemplo `cursos`), crea `plugins/cursos/` con su `.claude-plugin/plugin.json` y añádelo a `.claude-plugin/marketplace.json`.
2. Dentro, un `SKILL.md` con esta cabecera:

   ```
   ---
   name: nombre-skill
   description: Qué hace y cuándo usarla, en una o dos frases. Es lo que Claude lee para decidir si la usa.
   ---
   ```

   Debajo, las instrucciones. Plantillas, imágenes o datos van en la misma carpeta.
3. Nombres en minúsculas y con guiones. Las skills nuevas empiezan por `thc-` (las de presentaciones heredadas de Course-Builder conservan su nombre para no romper referencias).
4. Si usa la marca, di en el `SKILL.md` que use `thc-marca`. No copies colores ni logos.
5. Ejecuta `./empaquetar.sh` para regenerar los `.zip`, sube la versión en `plugins/<area>/.claude-plugin/plugin.json` y haz commit.

## Marca

Los logos, las ilustraciones, las tipografías elegidas y la guía de marca son de The Hero Camp. Puedes usar las skills y el tema como referencia, pero no uses la marca de THC en piezas que no sean de THC.
