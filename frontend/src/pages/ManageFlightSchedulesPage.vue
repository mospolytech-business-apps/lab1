<script setup>
import UIHeader from "@/components/UIHeader.vue";
import UIButton from "@/components/UIButton.vue";
import UISelect from "@/components/UISelect.vue";
import UINav from "@/components/UINav.vue";
import ScheduleEditModal from "@/components/ScheduleEditModal.vue";
import ApplyScheduleChangesModal from "@/components/ApplyScheduleChangesModal.vue";

import { onMounted, ref, computed } from "vue";
import { useSchedulesStore } from "@/stores/schedules.store";
import { useAirportsStore } from "@/stores/airports.store";
import { storeToRefs } from "pinia";
import { useErrorsStore } from "@/stores/errors.store";

const { addError } = useErrorsStore();
const { allSchedules } = storeToRefs(useSchedulesStore());
const { getAllSchedules, cancelFlight } = useSchedulesStore();
const { allAirports } = storeToRefs(useAirportsStore());
const { getAllAirports } = useAirportsStore();

const isApplyScheduleChangesModalOpen = ref(false);
const isScheduleEditModalOpen = ref(false);

const airports = ref([]);
const schedules = ref([]);
const flights = ref([]);
const isFiltered = ref(false);

const selectedFlight = ref(null);
const editingFlightSchedule = ref(null);

const selectFlight = (flight) => {
  selectedFlight.value = flight;
};

const filter = ref({
  from: "all",
  to: "all",
  sortBy: "default",
  date: null,
  flightNumber: null,
});

const applyFlightsFilter = () => {
  isFiltered.value = true;
  flights.value = [...schedules.value];

  if (filter.value.from !== "all") {
    flights.value = flights.value.filter(
      (flight) => flight.Route.DepartureAirport.IATACode === filter.value.from
    );
  }

  if (filter.value.to !== "all") {
    flights.value = flights.value.filter(
      (flight) => flight.Route.ArrivalAirport.IATACode === filter.value.to
    );
  }

  if (filter.value.sortBy === "dateTime") {
    flights.value = flights.value.sort((a, b) => {
      return new Date(a.Date + " " + a.Time) - new Date(b.Date + " " + b.Time);
    });
  } else if (filter.value.sortBy === "economyPrices") {
    flights.value = flights.value.sort((a, b) => {
      return a.EconomyPrice - b.EconomyPrice;
    });
  } else if (filter.value.sortBy === "approved") {
    flights.value = flights.value.filter((flight) => flight.Confirmed);
  }

  if (filter.value.date) {
    flights.value = flights.value.filter(
      (flight) => flight.Date === filter.value.date
    );
  }

  if (filter.value.flightNumber) {
    flights.value = flights.value.filter(
      (flight) => flight.FlightNumber === filter.value.flightNumber
    );
  }
};

const displayedFlights = computed(() =>
  isFiltered.value ? flights.value : schedules.value
);

const applyFlightCancel = async (flight) => {
  if (flight === null) {
    addError("Error: Select flight first!");
    return;
  }
  cancelFlight(flight.id);
  await fetchNewData();
  selectedFlight.value = null;
};

const editFlight = (flight) => {
  editingFlightSchedule.value = flight;
  if (editingFlightSchedule.value === null) {
    addError("Error: Select flight first!");
    return;
  }
  openEditFlightScheduleModal();
};

const openEditFlightScheduleModal = () => {
  isScheduleEditModalOpen.value = true;
};

const closeEditFlightScheduleModal = () => {
  isScheduleEditModalOpen.value = false;
  selectedFlight.value = null;
};

const openApplyScheduleChangesModal = () => {
  isApplyScheduleChangesModalOpen.value = true;
};

const closeApplyScheduleChangesModal = () => {
  isApplyScheduleChangesModalOpen.value = false;
};

const formatPrice = (price) => {
  if (price) {
    return "$" + Math.floor(price);
  } else {
    return null;
  }
};

const fetchNewData = async () => {
  schedules.value = await getAllSchedules();
  schedules.value = await getAllSchedules();
  applyFlightsFilter();
};

onMounted(async () => {
  schedules.value = allSchedules.value.length
    ? allSchedules.value
    : await getAllSchedules();

  airports.value = allAirports.value.length
    ? allAirports.value
    : await getAllAirports();
});
</script>

<template>
  <UIHeader title="Manage Flight Schedules" />
  <UINav />
  <main class="main">
    <fieldset class="filters">
      <legend>Filter by</legend>
      <label class="field">
        <span class="label">From</span>
        <UISelect v-model="filter.from" required>
          <option value="all" selected>All</option>
          <option
            v-for="airport in airports.filter((a) => a.IATACode !== filter.to)"
            :value="airport.IATACode"
          >
            {{ airport.IATACode }}
          </option>
        </UISelect>
      </label>
      <label class="field">
        <span class="label">Outbound</span>
        <input v-model="filter.date" class="input" type="date" />
      </label>
      <label class="field">
        <span class="label">To</span>
        <UISelect v-model="filter.to" required>
          <option value="all" selected>All</option>
          <option
            v-for="airport in airports.filter(
              (a) => a.IATACode !== filter.from
            )"
            :value="airport.IATACode"
          >
            {{ airport.IATACode }}
          </option>
        </UISelect>
      </label>
      <label class="field">
        <span class="label">Flight Number</span>
        <input
          class="input"
          v-model="filter.flightNumber"
          type="number"
          min="0"
          placeholder="Enter flight number"
        />
      </label>
      <label class="field">
        <span class="label">Sort by</span>
        <UISelect v-model="filter.sortBy" requited>
          <option value="default" selected>Default</option>
          <option value="dateTime">Date-Time</option>
          <option value="economyPrices">Economy Class Prices</option>
          <option value="approved">Approved</option>
        </UISelect>
      </label>
      <UIButton @click="applyFlightsFilter" class="apply-button"
        >Apply</UIButton
      >
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
            v-for="flight in displayedFlights"
            :key="flight.id"
            @click="selectFlight(flight)"
            :class="{
              selected: flight === selectedFlight,
              canceled: !flight.Confirmed,
              row: true,
            }"
          >
            <td>{{ flight?.Date ?? "–" }}</td>
            <td>{{ flight?.Time ?? "–" }}</td>
            <td>{{ flight?.Route?.DepartureAirport?.IATACode ?? "–" }}</td>
            <td>{{ flight?.Route?.ArrivalAirport?.IATACode ?? "–" }}</td>
            <td>{{ flight?.FlightNumber ?? "–" }}</td>
            <td>{{ flight?.Aircraft?.Name ?? "–" }}</td>
            <td>{{ formatPrice(flight.EconomyPrice) ?? "–" }}</td>
            <td>{{ formatPrice(flight.EconomyPrice * 1.35) ?? "–" }}</td>
            <td>{{ formatPrice(flight.EconomyPrice * 1.35 * 1.3) ?? "–" }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="buttons">
      <UIButton @click="applyFlightCancel(selectedFlight)">
        <img
          src="https://bayrivercolleges.ca/files/logo-x-twitter.svg"
          alt="Cross icon"
          width="25"
          style="padding: 2px; border: 1px solid black"
        />
        <span>Cancel Flight</span>
      </UIButton>
      <UIButton @click="editFlight(selectedFlight)">
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
    @updateData="fetchNewData"
    :flight="editingFlightSchedule"
    :open="isScheduleEditModalOpen"
    @close="closeEditFlightScheduleModal"
  />
  <ApplyScheduleChangesModal
    :open="isApplyScheduleChangesModalOpen"
    @close="closeApplyScheduleChangesModal"
  />
</template>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
  padding: 1rem;
  gap: 1rem;
  flex-grow: 0;
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
  width: 100%;
  border-collapse: collapse;
}

td,
th {
  border: 1px solid black;
  text-align: start;
}

.buttons {
  display: flex;
  gap: 1rem;
}

.thead {
  background-color: lightgray;
  position: sticky;
  top: 0;
}
.import-changes {
  margin-left: auto;
}

.selected {
  box-shadow: inset 0 0 0 2px black;
}

.canceled {
  background-color: salmon;
}
</style>
