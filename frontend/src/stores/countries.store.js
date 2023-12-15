import { ref } from "vue";
import { defineStore } from "pinia";
import { api } from "@/api";
import { useNotificationsStore } from "@/stores/notifications.store";

export const useCountriesStore = defineStore("countries", () => {
  const { addError } = useNotificationsStore();

  const allCountries = ref([]);

  const getAllCountries = async () => {
    const { res, err } = await api.getAllCountries();

    if (err !== null) {
      addError(err.message);
      return;
    }

    allCountries.value = res;

    return res;
  };

  return {
    allCountries,
    getAllCountries,
  };
});
