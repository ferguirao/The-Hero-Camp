<script setup lang="ts">
// Descanso o pausa: título grande, hora de vuelta y duración.
defineProps<{ vuelta?: string; duracion?: string }>()
</script>

<template>
  <div class="slidev-layout thc-pausa">
    <div class="fondo"><slot name="foto" /></div>
    <div class="centro">
      <slot />
      <p v-if="duracion" class="duracion">{{ duracion }}</p>
      <p v-if="vuelta" class="vuelta"><span class="thc-kicker">Nos vemos a las</span><br /><span class="hora thc-acento">{{ vuelta }}</span></p>
    </div>
    <Logo version="simbolo" ancho="26px" class="logo" color="var(--thc-lima)" />
  </div>
</template>

<style scoped>
.thc-pausa { background: var(--thc-verde-oscuro); background-size: cover; background-position: center; color: var(--thc-blanco); display: flex; align-items: center; justify-content: center; text-align: center; position: relative; }
.fondo { position: absolute; inset: 0; }
.fondo :deep(img) { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; margin: 0; }
.fondo:not(:empty)::after { content: ''; position: absolute; inset: 0; background: rgba(0, 49, 51, 0.78); }
.centro { position: relative; }
.centro :deep(h1) { color: var(--thc-blanco); font-size: 3rem; }
.duracion { color: var(--thc-gris-claro); font-size: 1.2rem; }
.vuelta { margin-top: 1.4rem; }
.hora { font-size: 3.4rem; }
.logo { position: absolute; right: 2rem; bottom: 1.6rem; }
</style>
