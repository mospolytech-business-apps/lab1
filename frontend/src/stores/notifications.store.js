import { defineStore } from "pinia";
import { ref } from "vue";

export const useNotificationsStore = defineStore("notifications", () => {
  const errors = ref([]);
  const alerts = ref([]);

  const addError = (error) => {
    console.log("err", error);
    errors.value.push(error);
  };

  const addAlert = (alert) => {
    alerts.value.push(alert);
  };

  const removeError = (error) => {
    errors.value = errors.value.filter((e) => e !== error);
  };

  const removeAlert = (alert) => {
    alerts.value = alerts.value.filter((a) => a !== alert);
  };

  const clearErrors = () => {
    errors.value = [];
  };

  const clearAlerts = () => {
    alerts.value = [];
  };

  return {
    errors,
    addError,
    removeError,
    clearErrors,
    alerts,
    addAlert,
    removeAlert,
    clearAlerts,
  };
});
