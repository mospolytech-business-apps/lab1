<template>
  <div class="wrapper">
    <RouterView />
  </div>
</template>

<script setup>
import { RouterView } from "vue-router";
</script>

<style scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  height: 100%;
  background-color: white;
  border: 2px solid black;
}
</style>
