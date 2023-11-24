<template>
  <div v-for="err of errors" class="popup">
    <p>{{ err }}</p>
    <button @click="removeError(err)">X</button>
  </div>
</template>

<script setup>
import { errors, removeError } from storeToRefs(useErrorStore());
</script>

<style scoped></style>
