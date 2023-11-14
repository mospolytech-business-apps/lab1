<template>
  <UIHeader title="Search for flights" />
  <UINav class="menu" />
  <main class="main">
    <fieldset>
      <legend>Search Parameters</legend>
      <label class="field">
        <span class="label">From</span>
        <UISelect placeholder="[ Airport list ]" required>
          <option value="SFO">San Francisco International</option>
          <option value="LAX">Los Angeles International</option>
          <option value="JFK">John F. Kennedy International</option>
        </UISelect>
      </label>
      <label class="field">
        <span class="label">To</span>
        <UISelect placeholder="[ Airport list ]" required>
          <option value="SFO">San Francisco International</option>
          <option value="LAX">Los Angeles International</option>
          <option value="JFK">John F. Kennedy International</option>
        </UISelect>
      </label>
      <label class="field">
        <span class="label">Cabin Type</span>
        <UISelect placeholder="[ Cabin Type ]" required>
          <option value="Economy">San Francisco International</option>
          <option value="Business">Los Angeles International</option>
          <option value="First Class">John F. Kennedy International</option>
        </UISelect>
      </label>
      <br />
      <div class="return-type">
        <label class="radio">
          <span class="label">Return</span>
          <input class="radio" type="radio" name="returnType" />
        </label>
        <label class="radio">
          <span class="label">On way</span>
          <input class="radio" type="radio" name="returnType" />
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
        <input type="date" />
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
        <input type="date" />
      </label>
      <UIButton @click="applyFilters" class="apply-button">
        <img
          src="https://static.thenounproject.com/png/875351-200.png"
          width="20"
          height="20"
          alt="Search icon"
        />
        <span>Apply</span>
      </UIButton>
    </fieldset>
    <div class="outbounding">
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

    <div class="returning">
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
      <UIButton class="actions-btn">
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

<script setup>
import UIHeader from "@/components/UIHeader.vue";
import UINav from "@/components/UINav.vue";
import UISelect from "@/components/UISelect.vue";
import UIButton from "@/components/UIButton.vue";
import BookingConfirmationModal from "@/components/BookingConfirmationModal.vue";
import { ref } from "vue";

const isBookingConfirmationModalOpen = ref(false);

const openBookingConfirmationModal = () => {
  isBookingConfirmationModalOpen.value = true;
};

const closeBookingConfirmationModal = () => {
  isBookingConfirmationModalOpen.value = false;
};

const outbounding = [
  {
    id: 1,
    fromAirport: {
      code: "SFO",
      name: "San Francisco International Airport",
    },
    toAirport: {
      code: "LAX",
      name: "Los Angeles International Airport",
    },
    date: "2023-11-12",
    time: "10:00 AM",
    flightNumber: "UA1234",
    economyClassPrice: 200,
    numberOfStops: 0,
  },
  {
    id: 2,
    fromAirport: {
      code: "LAX",
      name: "Los Angeles International Airport",
    },
    toAirport: {
      code: "JFK",
      name: "John F. Kennedy International Airport",
    },
    date: "2023-11-12",
    time: "12:00 PM",
    flightNumber: "AA5678",
    economyClassPrice: 300,
    numberOfStops: 1,
  },
  {
    id: 3,
    fromAirport: {
      code: "JFK",
      name: "John F. Kennedy International Airport",
    },
    toAirport: {
      code: "SFO",
      name: "San Francisco International Airport",
    },
    date: "2023-11-14",
    time: "2:00 PM",
    flightNumber: "DL91011",
    economyClassPrice: 250,
    numberOfStops: 0,
  },
];

const returning = [
  {
    id: 1,
    fromAirport: {
      code: "SFO",
      name: "San Francisco International Airport",
    },
    toAirport: {
      code: "LAX",
      name: "Los Angeles International Airport",
    },
    date: "2023-11-12",
    time: "10:00 AM",
    flightNumber: "UA1234",
    economyClassPrice: 200,
    numberOfStops: 0,
  },
  {
    id: 2,
    fromAirport: {
      code: "LAX",
      name: "Los Angeles International Airport",
    },
    toAirport: {
      code: "JFK",
      name: "John F. Kennedy International Airport",
    },
    date: "2023-11-12",
    time: "12:00 PM",
    flightNumber: "AA5678",
    economyClassPrice: 300,
    numberOfStops: 1,
  },
  {
    id: 3,
    fromAirport: {
      code: "JFK",
      name: "John F. Kennedy International Airport",
    },
    toAirport: {
      code: "SFO",
      name: "San Francisco International Airport",
    },
    date: "2023-11-14",
    time: "2:00 PM",
    flightNumber: "DL91011",
    economyClassPrice: 250,
    numberOfStops: 0,
  },
];

const applyFilters = () => {
  alert("Filters are not applied!");
};
</script>

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

.actions {
  margin-inline: 10rem;
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

.actions-btn {
  align-self: center;
  margin-top: 0.5rem;
  height: 2.5rem;
}
</style>
