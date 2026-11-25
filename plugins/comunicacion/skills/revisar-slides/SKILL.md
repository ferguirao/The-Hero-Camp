---
name: revisar-slides
description: Lista de revisión y bucle de comprobación visual de las slides de un curso de The Hero Camp antes de pasar por una puerta de aprobación. Úsala tras maquetar o modificar slides: exporta, mira hojas de contacto, detecta desbordes, huecos, repeticiones, texto de relleno y datos inventados.
---

# Revisar slides

## Bucle visual

1. Exporta: `npx slidev export <deck> --format png --output <carpeta>`.
2. Monta hojas de contacto de 6 slides (2 columnas, 3 filas) con numeración visible y míralas una a una. Sin poppler ni PIL se puede hacer con Swift y AppKit.
3. Anota por número de slide los problemas y arregla por lotes.
4. Reexporta y comprueba solo las slides tocadas, más las que usen el mismo layout si cambiaste un layout.

## Qué mirar

- **Desborde:** texto cortado abajo, figura que tapa el título, pies encima del contenido.
- **Huecos:** más de un tercio de la slide vacío sin intención; imagen que no carga; slot vacío.
- **Garabatos:** separadores con garabato, ninguno repetido sin motivo ni que contradiga el mensaje, uno por slide, color correcto sobre el fondo (ver `garabatos-thc`).
- **Aire:** título separado del contenido, tarjetas separadas de las notas, nada apelotonado ni pegado al borde (ver "Espacios y ritmo vertical" en `maquetacion-thc`). Si se ve apretado, sube el espacio o recorta contenido.
- **Saltos de línea:** ningún título parte una expresión por la mitad ni deja una palabra o una pregunta cortada; si pasa, `.linea` o `.nb` (ver `maquetacion-thc`).
- **Jerarquía:** una cosa domina la slide; el título afirma algo.
- **Negrita:** ninguna tarjeta, chip, eslabón o título lleva todo su texto en negrita sin texto más ligero cerca. En títulos de contenido, peso 400 con negrita solo en lo clave.
- **Verde claro:** no más de un 20 % de la slide ni en grupos de muchos elementos (usa el gris sutil). Sin texto gris dentro de verde. Los fondos oscuros son `--thc-verde-oscuro`, nunca un negro nuevo.
- **Elementos vacíos:** ninguna caja con solo un título y nada más.
- **Títulos:** en slides de contenido, hasta 1,7 rem; los grandes solo en portada, separador, mensaje o pregunta.
- **Ritmo de formatos:** en cada 8 slides hay una a sangre, un visual dibujado y un grupo de tarjetas con jerarquía; no hay más de 2 seguidas de «título + un bloque» (ver `maquetacion-thc/referencias/diseno-elegante.md`).
- **SVG:** el texto de los SVG lleva el tamaño en `style`, no en atributos (si se ve gigante, es eso).
- **Variedad:** no más de 3 slides seguidas del mismo layout; hay pausas visuales.
- **Marca:** colores, tipografías, fuente de acento solo donde toca, logo bien puesto.
- **Datos:** nada inventado; lo que falta es `TODO(autor)` o `UNKNOWN`; las cifras ajenas llevan fuente.
- **Imágenes:** crédito visible, nota de uso interno, memes marcados.
- **Voz:** pasa por `voz-thc` y por `humanizer`.
- **Hilo:** test de las slides fantasma (solo los títulos cuentan el argumento); en módulos del macrocurso, `python3 scripts/comprobar-hilo.py`.
- **Ejercicios:** cada hands on trae duración, herramienta y enunciado de una frase.

## Informe

Una lista corta: problemas arreglados, problemas abiertos con su slide y qué `TODO(autor)` quedan. No des el trabajo por terminado con problemas abiertos sin decirlo.
