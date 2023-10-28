<template>
  <div class="container">
    <header>
      <h1>AMONIC Airlines Automation System</h1>
    </header>
    <main>
      <table class="table">
        <thead>
          <tr>
            <th>Name</th>
            <th>Last Name</th>
            <th>Age</th>
            <th>User Role</th>
            <th>Email Address</th>
            <th>Office</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="user in users"
            :key="user.id"
            @click="selectUser(user)"
            :class="{
              selected: user === selectedUser,
              enabled: user.loginStatus === 'enabled',
              disabled: user.loginStatus === 'disabled',
              notSet: user.loginStatus === 'notSet',
            }"
          >
            <td>{{ user.name }}</td>
            <td>{{ user.lastName }}</td>
            <td>{{ user.age }}</td>
            <td>{{ user.userRole }}</td>
            <td>{{ user.emailAddress }}</td>
            <td>{{ user.office }}</td>
          </tr>
        </tbody>
      </table>
      <div class="buttons">
        <button class="btn" @click="changeRole(selectedUser)">
          Change Role
        </button>
        <button class="btn" @click="enableDisableLogin(selectedUser)">
          Enable/Disable Login
        </button>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onUnmounted } from "vue";

const apiUrl = "src/assets/users.json";

const fetchUsers = async () => {
  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    users.value = data; // Store the fetched users
  } catch (error) {
    console.error("Error fetching users:", error);
  }
};

const users = ref([]); // Define a ref to hold the users

const selectedUser = ref(null);

const selectUser = (user) => {
  selectedUser.value = user;
  console.log(user.id);
};

const changeRole = (user) => {
  user.userRole =
    user.userRole === "administrator" ? "office user" : "administrator";
};

const enableDisableLogin = (user) => {
  user.loginStatus = user.loginStatus === "enabled" ? "disabled" : "enabled";
};

onUnmounted(() => {
  selectedUser.value = null;
});

fetchUsers();
</script>

<style scoped>
.selected {
  box-shadow: inset 0 0 0 2px black;
}

.enabled {
  background-color: lightgreen;
}
.disabled {
  background-color: salmon;
}
.notSet {
  background-color: lightgray;
}

.table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 1rem;
}
.buttons {
  display: flex;
  gap: 5rem;
}
</style>
