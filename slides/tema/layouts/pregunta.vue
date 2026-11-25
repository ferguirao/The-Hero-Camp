<script setup lang="ts">
// Pregunta que abre o cierra un módulo: el elemento que más se repite en el curso
defineProps<{ tipo?: 'abre' | 'cierra'; etiqueta?: string; marca?: string }>()
</script>

<template>
  <div class="slidev-layout thc-pregunta thc-fondo-claro">
    <span class="thc-kicker etiqueta">{{ etiqueta ?? (tipo === 'cierra' ? 'Cierra con' : 'Abre con') }}</span>
    <div class="cuerpo">
      <span class="thc-acento marca">{{ marca ?? (tipo === 'cierra' ? 'y ahora…' : 'la pregunta') }}</span>
      <div class="texto"><slot /></div>
    </div>
    <Logo version="simbolo" ancho="34px" class="logo" />
  </div>
</template>

<style scoped>
.thc-pregunta { display: flex; flex-direction: column; justify-content: center; position: relative; }
.etiqueta { position: absolute; top: 3rem; left: 3.5rem; color: var(--thc-gris-oscuro); }
.marca { color: var(--thc-verde-oscuro); font-size: 1.3rem; display: inline-block; transform: rotate(-4deg); margin-bottom: 0.6rem; }
.texto :deep(p), .texto :deep(h1) { font-family: var(--thc-sans); font-size: 2.3rem; font-weight: 500; line-height: 1.2; color: var(--thc-verde-oscuro); max-width: 85%; }
.logo { position: absolute; right: 3.5rem; top: 3rem; }
</style>
