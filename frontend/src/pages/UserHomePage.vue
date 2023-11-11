<template>
  <UIHeader title="User Home Page" />
  <main class="main">
    <h1 class="title">Hi <b>user</b>, Welcome to ANOMIC Airlines</h1>
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
          <tr
            v-for="session in sessions"
            :key="session.id"
            :class="{
              crashed: session.logoutTime === null,
              row: true,
            }"
          >
            <td>{{ session.date || "–" }}</td>
            <td>{{ session.loginTime || "–" }}</td>
            <td>{{ session.logoutTime || "–" }}</td>
            <td>{{ session.timeSpentOnSystem || "–" }}</td>
            <td>{{ session.unsuccessfulLogoutReason || "–" }}</td>
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
import NoLogoutModal from "@/components/NoLogoutModal.vue";
import { useLogoutStore } from "@/stores/logout";

const logoutStore = useLogoutStore();

const sessions = [
  {
    id: 1,
    date: "2021-05-01",
    loginTime: "10:00:00",
    logoutTime: "10:30:00",
    timeSpentOnSystem: "00:30:00",
    unsuccessfulLogoutReason: null,
  },
  {
    id: 2,
    date: "2021-05-01",
    loginTime: "10:00:00",
    logoutTime: null,
    timeSpentOnSystem: null,
    unsuccessfulLogoutReason: "System crashed",
  },
  {
    id: 3,
    date: "2021-05-01",
    loginTime: "10:00:00",
    logoutTime: "10:30:00",
    timeSpentOnSystem: "00:30:00",
    unsuccessfulLogoutReason: null,
  },
  {
    id: 4,
    date: "2021-05-01",
    loginTime: "10:00:00",
    logoutTime: "10:30:00",
    timeSpentOnSystem: "00:30:00",
    unsuccessfulLogoutReason: null,
  },
];

const isNoLogoutModalOpen = ref(true);
</script>

<style scoped>
.main {
  margin: 1rem;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.title {
  font-size: 1.5em;
  font-weight: 400;
}
.crashes-table-section {
  margin-bottom: 20px;
}

thead {
  background-color: lightgray;
  border-bottom: 2px solid black;
}

td,
th {
  border: 1px solid black;
  padding-inline-start: 0.25rem;
  text-align: start;
}

.table-wrapper {
  flex-grow: 1;
  width: 100%;
  border: 2px solid black;
  overflow: scroll;
}

.table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid black;
  overflow: scroll;
}

.crashed {
  background-color: salmon;
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
