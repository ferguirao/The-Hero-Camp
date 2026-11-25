<script setup lang="ts">
// Agenda lateral: a la izquierda todos los pasos y el actual destacado; a la derecha el contenido del paso.
// Los pasos se declaran una vez en el headmatter de la presentación (clave `agenda`).
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'
const props = defineProps<{ actual?: number; titulo?: string }>()
const { $slidev } = useSlideContext()
const pasos = computed<string[]>(() => ($slidev.configs as any).agenda || [])
const encabezado = computed(() => ($slidev.configs as any).agendaTitulo || '')
</script>

<template>
  <div class="slidev-layout thc-pasos">
    <aside class="lateral">
      <div class="fondo"><slot name="foto" /></div>
      <div class="velo" />
      <ol>
        <li v-for="(p, i) in pasos" :key="i" :class="{ activo: i + 1 === props.actual, resto: props.actual && i + 1 !== props.actual }">
          <span class="n">{{ i + 1 }}.</span><span class="t">{{ p }}</span>
        </li>
      </ol>
    </aside>
    <main class="principal">
      <div class="thc-kicker enc">{{ encabezado }}</div>
      <div v-if="props.actual" class="paso-actual"><span class="n">{{ props.actual }}.</span> {{ pasos[props.actual - 1] }}</div>
      <slot />
    </main>
    <Logo version="simbolo" ancho="24px" class="logo" />
  </div>
</template>

<style scoped>
.thc-pasos { display: flex; align-items: stretch; padding: 0; position: relative; }
.lateral { align-self: stretch; height: 100%; width: 34%; flex: none; position: relative; display: flex; align-items: center; overflow: hidden; background: var(--thc-gris-sutil); }
.fondo { position: absolute; inset: 0; }
.fondo :deep(img) { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; margin: 0; }
.velo { position: absolute; inset: 0; background: rgba(255, 255, 255, 0.84); }
.lateral ol { position: relative; list-style: none; padding: 0 1.3rem; margin: 0; width: 100%; }
.lateral li { display: flex; gap: 0.5rem; margin: 0.6rem 0; font-size: 0.78rem; line-height: 1.25; }
.lateral .n { font-weight: 700; color: var(--thc-gris-medio); }
.lateral .t { color: var(--thc-gris-oscuro); }
.lateral li.activo .n { color: var(--thc-lima); text-shadow: 0 0 1px var(--thc-verde-oscuro); }
.lateral li.activo .t { color: var(--thc-verde-oscuro); font-weight: 700; }
.lateral li.resto { opacity: 0.85; }
.principal { flex: 1; padding: 2.6rem 2.6rem 2rem; display: flex; flex-direction: column; }
.enc { margin-bottom: 0.3rem; }
.paso-actual { font-size: 1.15rem; font-weight: 500; color: var(--thc-negro); margin: 0.2rem 0 1rem; }
.paso-actual .n { color: var(--thc-verde-oscuro); font-weight: 700; }
.logo { position: absolute; right: 1.6rem; bottom: 1.2rem; }
</style>
