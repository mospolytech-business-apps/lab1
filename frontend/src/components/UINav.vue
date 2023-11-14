<template>
  <nav class="nav-menu">
    <slot></slot>
    <button class="exit" @click="$router.push('/')">Exit</button>
  </nav>
</template>

<script setup></script>

<style>
.nav-menu {
  display: flex;
  justify-content: left;
  gap: 0.25rem;
  min-height: 30px;
  border-bottom: 2px solid black;
}

.nav-menu > * {
  background: 0;
  border: 0;
  cursor: pointer;
}
.nav-menu > *::first-letter {
  text-decoration: underline;
}

.nav-menu > *:hover {
  background-color: lightgray;
}

.nav-menu > *:active {
  background-color: gray;
}

.exit:hover {
  background-color: salmon;
}
</style>
