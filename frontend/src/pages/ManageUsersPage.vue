<template>
  <UIHeader title="Manage Users" />
  <UINav>
    <button @click="openAddUserModal">Add user</button>
    <button @click="reload">Exit</button>
  </UINav>
  <main class="main">
    <div class="filter">
      <p class="filter-title">Office:</p>
      <select
        class="select"
        id="company-filter"
        style="
          border-radius: 5px;
          border: 1px solid black;
          padding: 0.25rem 1rem;
          width: 100%;
        "
      >
        <option value="">All Offices</option>
        <option
          v-for="company in companies"
          :key="company.id"
          :value="company.id"
        >
          {{ company.name }}
        </option>
      </select>
    </div>
    <div class="table-wrapper">
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
    </div>
    <div class="buttons">
      <UIButton @click="changeRole(selectedUser)">Change Role</UIButton>
      <UIButton @click="enableDisableLogin(selectedUser)">
        Enable/Disable Login
      </UIButton>
    </div>
  </main>
  <AddUserModal :open="isAddUserModalOpen" @close="closeAddUserModal" />
  <EditRoleModal
    :user="editableUser"
    :open="isEditRoleModalOpen"
    @close="closeEditRoleModal"
  />
</template>

<script setup>
import { ref, onUnmounted } from "vue";
import AddUserModal from "../components/AddUserModal.vue";
import EditRoleModal from "../components/EditRoleModal.vue";
import UIHeader from "@/components/UIHeader.vue";
import UINav from "@/components/UINav.vue";
import UIButton from "@/components/UIButton.vue";
import reload from "@/scripts/reload.js";

const isAddUserModalOpen = ref(false);
const isEditRoleModalOpen = ref(false);
const editableUser = ref(null);

const openAddUserModal = () => {
  isAddUserModalOpen.value = true;
};

const closeAddUserModal = () => {
  isAddUserModalOpen.value = false;
};

const openEditRoleModal = () => {
  isEditRoleModalOpen.value = true;
};

const closeEditRoleModal = () => {
  isEditRoleModalOpen.value = false;
};

const apiUrl = "src/assets/users.json";
const fetchUsers = async () => {
  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    users.value = data;
  } catch (error) {
    console.error("Error fetching users:", error);
  }
};

const users = ref([]);

const selectedUser = ref(null);

const selectUser = (user) => {
  selectedUser.value = user;
};

const changeRole = (user) => {
  editableUser.value = user;
  openEditRoleModal();
};

const enableDisableLogin = (user) => {
  openEditRoleModal;
  user.loginStatus = user.loginStatus === "enabled" ? "disabled" : "enabled";
};

onUnmounted(() => {
  selectedUser.value = null;
});

fetchUsers();
</script>

<style scoped>
.main {
  margin: 1rem 1rem;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
  gap: 1rem;
}

.filter {
  align-items: center;
  display: flex;
  gap: 1rem;
}

.filter-title {
  margin: 0;
}

.select {
  border-radius: 5px;
  border: 1px solid black;
  height: 100%;
  padding: 0.25rem 1rem;
  width: 100%;
}
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
  background-color: white;
}

thead {
  background-color: lightgray;
  border-bottom: 2px solid black;
}

.table-wrapper {
  flex-grow: 1;
  width: 100%;
  border: 2px solid black;
  overflow: scroll;
}
.table {
  border-collapse: collapse;
  overflow: scroll;
}
.buttons {
  display: flex;
  gap: 5rem;
}
</style>
