<script setup lang="ts">
// Logo de The Hero Camp en cualquier color de marca (máscara CSS sobre el PNG negro)
import simbolo from '../assets/simbolo-negro.png'
import horizontal from '../assets/logo-horizontal-negro.png'
import apilado from '../assets/logo-apilado-negro.png'
import simboloArriba from '../assets/logo-simbolo-arriba-negro.png'

const props = withDefaults(defineProps<{
  version?: 'simbolo' | 'horizontal' | 'apilado' | 'simbolo-arriba'
  color?: string
  ancho?: string
}>(), { version: 'simbolo', color: 'var(--thc-verde-oscuro)', ancho: '48px' })

const fuentes = { 'simbolo': [simbolo, 770 / 661], 'horizontal': [horizontal, 2179 / 746], 'apilado': [apilado, 1043 / 1078], 'simbolo-arriba': [simboloArriba, 1459 / 851] } as const
const [src, ratio] = fuentes[props.version]
</script>

<template>
  <span class="thc-logo" :style="{ color: props.color, width: props.ancho, aspectRatio: String(ratio), WebkitMaskImage: `url(${src})`, maskImage: `url(${src})` }" />
</template>
