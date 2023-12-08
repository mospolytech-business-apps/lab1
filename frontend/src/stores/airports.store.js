import { ref } from "vue";
import { defineStore, storeToRefs } from "pinia";
import { api } from "@/api";
import { useErrorsStore } from "@/stores/errors.store";

export const useAirportsStore = defineStore("airports", () => {
  const { addError } = useErrorsStore();

  const allAirports = ref([]);

  const getAllAirports = async () => {
    const { res, err } = await api.getAllAirports();

    if (err !== null) {
      addError(err.message);
      return;
    }

    allAirports.value = res;

    return res;
  };

  return {
    allAirports,
    getAllAirports,
  };
});
