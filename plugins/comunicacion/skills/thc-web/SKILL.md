---
name: thc-web
description: Cómo maquetar webs, landings, campañas (Black Friday, lanzamientos) y emails de The Hero Camp con la estructura y los componentes de la web. Úsala con thc-marca cuando haya que diseñar o programar una página o un email.
---

# Webs, landings y emails · The Hero Camp

Primero lee entera `thc-marca`: colores por fondo, pesos, bordes, sombras y botones salen de ahí. Esta skill dice cómo se compone una página. `plantillas/pagina.html` es una página de ejemplo con todos los componentes maquetados: **parte siempre de ella** y copia sus clases en vez de inventar estilos nuevos.

## Ritmo de una página

La base es **papel `#F4F6F5`**. Las secciones de peso van en **verde oscuro** y alguna en **blanco** para cambiar de ritmo. Nunca dos oscuras seguidas. Entre secciones de distinto fondo, un borde de 2px `--ink`.

Orden típico de una landing:

1. Barra de aviso (amarilla, opcional)
2. Cabecera (blanca)
3. Hero (papel) con muro de fotos
4. Logos de empresas (blanco)
5. La oferta: programas o cursos (oscuro)
6. Método o cómo funciona, en pasos (papel)
7. Banda de cifras (lima)
8. Profesores o personas (papel o blanco)
9. Empresas o casos (oscuro)
10. Preguntas frecuentes (blanco)
11. Contacto (papel, con caja verde claro)
12. Footer (oscuro, con franja lima al final)

## Componentes

**Barra de aviso.** Fondo amarillo, borde inferior de 2px, texto centrado de 14px peso 600 en `--ink`, una línea con un enlace subrayado.

**Cabecera.** Blanca, 72px de alto, borde inferior de 2px. Logo (isotipo + "The Hero / Camp") a la izquierda, enlaces de 15.5px peso 500 con subrayado lima de 3px al pasar el ratón, y a la derecha un botón lima con sombra de 3px.

**Hero.** Fondo papel, borde inferior de 2px. Dos columnas (`1.08fr .92fr`), alineado a la izquierda:

- Arriba, la caja de novedad (etiqueta "NEW" en verde oscuro + texto + flecha).
- H1 con una o dos palabras con subrayado de rotulador.
- Entradilla de 20px en `--cuerpo`.
- Botón principal lima y secundario blanco, separados 14px.
- Debajo, tres pruebas en fila separadas por una línea de 1px `--linea` arriba: cifra en 26px 700 y texto de 14px en `--gris` ("+3.000 alumnos", "4,8/5 de valoración"…).
- A la derecha, el muro de retratos: fondo verde oscuro, borde de 2px y sombra, tres columnas de fotos a color con el nombre y la empresa en una franja verde oscuro.

**Logos de empresas.** Fondo blanco, borde superior de 2px, rótulo pequeño en mayúsculas y los logos en fila, monocromos en `--gris`.

**Cabecera de sección.** Dos columnas alineadas abajo: manuscrito + H2 a la izquierda, entradilla en `--gris` a la derecha.

**Tarjeta de programa.** Blanca, borde de 2px, sombra `5px 5px 0 var(--lime)` (sobre oscuro se ve la sombra lima). Imagen 16:10 con borde inferior de 2px, etiqueta de fecha en la esquina y como mucho una pegatina amarilla girada. Cuerpo con H3 de 22px, una línea de descripción en `--cuerpo`, datos en etiquetas pequeñas y aviso de plazas en manuscrito rosa. Pie con línea de 1px `--linea`: precio tachado en `--gris` encima del precio en 26px 700, y "Ver programa →" a la derecha. Rejilla de tres o cuatro.

**Pasos del método.** Tarjetas blancas con borde de 2px y sombra `--ink`. Número de 54px peso 900 solo con contorno de 2px (se rellena de lima al pasar el ratón), H3, dos líneas de texto y una foto 4:3 con borde.

**Banda de cifras.** Fondo lima, bordes de 2px arriba y abajo, cuatro columnas separadas por líneas de 2px. Cifra en 700 y etiqueta de 16px peso 500, todo en `--ink`.

**Profesores.** Foto 3:4 con borde de 2px y sombra, etiqueta de empresa blanca encima, nombre en H3 de 20px y cargo en `--gris`. Flechas de carrusel cuadradas con borde de 2px y sombra de 3px.

**Empresas y casos.** Sección oscura. A la izquierda una lista de pestañas separadas por líneas blancas al 20 %; la elegida, con fondo lima y texto `--ink`. A la derecha la tarjeta del caso, blanca, con borde de 2px y sombra `6px 6px 0 var(--lime)`, cita de 22–34px peso 500 y el autor debajo.

**Preguntas frecuentes.** Fondo blanco. Lista con borde superior de 2px y cada pregunta con borde inferior de 2px. Pregunta de 20px peso 600 y a la derecha un cuadrado de 30px con borde de 2px y un +. Abierta: fondo verde claro y cuadrado en lima.

**Contacto.** Caja verde claro con borde de 2px y sombra `8px 8px 0 var(--ink)`. Dentro, el H2, la entradilla y un botón `btn-oscuro`, o tarjetas blancas de contacto (email, teléfono) con borde de 2px y sombra de 4px.

**Footer.** Verde oscuro. Arriba un lema grande (`clamp(34px,4.4vw,62px)`, 700) con una palabra en lima. Boletín: etiqueta en manuscrito amarillo, campo blanco con borde de 2px y sombra lima, botón lima pegado. Columnas de enlaces con títulos en rótulo pequeño `#9FBAB6` y enlaces en blanco. Redes en cuadrados de 42px con borde blanco de 2px. Abajo, "The Hero Camp" gigante en blanco al 8 % y una franja lima con el copyright en `--ink`.

## Campañas (Black Friday, lanzamientos)

- El descuento va en el titular con subrayado de rotulador ("Un **35 % menos** en todos los programas"). Nunca en badges.
- La barra de aviso amarilla anuncia la campaña y la fecha de fin.
- La cuenta atrás, si la hay, va en la banda lima: cifras grandes en 700 separadas por líneas de 2px, con la etiqueta debajo.
- El regalo o extra va en una caja verde claro con borde y sombra, con una pegatina girada.
- Los packs se explican con una frase o con pasos numerados con contorno, nunca con cajitas unidas por flechas.

## Emails

600px de ancho. Cabecera blanca con el logo y borde inferior de 2px; cuerpo en papel con texto `--ink` de 16px; titulares en 700; un único botón lima con borde de 2px (la sombra con `box-shadow` no sale en todos los clientes de correo, así que añade un borde inferior y derecho de 4px como alternativa). Footer verde oscuro con texto blanco y `#C5D8D5`. Si no carga DM Sans, cae a Arial.
