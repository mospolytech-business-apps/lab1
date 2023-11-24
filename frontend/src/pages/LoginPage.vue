<template>
  <main class="main">
    <UIHeader />
    <form class="form" @submit.prevent="onSubmit">
      <img width="500" class="logo" src="@/assets/logo.png" alt="Amonic" />
      <label class="label">
        <span class="span">Username:</span>
        <input
          class="input"
          type="text"
          v-model="username"
          ref="usernameInput"
        />
      </label>
      <label class="label">
        <span class="span">Password:</span>
        <input class="input" type="password" v-model="password" />
      </label>
      <div class="buttons">
        <button class="btn" type="submit">Login</button>
        <button class="btn" @click="openExit" type="reset">Exit</button>
      </div>
    </form>
  </main>
</template>

<script setup>
import { onMounted, ref } from "vue";
import router from "../router";
import UIHeader from "@/components/UIHeader.vue";

import { storeToRefs } from "pinia";

const username = ref("");
const password = ref("");

const onSubmit = async () => {
  let userRole = "";

  const status = await login(username.value, password.value);

  if (status == 200) {
    userRole = "admin";
  } else {
    userRole = "user";
  }

  if (username.value == "admin" && password.value == "admin") {
    userRole = "admin";
  }

  if (username.value == "user" && password.value == "user") {
    userRole = "user";
  }

  userRoleStore.setUserRole(userRole);

  router.push("/");
};

const usernameInput = ref(null);

onMounted(() => {
  usernameInput.value.focus();
});

const openExit = () => {
  popup.value?.show();
};
</script>

<style scoped>
.main {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  overflow: scroll;
}
.login-page {
  width: 100%;
  height: 100%;
  display: grid;
  place-items: center;
}
.form {
  padding: 2rem;
  display: flex;
  height: 100%;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 1rem;
}

.label {
  position: relative;
}
.span {
  position: absolute;
  left: -25%;
}

.input {
  min-width: 20rem;
}

.buttons {
  display: flex;
  gap: 1rem;
}
.btn {
  padding: 0.25rem 3rem;
  border: 1px solid black;
  border-radius: 5px;
  background-color: white;
  cursor: pointer;
}
</style>
