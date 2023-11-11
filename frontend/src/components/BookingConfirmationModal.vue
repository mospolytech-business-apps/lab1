<template>
  <div class="booking-confirmation">
    <div class="header">
      <h1>Booking Confirmation</h1>
    </div>

    <div class="main">
      <div class="outbound-flight">
        <h3>Outbound Flight</h3>
        <table>
          <tr>
            <th>Flight Number</th>
            <td>{{ outboundFlight.flightNumber }}</td>
          </tr>
          <tr>
            <th>Departure Airport</th>
            <td>{{ outboundFlight.departureAirport }}</td>
          </tr>
          <tr>
            <th>Arrival Airport</th>
            <td>{{ outboundFlight.arrivalAirport }}</td>
          </tr>
          <tr>
            <th>Departure Date</th>
            <td>{{ outboundFlight.departureDate }}</td>
          </tr>
          <tr>
            <th>Departure Time</th>
            <td>{{ outboundFlight.departureTime }}</td>
          </tr>
        </table>
      </div>

      <div class="return-flight">
        <h3>Return Flight</h3>
        <table>
          <tr>
            <th>Flight Number</th>
            <td>{{ returnFlight.flightNumber }}</td>
          </tr>
          <tr>
            <th>Departure Airport</th>
            <td>{{ returnFlight.departureAirport }}</td>
          </tr>
          <tr>
            <th>Arrival Airport</th>
            <td>{{ returnFlight.arrivalAirport }}</td>
          </tr>
          <tr>
            <th>Departure Date</th>
            <td>{{ returnFlight.departureDate }}</td>
          </tr>
          <tr>
            <th>Departure Time</th>
            <td>{{ returnFlight.departureTime }}</td>
          </tr>
        </table>
      </div>

      <div class="passenger-details">
        <h3>Passenger Details</h3>
        <ul>
          <li>Name: {{ passenger.firstName }} {{ passenger.lastName }}</li>
          <li>Email: {{ passenger.email }}</li>
          <li>Phone: {{ passenger.phone }}</li>
        </ul>
      </div>
    </div>

    <div class="footer">
      <button type="button" @click="closeBookingConfirmation()">Close</button>
    </div>
  </div>
</template>

<script setup>
import { defineComponent } from "vue";

const BookingConfirmation = defineComponent({
  props: {
    outboundFlight: {
      type: Object,
      required: true,
    },
    returnFlight: {
      type: Object,
      required: true,
    },
    passenger: {
      type: Object,
      required: true,
    },
  },
  methods: {
    closeBookingConfirmation() {
      this.$emit("close");
    },
  },
});
</script>

<style scoped lang="scss">
.booking-confirmation {
  width: 500px;
  margin: 0 auto;
  padding: 15px;
}

.header {
  text-align: center;
}

.main {
  margin-top: 15px;
}

table,
th,
td {
  border: 1px solid black;
  border-collapse: collapse;
  padding: 5px;
}

th {
  background-color: #ccc;
}

.passenger-details {
  margin-top: 15px;
  list-style-type: none;
}

.footer {
  text-align: right;
  margin-top: 15px;
}
</style>
