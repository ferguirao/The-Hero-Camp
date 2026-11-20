---
name: thc-web
description: Cómo maquetar webs, landings, campañas (Black Friday, lanzamientos) y emails de The Hero Camp con la estructura y los componentes de la web real. Úsala con thc-marca cuando haya que diseñar o programar una página o un email.
---

# Webs, landings y emails · The Hero Camp

Primero lee entera `thc-marca`. Esta skill dice cómo se componen las páginas. Las medidas salen del diseño de la home de theherocamp.com (ver `thc-marca/referencias/si/`).

## Ritmo de una página

Las secciones alternan **verde oscuro** y **verde fondo `#F4FAF1`**, con un bloque en verde claro `#EAFFBF` como mucho. Nunca dos secciones seguidas con el mismo fondo, salvo el footer. Cada sección tiene una sola idea, un titular y, como mucho, dos botones.

Orden típico de una landing:

1. Hero (oscuro)
2. Prueba social: logos de empresas o cifras (claro)
3. La oferta: cursos o packs (claro u oscuro)
4. Personas: profesores o alumnos con foto (claro)
5. Cómo es la experiencia: teoría, práctica, mentoría, con fotos (claro)
6. Empresas o bloque de cierre con botón (oscuro)
7. Preguntas frecuentes (claro)
8. Footer (oscuro)

## Componentes

**Cabecera.** Sobre verde oscuro. Logo blanco en SVG a la izquierda (40–56 px de alto, nunca el nombre en texto), enlaces en blanco a 16 px Medium y un botón principal lima a la derecha.

**Banner superior de campaña** (opcional). Franja fina en lima con texto verde oscuro de 14 px SemiBold en mayúsculas con tracking +1 %. Una línea.

**Hero.** Fondo verde oscuro, todo centrado, con mucho aire arriba (unos 190 px) y ancho de texto de unos 680 px.

- Titular H1 en blanco, una palabra en pastilla rosa.
- Entradilla Body L en blanco.
- 32 px más abajo, botón principal (lima) y secundario (borde blanco de 1 px con flecha →), separados 12 px.
- Debajo, la prueba social pequeña: fila de avatares de 32 px y "Únete a más de **+3000** alumnos" en 14 px gris claro con la cifra en blanco.
- Doodles en blanco al 10–20 % de opacidad repartidos por los laterales.
- Remata con una tira de retratos en blanco y negro, cada uno con su marco dibujado a mano en blanco y el logo de su empresa en blanco encima.

**Cabecera de sección.** Manuscrito pequeño en rosa o verde oscuro (sobre claro) o lima (sobre oscuro). Debajo, el titular H2 centrado y una entradilla de una o dos líneas en gris.

**Tarjetas de curso.** Bloques en verde oscuro con esquinas rectas y una textura de patrón o doodle sutil. Nombre del curso en blanco y precio grande en blanco abajo a la derecha. Debajo de la tarjeta, sobre el fondo claro, el área en manuscrito pequeño, el nombre en H5 y una línea de descripción en gris. En una fila de cuatro como mucho. Sin bordes finos, sin badges de ahorro: si hay descuento, el precio antiguo tachado en gris encima del nuevo y punto.

**Personas.** Cuadrícula de fotos en blanco y negro con el nombre y el cargo en una franja verde oscuro debajo, en blanco y gris claro.

**Experiencia o método.** Filas alternas: a un lado un número o manuscrito y el título H4 con dos o tres líneas de texto; al otro, una o dos fotos reales. Separadas por líneas de 1 px.

**Cifras.** Sobre claro, tarjetas verde oscuro con la etiqueta pequeña arriba en gris claro y la cifra grande en blanco (SemiBold, tracking negativo). Un doodle lima cerca para señalarlas.

**Bloque de cierre o empresas.** Sección verde oscuro con manuscrito lima, titular H3 en blanco, entradilla en gris claro y un botón principal lima alineado a la derecha.

**Preguntas frecuentes.** Lista con separadores de 1 px gris claro. Cada pregunta en Body M negro con una flecha → en verde oscuro delante.

**Footer.** Verde oscuro: logo y una frase a la izquierda, formulario de newsletter con botón lima a la derecha, y debajo las columnas de enlaces en blanco con títulos en gris claro.

## Campañas (Black Friday, lanzamientos)

- El descuento va en el titular, con la cifra en lima o en la pastilla rosa ("Un **35 %** menos."). No en badges.
- La cuenta atrás, si la hay, en cifras grandes blancas sobre verde oscuro, sin cajas, con las etiquetas en gris claro debajo.
- El regalo o extra en un bloque verde claro con una ilustración o una foto, y un sello rosa redondo como único elemento girado.
- Los packs se explican con un doodle de camino o con una frase ("Digital PM, después una mentoría y después AI Builder"), nunca con cajitas y flechas.

## Emails

Ancho de 600 px. Cabecera verde oscuro con el logo blanco, cuerpo en verde fondo o blanco con texto negro de 16 px, un único botón principal lima rectangular y un footer verde oscuro. Imágenes con texto alternativo. Si el cliente de correo no carga fuentes web, DM Sans cae a Arial.

`plantillas/hero.html` tiene el hero maquetado como referencia.
