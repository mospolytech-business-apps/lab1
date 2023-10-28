import { defineStore } from "pinia";

export const useUserRoleStore = defineStore("userStore", {
  state: () => ({
    userRole: null,
  }),

  actions: {
    setUserRole(userRole) {
      this.userRole = userRole;
    },
  },
});
