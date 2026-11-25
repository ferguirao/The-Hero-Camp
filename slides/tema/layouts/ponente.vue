<script setup lang="ts">
// Presentación de la persona que imparte: retrato en círculo, nombre grande, rol, lo más característico en puntos y un enlace.
// puntos: lista corta (3 o 4) de lo más característico de la persona.
defineProps<{ nombre?: string; rol?: string; frase?: string; puntos?: string[]; enlace?: string; cierre?: boolean }>()
</script>

<template>
  <div class="slidev-layout thc-ponente" :class="{ cierre }">
    <div class="texto">
      <div class="titulo"><slot /></div>
      <p v-if="nombre" class="nombre">{{ nombre }}</p>
      <p v-if="rol" class="rol thc-kicker">{{ rol }}</p>
      <ul v-if="puntos?.length" class="puntos"><li v-for="(p, i) in puntos" :key="i">{{ p }}</li></ul>
      <p v-if="frase" class="frase">{{ frase }}</p>
      <p v-if="enlace" class="enlace thc-kicker">{{ enlace }}</p>
    </div>
    <div v-if="$slots.foto" class="retrato"><slot name="foto" /></div>
    <Logo version="simbolo" ancho="26px" class="logo" :color="cierre ? 'var(--thc-verde-oscuro)' : 'var(--thc-lima)'" />
  </div>
</template>

<style scoped>
.thc-ponente { background: var(--thc-verde-oscuro); color: var(--thc-blanco); display: flex; align-items: center; justify-content: space-between; gap: 2rem; position: relative; }
.thc-ponente.cierre { background: var(--thc-lima); color: var(--thc-verde-oscuro); }
.texto { flex: 1; }
.titulo :deep(h1) { color: var(--thc-lima); font-family: var(--thc-acento); font-weight: 400; font-size: 3rem; margin-bottom: 1.2rem; }
.cierre .titulo :deep(h1) { color: var(--thc-verde-oscuro); }
.nombre { font-size: 2.4rem; font-weight: 700; line-height: 1.1; margin: 0; }
.rol { color: var(--thc-gris-claro); margin: 0.5rem 0 1.1rem; }
.puntos { margin: 0 0 1rem; padding-left: 1.4rem; list-style: disc; }
.puntos li { list-style: disc; }
.puntos li { font-size: 1.1rem; margin: 0.4rem 0; }
.puntos li::marker { color: var(--thc-lima); }
.cierre .puntos li::marker { color: var(--thc-verde-oscuro); }
.cierre .rol, .cierre .frase, .cierre .enlace { color: var(--thc-verde-oscuro); }
.frase { max-width: 85%; color: var(--thc-gris-claro); font-size: 0.95rem; }
.enlace { margin-top: 0.8rem; }
.retrato { width: 230px; height: 230px; border-radius: 50%; overflow: hidden; flex: none; border: 3px solid var(--thc-lima); }
.retrato :deep(img) { width: 100%; height: 100%; object-fit: cover; object-position: center top; margin: 0; }
.cierre .retrato { border-color: var(--thc-verde-oscuro); }
.logo { position: absolute; right: 2rem; bottom: 1.6rem; }
</style>
