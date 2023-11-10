<template>
  <div class="modal" v-if="open">
    <HeaderComponent :title="props.title" :closeButtonHandler="close" />
    <nav>
      <slot name="buttons"></slot>
    </nav>

    <main>
      <slot></slot>
    </main>

    <footer>
      <button @click="handleClose">Close Window</button>
    </footer>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from "vue";
import HeaderComponent from "@/components/HeaderComponent.vue";

const props = defineProps({
  open: { type: Boolean, required: true },
  title: { type: String, required: true },
});

const emit = defineEmits(["close"]);

function close() {
  emit("close");
}
</script>
