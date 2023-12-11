<script setup>
import UIHeader from "@/components/UIHeader.vue";
import UIButton from "@/components/UIButton.vue";
import { ref } from "vue";

const props = defineProps({
  open: { type: Boolean, required: true, default: true },
  failedSession: { type: Object, required: true },
});

const close = () => {
  emit("close");
};

const reason = ref("");

const emit = defineEmits(["close", "updateReason"]);

const closeModal = () => {
  if (!reason.value) return;
  emit("updateReason", reason.value);
  emit("close");
};
</script>

<template>
  <div class="modal" v-if="open" ref="modal">
    <UIHeader :title="props.title" :closeButtonHandler="close" />
    <main class="main">
      <h1 class="title">
        No logout detected on your last login on
        {{ props.failedSession.date }} at {{ props.failedSession.loginTime }}
      </h1>
      <p>Reason:</p>
      <textarea class="textarea" />
      <div class="bottom-row">
        <label class="label">
          <input
            v-model="reason"
            value="Software crash"
            type="radio"
            name="reason"
          />
          <span class="reason">Software crash</span>
        </label>
        <label class="label">
          <input
            v-model="reason"
            value="System crash"
            type="radio"
            name="reason"
          />
          <span class="reason">System crash</span>
        </label>
        <UIButton class="btn" @click="closeModal">Confirm</UIButton>
      </div>
    </main>
  </div>
</template>

<style scoped>
.modal {
  position: absolute;
  top: 50%;
  left: 50%;
  background-color: white;
  min-width: 45%;
  transform: translate(-50%, -50%);
  border: 1px solid black;
  box-shadow: 0 0 2rem black;
}

.main {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  padding: 1rem 2rem;
}

.textarea {
  flex-grow: 1;
  min-height: 16ch;
  margin-bottom: 1rem;
  resize: none;
}

.title {
  font-size: 1em;
  font-weight: 400;
}

.bottom-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.btn {
  border: 1px solid black;
  border-radius: 0.25rem;
  padding: 0.25rem 1.5rem;
  background: 0;
  cursor: pointer;
}
</style>
