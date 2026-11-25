<script setup lang="ts">
// Cita: frase en fuente de acento lima, autor en mono
defineProps<{ autor?: string; kicker?: string; rol?: string }>()
</script>

<template>
  <div class="slidev-layout thc-cita">
    <span class="thc-kicker">{{ kicker }}</span>
    <div class="cuerpo">
      <div class="texto"><slot /></div>
      <div v-if="autor" class="firma">
        <div class="retrato"><slot name="retrato" /></div>
        <p class="autor">{{ autor }}<template v-if="rol"><br />{{ rol }}</template></p>
      </div>
    </div>
    <Logo version="simbolo" ancho="30px" class="logo" />
  </div>
</template>

<style scoped>
.thc-cita { display: flex; flex-direction: column; position: relative; }
.cuerpo { flex: 1; display: flex; flex-direction: column; justify-content: center; }
.texto :deep(p) { font-family: var(--thc-acento); color: var(--thc-lima); font-size: 2.1rem; line-height: 1.25; max-width: 80%; }
.firma { display: flex; align-items: center; gap: 0.9rem; margin-top: 0.6rem; }
.retrato:empty { display: none; }
.retrato { width: 56px; height: 56px; border-radius: 50%; overflow: hidden; border: 2px solid var(--thc-lima); }
.retrato :deep(img) { width: 100%; height: 100%; object-fit: cover; object-position: center top; margin: 0; }
.autor { font-family: var(--thc-mono); color: var(--thc-gris-oscuro); font-size: 0.8rem; margin: 0; line-height: 1.4; }
.logo { position: absolute; right: 3.5rem; top: 3rem; }
</style>
