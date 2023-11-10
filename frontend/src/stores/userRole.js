import { defineStore } from "pinia";

export const useUserRoleStore = defineStore("userRoleStore", {
  state: () => ({
    userRole: null,
  }),

  actions: {
    setUserRole(userRole) {
      this.userRole = userRole;
    },
  },
});
