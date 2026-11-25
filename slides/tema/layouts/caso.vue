<script setup lang="ts">
// Caso real: nombre, año y lugar, datos clave, una cifra destacada y una captura grande del producto.
defineProps<{ marca?: string; anio?: string; lugar?: string; cifra?: string; etiqueta?: string; marco?: string; fuente?: string }>()
</script>

<template>
  <div class="slidev-layout thc-caso">
    <div class="izq">
      <div class="thc-kicker">Caso</div>
      <h2 class="marca">{{ marca }}</h2>
      <p class="meta"><span class="acento">{{ anio }}</span> · {{ lugar }}</p>
      <div class="datos"><slot /></div>
      <div v-if="cifra" class="cifra"><span class="et thc-kicker">{{ etiqueta || 'Valor de mercado' }}</span><span class="num">{{ cifra }}</span></div>
    </div>
    <div class="der">
      <div class="pantalla" :class="{ marco: marco !== 'no' }"><slot name="pantalla" /></div>
      <p v-if="fuente" class="fuente">{{ fuente }}</p>
    </div>
    <Logo version="simbolo" ancho="26px" class="logo" />
  </div>
</template>

<style scoped>
.thc-caso { display: flex; gap: 2rem; position: relative; }
.izq { flex: 0.9; display: flex; flex-direction: column; }
.marca { font-size: 2.2rem; font-weight: 700; color: var(--thc-verde-oscuro); margin: 0.2rem 0 0; }
.meta { color: var(--thc-gris-oscuro); margin: 0.2rem 0 1rem; }
.meta .acento { font-size: 1.2rem; }
.datos :deep(li) { font-size: 1rem; }
.cifra { margin-top: auto; background: var(--thc-lima); border-radius: 16px; padding: 0.7rem 1.1rem; align-self: flex-start; }
.cifra .et { display: block; color: var(--thc-verde-oscuro); }
.cifra .num { font-size: 2.2rem; font-weight: 700; color: var(--thc-verde-oscuro); }
.der { flex: 1.2; display: flex; flex-direction: column; justify-content: center; align-items: center; }
.pantalla { width: 100%; display: flex; justify-content: center; }
.pantalla.marco { background: var(--thc-gris-sutil); border-radius: 14px; padding: 0.8rem; box-shadow: inset 0 0 0 1px var(--thc-gris-claro); }
.pantalla :deep(p) { display: flex; gap: 0.8rem; align-items: center; justify-content: center; margin: 0; }
.pantalla :deep(img) { min-width: 0; flex: 0 1 auto; max-width: 100%; max-height: 330px; object-fit: contain; border-radius: 6px; margin: 0; }
.logo { position: absolute; right: 1.6rem; bottom: 1.2rem; }
</style>
