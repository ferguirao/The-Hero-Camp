<script setup lang="ts">
// Callout: tip, comentario o pregunta de reflexión en fuente de acento sobre fondo sutil
withDefaults(defineProps<{ kicker?: string; garabato?: string }>(), { garabato: 'rayo-contorno' })
</script>

<template>
  <div class="slidev-layout thc-callout thc-fondo-sutil">
    <span class="thc-kicker">{{ kicker }}</span>
    <div class="cuerpo">
      <Garabato v-if="garabato && garabato !== 'ninguno'" :nombre="garabato" color="lima" ancho="64px" class="rayo" />
      <div class="texto thc-acento"><slot /></div>
    </div>
  </div>
</template>

<style scoped>
.thc-callout { display: flex; flex-direction: column; }
.cuerpo { flex: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; }
.rayo { margin-bottom: 1rem; }
.texto :deep(p) { font-family: var(--thc-acento); font-size: 2rem; color: var(--thc-verde-oscuro); max-width: 75%; margin: 0 auto; }
</style>
