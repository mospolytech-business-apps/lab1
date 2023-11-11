<template>
  <UIHeader title="User Home Page" />

  <main class="container">
    <h1>Hi <b>user</b>, Welcome to ANOMIC AIRLINES</h1>
    <div class="metrics">
      <p>
        Time spent on system: <b>{{ timeSpent || "–" }}</b>
      </p>
      <p>
        Number of crashes: <b>{{ numberOfCrashes || "–" }}</b>
      </p>
    </div>

    <div class="table-wrapper">
      <table class="table">
        <thead>
          <tr>
            <th>Date</th>
            <th>Login time</th>
            <th>Logout time</th>
            <th>Time spent on system</th>
            <th>Unsuccessful logout reason</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="crash in crashes" :key="crash.id">
            <td>{{ crash.date }}</td>
            <td>{{ crash.loginTime }}</td>
            <td>{{ crash.logoutTime }}</td>
            <td>{{ crash.timeSpentOnSystem }}</td>
            <td>{{ crash.unsuccessfulLogoutReason }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="links">
      <router-link class="link" to="/purchase-amenities"
        >Purchase Amenities</router-link
      >
    </div>
  </main>
  <NoLogoutModal
    :open="isNoLogoutModalOpen"
    @submit="logoutStore.setLogoutInformation;"
    @close="isNoLogoutModalOpen = false"
  />
</template>

<script setup>
import { ref } from "vue";
import UIHeader from "@/components/UIHeader.vue";
import NoLogoutModal from "../components/NoLogoutModal.vue";
import { useLogoutStore } from "@/stores/logout";

const logoutStore = useLogoutStore();

const crashes = [
  {
    id: 1,
    date: "2021-05-01",
    loginTime: "10:00:00",
    logoutTime: "10:30:00",
    timeSpentOnSystem: "00:30:00",
    unsuccessfulLogoutReason: "System crashed",
  },
  {
    id: 1,
    date: "2021-05-01",
    loginTime: "10:00:00",
    logoutTime: "10:30:00",
    timeSpentOnSystem: "00:30:00",
    unsuccessfulLogoutReason: "System crashed",
  },
];

const isNoLogoutModalOpen = ref(true);
</script>

<style>
.container {
  max-width: 960px;
  margin: 0 auto;
}

.crashes-table-section {
  margin-bottom: 20px;
}

.table {
  border-collapse: collapse;
  flex-grow: 1;
  width: 100%;
  border: 2px solid black;
  overflow: scroll;
}

.table th,
.table td {
  border: 1px solid black;
  padding: 5px;
}

.table-wrapper {
}
.table {
  border-collapse: collapse;
  overflow: scroll;
}

.metrics {
  display: flex;
  justify-content: end;
  gap: 3rem;
}

.links {
  display: flex;
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
</style>
