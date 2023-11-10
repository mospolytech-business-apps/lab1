<template>
  <HeaderComponent title="Parent Test title" />

  <div align="center">
    <button @click="openModal1">Open model1</button>
  </div>

  <ModelWindow1
    v-if="isOpen1"
    :open="isOpen1"
    title="model1"
    @close="closeWindow1"
  />
  <ModelWindow2
    v-if="isOpen2"
    :open="isOpen2"
    title="model2"
    @close="closeWindow2"
  />
</template>

<script setup>
import ModelWindow1 from "@/components/ModelWindow1.vue";
import HeaderComponent from "@/components/HeaderComponent.vue";
import { ref } from "vue";

const isOpen1 = ref(false);
const isOpen2 = ref(false);

function openModal1() {
  isOpen1.value = true;
}

function openModal2() {
  isOpen2.value = true;
}

function closeWindow1() {
  isOpen1.value = false;
}

function closeWindow2() {
  isOpen2.value = false;
}
</script>
