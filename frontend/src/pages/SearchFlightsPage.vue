<script setup>
import { ref, onMounted, computed } from "vue";
import { useAirportsStore } from "@/stores/airports.store";
import { useSchedulesStore } from "@/stores/schedules.store";
import { useTicketsStore } from "@/stores/tickets.store";
import { storeToRefs } from "pinia";
import { useNotificationsStore } from "@/stores/notifications.store";

import UIHeader from "@/components/UIHeader.vue";
import UINav from "@/components/UINav.vue";
import UISelect from "@/components/UISelect.vue";
import UIButton from "@/components/UIButton.vue";
import BookingConfirmationModal from "@/components/BookingConfirmationModal.vue";

const { addAlert } = useNotificationsStore();
const isBookingConfirmationModalOpen = ref(false);
const schedules = ref([]);
const airports = ref([]);

const { allSchedules } = storeToRefs(useSchedulesStore());
const { getAllSchedules } = useSchedulesStore();
const { allAirports } = storeToRefs(useAirportsStore());
const { getAllAirports } = useAirportsStore();
const { searchForTickets } = useTicketsStore();

const openBookingConfirmationModal = () => {
  if (!outboundChosenFlight.value) {
    addAlert("Please select a passenger");
    return;
  }

  if (!numberOfPassengers.value) {
    addAlert("Please select a number of passengers");
    return;
  }

  isBookingConfirmationModalOpen.value = true;
};

const closeBookingConfirmationModal = () => {
  isBookingConfirmationModalOpen.value = false;
};

const search = ref({
  from: null, // BAH
  to: null, // AUH
  cabinType: "Economy",
  onboardDate: null, // 2017-10-07
  returnDate: null, // 2017-10-09
  searchType: "return",
});

const outboundingWideSearch = ref(false);
const returningWideSearch = ref(false);
const priceIndex = ref(1);

const searchResults = ref(null);

const numberOfPassengers = ref(null);

const searchTickets = async () => {
  const searchCopy = { ...search.value };
  if (searchCopy.searchType === "oneway") {
    searchCopy.returnDate = null;
  }

  searchResults.value = await searchForTickets(searchCopy);
  priceIndex.value =
    search.value.cabinType === "First Class"
      ? 1.35 * 1.3
      : search.value.cabinType === "Business"
      ? 1.3
      : 1;

  outboundChosenFlight.value = searchResults.value?.outbound?.find(
    (f) => f.date === search.value?.onboardDate
  );

  returnChosenFlight.value = searchResults.value?.returning?.find(
    (f) => f.date === search.value?.returnDate
  );
};

const outboundChosenFlight = ref(null);
const returnChosenFlight = ref(null);

const handleTicketsCreated = () => {
  closeBookingConfirmationModal();
  outboundChosenFlight.value = null;
  returnChosenFlight.value = null;
  numberOfPassengers.value = null;
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
            <option value="Economy" selected>Economy</option>
            <option value="Business">Business</option>
            <option value="First Class">First class</option>
          </UISelect>
        </label>
        <br />
        <div class="return-type">
          <label class="radio">
            <span class="label">Return</span>
            <input
              v-model="search.searchType"
              class="radio"
              type="radio"
              value="return"
              name="searchType"
              required
            />
          </label>
          <label class="radio">
            <span class="label">On way</span>
            <input
              v-model="search.searchType"
              class="radio"
              type="radio"
              value="oneway"
              name="searchType"
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
          <input
            type="date"
            v-model="search.returnDate"
            :disabled="search.searchType !== 'return'"
          />
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
      <div class="outbounding" v-show="searchResults?.outbound">
        <div class="table-heading">
          <p>Outbounding flight details:</p>
          <label class="table-filter">
            <input
              v-model="outboundingWideSearch"
              @change="
                !outboundingWideSearch
                  ? (outboundChosenFlight = searchResults?.outbound?.find(
                      (f) => f.date === search?.onboardDate
                    ))
                  : null
              "
              class="checkbox"
              type="checkbox"
              name="filterReturning"
            />
            <span class="label">Display three days before and after</span>
          </label>
        </div>
        <div class="table-wrapper">
          <table class="table">
            <thead>
              <tr>
                <th>From</th>
                <th>To</th>
                <th>Date</th>
                <th>Time</th>
                <th>Flight Number(s)</th>
                <th>Cabin Price</th>
                <th>Number of stops</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="flight in searchResults?.outbound.filter((f) =>
                  outboundingWideSearch ? f : f.date == search?.onboardDate
                )"
                v-if="searchResults?.outbound.length !== 0"
                @click="outboundChosenFlight = flight"
                :class="{ selected: flight === outboundChosenFlight }"
                :key="flight.id"
              >
                <td>{{ flight?.from ?? "–" }}</td>
                <td>{{ flight?.to ?? "–" }}</td>
                <td>{{ flight?.date ?? "–" }}</td>
                <td>{{ flight?.time ?? "–" }}</td>
                <td>
                  {{
                    flight?.flight_numbers?.reduce(
                      (a, c, i) => a + (i ? " – " : "") + c,
                      ""
                    ) ?? "–"
                  }}
                </td>
                <td>
                  {{ "$" + parseInt(flight?.base_price * priceIndex) ?? "–" }}
                </td>
                <td>{{ flight?.flight_numbers?.length - 1 ?? "–" }}</td>
              </tr>
              <tr v-else>
                &#x200B;
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="returning" v-show="searchResults?.returning">
        <div class="table-heading">
          <p>Return flight details:</p>
          <label class="table-filter">
            <input
              v-model="returningWideSearch"
              @change="
                !returningWideSearch
                  ? (returnChosenFlight = searchResults?.returning?.find(
                      (f) => f.date === search?.returnDate
                    ))
                  : null
              "
              class="checkbox"
              type="checkbox"
              name="filterReturning"
            />
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
              <tr
                v-if="(searchResults?.returning?.length ?? false) !== 0"
                v-for="flight in searchResults?.returning?.filter((f) =>
                  returningWideSearch ? f : f.date == search?.returnDate
                )"
                @click="returnChosenFlight = flight"
                :class="{ selected: flight === returnChosenFlight }"
                :key="flight.id"
              >
                <td>{{ flight?.from ?? "–" }}</td>
                <td>{{ flight?.to ?? "–" }}</td>
                <td>{{ flight?.date ?? "–" }}</td>
                <td>{{ flight?.time ?? "–" }}</td>
                <td>
                  {{
                    flight?.flight_numbers?.reduce(
                      (a, c, i) => a + (i ? " – " : "") + c,
                      ""
                    ) ?? "–"
                  }}
                </td>
                <td>
                  {{ "$" + parseInt(flight?.base_price * priceIndex) ?? "–" }}
                </td>
                <td>{{ flight?.flight_numbers?.length - 1 ?? "–" }}</td>
              </tr>
              <tr v-else>
                &#x200B;
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
            v-model="numberOfPassengers"
            placeholder="[XX]"
            min="0"
            type="number"
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
    :numberOfPassengers="numberOfPassengers"
    :outboundChosenFlight="outboundChosenFlight"
    :returnChosenFlight="returnChosenFlight"
    :cabinType="search.cabinType"
    :open="isBookingConfirmationModalOpen"
    @close="closeBookingConfirmationModal"
    @ticketsCreated="handleTicketsCreated"
    @click.stop
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
  margin-inline: auto;
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
.selected {
  box-shadow: inset 0 0 0 3px lightgreen;
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
