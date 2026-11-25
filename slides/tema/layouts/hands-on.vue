<script setup lang="ts">
// Dinámica práctica: fondo verde oscuro, "Hands on" en acento, título, duración y herramienta.
// Si la herramienta tiene logo (por ahora Notion), sale en el recuadro en lugar del texto.
// `enlace`: a dónde lleva el recuadro. Con Notion y sin enlace, va a notion.com.
import LogoHerramienta from '../components/LogoHerramienta.vue'
const props = defineProps<{ duracion?: string; herramienta?: string; codigo?: string; plantilla?: string; garabato?: string; enlace?: string }>()
const conLogo = ['notion'].includes((props.herramienta || '').toLowerCase())
const destino = props.enlace || (conLogo ? 'https://www.notion.com' : undefined)
</script>

<template>
  <div class="slidev-layout thc-hands-on">
    <div class="izq">
      <span class="thc-acento etiqueta">Hands on</span>
      <slot />
      <div class="fila">
        <span v-if="duracion" class="chip">{{ duracion }}</span>
        <span v-if="herramienta" class="chip oscuro borde">{{ herramienta }}</span>
      </div>
    </div>
    <div class="der">
      <component :is="destino ? 'a' : 'div'" :href="destino" target="_blank" rel="noopener" class="qr" :class="{ 'con-logo': conLogo }"><LogoHerramienta v-if="conLogo" :nombre="herramienta!" ancho="96px" /><span v-else class="thc-kicker">{{ herramienta || 'Herramienta' }}</span><span class="codigo">{{ codigo || 'código / QR' }}</span><span v-if="destino" class="abrir">Abrir ↗</span></component>
      <div v-if="plantilla" class="plantilla thc-kicker">{{ plantilla }}</div>
    </div>
    <Garabato v-if="garabato" :nombre="garabato" color="lima" pos="sup-der" ancho="18%" sangrado="2.5rem" rotar="-8" />
    <Logo version="simbolo" ancho="26px" class="logo" color="var(--thc-lima)" />
  </div>
</template>

<style scoped>
.thc-hands-on { background: var(--thc-verde-oscuro); color: var(--thc-blanco); display: flex; align-items: center; gap: 2rem; position: relative; }
.izq { flex: 1.4; }
.etiqueta { font-size: 1.5rem; display: inline-block; transform: rotate(-3deg); margin-bottom: 0.6rem; }
.izq :deep(h1) { color: var(--thc-blanco); font-size: 2.3rem; margin-bottom: 0.5rem; }
.izq :deep(p) { color: var(--thc-gris-claro); font-size: 1.1rem; }
.fila { margin-top: 1.4rem; display: flex; gap: 0.6rem; }
.borde { border: 1.5px solid var(--thc-lima); background: transparent; color: var(--thc-lima); }
.der { flex: 0.8; display: flex; flex-direction: column; align-items: center; gap: 1rem; }
.qr { width: 190px; height: 190px; border: 2px dashed var(--thc-gris-oscuro); border-radius: 16px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 0.5rem; color: var(--thc-gris-medio); }
.qr.con-logo { border-style: solid; border-color: var(--thc-gris-oscuro); }
.qr, .qr * { text-decoration: none !important; }
.qr.con-logo:hover { border-color: var(--thc-lima); }
.abrir { font-family: var(--thc-mono); font-size: 0.65rem; color: var(--thc-lima); text-transform: uppercase; }
.codigo { font-family: var(--thc-mono); font-size: 0.75rem; text-transform: uppercase; }
.plantilla { color: var(--thc-gris-medio); }
.logo { position: absolute; right: 2rem; bottom: 1.6rem; }
</style>
