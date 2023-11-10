<template>
  <div class="modal" v-if="open" ref="modal">
    <HeaderComponent :title="props.title" :closeButtonHandler="close" />
    <main class="main">
      <h1 class="title">
        No logout detected on your last login on {{ lastLogin }}
      </h1>
      <p>Reason:</p>
      <textarea
        class="textarea"
        name="additionalInformation"
        id="additionalInformation"
        v-model="additionalInformation"
      />
      <div class="bottom-row">
        <label class="label">
          <span class="reason">Software crash</span>
          <input type="radio" name="" id="" />
        </label>
        <label class="label">
          <span class="reason">System crash</span>
          <input type="radio" name="" />
        </label>
        <button class="btn" @click="submitForm">Confirm</button>
      </div>
    </main>
  </div>
</template>

<script setup>
import { defineProps, defineEmits, ref, onMounted } from "vue";
import { useLogoutStore } from "@/stores/logout";
import HeaderComponent from "@/components/HeaderComponent.vue";

const props = defineProps({
  open: { type: Boolean, required: true, default: true },
});

const close = () => {
  emit("close");
};

const emit = defineEmits(["close", "submit"]);

const logoutStore = useLogoutStore();

let logoutReason = "";
let additionalInformation = "";

async function submitForm() {
  const response = await fetch("/api/submit-no-logout-form", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      logoutReason,
      additionalInformation,
    }),
  });

  if (response.ok) {
    emit("submit");
    emit("close");
    alert("Data send successfully. Thank you for your feedback.");
  } else {
    alert("An error occurred while submitting the form. Please try again");
  }
}
</script>
<style scoped>
.modal {
  position: absolute;
  top: 50%;
  left: 50%;
  background-color: white;
  min-width: 40%;
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
}

.title {
  font-size: 1em;
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
