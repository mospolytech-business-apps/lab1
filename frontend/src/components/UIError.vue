<script setup>
import { useErrorsStore } from "@/stores/errors.store";
import { storeToRefs } from "pinia";

const errorStore = useErrorsStore();
const { removeError } = errorStore;
const { errors } = storeToRefs(errorStore);

errorStore.$subscribe((state) => {
  if (state.events.target.length > 0) {
    setTimeout(() => {
      removeError(errors.value[0]);
    }, 3000);
  }
});
</script>

<template>
  <span class="err" v-show="errors.length"> {{ "🚨 " + errors?.at(-1) }}</span>
</template>

<style scoped>
.err {
  color: darkred;
}
</style>
