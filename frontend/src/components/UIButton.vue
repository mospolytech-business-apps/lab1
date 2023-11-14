<template>
  <button class="btn" @click="clickHandler">
    <slot></slot>
  </button>
</template>

<script setup></script>

<style scoped>
.btn {
  padding: 0.25rem 2rem;
  border: 1px solid black;
  border-radius: 5px;
  background-color: white;
  cursor: pointer;
  display: flex;
  gap: 0.5rem;
  align-items: center;
  position: relative;
}
.btn:hover {
  background-color: lightgray;
}

.btn:active {
  background-color: grey;
}
</style>
