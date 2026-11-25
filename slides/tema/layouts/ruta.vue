<script setup lang="ts">
// Hoja de ruta: pasos numerados en línea con el actual destacado ("Nuestro viaje... Hoy"). flechas: true une cada paso con el siguiente.
defineProps<{ pasos?: string[]; actual?: number; marca?: string; flechas?: boolean }>()
</script>

<template>
  <div class="slidev-layout thc-ruta">
    <div class="titulo"><slot /></div>
    <div class="linea" :class="{ flechas }" :style="{ '--n': pasos?.length || 1 }">
      <div v-for="(p, i) in pasos" :key="i" class="paso" :class="{ actual: i + 1 === actual }">
        <span v-if="i + 1 === actual" class="marca thc-acento">{{ marca || 'hoy' }}</span>
        <span class="num">{{ i + 1 }}</span>
        <span class="txt thc-kicker">{{ p }}</span>
      </div>
    </div>
    <Logo version="simbolo" ancho="26px" class="logo" />
  </div>
</template>

<style scoped>
.thc-ruta { position: relative; display: flex; flex-direction: column; }
.titulo :deep(h1) { font-size: 1.7rem; }
.linea { flex: 1; display: flex; justify-content: space-between; align-items: flex-start; padding-top: 7.5rem; }
.paso { width: 10.5%; display: flex; flex-direction: column; align-items: center; gap: 0.7rem; text-align: center; position: relative; padding: 0.8rem 0.2rem; border-radius: 16px; }
.num { width: 44px; height: 44px; border-radius: 50%; border: 2px solid var(--thc-verde-oscuro); background: var(--thc-verde-claro); display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.1rem; }
.txt { color: var(--thc-gris-oscuro); font-size: 0.55rem; line-height: 1.25; }
.actual { background: var(--thc-gris-sutil); outline: 2px solid var(--thc-verde-oscuro); }
.actual .num { background: var(--thc-lima); }
.actual .txt { color: var(--thc-verde-oscuro); font-weight: 700; }
.marca { position: absolute; top: -1.9rem; color: var(--thc-verde-oscuro); font-size: 1.3rem; }
.flechas .paso { --d: calc(((100 - 10.5 * var(--n)) / (10.5 * (var(--n) - 1)) + 1) * 100%); }
.flechas .paso:not(:last-child)::before { content: ''; position: absolute; top: calc(0.8rem + 21px); left: calc(50% + 30px); width: calc(var(--d) - 70px); height: 2px; background: var(--thc-verde-oscuro); }
.flechas .paso:not(:last-child)::after { content: ''; position: absolute; top: calc(0.8rem + 16px); left: calc(50% + 30px + var(--d) - 72px); border-top: 6px solid transparent; border-bottom: 6px solid transparent; border-left: 11px solid var(--thc-verde-oscuro); }
.logo { position: absolute; right: 3.5rem; bottom: 2.4rem; }
</style>
