<script setup>
import { ref, onMounted, computed } from "vue";
import { useAirportsStore } from "@/stores/airports.store";
import { useSchedulesStore } from "@/stores/schedules.store";
import { useTicketsStore } from "@/stores/tickets.store";
import { storeToRefs } from "pinia";

import UIHeader from "@/components/UIHeader.vue";
import UINav from "@/components/UINav.vue";
import UISelect from "@/components/UISelect.vue";
import UIButton from "@/components/UIButton.vue";

const isBookingConfirmationModalOpen = ref(false);
const schedules = ref([]);
const airports = ref([]);

const { allSchedules } = storeToRefs(useSchedulesStore());
const { getAllSchedules, cancelFlight } = useSchedulesStore();
const { allAirports } = storeToRefs(useAirportsStore());
const { getAllAirports } = useAirportsStore();
const { searchForTickets, issueTicket } = useTicketsStore();

const openBookingConfirmationModal = () => {
  isBookingConfirmationModalOpen.value = true;
};

const closeBookingConfirmationModal = () => {
  isBookingConfirmationModalOpen.value = false;
};

const search = ref({
  from: null,
  to: null,
  cabinType: 1,
  onboard: null,
  return: null,
});

const filteredFromAirports = computed(() => {
  return airports.value.filter((a) => a.IATACode !== search.value.to);
});

const filteredToAirports = computed(() => {
  return airports.value.filter((a) => a.IATACode !== search.value.from);
});

const searchResults = ref(null);

const searchTickets = async () => {
  searchResults.value = await searchForTickets(search.value);
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
  <UIHeader title="Search for flights" />
  <UINav class="menu" />
  <main class="main">
    <form @submit.prevent="searchTickets">
      <fieldset>
        <legend>Search Parameters</legend>
        <label class="field">
          <span class="label">From</span>
          <UISelect
            v-model="search.from"
            placeholder="[ Airport list ]"
            required
          >
            <option
              v-for="airport in airports.filter(
                (a) => a.IATACode !== search.to
              )"
              :value="airport.IATACode"
              :key="airport.IATACode"
            >
              {{ airport.IATACode }}
            </option>
          </UISelect>
        </label>

        <label class="field">
          <span class="label">To</span>
          <UISelect v-model="search.to" placeholder="[ Airport list ]" required>
            <option
              v-for="airport in airports.filter(
                (a) => a.IATACode !== search.from
              )"
              :value="airport.IATACode"
              :key="airport.IATACode"
            >
              {{ airport.IATACode }}
            </option>
          </UISelect>
        </label>
        <label class="field">
          <span class="label">Cabin Type</span>
          <UISelect v-model="search.cabinType" required>
            <option value="1" selected>Economy</option>
            <option value="2">Business</option>
            <option value="3">First</option>
          </UISelect>
        </label>
        <br />
        <div class="return-type">
          <label class="radio">
            <span class="label">Return</span>
            <input
              v-model="search.returnType"
              class="radio"
              type="radio"
              value="Return"
              name="returnType"
              required
            />
          </label>
          <label class="radio">
            <span class="label">On way</span>
            <input
              v-model="search.returnType"
              class="radio"
              type="radio"
              value="On way"
              name="returnType"
              required
            />
          </label>
        </div>
        <label class="field">
          <span class="label">
            <img
              src="@/assets/onboarding-icon.png"
              width="20"
              height="20"
              alt="Onboard icon"
            />
            Onboard
          </span>
          <input type="date" v-model="search.onboardDate" required />
        </label>
        <label class="field">
          <span class="label">
            <img
              src="@/assets/returning-icon.png"
              alt="Return icon"
              width="20"
              height="20"
            />
            Return
          </span>
          <input type="date" v-model="search.returnDate" />
        </label>
        <UIButton type="submit" class="apply-button">
          <img
            src="https://static.thenounproject.com/png/875351-200.png"
            width="20"
            height="20"
            alt="Search icon"
          />
          <span>Apply</span>
        </UIButton>
      </fieldset>
    </form>
    <div class="outbounding-returning-wrapper">
      <div class="outbounding" v-show="searchResults?.outbounding">
        <div class="table-heading">
          <p>Outbounding flight details:</p>
          <label class="table-filter">
            <input class="checkbox" type="checkbox" name="filterReturning" />
            <span class="label">Display three days before and after</span>
          </label>
        </div>
        <div class="table-wrapper">
          <table class="table">
            <thead>
              <tr>
                <th>From</th>
                <th>To time</th>
                <th>Date</th>
                <th>Time</th>
                <th>Flight Number(s)</th>
                <th>Cabin Price</th>
                <th>Number of stops</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="flight in outbounding" :key="flight.id">
                <td>{{ flight.fromAirport.code }}</td>
                <td>{{ flight.toAirport.code }}</td>
                <td>{{ flight.date }}</td>
                <td>{{ flight.time }}</td>
                <td>{{ flight.flightNumber }}</td>
                <td>{{ flight.economyClassPrice }}</td>
                <td>{{ flight.numberOfStops }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="returning" v-show="searchResults?.returning">
        <div class="table-heading">
          <p>Return flight details:</p>
          <label class="table-filter">
            <input class="checkbox" type="checkbox" name="filterReturning" />
            <span class="label">Display three days before and after</span>
          </label>
        </div>
        <div class="table-wrapper">
          <table class="table">
            <thead>
              <tr>
                <th>From</th>
                <th>To time</th>
                <th>Date</th>
                <th>Time</th>
                <th>Flight Number(s)</th>
                <th>Cabin Price</th>
                <th>Number of stops</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="flight in returning" :key="flight.id">
                <td>{{ flight.fromAirport.code }}</td>
                <td>{{ flight.toAirport.code }}</td>
                <td>{{ flight.date }}</td>
                <td>{{ flight.time }}</td>
                <td>{{ flight.flightNumber }}</td>
                <td>{{ flight.economyClassPrice }}</td>
                <td>{{ flight.numberOfStops }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div class="actions">
      <fieldset class="confirm">
        <legend>Confirm booking for</legend>
        <label class="passengers-field">
          <input
            class="passenger-number-input"
            placeholder="[XXX]"
            type="text"
          />
          <span class="label">Passengers</span>
        </label>
        <UIButton @click="openBookingConfirmationModal">
          <img src="@/assets/check-mark-icon.png" width="20" alt="check mark" />
          <span>Book flight</span>
        </UIButton>
      </fieldset>
      <UIButton class="exit-btn">
        <img src="@/assets/cross-icon.png" width="20" alt="Exit button" />
        <span>Exit</span>
      </UIButton>
    </div>
  </main>
  <BookingConfirmationModal
    :open="isBookingConfirmationModalOpen"
    @close="closeBookingConfirmationModal"
  />
</template>

<style scoped>
p {
  margin: 0;
}
.main {
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

thead {
  background-color: lightgray;
  border-bottom: 2px solid black;
}

td,
th {
  border: 1px solid black;
  padding-inline-start: 0.25rem;
  text-align: start;
}

.table-wrapper {
  flex-grow: 1;
  width: 100%;
  border: 2px solid black;
  overflow: scroll;
}

.table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid black;
  overflow: scroll;
}

.table-heading {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.25rem;
  align-items: center;
}

.field {
  display: inline-flex;
  gap: 1rem;
  margin-right: 4rem;
  margin-block: 1rem;
  min-height: 2.125rem;
}

.label {
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.apply-button {
  display: inline flex;
}

.table-filter {
  display: flex;
  gap: 0.25rem;
}

.outbounding-returning-wrapper {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  flex-grow: 1;
}

.actions {
  margin-inline: 10rem;
  align-self: end;
  display: grid;
  gap: 2rem;
  grid-template-columns: 1fr 6fr 1fr;
}

.confirm {
  grid-column: 2 / 3;
  display: flex;
  justify-content: space-between;
}

.passengers-field {
  display: flex;
  gap: 0.5rem;
}
.passenger-number-input {
  width: 4rem;
}

.return-type {
  display: inline-flex;
  gap: 1rem;
  margin-right: 4rem;
}

.radio {
  display: flex;
}

.exit-btn {
  align-self: center;
  display: flex;
  padding-left: 1rem;
  justify-content: space-between;
  margin-top: 0.5rem;
  height: 2.5rem;
  &:hover {
    background-color: salmon;
  }
}
</style>
