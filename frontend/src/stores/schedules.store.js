import { ref } from "vue";
import { defineStore, storeToRefs } from "pinia";
import { api } from "@/api";
import { useErrorsStore } from "@/stores/errors.store";
import Cookies from "js-cookie";

export const useOfficesStore = defineStore("offices", () => {
  const { addError } = useErrorsStore();

  const allSchedules = ref([]);

  const getAllSchedules = async () => {
    const { res, err } = await api.getAllSchedules(Cookies.get("accessToken"));

    if (err !== null) {
      addError(err.message);
      return;
    }

    allSchedules.value = res;

    return res;
  };

  const importCSV = async (file) => {
    const { res, err } = await api.importCSV(Cookies.get("accessToken"), file);

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
  };
});
