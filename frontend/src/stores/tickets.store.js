import { ref } from "vue";
import { defineStore, storeToRefs } from "pinia";
import { api } from "@/api";
import { useErrorsStore } from "@/stores/errors.store";
import Cookies from "js-cookie";

export const useTicketsStore = defineStore("tickets", () => {
  const { addError } = useErrorsStore();

  const searchForTickets = async (data) => {
    const { res, err } = await api.searchForTickets({
      accessToken: Cookies.get("ACCESS_TOKEN"),
      payload: data,
    });

    if (err !== null) {
      addError(err.message);
      return;
    }

    return res;
  };

  const issueTicket = async (data) => {
    const { res, err } = await api.issueTicket({
      accessToken: Cookies.get("ACCESS_TOKEN"),
      payload: data,
    });

    if (err !== null) {
      addError(err.message);
      return;
    }

    return res;
  };

  return {
    searchForTickets,
    issueTicket,
  };
});
