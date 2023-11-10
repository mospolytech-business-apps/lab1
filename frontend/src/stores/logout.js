import { defineStore } from "pinia";

export const useLogoutStore = defineStore("logout", {
  state: () => ({
    lastLogin: JSON.parse(localStorage.getItem("logoutInformation")),
    logoutReason: localStorage.getItem("logoutInformation"),
  }),
  getters: {
    isNoLogoutDetected() {
      return !!(this.lastLogin && !this.logoutReason);
    },
  },
  actions: {
    setLogoutInformation(lastLogin, logoutReason) {
      this.lastLogin = lastLogin;
      this.logoutReason = logoutReason;

      localStorage.setItem(
        "logoutInformation",
        JSON.stringify({ lastLogin, logoutReason })
      );
    },
    resetLogoutInformation() {
      this.lastLogin = null;
      this.logoutReason = null;
    },
  },
});
