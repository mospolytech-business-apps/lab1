<script setup>
import UIHeader from "@/components/UIHeader.vue";
import UIButton from "@/components/UIButton.vue";
import UISelect from "@/components/UISelect.vue";

import { ref, reactive, onMounted, watch, computed } from "vue";
import { useOfficesStore } from "@/stores/offices.store";
import { storeToRefs } from "pinia";
import { useErrorsStore } from "@/stores/errors.store";
import { useUsersStore } from "@/stores/users.store";

const { addError } = useErrorsStore();
const { allOffices } = storeToRefs(useOfficesStore());
const { getAllOffices } = useOfficesStore();
const { editUser } = useUsersStore();

const props = defineProps({
  open: { type: Boolean, required: true },
  user: { type: Object || null, required: true },
});

const emit = defineEmits(["close"]);

const offices = ref([]);
const editedUser = ref({});

watch(
  () => props.user,
  (newVal) => {
    editedUser.value = {
      ...newVal,
      role: newVal?.is_superuser ? "admin" : "user",
    };
  },
  { immediate: true }
);

const applyRoleChanges = () => {
  editUser(editedUser.value.id, {
    ...editedUser.value,
    is_superuser: editedUser.value.role === "admin",
  });
  emit("updateData");
  emit("close");
};

onMounted(async () => {
  offices.value = allOffices.value.length
    ? allOffices.value
    : await getAllOffices();
});

const close = () => {
  emit("close");
};
</script>

<template>
  <div v-if="props.open" class="modal">
    <UIHeader title="Edit Role" :closeButtonHandler="close" />
    <main class="main">
      <label for="firstName" class="label">First name </label>
      <input
        v-model="editedUser.first_name"
        type="text"
        id="firstName"
      />

      <label for="lastName" class="label">Last name</label>
      <input v-model="editedUser.last_name" type="text" id="lastName" />

      <label for="email" class="label">Email address </label>
      <input v-model="editedUser.email" type="email" id="email" />

      <label for="office" class="label">Office</label>
      <UISelect
        v-model="editedUser.office"
        placeholder="Office name"
        required
        id="office"
      >
        <option
          v-for="office in offices"
          :key="office.id"
          :value="office.title"
        >
          {{ office.title }}
        </option>
      </UISelect>

      <label class="role-label" for="role">Role</label>
      <div class="role-inputs">
        <label for="user" class="label">
          <input
            v-model="editedUser.role"
            class="input"
            type="radio"
            value="user"
            name="role"
            id="user"
          />
          User
        </label>

        <label for="admin" class="label">
          <input
            v-model="editedUser.role"
            class="input"
            type="radio"
            name="role"
            value="admin"
            id="admin"
          />
          Administrator
        </label>
      </div>

      <div class="actions">
        <UIButton @click="applyRoleChanges">Apply</UIButton>
        <UIButton class="cancel-btn" @click="close">Cancel</UIButton>
      </div>
    </main>
  </div>
</template>

<style scoped>
.modal {
  position: absolute;
  top: 50%;
  left: 50%;
  background-color: white;
  min-width: 40%;
  transform: translate(-50%, -50%);
  border: 1px solid black;
  box-shadow: 0 0 2rem black;
}

.main {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr 2fr;
  grid-template-rows: 1fr 1fr 1fr 1fr 2fr;
  flex-direction: column;
  align-items: center;
  width: 100%;
  padding: 1.5rem 4rem;
  background-color: white;
}

.title {
  margin-bottom: 1rem;
}

.field {
  width: 100%;
  display: flex;
  grid-column: 1 / -1;
  justify-content: space-between;
}

.role-inputs {
  display: flex;
  flex-direction: column;
}

.fieldset {
  border: 0;
  margin: 0;
  padding: 0;
  display: flex;
  display: block;
  grid-column: 1 / -1;
}

.legend {
  display: block;
  font-size: 1rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}
.role {
  display: flex;
  flex-direction: column;
}

.role-label {
  margin-bottom: auto;
  margin-top: 0.5rem;
}

.buttons {
  display: flex;
  justify-content: center;
  gap: 6rem;
  margin-bottom: 2rem;
}

.actions {
  grid-row: -1;
  grid-column: 1 / -1;
  display: flex;
  justify-content: center;
  gap: 4rem;
}

.cancel-btn:hover {
  background-color: salmon;
}
</style>
