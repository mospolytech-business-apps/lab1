<template>
  <div v-if="props.open" class="modal">
    <UIHeader title="Edit Role" :closeButtonHandler="close" />
    <main class="main">
      <label for="firstName" class="label">First name </label>
      <input type="text" id="firstName" />

      <label for="lastName" class="label">Last name</label>
      <input type="text" id="lastName" />

      <label for="email" class="label">Email address </label>
      <input type="email" id="email" />

      <label for="company" class="label">Office</label>
      <UISelect
        options="companies"
        placeholder="Office name"
        required
        id="company"
      >
        <option v-for="company in companies" :value="company">
          {{ company }}
        </option>
      </UISelect>

      <label class="role-label" for="role">Role</label>
      <div class="role-inputs">
        <label for="user" class="label">
          <input class="input" type="radio" name="role" id="user" />
          User
        </label>

        <label for="admin" class="label">
          <input class="input" type="radio" name="role" id="admin" />
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

<script setup>
import UIHeader from "@/components/UIHeader.vue";
import UIButton from "@/components/UIButton.vue";
import UISelect from "@/components/UISelect.vue";

const companies = ["Company 1", "Company 2", "Company 3"];

const props = defineProps({
  open: { type: Boolean, required: true },
});

const emit = defineEmits(["close"]);

const applyRoleChanges = () => {
  alert("Role changes not applied!");
};

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
