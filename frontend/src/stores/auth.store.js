import { defineStore, storeToRefs } from "pinia";
import { api } from "@/api";
import { useErrorsStore } from "@/stores/errors.store";
import { useUsersStore } from "@/stores/users.store";
import router from "@/router";

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

    console.log(res.data);

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

    console.log(currentUser.value);

    userRole.value = currentUser.value.isAdmin ? "admin" : "user";

    Cookies.set("ACCESS_TOKEN", res.access);

    router.push("/");
  };

  const logout = async ({ token, error }) =>
    fetch(`${BACKEND_URL}/auth/logout/`, {
      method: "POST",
      headers: {
        ...headers,
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ error }),
    }).then((res) => res.json());

  return {
    login,
    logout,
  };
});
