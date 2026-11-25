<script setup lang="ts">
// Separador de sección: color de marca a toda la slide, garabato en una esquina, número y título abajo.
const props = withDefaults(defineProps<{ numero?: string; subtitulo?: string; color?: 'lima' | 'oscuro' | 'claro'; garabato?: string; garabatoColor?: string; garabatoPos?: string }>(), { color: 'lima', garabatoPos: 'sup-der' })
const colorG = (c: string) => props.garabatoColor || (c === 'oscuro' ? 'lima' : 'verde-oscuro')
</script>

<template>
  <div class="slidev-layout thc-separador-sec" :class="props.color">
    <Garabato v-if="props.garabato" :nombre="props.garabato" :color="colorG(props.color)" :pos="(props.garabatoPos as any)" ancho="34%" sangrado="1.5rem" />
    <div class="pie">
      <div class="titulo">
        <span v-if="props.numero" class="numero">{{ props.numero }}.</span>
        <slot />
      </div>
      <p v-if="props.subtitulo" class="subtitulo">{{ props.subtitulo }}</p>
    </div>
  </div>
</template>

<style scoped>
.thc-separador-sec { display: flex; align-items: flex-end; position: relative; }
.lima { background: var(--thc-lima); color: var(--thc-verde-oscuro); }
.oscuro { background: var(--thc-verde-oscuro); color: var(--thc-blanco); }
.claro { background: var(--thc-verde-claro); color: var(--thc-verde-oscuro); }
.pie { max-width: 75%; }
.titulo { display: flex; align-items: baseline; gap: 0.6rem; }
.numero { font-family: var(--thc-mono); font-size: 1.8rem; opacity: 0.8; }
.titulo :deep(h1) { color: inherit; font-weight: 700; font-size: 2.2rem; margin: 0; }
.subtitulo { margin-top: 0.7rem; font-size: 1.1rem; opacity: 0.8; }
</style>
