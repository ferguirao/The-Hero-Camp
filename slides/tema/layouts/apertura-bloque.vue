<script setup lang="ts">
// Apertura de bloque: fondo negro, letra del bloque en mono + título, como "04. Recursos visuales"
defineProps<{ bloque?: string; pregunta?: string }>()
</script>

<template>
  <div class="slidev-layout thc-apertura thc-fondo-negro">
    <div class="pie">
      <p v-if="pregunta" class="pregunta">{{ pregunta }}</p>
      <div class="titulo">
        <span v-if="bloque" class="numero">{{ bloque }}.</span>
        <slot />
      </div>
    </div>
    <Logo version="simbolo" color="var(--thc-lima)" ancho="40px" class="logo" />
  </div>
</template>

<style scoped>
.thc-apertura { display: flex; align-items: flex-end; position: relative; }
.titulo { display: flex; align-items: baseline; gap: 0.6rem; }
.numero { font-family: var(--thc-mono); color: var(--thc-gris-medio); font-size: 2.2rem; }
.titulo :deep(h1) { color: var(--thc-blanco); font-weight: 400; font-size: 2.2rem; margin: 0; }
.pie { max-width: 70%; }
.pregunta { color: var(--thc-gris-medio); font-size: 1.1rem; margin-bottom: 1rem; }
.logo { position: absolute; right: 3.5rem; top: 3rem; }
</style>
