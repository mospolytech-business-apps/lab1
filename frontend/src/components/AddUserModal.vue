<script setup>
import UIHeader from "@/components/UIHeader.vue";
import UIButton from "@/components/UIButton.vue";
import UISelect from "@/components/UISelect.vue";

import { ref, onMounted } from "vue";
import { useOfficesStore } from "@/stores/offices.store";
import { useUsersStore } from "@/stores/users.store";
import { storeToRefs } from "pinia";

const { getAllOffices } = useOfficesStore();
const { allOffices } = storeToRefs(useOfficesStore());
const { addUser } = useUsersStore();

const props = defineProps({
  open: { type: Boolean, required: true },
  user: { type: Object || null, required: true },
});

const emit = defineEmits(["close"]);

const offices = ref([]);

const saveUser = () => {
  addUser({
    ...formData.value,
    is_superuser: false,
  });
  emit("updateData");
  emit("close");
};

const formData = ref({
  email: "",
  first_name: "",
  last_name: "",
  office: "",
  birth_date: "",
  password: "",
});

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
    <UIHeader title="Add User" :closeButtonHandler="close" />
    <main class="main">
      <label class="label" for="email">Email address </label>
      <input
        class="field"
        type="email"
        v-model="formData.email"
        id="email"
        required
      />

      <label class="label" for="firstName">First name </label>
      <input
        class="field"
        type="text"
        v-model="formData.first_name"
        id="firstName"
        required
      />

      <label class="label" for="lastName">Last name </label>
      <input
        class="field"
        type="text"
        v-model="formData.last_name"
        id="lastName"
        required
      />

      <label class="label" for="officeName">Office</label>
      <UISelect
        v-model="formData.office"
        class="field"
        placeholder="Office name"
        placeholderBlue
        placeholderUnderline
        name="officeName"
        required
      >
        <option v-for="office in offices" :value="office.title">
          {{ office.title }}
        </option>
      </UISelect>

      <label class="label" for="birthDate">Birthdate</label>
      <input
        class="field"
        type="date"
        v-model="formData.birth_date"
        placeholder="Birthdate [dd/mm/yy]"
        id="birthDate"
      />

      <label class="label" for="password">Password</label>
      <input
        class="field"
        type="password"
        v-model="formData.password"
        id="password"
        required
      />
      <div class="actions">
        <UIButton @click="saveUser">Save</UIButton>
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
  grid-template-rows: repeat(6, 1fr);
  flex-direction: column;
  align-items: center;
  width: 100%;
  padding: 1.5rem 4rem;
  background-color: white;
}

.title {
  display: block;
  min-height: 1rem;
  margin-bottom: 0.25rem;
}

.label {
  display: block;
  min-height: 1rem;
  margin-bottom: 0.25rem;
}

.field {
  display: block;
  margin-bottom: 0.25rem;
}

.actions {
  grid-row: -1;
  grid-column: 1 / -1;
  margin-top: 3rem;
  padding-inline: 1.5rem;
  display: flex;
  gap: 4rem;
  justify-content: center;
}

.cancel-btn:hover {
  background-color: salmon;
}
</style>
