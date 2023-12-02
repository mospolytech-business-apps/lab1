<script setup>
import AddUserModal from "@/components/AddUserModal.vue";
import EditRoleModal from "@/components/EditRoleModal.vue";
import UIHeader from "@/components/UIHeader.vue";
import UINav from "@/components/UINav.vue";
import UIButton from "@/components/UIButton.vue";
import UISelect from "@/components/UISelect.vue";

import { ref, onUnmounted, onMounted, computed } from "vue";
import { storeToRefs } from "pinia";
import { useUsersStore } from "@/stores/users.store";
import { useOfficesStore } from "@/stores/offices.store";
import { useErrorsStore } from "@/stores/errors.store";

const { getAllUsers, ban, unban } = useUsersStore();
const { allUsers } = storeToRefs(useUsersStore());
const { getAllOffices } = useOfficesStore();
const { allOffices } = storeToRefs(useOfficesStore());
const { addError } = useErrorsStore();

const isAddUserModalOpen = ref(false);
const isEditRoleModalOpen = ref(false);
const editableUser = ref(null);

const openAddUserModal = () => {
  isAddUserModalOpen.value = true;
};

const closeAddUserModal = async () => {
  await fetchNewData();
  isAddUserModalOpen.value = false;
  editableUser.value = null;
};

const openEditRoleModal = () => {
  isEditRoleModalOpen.value = true;
};

const closeEditRoleModal = async () => {
  await fetchNewData();
  isEditRoleModalOpen.value = false;
  editableUser.value = null;
  selectedUser.value = null;
};

const selectedUser = ref(null);

const selectUser = (user) => {
  selectedUser.value = user;
};

const calculateAge = (birthday) => {
  const today = new Date();
  const birthDate = new Date(birthday);
  let age = today.getFullYear() - birthDate.getFullYear();
  const month = today.getMonth() - birthDate.getMonth();
  if (month < 0 || (month === 0 && today.getDate() < birthDate.getDate())) {
    age--;
  }
  return age;
};

const changeRole = (user) => {
  editableUser.value = user;
  if (editableUser.value === null) {
    addError("Error: Select user first!");
    return;
  }
  openEditRoleModal();
};

const enableDisableLogin = async (user) => {
  if (user === null) {
    addError("Error: Select user first!");
    return;
  }

  if (user?.is_new) {
    await unban(user.id);
  } else {
    if (user?.is_active) {
      await ban(user.id);
    } else if (!user?.is_active) {
      await unban(user.id);
    }
  }
  await fetchNewData();
  editableUser.value = null;
  selectedUser.value = null;
};

const users = ref([]);
const offices = ref([]);
const selectedOffice = ref(null);

const filteredUsers = computed(() => {
  if (!selectedOffice.value) {
    return users.value;
  }
  return users.value.filter((user) => user.office === selectedOffice.value);
});

onMounted(async () => {
  users.value = allUsers.value.length ? allUsers.value : await getAllUsers();
  offices.value = allOffices.value.length
    ? allOffices.value
    : await getAllOffices();
});

const fetchNewData = async () => {
  users.value = await getAllUsers();
};

onUnmounted(() => {
  selectedUser.value = null;
});
</script>

<template>
  <UIHeader title="Manage Users" />
  <UINav>
    <button @click="openAddUserModal">Add user</button>
  </UINav>
  <main class="main">
    <div class="filter">
      <p class="filter-title">Office:</p>
      <UISelect v-model="selectedOffice" class="company-filter">
        <option value="">All Offices</option>
        <option
          v-for="office in offices"
          :key="office.id"
          :value="office.title"
        >
          {{ office.title }}
        </option>
      </UISelect>
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
            v-for="user in filteredUsers"
            :key="user.id"
            @click="selectUser(user)"
            :class="{
              selected: user === selectedUser,
              enabled: user.is_active,
              disabled: !user.is_active,
              notSet: user.is_new,
            }"
          >
            <td>{{ user.first_name }}</td>
            <td>{{ user.last_name }}</td>
            <td class="align-center">{{ calculateAge(user.birthday) }}</td>
            <td>{{ user.is_superuser ? "Administrator" : "User" }}</td>
            <td>{{ user.email }}</td>
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
  <AddUserModal
    @updateData="fetchNewData"
    :open="isAddUserModalOpen"
    @close="closeAddUserModal"
  />
  <EditRoleModal
    @updateData="fetchNewData"
    :user="editableUser"
    :open="isEditRoleModalOpen"
    @close="closeEditRoleModal"
  />
</template>

<style scoped>
.main {
  margin: 1rem;
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

.company-filter {
  min-width: 10rem;
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

.align-center {
  text-align: center;
}

thead {
  background-color: lightgray;
  border-bottom: 2px solid black;
}

td,
th {
  border: 1px solid black;
  padding-inline-start: 0.25rem;
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
  overflow: scroll;
}

.buttons {
  display: flex;
  gap: 5rem;
}
</style>
