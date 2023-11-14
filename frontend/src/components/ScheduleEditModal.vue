<template>
  <div v-if="props.open" class="modal">
    <UIHeader title="Schedule edit" :closeButtonHandler="cancel" />
    <main class="main">
      <fieldset class="info">
        <legend>Flight route</legend>
        <p>From: <b>AUH</b></p>
        <p>To: <b>ADE</b></p>
        <p>Aircraft: <b>Boeing 739</b></p>
      </fieldset>
      <div class="inputs">
        <label class="field">
          <span class="label">Date: </span>
          <input class="input" type="date" />
        </label>
        <label class="field">
          <span class="label">Time: </span>
          <input class="input" type="time" />
        </label>
        <label class="field">
          <span class="label">Economy price: $ </span>
          <input class="input price-input" type="text" />
        </label>
      </div>
      <div class="buttons">
        <UIButton @click="update" type="button" id="saveSchedule">
          Update
        </UIButton>
        <UIButton
          class="cancel-btn"
          @click="cancel"
          type="button"
          data-dismiss="modal"
        >
          Cancel
        </UIButton>
      </div>
    </main>
  </div>
</template>

<script setup>
import UIHeader from "@/components/UIHeader.vue";
import UIButton from "@/components/UIButton.vue";

const props = defineProps({
  open: { type: Boolean, required: true },
});

const emit = defineEmits(["close"]);

const cancel = () => {
  emit("close");
};

const update = () => {
  // TODO: implement updae logic
  alert("Schedule updated");
  emit("close");
};
</script>

<style scoped>
.modal {
  position: absolute;
  top: 50%;
  left: 50%;
  background-color: white;
  min-width: 60%;
  transform: translate(-50%, -50%);
  border: 1px solid black;
  box-shadow: 0 0 2rem black;
}

.main {
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.field {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.inputs {
  display: flex;
  justify-content: space-around;
}
.info {
  display: flex;
  gap: 4rem;
  padding-bottom: 2rem;
}
.buttons {
  display: flex;
  justify-content: end;
  gap: 2rem;
}
.price-input {
  max-width: 5rem;
}

.cancel-btn:hover {
  background-color: salmon;
}
</style>
