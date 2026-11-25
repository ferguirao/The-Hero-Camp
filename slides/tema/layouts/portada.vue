<script setup lang="ts">
// Portada de una formación: fondo verde oscuro, kicker en acento, título y logo apilado
defineProps<{ kicker?: string; subtitulo?: string; garabato?: string; garabatoPos?: string }>()
</script>

<template>
  <div class="slidev-layout thc-portada thc-fondo-oscuro">
    <div class="contenido">
      <p v-if="kicker" class="thc-acento kicker">{{ kicker }}</p>
      <slot />
      <p v-if="subtitulo" class="subtitulo">{{ subtitulo }}</p>
    </div>
    <Garabato v-if="garabato" :nombre="garabato" color="lima" :pos="(garabatoPos || 'sup-der') as any" ancho="30%" sangrado="2rem" />
    <Logo version="apilado" color="var(--thc-blanco)" ancho="150px" class="logo" />
  </div>
</template>

<style scoped>
.thc-portada { display: flex; align-items: flex-end; position: relative; }
.contenido { max-width: 72%; }
.kicker { font-size: 1.5rem; margin-bottom: 0.4rem; }
.contenido :deep(h1) { font-size: 2.8rem; color: var(--thc-blanco); }
.subtitulo { color: var(--thc-gris-medio); font-size: 1.2rem; }
.logo { position: absolute; right: 3.5rem; bottom: 3rem; }
</style>
