import { ref } from "vue";
import { defineStore, storeToRefs } from "pinia";
import { api } from "@/api";
import { useNotificationsStore } from "@/stores/notifications.store";
import Cookies from "js-cookie";

export const useSchedulesStore = defineStore("schedules", () => {
  const { addError } = useNotificationsStore();

  const allSchedules = ref([]);

  const getAllSchedules = async () => {
    const { res, err } = await api.getAllSchedules({
      accessToken: Cookies.get("ACCESS_TOKEN"),
    });

    if (err !== null) {
      addError(err.message);
      return;
    }

    allSchedules.value = res;

    return res;
  };

  const importCSV = async (formData) => {
    const { res, err } = await api.importSchedules({
      accessToken: Cookies.get("ACCESS_TOKEN"),
      formData,
    });

    if (err !== null) {
      addError(err.message);
      return;
    }

    allSchedules.value = res;

    return res;
  };

  const cancelFlight = async (id) => {
    const { res, err } = await api.cancelFlight({
      accessToken: Cookies.get("ACCESS_TOKEN"),
      id,
    });

    if (err !== null) {
      addError(err.message);
      return;
    }

    allSchedules.value = res;

    return res;
  };

  const updateFlight = async (id, ...data) => {
    const { res, err } = await api.updateFlight({
      accessToken: Cookies.get("ACCESS_TOKEN"),
      id,
      ...data,
    });

    if (err !== null) {
      addError(err.message);
      return;
    }

    allSchedules.value = res;

    return res;
  };

  return {
    allSchedules,
    getAllSchedules,
    importCSV,
    cancelFlight,
    updateFlight,
  };
});
