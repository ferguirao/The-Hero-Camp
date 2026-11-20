# The Hero Camp · skills de Claude

Skills para que Claude trabaje con el estilo, los formatos y el contenido de The Hero Camp sin tener que explicárselo cada vez.

Las skills se agrupan en plugins, uno por área. Hoy hay uno; la idea es que crezca con los cursos, las formaciones y lo que vayamos necesitando.

| Plugin | Skill | Para qué |
| --- | --- | --- |
| `comunicacion` | `thc-marca` | Sistema visual completo: color de texto por fondo, pesos, botones, líneas, espaciado, doodles, fotos y logo. Incluye referencias de lo que sí y lo que no. La usan las demás. |
| `comunicacion` | `thc-carrusel-caso` | Carrusel de LinkedIn/Instagram y texto del post contando una formación in-company. Incluye plantilla HTML. |
| `comunicacion` | `thc-web` | Webs, landings, campañas y emails con la estructura y los componentes de la web real. Incluye plantilla del hero. |
| `comunicacion` | `thc-presentaciones` | Presentaciones de formación 16:9, fichas de ejercicio, documentos y otras piezas con la marca. Incluye plantilla HTML. |

## Usarlas en claude.ai

1. Descarga los `.zip` de la carpeta [`dist/`](dist). Instala siempre `thc-marca`: las demás dependen de ella.
2. En claude.ai, abre la configuración, ve a la sección de Skills y sube cada `.zip`.
3. Pídele a Claude, por ejemplo: "Haz el carrusel de la formación que hicimos en [empresa]" o "Maqueta esta presentación con la marca de THC".

## Usarlas en Claude Code

```
/plugin marketplace add ferguirao/The-Hero-Camp
/plugin install comunicacion@the-hero-camp
```

## Estructura

```
.claude-plugin/marketplace.json   lista de plugins del repo
plugins/
  comunicacion/                   un plugin por área
    .claude-plugin/plugin.json
    skills/
      thc-marca/SKILL.md          una carpeta por skill
      thc-carrusel-caso/SKILL.md
      thc-web/SKILL.md
      thc-presentaciones/SKILL.md
dist/                             un .zip por skill, para claude.ai
empaquetar.sh                     regenera dist/
```

## Añadir una skill

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
5. Ejecuta `./empaquetar.sh` para regenerar los `.zip` y haz commit.

Quien ya tenga las skills en claude.ai tiene que volver a subir el `.zip` de la que haya cambiado.
