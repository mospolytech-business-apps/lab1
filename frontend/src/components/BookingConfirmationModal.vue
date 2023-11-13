<template>
  <div v-if="props.open" class="modal">
    <UIHeader title="Add User" :closeButtonHandler="close" />
    <main class="main"></main>
  </div>
</template>

<script setup>
import UIHeader from "@/components/UIHeader.vue";
import UIButton from "@/components/UIButton.vue";
import { ref } from "vue";

const props = defineProps({
  open: { type: Boolean, required: true },
});

const emit = defineEmits(["close"]);

const apiUrl = "src/assets/confirmation.json";

const close = () => {
  emit("close");
};

// const fetchUsers = async () => {
//   try {
//     const response = await fetch(apiUrl);
//     const data = await response.json();
//     companies.value = data;
//   } catch (error) {
//     console.error("Error fetching list of companies:", error);
//   }
// };
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
  align-items: center;
  gap: 0.25rem;
  width: 100%;
  padding: 1rem 2rem;
  background-color: white;
  padding: 1rem;
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
