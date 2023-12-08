<script setup>
import UIHeader from "@/components/UIHeader.vue";
import UIButton from "@/components/UIButton.vue";

import { ref, watch, onMounted } from "vue";
import { useSchedulesStore } from "@/stores/schedules.store";
const { updateFlight } = useSchedulesStore();

const props = defineProps({
  open: { type: Boolean, required: true },
  flight: { type: Object, required: true },
});

const emit = defineEmits(["close", "updateData"]);

const date = ref(null);
const time = ref(null);
const economyPrice = ref(null);

watch(
  () => props.flight,
  (newVal) => {
    if (newVal) {
      date.value = newVal.Date;
      time.value = newVal.Time;
      economyPrice.value = newVal.EconomyPrice;
    }
  },
  { immediate: true }
);

const applyFlightChanges = () => {
  console.log(props.flight);
  const payload = {
    date: date.value,
    time: time.value,
    economyPrice: economyPrice.value,
  };
  console.log(payload);
  updateFlight(props.flight.id, payload);
  emit("updateData");
  date.value = null;
  time.value = null;
  economyPrice.value = null;
  emit("close");
};

const cancel = () => {
  emit("close");
};
</script>

<template>
  <div v-if="props.open" class="modal">
    <UIHeader title="Schedule edit" :closeButtonHandler="cancel" />
    <main class="main">
      <fieldset class="info">
        <legend>Flight route</legend>
        <p>
          From: <b>{{ props.flight.Route.DepartureAirport.IATACode }}</b>
        </p>
        <p>
          To: <b>{{ props.flight.Route.ArrivalAirport.IATACode }}</b>
        </p>
        <p>
          Aircraft: <b>{{ props.flight.Aircraft.Name }}</b>
        </p>
      </fieldset>
      <div class="inputs">
        <label class="field">
          <span class="label">Date: </span>
          <input v-model="date" class="input" type="date" />
        </label>
        <label class="field">
          <span class="label">Time: </span>
          <input v-model="time" class="input" type="time" />
        </label>
        <label class="field">
          <span class="label">Economy price: $ </span>
          <input v-model="economyPrice" class="input price-input" type="text" />
        </label>
      </div>
      <div class="buttons">
        <UIButton @click="applyFlightChanges" type="button" id="saveSchedule">
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
