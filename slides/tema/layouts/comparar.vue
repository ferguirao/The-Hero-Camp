<script setup lang="ts">
// Dos columnas contrastadas ("Roadmap" frente a "No es un roadmap"). Usa ::izq:: y ::der:: para cada columna.
defineProps<{ izq?: string; der?: string; kicker?: string }>()
</script>

<template>
  <div class="slidev-layout thc-comparar">
    <div class="cabecera"><span class="thc-kicker">{{ kicker }}</span><Logo version="simbolo" ancho="26px" /></div>
    <div class="titulo"><slot /></div>
    <div class="cols">
      <section class="col si">
        <h3><span class="marca">✓</span>{{ izq }}</h3>
        <div class="checklist"><slot name="izq" /></div>
      </section>
      <section class="col no">
        <h3><span class="marca">×</span>{{ der }}</h3>
        <div class="aspas"><slot name="der" /></div>
      </section>
    </div>
  </div>
</template>

<style scoped>
.cabecera { display: flex; justify-content: space-between; align-items: flex-start; }
.titulo :deep(h1) { font-size: 1.7rem; margin: 0.5rem 0 1.5rem; }
.cols { display: grid; grid-template-columns: 1fr 1fr; gap: 1.4rem; }
.col { border-radius: 18px; padding: 1.1rem 1.4rem; min-height: 270px; }
.si { background: var(--thc-verde-claro); }
.no { background: var(--thc-gris-sutil); }
.col h3 { display: flex; align-items: center; gap: 0.6rem; font-size: 1.3rem; margin: 0 0 0.8rem; color: var(--thc-verde-oscuro); }
.marca { display: inline-flex; width: 1.8rem; height: 1.8rem; border-radius: 50%; align-items: center; justify-content: center; font-size: 1.1rem; }
.si .marca { background: var(--thc-lima); color: var(--thc-verde-oscuro); }
.no .marca { background: var(--thc-rosa); color: var(--thc-blanco); }
</style>
