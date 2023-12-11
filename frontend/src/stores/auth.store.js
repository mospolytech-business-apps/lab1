import { defineStore, storeToRefs } from "pinia";
import { api } from "@/api";
import { useErrorsStore } from "@/stores/errors.store";
import { useUsersStore } from "@/stores/users.store";
import router from "@/router";
import { ref } from "vue";

import Cookies from "js-cookie";

export const useAuthStore = defineStore("auth", () => {
  const { addError } = useErrorsStore();
  const { currentUser, userRole } = storeToRefs(useUsersStore());

  const login = async (username, password) => {
    const { res, err } = await api.login({
      username,
      password,
    });

    if (err !== null) {
      addError(err.message);
      return;
    }

    currentUser.value = {
      id: res.data.id,
      office: res.data.office,
      role: res.data.role,
      lastLogin: res.data.last_login,
      username: res.data.email,
      firstName: res.data.first_name,
      lastName: res.data.last_name,
      birthday: res.data.birthday,
      isAdmin: res.data.is_superuser,
      isActive: res.data.is_active,
      login_logout_times: res.data.login_logout_times,
    };

    userRole.value = currentUser.value.isAdmin ? "admin" : "user";

    Cookies.set("ACCESS_TOKEN", res.access);

    router.push("/");
  };

  const logout = async () => {
    if (confirm("Are you sure you want to log out?")) {
      const _ = await api.logout({
        accessToken: Cookies.get("ACCESS_TOKEN"),
      });

      currentUser.value = null;
      userRole.value = null;

      Cookies.remove("ACCESS_TOKEN");

      window.location.href = "about:blank";
    }
  };

  const me = async () => {
    const { res, err } = await api.me({
      accessToken: Cookies.get("ACCESS_TOKEN"),
    });

    if (err !== null) {
      userRole.value = null;
      return userRole.value;
    }

    currentUser.value = {
      id: res.id,
      office: res.office,
      role: res.role,
      lastLogin: res.last_login,
      username: res.email,
      firstName: res.first_name,
      lastName: res.last_name,
      birthday: res.birthday,
      isAdmin: res.is_superuser,
      isActive: res.is_active,
      login_logout_times: res.login_logout_times,
    };

    return currentUser.value;
  };

  return {
    me,
    login,
    logout,
  };
});
