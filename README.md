# The Hero Camp · skills de Claude y tema de slides

Este repo tiene dos cosas:

1. **Skills de Claude** para que Claude trabaje con la marca, los formatos y el contenido de The Hero Camp (THC) sin tener que explicárselo cada vez: webs, emails, carruseles, presentaciones y materiales de sesión.
2. **El tema de slides de THC** para [Slidev](https://sli.dev), con sus layouts, estilos, logos y garabatos. La skill `thc-presentaciones` lo usa.

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
| `thc-presentaciones` | Presentaciones de formación y charlas 16:9 en Slidev con el tema de THC: plan slide a slide, montaje y trampas de Slidev, layouts y recetas, garabatos, fotos de bancos libres y revisión. También fichas de ejercicio, documentos y piezas sueltas. Incluye plantilla HTML para piezas sueltas y un script para buscar fotos. |

Para maquetar slides, `thc-presentaciones` necesita el tema y poder ejecutar comandos, así que funciona mejor en Claude Code con este repo clonado (ver abajo).

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

El tema no está publicado en npm. Clona este repo (o añádelo como submódulo) e instala el tema desde su carpeta:

```
npm install -D @slidev/cli slidev-theme-thc@file:<ruta-a-The-Hero-Camp>/slides/tema
```

### Fotos de bancos gratuitos

`thc-presentaciones` incluye `scripts/buscar-imagen.py`, que busca y descarga fotos de Pexels, Unsplash o Pixabay con claves gratuitas. Copia `.env.example` a `.env` en la carpeta desde la que lo ejecutes y rellénalas. `.env` no se sube a Git.

## Estructura

```
.claude-plugin/marketplace.json   lista de plugins del repo
plugins/
  comunicacion/                   un plugin por área
    .claude-plugin/plugin.json
    skills/<skill>/SKILL.md       una carpeta por skill, con sus plantillas y referencias
slides/tema/                      tema de Slidev: layouts, estilos, componentes, logos
  ilustraciones/                  garabatos de marca (SVG) con su índice
  muestra.md                      todos los layouts en una presentación
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
3. Nombres en minúsculas y con guiones, empezando por `thc-`.
4. Si usa la marca, di en el `SKILL.md` que use `thc-marca`. No copies colores ni logos.
5. Ejecuta `./empaquetar.sh` para regenerar los `.zip`, sube la versión en `plugins/<area>/.claude-plugin/plugin.json` y haz commit.

## Marca

Los logos, las ilustraciones, las tipografías elegidas y la guía de marca son de The Hero Camp. Puedes usar las skills y el tema como referencia, pero no uses la marca de THC en piezas que no sean de THC.
