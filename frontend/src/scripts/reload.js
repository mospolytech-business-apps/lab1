import { useLogoutStore } from "@/stores/logout";

export default () => {
  if (confirm("Are you sure you want to logout?")) {
    // Get the logout information from browser storage
    const logoutInformation = JSON.parse(
      localStorage.getItem("logoutInformation")
    );

    // If logout information exists, set it in the logout store
    if (logoutInformation) {
      const logoutStore = useLogoutStore();
      logoutStore.setLogoutInformation(
        logoutInformation.lastLogin,
        logoutInformation.logoutReason
      );
    }

    // Reload the page
    window.location.reload();
  }
};
