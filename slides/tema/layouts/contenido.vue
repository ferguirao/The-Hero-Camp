<script setup lang="ts">
// Contenido: fondo blanco, kicker mono arriba a la izquierda, símbolo pequeño arriba a la derecha
defineProps<{ kicker?: string }>()
</script>

<template>
  <div class="slidev-layout thc-contenido">
    <div class="cabecera">
      <span class="thc-kicker">{{ kicker }}</span>
      <Logo version="simbolo" ancho="30px" />
    </div>
    <div class="cuerpo"><slot /></div>
  </div>
</template>

<style scoped>
.cabecera { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1.4rem; }
</style>
