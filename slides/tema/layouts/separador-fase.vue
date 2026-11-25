<script setup lang="ts">
// Separador de fase del bucle: fondo lima, garabato en una esquina, "I. Conviction" abajo a la izquierda
defineProps<{ fase?: string; pregunta?: string; garabato?: string }>()
</script>

<template>
  <div class="slidev-layout thc-separador thc-fondo-lima">
    <Garabato v-if="garabato" :nombre="garabato" color="verde-oscuro" pos="sup-der" ancho="34%" sangrado="1.5rem" />
    <div class="pie">
      <p v-if="pregunta" class="pregunta">{{ pregunta }}</p>
      <div class="titulo">
        <span v-if="fase" class="numero">{{ fase }}.</span>
        <slot />
      </div>
    </div>
  </div>
</template>

<style scoped>
.thc-separador { display: flex; align-items: flex-end; position: relative; }
.titulo { display: flex; align-items: baseline; gap: 0.6rem; }
.numero { font-family: var(--thc-mono); font-size: 2rem; color: var(--thc-verde-oscuro); }
.titulo :deep(h1) { color: var(--thc-verde-oscuro); font-weight: 400; font-size: 2rem; margin: 0; }
.pie { max-width: 70%; }
.pregunta { color: var(--thc-verde-oscuro); font-size: 1.05rem; margin-bottom: 1rem; opacity: 0.8; }
</style>
