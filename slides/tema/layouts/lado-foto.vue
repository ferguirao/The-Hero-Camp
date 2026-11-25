<script setup lang="ts">
// Foto a un lado y contenido al otro. La foto va en el slot `foto` (::foto:: + imagen Markdown).
// lado: 'izq' (foto a la izquierda) o 'der'. ancho: ancho de la foto. posicion: object-position.
const props = withDefaults(defineProps<{ lado?: 'izq' | 'der'; ancho?: string; kicker?: string; fondo?: 'claro' | 'sutil' | 'oscuro'; posicion?: string; ajuste?: 'cover' | 'contain' }>(), { lado: 'der', ancho: '38%', fondo: 'claro', posicion: 'center', ajuste: 'cover' })
</script>

<template>
  <div class="slidev-layout thc-lado-foto" :class="[`fondo-${props.fondo}`, props.lado === 'izq' ? 'foto-izq' : 'foto-der']" :style="{ '--ancho-foto': props.ancho, '--pos': props.posicion, '--ajuste': props.ajuste }">
    <div class="foto"><slot name="foto" /></div>
    <div class="texto">
      <div v-if="props.kicker" class="thc-kicker kicker">{{ props.kicker }}</div>
      <slot />
    </div>
    <Logo version="simbolo" ancho="26px" class="logo" :color="props.fondo === 'oscuro' ? 'var(--thc-lima)' : 'var(--thc-verde-oscuro)'" />
  </div>
</template>

<style scoped>
.thc-lado-foto { display: flex; padding: 0; position: relative; }
.foto-izq { flex-direction: row; }
.foto-der { flex-direction: row-reverse; }
.foto { width: var(--ancho-foto); flex: none; background: var(--thc-gris-sutil); position: relative; overflow: hidden; }
.foto :deep(img) { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: var(--ajuste); object-position: var(--pos); margin: 0; }
.texto { flex: 1; padding: 3.2rem 3.4rem 3rem; display: flex; flex-direction: column; justify-content: center; }
.kicker { margin-bottom: 1.1rem; }
.texto :deep(h1) { font-size: 2.1rem; line-height: 1.15; margin: 0 0 1.2rem; }
.texto :deep(p) { margin: 0 0 1.3rem; line-height: 1.45; }
.texto :deep(.checklist li), .texto :deep(.numerada li) { margin: 0.55rem 0; }
.fondo-sutil { background: var(--thc-gris-sutil); }
.fondo-oscuro { background: var(--thc-verde-oscuro); color: var(--thc-blanco); }
.fondo-oscuro :deep(h1) { color: var(--thc-blanco); }
.logo { position: absolute; right: 1.6rem; bottom: 1.4rem; }
</style>
