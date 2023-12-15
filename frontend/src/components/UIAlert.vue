<script setup>
import { useNotificationsStore } from "@/stores/notifications.store";
import { storeToRefs } from "pinia";

const errorStore = useNotificationsStore();
const { removeAlert } = errorStore;
const { alerts } = storeToRefs(errorStore);

errorStore.$subscribe((state) => {
  if (state.events.target.length > 0) {
    setTimeout(() => {
      removeAlert(alerts.value[0]);
    }, 3000);
  }
});
</script>

<template>
  <span class="err" v-show="alerts.length"> {{ "🔔 " + alerts?.at(-1) }}</span>
</template>

<style scoped>
.err {
  color: orange;
}
</style>
