<template>
  <div class="window">
    <header class="header">
      <h1 class="title">{{ props.title }}</h1>
      <button class="exit-icon" @click="close">
        <img
          width="20"
          src="https://cdn2.iconfinder.com/data/icons/general-ui-icons/800/delete85-1024.png"
          alt="Exit icon"
        />
      </button>
    </header>

    <nav>
      <slot name="buttons"></slot>
    </nav>

    <main>
      <slot></slot>
    </main>

    <MyModal :open="isOpen" @close="handleClose">
      <slot name="header">
        {{ props.modalTitle }}
      </slot>

      <slot name="content"></slot>

      <slot name="footer">
        <button @click="handleClose">Close Window</button>
      </slot>
    </MyModal>
  </div>
</template>

<script setup>
import MyModal from "@/components/MyModal.vue";

import { defineProps } from "vue";

const props = defineProps({
  isOpen: { type: Boolean, default: false },
  title: { type: String, required: true },
});

function handleClose() {
  emit("close");
}
</script>

<style></style>
