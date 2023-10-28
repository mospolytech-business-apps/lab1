<template>
  <div class="manage-flight-schedules">
    <h1>Manage Flight Schedules</h1>
    <div class="filter-bar">
      <select v-model="filter.from">
        <option value="">From</option>
        <option v-for="airport in airports" :value="airport.code">
          {{ airport.name }}
        </option>
      </select>
      <select v-model="filter.to">
        <option value="">To</option>
        <option v-for="airport in airports" :value="airport.code">
          {{ airport.name }}
        </option>
      </select>
      <select v-model="filter.sortBy">
        <option value="date_time">Date-Time</option>
        <option value="outbound">Outbound</option>
        <option value="flight_number">Flight Number</option>
      </select>
      <input
        type="text"
        v-model="filter.date"
        placeholder="Date (dd/mm/yyyy)"
      />
      <input
        type="text"
        v-model="filter.flightNumber"
        placeholder="Flight Number"
      />
      <button @click="applyFilter">Apply</button>
    </div>
    <div class="flight-list">
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Time</th>
            <th>From</th>
            <th>To</th>
            <th>Flight Number</th>
            <th>Aircraft</th>
            <th>Economy Price</th>
            <th>Business Price</th>
            <th>First Class Price</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="flight in filteredFlights" :key="flight.id">
            <td>{{ flight.date }}</td>
            <td>{{ flight.time }}</td>
            <td>{{ flight.fromAirport.name }}</td>
            <td>{{ flight.toAirport.name }}</td>
            <td>{{ flight.flightNumber }}</td>
            <td>{{ flight.aircraft }}</td>
            <td>{{ flight.economyPrice }}</td>
            <td>{{ flight.businessPrice }}</td>
            <td>{{ flight.firstClassPrice }}</td>
            <td>
              <button @click="editFlight(flight)">Edit</button>
              <button @click="cancelFlight(flight)">Cancel</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="import-changes">
      <button @click="importChanges">Import Changes</button>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "ManageFlightSchedules",
  data() {
    return {
      airports: [],
      flights: [],
      filteredFlights: [],
      filter: {
        from: "",
        to: "",
        sortBy: "date_time",
        date: "",
        flightNumber: "",
      },
    };
  },
  mounted() {
    // Fetch airports and flights data
    fetch("/api/airports")
      .then((response) => response.json())
      .then((airports) => (this.airports = airports));

    fetch("/api/flights")
      .then((response) => response.json())
      .then((flights) => (this.flights = flights));
  },
  methods: {
    applyFilter() {
      this.filteredFlights = this.flights.filter((flight) => {
        return (
          (this.filter.from === "" ||
            flight.fromAirport.code === this.filter.from) &&
          (this.filter.to === "" || flight.toAirport.code === this.filter.to) &&
          (this.filter.date === "" || flight.date === this.filter.date) &&
          (this.filter.flightNumber === "" ||
            flight.flightNumber.includes(this.filter.flightNumber))
        );
      });
    },
    editFlight(flight) {
      // Open edit flight modal
    },
    cancelFlight(flight) {
      // Cancel flight
    },
    importChanges() {
      // Save changes to flights
    },
  },
});
</script>

<style scoped>
.manage-flight-schedules {
  width: 100%;
  margin: 0 auto;
}

.filter-bar {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.filter-bar select {
  width: 150px;
  margin-right: 10px;
}

.filter-bar input {
  width: 200px;
  margin-right: 10px;
}

.filter-bar button {
  background-color: #000;
  color: #fff;
  padding: 10px;
  border: none;
  cursor: pointer;
}

.flight-list {
  width: 100%;
  overflow-x: auto;
}

.flight-list table {
  border-collapse: collapse;
  width: 100%;
}

.flight-list th,
.flight-list td {
  border: 1px solid #ccc;
  padding: 10px;
}

.flight-list th {
  background-color: #eee;
}

.import-changes {
  text-align: right;
  margin-top: 20px;
}

.import-changes button {
  background-color: #000;
  color: #fff;
  padding: 10px;
  border: none;
  cursor: pointer;
}
</style>
