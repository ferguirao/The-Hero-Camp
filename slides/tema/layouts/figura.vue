<script setup lang="ts">
// Una figura (diagrama, captura, esquema) con título de acción arriba y fuente debajo. La figura va en el slot `cuerpo` (::cuerpo:: + imagen Markdown o HTML); lo que va debajo de ella, en el slot `pie` (::pie::).
const props = withDefaults(defineProps<{ fuente?: string; kicker?: string; alto?: string; fondo?: 'claro' | 'sutil' }>(), { alto: '340px', fondo: 'claro' })
</script>

<template>
  <div class="slidev-layout thc-figura" :class="`fondo-${props.fondo}`">
    <div class="cabecera"><span class="thc-kicker">{{ props.kicker }}</span><Logo version="simbolo" ancho="26px" /></div>
    <div class="titulo"><slot /></div>
    <div class="marco" :style="{ height: props.alto }"><slot name="cuerpo" /></div>
    <div class="resto"><slot name="pie" /></div>
    <p v-if="props.fuente" class="fuente pie">{{ props.fuente }}</p>
  </div>
</template>

<style scoped>
.cabecera { display: flex; justify-content: space-between; align-items: flex-start; }
.titulo :deep(h1) { font-size: 1.7rem; margin: 0.5rem 0 0.8rem; }
.titulo :deep(p) { font-size: 0.95rem; color: var(--thc-gris-oscuro); margin: 0.2rem 0 0; }
.marco { display: flex; align-items: center; justify-content: center; margin-top: 1.2rem; }
.marco :deep(p) { margin: 0; height: 100%; display: flex; justify-content: center; align-items: center; }
.marco :deep(img) { max-width: 100%; max-height: 100%; object-fit: contain; margin: 0 auto; }
.resto { margin-top: 1.1rem; }
.pie { position: absolute; left: 3.5rem; bottom: 1.3rem; margin: 0; }
.fondo-sutil { background: var(--thc-gris-sutil); }
</style>
