<template>
  <header class="header">
    <h1 class="title">{{ props.title }}</h1>
    <button class="exit-icon">
      <img
        width="20"
        src="https://cdn2.iconfinder.com/data/icons/general-ui-icons/800/delete85-1024.png"
        alt="Exit icon"
      />
    </button>
  </header>
  <PopupMenu />
</template>

<script setup>
import PopupMenu from "@/components/PopupMenu.vue";
const props = defineProps({
  title: {
    type: String,
    default: "Amonic Airlines Automation System",
  },
});
</script>

<style lang="scss" scoped>
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
.exit-icon {
  border: 0;
  background: 0;
}
</style>
