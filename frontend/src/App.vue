<template>
  <div class="wrapper">
    <RouterView />
  </div>
</template>

<script setup>
import { RouterView } from "vue-router";
</script>

<style>
.wrapper {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  height: 100%;
  background-color: white;
  border: 2px solid black;
}
.main {
  height: calc(100% - 3.6rem);
}
</style>
