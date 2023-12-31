import { ref } from "vue";
import { defineStore } from "pinia";
import { api } from "@/api";
import { useNotificationsStore } from "@/stores/notifications.store";

export const useAirportsStore = defineStore("airports", () => {
  const { addError } = useNotificationsStore();

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
