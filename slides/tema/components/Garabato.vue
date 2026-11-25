<script setup lang="ts">
// Garabato de marca en cualquier color (máscara CSS sobre el SVG, como el logo).
// <Garabato nombre="constelacion" color="lima" pos="sup-der" ancho="30%" rotar="-6" />
// Sin `pos` se coloca en el flujo; con `pos` se ancla a una esquina del layout (que debe ser position: relative).
import { computed } from 'vue'

const archivos = import.meta.glob('../ilustraciones/**/*.svg', { query: '?url', import: 'default', eager: true }) as Record<string, string>
const mapa: Record<string, string> = {}
for (const [ruta, url] of Object.entries(archivos)) {
  const rel = ruta.split('/ilustraciones/')[1].replace(/\.svg$/, '')
  mapa[rel] = url
  mapa[rel.split('/').pop() as string] = mapa[rel.split('/').pop() as string] || url
}

const colores: Record<string, string> = {
  'verde-oscuro': 'var(--thc-verde-oscuro)', lima: 'var(--thc-lima)', blanco: 'var(--thc-blanco)',
  rosa: 'var(--thc-rosa)', amarillo: 'var(--thc-amarillo)', gris: 'var(--thc-gris-medio)', actual: 'currentColor',
}
const props = withDefaults(defineProps<{
  nombre: string
  color?: string
  ancho?: string
  rotar?: number | string
  pos?: 'sup-der' | 'sup-izq' | 'inf-der' | 'inf-izq' | 'centro-der' | 'centro-izq' | 'arriba-centro' | 'abajo-centro'
  sangrado?: string // cuánto se sale del borde (por defecto 0)
  opacidad?: number | string
}>(), { color: 'verde-oscuro', ancho: '22%', rotar: 0, sangrado: '0px', opacidad: 1 })

const url = computed(() => mapa[props.nombre])
const estilo = computed(() => ({
  width: props.ancho,
  color: colores[props.color] || props.color,
  opacity: String(props.opacidad),
  transform: `rotate(${props.rotar}deg)`,
  '--sangrado': props.sangrado,
  WebkitMaskImage: `url("${url.value}")`, maskImage: `url("${url.value}")`,
}))
</script>

<template>
  <span v-if="url" class="thc-garabato" :class="props.pos ? `pos-${props.pos}` : ''" :style="estilo" aria-hidden="true">
    <img :src="url" alt="" />
  </span>
  <span v-else class="thc-hueco-doodle" style="padding:0.3rem">¿{{ props.nombre }}?</span>
</template>

<style scoped>
.thc-garabato { display: inline-block; background-color: currentColor; -webkit-mask-repeat: no-repeat; mask-repeat: no-repeat; -webkit-mask-size: 100% 100%; mask-size: 100% 100%; line-height: 0; pointer-events: none; }
.thc-garabato img { width: 100%; opacity: 0; display: block; }
.pos-sup-der { position: absolute; top: var(--sangrado); right: var(--sangrado); }
.pos-sup-izq { position: absolute; top: var(--sangrado); left: var(--sangrado); }
.pos-inf-der { position: absolute; bottom: var(--sangrado); right: var(--sangrado); }
.pos-inf-izq { position: absolute; bottom: var(--sangrado); left: var(--sangrado); }
.pos-centro-der { position: absolute; top: 50%; right: var(--sangrado); margin-top: -10%; }
.pos-centro-izq { position: absolute; top: 50%; left: var(--sangrado); margin-top: -10%; }
.pos-arriba-centro { position: absolute; top: var(--sangrado); left: 50%; margin-left: -10%; }
.pos-abajo-centro { position: absolute; bottom: var(--sangrado); left: 50%; margin-left: -10%; }
</style>
