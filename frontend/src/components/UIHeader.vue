<template>
  <header class="header">
    <h1 class="title">{{ props.title }}</h1>
    <UIError />
    <button @click="closeButtonHandler" class="exit-btn">
      <img width="20" src="@/assets/cross-icon.png" alt="Exit button" />
    </button>
  </header>
</template>

<script setup>
import UIError from "@/components/UIError.vue";
import { useAuthStore } from "../stores/auth.store";

const props = defineProps({
  title: {
    type: String,
    default: "Amonic Airlines Automation System",
  },
  closeButtonHandler: {
    type: Function,
    required: false,
    default: async () => {
      const { logout } = useAuthStore();
      logout();
    },
  },
});
</script>

<style scoped>
.header {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 2px solid black;
  height: 30px;
}

.title {
  font-size: 1rem;
  margin: 0;
  padding-inline-start: 0.5rem;
}

.exit-btn {
  border: 0;
  background: 0;
}

.exit-btn:hover {
  cursor: pointer;
}
</style>
