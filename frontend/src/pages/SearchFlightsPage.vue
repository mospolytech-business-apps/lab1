<template>
  <UIHeader title="Search for flights" />
  <UINav class="menu">
    <button @click="$router.push('/')">Exit</button>
  </UINav>
  <main class="main">
    <fieldset class="filters">
      <legend>Search Parameters</legend>
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
        <span class="label">Cabin Type</span>
        <div class="select-wrapper">
          <select class="select" required>
            <option value="" disabled selected>[ Cabin Type ]</option>
            <option value="Economy">San Francisco International</option>
            <option value="Business">Los Angeles International</option>
            <option value="First Class">John F. Kennedy International</option>
          </select>
        </div>
      </label>
      <label class="field">
        <span class="label">Return</span>
        <input class="radio" type="radio" name="returnType" />
      </label>
      <label class="field">
        <span class="label">On way</span>
        <input class="radio" type="radio" name="returnType" />
      </label>
      <label class="field">
        <span class="label">
          <img src="" alt="Onboard icon" />
          Onboard
        </span>
        <input class="input" type="text" />
      </label>
      <label class="field">
        <span class="label">
          <img src="" alt="Return icon" />
          Return
        </span>
        <input class="input" type="text" />
      </label>
      <UIButton @click="applyFilters" class="apply-button">Apply</UIButton>
    </fieldset>
    <div class="outbounding">
      <div class="table-heading">
        <p>Outbounding flight details:</p>
        <label class="field">
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
        <label class="field">
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
  </main>
</template>

<script setup>
import UIHeader from "@/components/UIHeader.vue";
import UINav from "@/components/UINav.vue";
import UIButton from "@/components/UIButton.vue";

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

.filters > * {
  display: inline-flex;
  align-items: center;
  gap: 1rem;
  margin-right: 5rem;
  margin-block: 0.5rem;
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
  align-items: center;
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
  width: 100%;
  padding-inline-end: 2rem;
  outline: none;
  border: none;
}
.apply-button {
  display: inline;
}
</style>
