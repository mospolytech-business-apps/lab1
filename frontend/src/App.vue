<template>
  <div class="wrapper">
    <RouterView />
  </div>
  <dialog ref="dialog" id="dialog">
    <p>Are you sure you want to leave?</p>
    <button @click="showDialog = false">No</button>
    <button @click="logout()">Yes</button>
  </dialog>
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
