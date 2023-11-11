<template>
  <nav class="nav-menu">
    <slot></slot>
  </nav>
</template>

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
</style>
