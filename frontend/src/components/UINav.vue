<template>
  <nav class="menu">
    <slot></slot>
  </nav>
</template>

<style>
.menu {
  display: flex;
  justify-content: left;
  gap: 0.25rem;
  min-height: 30px;
  border-bottom: 2px solid black;
}

.menu > * {
  background: 0;
  border: 0;
  cursor: pointer;
}
.menu > *::first-letter {
  text-decoration: underline;
}

.menu > *:hover {
  background-color: lightgray;
}

.menu > *:active {
  background-color: gray;
}
</style>
