<script setup lang="ts">
// Cuatro (o tres) ideas cortas con un pictograma de línea. Los pictogramas son SVG propios de la marca.
defineProps<{ items?: { icono: string; texto: string }[]; kicker?: string }>()
const iconos: Record<string, string> = {
  camara: '<circle cx="32" cy="30" r="16" fill="none" stroke="currentColor" stroke-width="3"/><circle cx="32" cy="30" r="7" fill="var(--thc-lima)" stroke="currentColor" stroke-width="3"/><path d="M20 54h24M32 46v8" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
  manos: '<path d="M32 50C14 38 12 22 22 18c5-2 8 1 10 5 2-4 5-7 10-5 10 4 8 20-10 32z" fill="var(--thc-lima)" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>',
  ojo: '<path d="M6 32c8-14 18-20 26-20s18 6 26 20c-8 14-18 20-26 20S14 46 6 32z" fill="none" stroke="currentColor" stroke-width="3"/><circle cx="32" cy="32" r="9" fill="var(--thc-lima)" stroke="currentColor" stroke-width="3"/>',
  idea: '<path d="M32 8c-10 0-17 7-17 16 0 6 3 10 7 14 2 2 3 4 3 7h14c0-3 1-5 3-7 4-4 7-8 7-14 0-9-7-16-17-16z" fill="var(--thc-lima)" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M26 52h12M28 58h8" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
  check: '<circle cx="32" cy="32" r="24" fill="var(--thc-lima)" stroke="currentColor" stroke-width="3"/><path d="M21 33l8 8 15-17" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>',
  chat: '<path d="M10 14h44v28H30l-10 10v-10H10z" fill="var(--thc-lima)" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>',
}
</script>

<template>
  <div class="slidev-layout thc-iconos">
    <div class="cabecera"><span class="thc-kicker">{{ kicker }}</span><Logo version="simbolo" ancho="30px" /></div>
    <div class="titulo"><slot /></div>
    <div class="fila">
      <div v-for="(it, i) in items" :key="i" class="item">
        <svg viewBox="0 0 64 64" width="84" height="84" class="icono" v-html="iconos[it.icono] || iconos.check" />
        <p>{{ it.texto }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.cabecera { display: flex; justify-content: space-between; align-items: flex-start; }
.titulo :deep(h1) { margin-top: 0.6rem; }
.thc-iconos { display: flex; flex-direction: column; }
.fila { flex: 1; display: flex; justify-content: space-around; align-items: flex-start; gap: 1.5rem; padding-top: 4.5rem; }
.item { flex: 1; display: flex; flex-direction: column; align-items: center; text-align: center; }
.icono { display: block; flex: none; color: var(--thc-verde-oscuro); }
.item p { margin: 1rem 0 0; max-width: 14rem; font-size: 1.05rem; font-weight: 500; color: var(--thc-negro); }
</style>
