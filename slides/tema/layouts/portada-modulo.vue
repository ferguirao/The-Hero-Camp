<script setup lang="ts">
// Portada de módulo: fondo claro, kicker mono con bloque y módulo, título y símbolo en verde oscuro
withDefaults(defineProps<{ kicker?: string; audiencia?: string; desvio?: boolean; garabato?: string }>(), { garabato: 'flecha-ondulada' })
</script>

<template>
  <div class="slidev-layout thc-portada-modulo">
    <div class="cabecera">
      <span class="thc-kicker">{{ kicker }}<template v-if="desvio"> · Desvío de profundidad</template></span>
      <Logo version="simbolo" ancho="40px" />
    </div>
    <div class="contenido">
      <Garabato v-if="garabato && garabato !== 'ninguno'" :nombre="garabato" color="lima" ancho="110px" class="flecha" />
      <slot />
      <p v-if="audiencia" class="thc-kicker">Para: {{ audiencia }}</p>
    </div>
  </div>
</template>

<style scoped>
.thc-portada-modulo { display: flex; flex-direction: column; justify-content: space-between; }
.cabecera { display: flex; justify-content: space-between; align-items: flex-start; }
.contenido { margin-bottom: 1rem; }
.flecha { margin-bottom: 1rem; }
.contenido :deep(h1) { font-size: 2.6rem; }
</style>
