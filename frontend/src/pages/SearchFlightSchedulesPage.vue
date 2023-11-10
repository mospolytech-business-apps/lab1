<template>
  <div class="flight-search">
    <HeaderComponent title="Search For Flights" />
    <form @submit="searchFlights">
      <div class="input-group">
        <label for="from">From:</label>
        <input type="text" id="from" v-model="from" />
      </div>

      <div class="input-group">
        <label for="to">To:</label>
        <input type="text" id="to" v-model="to" />
      </div>

      <div class="input-group">
        <label for="departure_date">Departure date:</label>
        <input type="date" id="departure_date" v-model="departure_date" />
      </div>

      <div class="input-group">
        <label for="return_date">Return date:</label>
        <input type="date" id="return_date" v-model="return_date" />
      </div>

      <button type="submit">Search</button>
    </form>

    <div class="flight-results">
      <ul v-if="flightResults">
        <li v-for="flight in flightResults" :key="flight.id">
          <h1>{{ flight.airline }} {{ flight.flight_number }}</h1>
          <p>{{ flight.departure_airport }} - {{ flight.arrival_airport }}</p>
          <p>{{ flight.departure_time }} - {{ flight.arrival_time }}</p>
          <p>{{ flight.price }}</p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import HeaderComponent from "@/components/HeaderComponent.vue";
</script>

<style scoped>
.flight-search {
  width: 500px;
  margin: 0 auto;
}

.flight-results {
  margin-top: 20px;
}

.flight-results ul {
  list-style-type: none;
  padding: 0;
}

.flight-results li {
  border-bottom: 1px solid #ccc;
}

.flight-results li h1 {
  font-size: 20px;
}

.flight-results li p {
  font-size: 16px;
}
</style>
