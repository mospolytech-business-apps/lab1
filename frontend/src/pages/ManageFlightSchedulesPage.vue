<template>
  <UIHeader title="Manage Flight Schedules" />
  <main class="main">
    <fieldset class="filters">
      <legend>Filter by</legend>
      <label class="field">
        <span class="label">From</span>
        <div class="select-wrapper">
          <select class="select" required>
            <option value="" disabled selected>[ Airport list ]</option>
            <option value="SFO">San Francisco International</option>
            <option value="LAX">Los Angeles International</option>
            <option value="JFK">John F. Kennedy International</option>
          </select>
        </div>
      </label>
      <label class="field">
        <span class="label">Outbound</span>
        <input class="input" type="date" />
      </label>
      <label class="field">
        <span class="label">To</span>
        <div class="select-wrapper">
          <select class="select" required>
            <option value="" disabled selected>[ Airport list ]</option>
            <option value="SFO">San Francisco International</option>
            <option value="LAX">Los Angeles International</option>
            <option value="JFK">John F. Kennedy International</option>
          </select>
        </div>
      </label>
      <label class="field">
        <span class="label">Flight Number</span>
        <input class="input" type="text" placeholder="[ XX0000 ]" />
      </label>
      <label class="field">
        <span class="label">Sort by</span>
        <div class="select-wrapper">
          <select class="select">
            <option value="">Date-Time</option>
            <option value="">Economy Class Prices</option>
            <option value="">Approved</option>
          </select>
        </div>
      </label>
      <UIButton class="apply-button">Apply</UIButton>
    </fieldset>
    <div class="table-wrapper">
      <table class="table">
        <thead class="thead">
          <tr>
            <th>Date</th>
            <th>Time</th>
            <th>From</th>
            <th>To</th>
            <th>Flight number</th>
            <th>Aircraft</th>
            <th>Economy price</th>
            <th>Business price</th>
            <th>First class price</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="flight in flights"
            :key="flight.id"
            @click="selectFlight(flight)"
            :class="{
              selected: flight === selectedFlight,
              canceled: flight.status === 'canceled',
              row: true,
            }"
          >
            <td>{{ flight.date }}</td>
            <td>{{ flight.time }}</td>
            <td>{{ flight.fromAirport.code }}</td>
            <td>{{ flight.toAirport.code }}</td>
            <td>{{ flight.flightNumber }}</td>
            <td>{{ flight.aircraft }}</td>
            <td>{{ flight.economyClassPrice }}</td>
            <td>{{ flight.businessClassPrice }}</td>
            <td>{{ flight.firstClassPrice }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="buttons">
      <UIButton @click="cancelFlight(selectedFlight)">
        <img
          src="https://bayrivercolleges.ca/files/logo-x-twitter.svg"
          alt="Cross icon"
          width="25"
          style="padding: 2px; border: 1px solid black"
        />
        <span>Cancel Flight</span>
      </UIButton>
      <UIButton @click="openEditFlightScheduleModal">
        <img
          src="https://cdn-icons-png.flaticon.com/512/7398/7398464.png"
          width="25"
          alt="Edit Icon"
        />
        <span>Edit Flight</span>
      </UIButton>
      <UIButton class="import-changes" @click="openApplyScheduleChangesModal">
        <img
          src="https://cdn.icon-icons.com/icons2/1122/PNG/512/downloaddownarrowsymbolinsquarebutton_79508.png"
          width="25"
          alt="Import Icon"
        />
        <span>Import Changes</span>
      </UIButton>
    </div>
  </main>
  <ScheduleEditModal
    :open="isScheduleEditModalOpen"
    @close="closeEditFlightScheduleModal"
  />
  <ApplyScheduleChangesModal
    :open="isApplyScheduleChangesModalOpen"
    @close="closeApplyScheduleChangesModal"
  />
</template>

<script setup>
import UIHeader from "@/components/UIHeader.vue";
import UIButton from "@/components/UIButton.vue";
import ScheduleEditModal from "@/components/ScheduleEditModal.vue";
import ApplyScheduleChangesModal from "@/components/ApplyScheduleChangesModal.vue";
import { ref } from "vue";

const isApplyScheduleChangesModalOpen = ref(false);
const isScheduleEditModalOpen = ref(false);
const selectedFlight = ref(null);
const editingFlightSchedule = ref(null);

const airports = ref([]);
const flights = ref([]);
const filteredFlights = ref([]);

const filter = ref({
  from: "",
  to: "",
  sortBy: "date_time",
  date: "",
  flightNumber: "",
});

const apiUrl = "src/assets/flights.json";
const fetchFlights = async () => {
  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    flights.value = data;
  } catch (error) {
    console.error("Error fetching flights:", error);
  }
};

const users = ref([]);

const selectFlight = (flight) => {
  selectedFlight.value = flight;
};

function applyFilter() {
  filteredFlights.value = flights.value.filter((flight) => {
    return (
      (filter.value.from === "" ||
        flight.fromAirport.code === filter.value.from) &&
      (filter.value.to === "" || flight.toAirport.code === filter.value.to) &&
      (filter.value.date === "" || flight.date === filter.value.date) &&
      (filter.value.flightNumber === "" ||
        flight.flightNumber.includes(filter.value.flightNumber))
    );
  });
}

const cancelFlight = (flight) => {
  // TODO: Implement flight canceling
};

const openEditFlightScheduleModal = () => {
  isScheduleEditModalOpen.value = true;
};

const closeEditFlightScheduleModal = () => {
  isScheduleEditModalOpen.value = false;
};

const editFlightSchedule = (selectedFlight) => {
  editingFlightSchedule.value = selectedFlight;
  openEditFlightScheduleModal();
};

const openApplyScheduleChangesModal = () => {
  isApplyScheduleChangesModalOpen.value = true;
};

const closeApplyScheduleChangesModal = () => {
  isApplyScheduleChangesModalOpen.value = false;
};

fetchFlights();
</script>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
  height: calc(100% - 1.8rem);
  padding: 1rem;
  gap: 1rem;
}
.manage-flight-schedules {
  width: 100%;
  margin: 0 auto;
}

.filters {
  columns: 3;
  column-gap: 2rem;
  margin-bottom: 1rem;
}
.field {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
  gap: 1rem;
}

.input {
  flex-grow: 1;
}

.select-wrapper {
  padding: 0.25rem 0.5rem 0.25rem 0rem;
  border: 1px solid black;
  border-radius: 5px;
  background-color: white;
  cursor: pointer;
  flex-grow: 1;
}
.select {
  text-align-last: center;
  padding-inline-end: 2rem;
  outline: none;
  border: none;
}

.apply-button {
  margin-left: auto;
}

.table-wrapper {
  flex-grow: 1;
  border: 2px solid black;
  overflow-y: auto;
  overflow-x: hidden;
  scroll-behavior: smooth;
}

.table {
  border: 0;
}

.buttons {
  display: flex;
  gap: 1rem;
}

.thead {
  background-color: lightgray;
  position: sticky;
  top: 0;
  box-shadow: 1px 1px 1px 1px black;
}
.import-changes {
  margin-left: auto;
}

.selected {
  box-shadow: inset 0 0 0 2px black;
}
</style>
