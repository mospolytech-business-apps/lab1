<template>
  <UIHeader title="Admin Home Page" />
  <main class="main" align="center">
    <router-link class="link" to="/manage-users">Manage Users</router-link>
    <router-link class="link" to="/manage-flight-schedules"
      >Manage Flight Schedules</router-link
    >
    <router-link class="link" to="/client-survey"
      >Client Survey Summary</router-link
    >
    <router-link class="link" to="/amenities-report"
      >Amenities Report</router-link
    >

    <router-link class="link" to="/airlines-short-summary"
      >Airlines Short Summary Page</router-link
    >
  </main>
</template>

<script setup>
import UIHeader from "@/components/UIHeader.vue";
</script>

<style scoped>
.main {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  overflow: scroll;
}
.link {
  min-width: 25rem;
  margin: 1rem;
  padding: 1rem;
  border: 1px solid black;
  border-radius: 0.5rem;
  text-decoration: none;
  color: black;
  font-size: 1.5rem;
  font-weight: bold;
  transition: 0.3s;
}

.link:hover {
  background-color: #e6e6e6;
}
</style>
