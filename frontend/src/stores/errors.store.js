import { defineStore } from "pinia";
import { ref } from "vue";

export const useErrorsStore = defineStore("errors", () => {
  const errors = ref([]);

  const addError = (error) => {
    console.log("err", error);
    errors.value.push(error);
  };

  const removeError = (error) => {
    errors.value = errors.value.filter((e) => e !== error);
  };

  const clearErrors = () => {
    errors.value = [];
  };

  return {
    errors,
    addError,
    removeError,
    clearErrors,
  };
});
