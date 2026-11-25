<script setup lang="ts">
// Mensaje clave: una idea grande sobre verde oscuro, con lo importante en lima (negritas).
// responded: true pone "Responded" en letra a mano encima, para las slides de pregunta al grupo.
defineProps<{ kicker?: string; garabato?: string; garabatoPos?: string; garabatoColor?: string; responded?: boolean }>()
</script>

<template>
  <div class="slidev-layout thc-mensaje">
    <span v-if="kicker" class="thc-kicker kicker">{{ kicker }}</span>
    <div class="cuerpo"><span v-if="responded" class="thc-acento responded">Responded</span><slot /></div>
    <Garabato v-if="garabato" :nombre="garabato" :color="garabatoColor || 'lima'" :pos="(garabatoPos || 'sup-der') as any" ancho="22%" sangrado="2.5rem" />
    <Logo version="simbolo" ancho="26px" class="logo" color="var(--thc-lima)" />
  </div>
</template>

<style scoped>
.thc-mensaje { background: var(--thc-verde-oscuro); color: var(--thc-blanco); display: flex; flex-direction: column; justify-content: center; position: relative; }
.kicker { position: absolute; top: 2.6rem; left: 3.5rem; color: var(--thc-gris-medio); }
.cuerpo { max-width: 88%; }
.cuerpo :deep(h1) { color: var(--thc-blanco); font-size: 2.1rem; font-weight: 700; line-height: 1.2; }
.cuerpo :deep(p) { font-size: 1.7rem; font-weight: 500; line-height: 1.3; margin: 0.6rem 0; }
.cuerpo :deep(strong) { color: var(--thc-lima); }
.cuerpo :deep(.pequeno) { font-size: 0.95rem; color: var(--thc-gris-medio); }
.responded { display: inline-block; font-size: 1.3rem; transform: rotate(-3deg); margin-bottom: 0.5rem; }
.logo { position: absolute; right: 3rem; bottom: 2.4rem; }
.cuerpo :deep(h1) { text-wrap: balance; }
</style>
