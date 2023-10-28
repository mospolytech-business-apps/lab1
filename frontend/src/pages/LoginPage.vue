<template>
    <div class="login-page">
        <h1 class="title">Login</h1>
        <form @submit.prevent="onSubmit">
            <input type="text" v-model="username" placeholder="Username" />
            <input type="password" v-model="password" placeholder="Password" />
            <button type="submit">Login</button>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import router from '../router';
import { useUserRoleStore } from '@/store/userRole.js';

defineOptions({
    name: 'LoginPage',
})

const userRoleStore = useUserRoleStore();
const username = ref('');
const password = ref('');

const onSubmit = () => {
  let userRole = "";

  if (username.value == "admin" && password.value == "admin") { 
    userRole = "admin";
  }
  if (username.value == "user" && password.value == "user") {
    userRole = "user";
  }

  userRoleStore.setUserRole(userRole);
  console.log(userRoleStore.userRole)

  router.push("/");
};
</script>

<style scoped>
.login-page {
    width: 100%;
    max-width: 300px;
    margin: 0 auto;
}
</style>
