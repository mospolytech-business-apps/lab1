<template>
  <div v-if="props.open" class="modal">
    <UIHeader title="Add User" :closeButtonHandler="close" />
    <main class="main">
      <label class="label" for="email">Email address </label>
      <input class="field" type="email" v-model="formData.email" id="email" />

      <label class="label" for="firstName">First name </label>
      <input
        class="field"
        type="text"
        v-model="formData.firstName"
        id="firstName"
      />

      <label class="label" for="lastName">Last name </label>
      <input
        class="field"
        type="text"
        v-model="formData.lastName"
        id="lastName"
      />

      <label class="label" for="officeName">Office</label>
      <UISelect
        class="field"
        placeholder="Office name"
        placeholderBlue
        placeholderUnderline
        name="officeName"
      >
        <option v-for="company in companies" :value="company">
          {{ company }}
        </option>
      </UISelect>

      <label class="label" for="birthDate">Birthdate</label>
      <input
        class="field"
        type="date"
        v-model="formData.birthDate"
        placeholder="Birthdate [dd/mm/yy]"
        id="birthDate"
      />

      <label class="label" for="password">Password</label>
      <input
        class="field"
        type="password"
        v-model="formData.password"
        id="password"
      />
      <div class="actions">
        <UIButton @click="saveUser">Save</UIButton>
        <UIButton class="cancel-btn" @click="close">Cancel</UIButton>
      </div>
    </main>
  </div>
</template>

<script setup>
import UIHeader from "@/components/UIHeader.vue";
import UIButton from "@/components/UIButton.vue";
import UISelect from "@/components/UISelect.vue";
import { ref } from "vue";

const props = defineProps({
  open: { type: Boolean, required: true },
});

const emit = defineEmits(["close"]);

const formData = {
  email: "",
  firstName: "",
  lastName: "",
  officeName: "",
  birthDate: "",
  password: "",
};

const apiUrl = "src/data/companies.json";

const close = () => {
  emit("close");
};

const fetchUsers = async () => {
  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    companies.value = data;
  } catch (error) {
    console.error("Error fetching list of companies:", error);
  }
};

const companies = ["Apple", "Google", "Microsoft", "Facebook"];

const saveUser = () => {};

const closeModal = () => {};
</script>

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
