<template>
  <div v-if="props.open" class="modal">
    <UIHeader title="Edit Role" :closeButtonHandler="close" />
    <main class="main">
      <input
        type="email"
        v-model="formData.email"
        placeholder="Email address"
      />
      <input
        type="text"
        v-model="formData.firstName"
        placeholder="First name"
      />
      <input type="text" v-model="formData.lastName" placeholder="Last name" />
      <input
        type="text"
        v-model="formData.officeName"
        placeholder="Office name"
      />
      <select name="officeName" id="">
        <option v-for="company in companies" :value="company.name">
          {{ company.name }}
        </option>
      </select>
      <input
        type="date"
        v-model="formData.birthDate"
        placeholder="Birthdate [dd/mm/yy]"
      />
      <input
        type="password"
        v-model="formData.password"
        placeholder="Password"
      />
      <div class="actions">
        <UIButton @click="saveUser">Save</UIButton>
        <UIButton @click="closeModal">Cancel</UIButton>
      </div>
    </main>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from "vue";
import UIHeader from "@/components/UIHeader.vue";

const props = defineProps({
  open: { type: Boolean, required: true },
});

const emit = defineEmits(["close"]);

const close = () => {
  emit("close");
};
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
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  padding: 1rem 2rem;
  background-color: white;
  padding: 1rem;
  box-shadow: 0 0 2rem black;
}

.title {
  margin-bottom: 1rem;
}

.input {
  width: 100%;
  margin-bottom: 0.5rem;
}

.actions {
  display: flex;
  justify-content: space-between;
}
</style>
