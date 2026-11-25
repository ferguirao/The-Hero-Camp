# Revisar slides

## Bucle visual

1. Exporta a PNG: `npx slidev export <deck> --format png --output <carpeta>` (solo las tocadas: `--range N`).
2. Monta hojas de contacto de 6 slides (2 × 3) con el número visible y míralas una a una.
3. Anota los problemas por número de slide y arregla por lotes.
4. Reexporta las slides tocadas, y todas las de un layout si cambiaste el layout.

No des el trabajo por terminado sin haber mirado los PNG.

## Qué mirar

- **Desborde:** texto cortado, figura que tapa el título, pie encima del contenido.
- **Huecos:** más de un tercio vacío sin intención, imagen que no carga, slot vacío.
- **Aire:** título separado del contenido, nada pegado al borde ni al logo. Si se ve apretado, sube el espacio o recorta texto; no bajes la letra.
- **Saltos de línea:** ningún título parte una expresión ni deja una palabra suelta (`.linea`, `.nb`).
- **Jerarquía:** una cosa domina y el título afirma algo.
- **Negrita:** nada con todo el texto en negrita sin texto ligero cerca; títulos de contenido en peso 400 con negrita solo en lo clave y hasta 1,7 rem.
- **Verde claro:** no más del 20 % de la slide ni en muchos elementos; sin texto gris dentro.
- **Cajas vacías:** ninguna con solo un título.
- **Ritmo:** cada 8 slides, una a sangre, un visual y un grupo de tarjetas; no más de 3 seguidas del mismo layout.
- **Garabatos:** todos los separadores con uno; ninguno repetido sin motivo, contradiciendo el mensaje o dominando; color correcto sobre el fondo.
- **SVG:** si un texto sale gigante, lleva el tamaño en atributo y no en `style`.
- **Marca:** colores y fuentes del tema; manuscrito solo donde toca; logo bien puesto.
- **Datos:** nada inventado. Lo que falta, `TODO(autor)`. Cifras ajenas con fuente.
- **Imágenes:** crédito anotado.
- **Hilo:** leyendo solo los títulos se entiende el argumento.
- **Ejercicios:** cada hands on con duración, herramienta y enunciado de una frase.

## Informe

Lista corta: lo arreglado, lo abierto con su número de slide y los `TODO(autor)` que quedan.
