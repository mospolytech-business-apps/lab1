import { ref } from "vue";
import { defineStore, storeToRefs } from "pinia";
import { api } from "@/api";
import { useErrorsStore } from "@/stores/errors.store";

export const useOfficesStore = defineStore("offices", () => {
  const { addError } = useErrorsStore();

  const allOffices = ref([]);

  const getAllOffices = async () => {
    const { res, err } = await api.getAllOffices();

    if (err !== null) {
      addError(err.message);
      return;
    }

    allOffices.value = res;

    return res;
  };

  return {
    allOffices,
    getAllOffices,
  };
});
