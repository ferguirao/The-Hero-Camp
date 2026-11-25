# Ilustraciones de la marca (garabatos)

Dibujos vectoriales de The Hero Camp, separados del archivo de Figma "Recursos visuales". Un SVG por ilustración, con el recuadro ajustado.

- `*.svg`: 93 ilustraciones. Vista general: `_hoja-principal.png`.
- `confeti/*.svg`: 12 figuras de confeti (gotas, rayitas, puntos, acentos, un camino de trazos...). Vista general: `_hoja-confeti.png`.

`indice.json` describe cada ilustración (significado, roles, tamaño) para elegirla por lo que dice la slide; las reglas de uso están en la skill `thc-presentaciones` (`referencias/garabatos.md`).

## Un solo color

Todas las ilustraciones usan `fill="currentColor"` y llevan en la etiqueta `<svg>` el estilo `color:#003133` (verde oscuro de la marca). Así se ven en verde oscuro por defecto y se recolorean con un único criterio:

- **Incrustadas en HTML o Vue:** `color: var(--thc-lima)` en el elemento o en un ancestro.
- **Como `<img>`:** el color es el del propio archivo; para cambiarlo, incrustar el SVG o usarlo como máscara CSS (como el logo).
- En el diseño original algunas iban en lima, amarillo y rosa; aquí se han unificado a propósito.

## Como se hizo (y limites)

El archivo de Figma venia **plano**: 271 elementos sueltos, sin grupos ni nombres de capa. Se agruparon por cercania y se revisaron contra la composicion completa: los conjuntos que forman una figura (la constelacion, el camino de trazos, la hilera de acentos, "xoxo", la espiral grande con sus marcas, las gotas de cada zona...) estan unidos en un solo archivo. Los **nombres son descriptivos, puestos a ojo** y se pueden renombrar. Algun conjunto puede estar partido o unido de forma distinta a la del disenador.

## Lista

**Ilustraciones:** almohadilla-01, almohadilla-02, arco-con-bucle, avion-de-papel, bocadillo-con-corazon, brote-con-trazo, bucles-grandes, bucles-medios, calavera, cara-sonriente-sin-contorno, carita-sonriente, check, chispa-con-rayitas, chispas-cuatro, chispas-dobles, chispas-tres, cometa-con-estela, constelacion, corazon-alargado, corazon-cometa, corazon-con-bucle, corazon-con-orbita, corazon-con-tallo, corazon-diminuto-01, corazon-diminuto-02, corazon-diminuto-03, corazon-diminuto-04, corazon-doble-trazo, corazon-pequeno-01, corazon-pequeno-02, corazon-relleno, corazon-reticulado, corazon-simple, corona, destello-asterisco, destello-cuatro-puntas, dos-estrellas-garabato, dos-flechas-con-puntos, equis-gruesa, espina-de-pescado, espiral-grande, espiral-pequena-01, espiral-pequena-02, espiral-pequena-03, estrella-con-destellos, estrella-explosion, estrella-fugaz-con-estela, estrella-fugaz-con-rayo, flecha-abajo, flecha-ascendente-con-bucle, flecha-con-bucle, flecha-con-corazon, flecha-con-gafas-de-sol, flecha-con-muelle, flecha-con-rizo, flecha-con-rizo-y-corazon, flecha-curva, flecha-ondulada, flor, globo-corazon, guirnalda-de-corazones, labios, linea-con-bucle, lineas-con-rizos, nube-con-bucles, nube-con-lluvia, nube-con-rayas, nube-rizada, ojo-con-pestanas, ola-con-acento, ola-suave, pez, piruleta, planeta-con-anillo, planeta-con-bandera, ramita, rayo-contorno, rayo-relleno, rizo-con-flecha, rizo-largo-con-rayas, rizos-grandes, rizos-largos, sol-con-cara, torbellino, trazo-con-bucle, trazos-en-v, tulipan, xoxo, zigzag-apretado, zigzag-enredado, zigzag-grande, zigzag-picos, zigzag-suave.

**Confeti:** acentos-en-fila, camino-de-trazos, chispazo-de-rayitas, estallido-de-rayitas, gota-coma, gotas-centro-derecha, gotas-derecha, puntos-abajo, puntos-centro, rayitas-paralelas, trazo-curvo-01, trazo-curvo-02.
