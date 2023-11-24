import { defineStore } from "pinia";

export const useLogoutStore = defineStore("logout", () => {
  const lastLogin = ref(JSON.parse(localStorage.getItem("logoutInformation")));
  const logoutReason = ref(localStorage.getItem("logoutInformation"));

  const isNoLogoutDetected = computed(() => {
    return !!(this.lastLogin && !this.logoutReason);
  });

  const setLogoutInformation = (lastLogin, logoutReason) => {
    lastLogin.value = lastLogin;
    logoutReason.value = logoutReason;

    localStorage.setItem(
      "logoutInformation",
      JSON.stringify({ lastLogin, logoutReason })
    );
  };

  const resetLogoutInformation = () => {
    lastLogin.value = null;
    logoutReason.value = null;
  };

  return {
    lastLogin,
    logoutReason,
    isNoLogoutDetected,
    setLogoutInformation,
    resetLogoutInformation,
  };
});
