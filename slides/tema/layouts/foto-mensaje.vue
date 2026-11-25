<script setup lang="ts">
// Foto a toda la slide con un velo de color y un mensaje corto encima. La foto va en el slot `foto`.
const props = withDefaults(defineProps<{ velo?: 'verde' | 'oscuro' | 'claro' | 'ninguno'; posicion?: string; caja?: boolean; alinear?: 'centro' | 'abajo' }>(), { velo: 'verde', posicion: 'center', caja: true, alinear: 'centro' })
const velos = { verde: 'rgba(0,49,51,0.58)', oscuro: 'rgba(28,33,37,0.55)', claro: 'rgba(244,246,245,0.62)', ninguno: 'transparent' }
</script>

<template>
  <div class="slidev-layout thc-foto-mensaje" :class="`al-${props.alinear}`" :style="{ '--pos': props.posicion }">
    <div class="fondo"><slot name="foto" /></div>
    <div class="velo" :style="{ background: velos[props.velo] }" />
    <div class="mensaje" :class="{ caja: props.caja, sobre_claro: props.velo === 'claro' }"><slot /></div>
    <Logo version="simbolo" ancho="26px" class="logo" color="var(--thc-blanco)" />
  </div>
</template>

<style scoped>
.thc-foto-mensaje { position: relative; display: flex; justify-content: center; padding: 3rem; overflow: hidden; background: var(--thc-verde-oscuro); }
.fondo { position: absolute; inset: 0; }
.fondo :deep(img) { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: var(--pos); margin: 0; }
.al-centro { align-items: center; }
.al-abajo { align-items: flex-end; }
.velo { position: absolute; inset: 0; }
.mensaje { position: relative; text-align: center; color: var(--thc-blanco); max-width: 80%; }
.mensaje.caja { background: rgba(0, 49, 51, 0.82); padding: 2rem 2.8rem; border-radius: 14px; }
.mensaje.sobre_claro { color: var(--thc-verde-oscuro); }
.mensaje :deep(h1) { color: var(--thc-blanco); font-size: 2.2rem; margin: 0 0 1.1rem; line-height: 1.15; }
.mensaje :deep(h1:only-child) { margin-bottom: 0; }
.mensaje :deep(.thc-kicker) { display: block; margin-bottom: 0.9rem; }
.mensaje :deep(p) { font-size: 1.5rem; font-weight: 500; margin: 0 0 0.6rem; line-height: 1.35; }
.mensaje :deep(p:last-child) { margin-bottom: 0; }
.mensaje :deep(strong) { color: var(--thc-lima); }
.logo { position: absolute; right: 1.6rem; bottom: 1.4rem; opacity: 0.9; }
</style>
