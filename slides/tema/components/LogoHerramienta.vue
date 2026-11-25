<script setup lang="ts">
// Logo de una herramienta externa en cualquier color, con máscara CSS como Logo.
// Nombres: notion, gmail, googlecalendar, googledrive, googlesheets, hubspot, make, microsoftexcel, openai, slack, zapier,
// claude, googlegemini, deepseek, qwen, kimi, linkedin.
// <LogoHerramienta nombre="notion" color="var(--thc-verde-oscuro)" ancho="40px" enlace="https://www.notion.com" />
// Con `enlace`, el logo es un enlace que se abre en otra pestaña.
import notion from '../assets/herramientas/notion.png'
import gmail from '../assets/herramientas/gmail.svg'
import googlecalendar from '../assets/herramientas/googlecalendar.svg'
import googledrive from '../assets/herramientas/googledrive.svg'
import googlesheets from '../assets/herramientas/googlesheets.svg'
import hubspot from '../assets/herramientas/hubspot.svg'
import make from '../assets/herramientas/make.svg'
import microsoftexcel from '../assets/herramientas/microsoftexcel.svg'
import openai from '../assets/herramientas/openai.svg'
import slack from '../assets/herramientas/slack.svg'
import zapier from '../assets/herramientas/zapier.svg'
import claude from '../assets/herramientas/claude.svg'
import googlegemini from '../assets/herramientas/googlegemini.svg'
import deepseek from '../assets/herramientas/deepseek.svg'
import qwen from '../assets/herramientas/qwen.svg'
import kimi from '../assets/herramientas/kimi.svg'
import linkedin from '../assets/herramientas/linkedin.svg'

const props = withDefaults(defineProps<{ nombre: string; color?: string; ancho?: string; enlace?: string }>(), {
  color: 'var(--thc-blanco)', ancho: '48px',
})
const logos: Record<string, string> = { notion, gmail, googlecalendar, googledrive, googlesheets, hubspot, make, microsoftexcel, openai, slack, zapier, claude, googlegemini, deepseek, qwen, kimi, linkedin }
const src = logos[props.nombre.toLowerCase()]
const estilo = { color: props.color, width: props.ancho, WebkitMaskImage: `url("${src}")`, maskImage: `url("${src}")` }
</script>

<template>
  <a v-if="enlace" :href="enlace" target="_blank" rel="noopener" class="thc-logo-herramienta" :style="estilo" :aria-label="nombre" />
  <span v-else class="thc-logo-herramienta" :style="estilo" :aria-label="nombre" />
</template>

<style scoped>
.thc-logo-herramienta { display: inline-block; aspect-ratio: 1; background: currentColor; mask-size: contain; mask-repeat: no-repeat; mask-position: center; -webkit-mask-size: contain; -webkit-mask-repeat: no-repeat; -webkit-mask-position: center; }
</style>
