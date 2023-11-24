import { defineStore } from "pinia";
import { api } from "@/api";
import { addError } from "./error.store";

export default useAuthStore = defineStore("auth", () => {
  const users = ref([]);
  const offices = ref([]);
  const isLogoutModalOpen = ref(false);

  const login = async (username, password) => {
    try {
      const status = await api.login({
        username,
        password,
      });

      if (!data.is_active) {
        throw new Error("Пользователь заблокирован");
      }

      cookie.setCookie(ACCESS_TOKEN, access);

      commit("setUser", data);
    } catch (error) {
      if (error instanceof Error) {
        addError(error.message);
      }
    }
  };

  const me = async ({ token }) => {
    try {
      user.value = {
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
      } = await api.getUser({ id, token });
    } catch (error) {
      if (error instanceof Error) {
        addError(error.message);
      }
    }
  };

  const getUser = async ({ id, token }) => {
    try {
      user.value = {
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
      } = await api.getUser({ id, token });
    } catch (error) {
      if (error instanceof Error) {
        addError(error.message);
      }
    }
  };

  const editUser = ({ token, email, ...props }) =>
    fetch(`${BACKEND_URL}/auth/edit/`, {
      method: "PATCH",
      headers: {
        ...headers,
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ email, ...props }),
    }).then((res) => res.json());

  const getAllUsers = ({ token }) =>
    fetch(`${BACKEND_URL}/auth/users/`, {
      method: "GET",
      headers: { ...headers, Authorization: `Bearer ${token}` },
    }).then((res) => res.json());

  const getOffices = ({ token }) =>
    fetch(`${BACKEND_URL}/office/`, {
      method: "GET",
      headers: { ...headers, Authorization: `Bearer ${token}` },
    }).then((res) => res.json());

  const logout = ({ token, error }) =>
    fetch(`${BACKEND_URL}/auth/logout/`, {
      method: "POST",
      headers: {
        ...headers,
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ error }),
    }).then((res) => res.json());

  const surveys = ({ token }) =>
    fetch(`${BACKEND_URL}/survey/`, {
      method: "GET",
      headers: { ...headers, Authorization: `Bearer ${token}` },
    }).then((res) => res.json());

  const schedules = ({ token }) =>
    fetch(`${BACKEND_URL}/schedules/`, {
      method: "GET",
      headers: { ...headers, Authorization: `Bearer ${token}` },
    }).then((res) => res.json());

  const airports = ({ token }) =>
    fetch(`${BACKEND_URL}/airport/`, {
      method: "GET",
      headers: { ...headers, Authorization: `Bearer ${token}` },
    }).then((res) => res.json());

  const cancelSchedule = ({ token, id }) =>
    fetch(`${BACKEND_URL}/schedules/${id}/`, {
      method: "PATCH",
      headers: {
        ...headers,
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ Confirmed: false }),
    }).then((res) => res.json());

  const updateSchedule = ({ token, id, Date, Time, EconomyPrice }) =>
    fetch(`${BACKEND_URL}/schedules/${id}/`, {
      method: "PATCH",
      headers: {
        ...headers,
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ Date, Time, EconomyPrice }),
    }).then((res) => res.json());

  const importSchedules = ({ token, formData }) =>
    fetch(`${BACKEND_URL}/schedules/import/`, {
      method: "POST",
      headers: {
        ...headers,
        Authorization: `Bearer ${token}`,
      },
      body: formData,
    }).then((res) => res.json());

  return {
    users,
    offices,
    isLogoutModalOpen,
    login,
    me,
    getUser,
    editUser,
    getAllUsers,
    getOffices,
    logout,
    surveys,
    schedules,
    airports,
    cancelSchedule,
    updateSchedule,
    importSchedules,
  };
});
