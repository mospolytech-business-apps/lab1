import { defineStore } from "pinia";
import { ref } from "vue";

export default useErrorStore = defineStore("app", () => {
  const errors = ref([]);

  const addError = (error) => {
    errors.value.push(error);
  };

  const clearErrors = () => {
    errors.value = [];
  };

  return {
    errors,
    addError,
    clearErrors,
  };
});
