<template>
  <div class="exit-popup" v-show="isVisible">
    <div class="popup-content">
      <h1>Are you sure you want to exit?</h1>
      <p>You will need to login again.</p>
      <button @click="closePopup">Cancel</button>
      <button @click="confirmExit">Leave</button>
    </div>
  </div>
</template>

<script setup>
import { ref, watchEffect, onUnmounted } from "vue";

const isVisible = ref(false);

const closePopup = () => {
  isVisible.value = false;
};

const confirmExit = () => {};

watchEffect(() => {
  document.addEventListener("mouseout", (event) => {
    if (event.toElement === null || event.relatedTarget === null) {
      isVisible.value = true;
    }
  });
});

onUnmounted(() => {
  document.removeEventListener("mouseout", (event) => {
    isVisible.value = false;
  });
});
</script>

<style scoped>
.exit-popup {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1000;
  display: none;
}

.popup-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 500px;
  height: 200px;
  background-color: white;
  padding: 20px;
  text-align: center;
}

.popup-content button {
  margin-top: 10px;
}
</style>
