import { defineStore } from "pinia";

export const modalStore = defineStore("modal", {
  state: () => ({
    activeModal: null,
  }),
});
