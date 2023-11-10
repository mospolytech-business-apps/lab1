<template>
  <div class="modal">
    <div class="main">
      <h3 class="title">Add User</h3>
      <input type="email" v-model="email" placeholder="Email address" />
      <input type="text" v-model="firstName" placeholder="First name" />
      <input type="text" v-model="lastName" placeholder="Last name" />
      <se type="text" v-model="officeName" placeholder="Office name" />
      <select name="officeName" id=""></select>
      <input
        type="date"
        v-model="birthDate"
        placeholder="Birthdate [dd/mm/yy]"
      />
      <input type="password" v-model="password" placeholder="Password" />
      <div class="actions">
        <button type="button" @click="saveUser">Save</button>
        <button type="button" @click="closeModal">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script setup>
const formData = {
  email: "",
  firstName: "",
  lastName: "",
  officeName: "",
  birthDate: "",
  password: "",
};

const saveUser = () => {};

const closeModal = () => {};
</script>

<style lang="scss">
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.main {
  background-color: white;
  width: 50%;
  height: 50%;
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

button {
  padding: 0.5rem;
  background-color: #3498db;
  color: white;
  border: none;
  cursor: pointer;
}
</style>
