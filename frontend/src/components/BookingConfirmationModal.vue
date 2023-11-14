<template>
  <div v-if="props.open" class="modal">
    <UIHeader title="Booking confirmation" :closeButtonHandler="close" />
    <main class="main">
      <fieldset class="details">
        <legend>Outbounding flight details</legend>
        <p class="detail">From: <b>QWE</b></p>
        <p class="detail">To: <b>ABC</b></p>
        <p class="detail">Cabin Type: <b>Economy</b></p>
        <p class="detail">Date: <b>11/10/2017</b></p>
        <p class="detail">Flight number: <b>1908</b></p>
      </fieldset>
      <fieldset class="details">
        <legend>Return flight details</legend>
        <p class="detail">From: <b>QWE</b></p>
        <p class="detail">To: <b>ABC</b></p>
        <p class="detail">Cabin Type: <b>Economy</b></p>
        <p class="detail">Date: <b>11/10/2017</b></p>
        <p class="detail">Flight number: <b>1908</b></p>
      </fieldset>
      <fieldset class="passenger-details">
        <legend>Passenger details</legend>
        <label class="field">
          <span class="label">Firstname</span>
          <input class="input" type="text" />
        </label>
        <label class="field">
          <span class="label">Lastname</span>
          <input class="input" type="text" />
        </label>
        <label class="field">
          <span class="label">Birthdate</span>
          <input class="input" type="date" />
        </label>
        <label class="field">
          <span class="label">Passport number</span>
          <input class="input" type="text" />
        </label>
        <label class="field">
          <span class="label">Passport country</span>
          <UISelect class="input" placeholder=" ">
            <option value="russia">Russia</option>
          </UISelect>
        </label>
        <label class="field">
          <span class="label">Phone</span>
          <input class="input" placeholder="(___) ___ __-__" type="tel" />
        </label>
        <UIButton class="passenger-details-btn">Add passenger</UIButton>
      </fieldset>

      <div class="passengers-list">
        <p class="table-title">Passengers list</p>
        <div class="table-wrapper">
          <table class="table">
            <thead>
              <tr>
                <th>Firstname</th>
                <th>Lastname</th>
                <th>Birthdate</th>
                <th>Passport number</th>
                <th>Passport country</th>
                <th>Phone</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="passenger in passengers"
                :key="passenger.id"
                @click="selectPassenger(passenger)"
                :class="{
                  selected: passenger === selectedPassenger,
                  row: true,
                }"
              >
                <td>{{ passenger.firstName || "–" }}</td>
                <td>{{ passenger.lastName || "–" }}</td>
                <td>{{ passenger.birthdate || "–" }}</td>
                <td>{{ passenger.passportNumber || "–" }}</td>
                <td>{{ passenger.passportCounty || "–" }}</td>
                <td>{{ passenger.phone || "–" }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <UIButton class="remove-passenger" @click="removePassenger"
          >Remove passenger</UIButton
        >
        <div class="bottom-actions">
          <UIButton @click="close">
            <img src="src/assets/reload-icon.png" width="20" alt="Back icon" />
            <span>Back to search for filters</span>
          </UIButton>
          <UIButton @click="openBillingConfirmationModal">
            <img
              src="src/assets/check-mark-icon.png"
              width="20"
              alt="Confirm icon"
            />
            <span>Confirm booking</span>
          </UIButton>
        </div>
      </div>
    </main>
  </div>
  <BillingConfirmation
    :open="isBillingConfirmationOpen"
    @close="closeBillingConfirmationModal"
  />
</template>

<script setup>
import UIHeader from "@/components/UIHeader.vue";
import UIButton from "@/components/UIButton.vue";
import UISelect from "@/components/UISelect.vue";
import BillingConfirmation from "@/components/BillingConfirmation.vue";
import { ref } from "vue";

const isBillingConfirmationOpen = ref(false);

const openBillingConfirmationModal = () => {
  isBillingConfirmationOpen.value = true;
};

const closeBillingConfirmationModal = () => {
  isBillingConfirmationOpen.value = false;
};

const props = defineProps({
  open: { type: Boolean, required: true },
});

const emit = defineEmits(["close"]);

const apiUrl = "src/data/passengers.json";

const passengers = ref([]);

const close = () => {
  emit("close");
};

const selectedPassenger = ref(null);

const selectPassenger = (passenger) => {
  selectedPassenger.value = passenger;
};

const removePassenger = () => {
  // TODO: remove passenger
  console.log("removePassenger");
};

const fetchPassengers = async () => {
  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    passengers.value = data;
  } catch (error) {
    console.error("Error fetching list of passengers:", error);
  }
};

fetchPassengers();
</script>

<style scoped>
.modal {
  position: absolute;
  top: 50%;
  left: 50%;
  background-color: white;
  min-width: 65%;
  transform: translate(-50%, -50%);
  border: 1px solid black;
  box-shadow: 0 0 2rem black;
}

.main {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  width: 100%;
  padding: 1rem 2rem;
  background-color: white;
  padding: 1rem;
  overflow: scroll;
}

.table-wrapper {
  flex-grow: 1;
  width: 100%;
  border: 2px solid black;
  overflow: scroll;
}

.details {
  display: flex;
  width: 100%;
  gap: 4rem;
}
.detail {
  display: inline;
  gap: 0.25rem;
}
.table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid black;
  overflow: scroll;
}

.passenger-details {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  row-gap: 1rem;
  column-gap: 2rem;
}

.field {
  display: flex;
  gap: 0.5rem;
}
.input {
  /* width: 100%; */
  min-width: 10rem;
  flex-grow: 1;
}

.label {
  flex-grow: 1;
  align-self: center;
  width: max-content;
}

thead {
  background-color: lightgray;
}

td,
th {
  border: 1px solid black;
  padding-inline-start: 0.25rem;
}

.passengers-list {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  width: 100%;
}
.table-title {
}

.passenger-details-btn {
  grid-column: -2 / -1;
  margin-left: auto;
}

.remove-passenger {
  margin-left: auto;
}
.remove-passenger:hover {
  background-color: salmon;
}

.bottom-actions {
  display: flex;
  justify-content: center;
  gap: 2rem;
}

.selected {
  box-shadow: inset 0 0 0 2px black;
}
</style>
