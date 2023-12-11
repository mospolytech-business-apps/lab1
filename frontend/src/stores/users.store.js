import { ref, computed } from "vue";
import { api } from "@/api";
import { defineStore } from "pinia";
import { useErrorsStore } from "@/stores/errors.store";
import Cookies from "js-cookie";

export const useUsersStore = defineStore("users", () => {
  const { addError } = useErrorsStore();

  const currentUser = ref({});
  const allUsers = ref([]);

  const userRole = ref(null);

  const getAllUsers = async () => {
    const { res, err } = await api.getAllUsers({
      accessToken: Cookies.get("ACCESS_TOKEN"),
    });

    if (err !== null) {
      addError(err.message);
      return;
    }

    allUsers.value = res;

    return res;
  };

  const getUser = async (id) => {
    const { res, err } = await api.getUser({
      accessToken: Cookies.get("ACCESS_TOKEN"),
      id,
    });

    if (err !== null) {
      addError(err.message);
      return;
    }

    return ({
      id,
      office,
      role,
      lastLogin: last_login,
      username: email,
      firstName: first_name,
      lastName: last_name,
      birthday,
      isAdmin: is_superuser,
      isActive: is_active,
      login_logout_times,
    } = res);
  };

  const addUser = async (props) => {
    const { status, err } = await api.addUser({
      accessToken: Cookies.get("ACCESS_TOKEN"),
      ...props,
    });

    if (err !== null) {
      addError(err.message);
      return;
    }

    return status;
  };

  const editUser = async (id, ...props) => {
    const { status, err } = await api.editUser({
      accessToken: Cookies.get("ACCESS_TOKEN"),
      id,
      ...props,
    });

    if (err !== null) {
      addError(err.message);
      return;
    }

    return status;
  };

  const ban = async (id) => {
    const { status, err } = await api.banUser({
      accessToken: Cookies.get("ACCESS_TOKEN"),
      id,
    });

    if (err !== null) {
      addError(err.message);
      return;
    }

    return status;
  };

  const unban = async (id) => {
    const { status, err } = await api.unbanUser({
      accessToken: Cookies.get("ACCESS_TOKEN"),
      id,
    });

    if (err !== null) {
      addError(err.message);
      return;
    }

    return status;
  };

  const sendLogoutInformation = async (reason, loginTime) => {
    const { status, err } = await api.sendLogoutInformation({
      accessToken: Cookies.get("ACCESS_TOKEN"),
      id: currentUser.value.id,
      reason,
      loginTime,
    });

    if (err !== null) {
      addError(err.message);
      return;
    }

    return status;
  };

  return {
    allUsers,
    currentUser,
    userRole,
    getUser,
    editUser,
    addUser,
    getAllUsers,
    ban,
    unban,
    sendLogoutInformation,
  };
});
