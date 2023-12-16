<script setup>
import { ref } from "vue";
import { api } from "@/api";
import Cookies from "js-cookie";
import { useNotificationsStore } from "@/stores/notifications.store";

import UIHeader from "@/components/UIHeader.vue";
import UIButton from "@/components/UIButton.vue";
import UINav from "@/components/UINav.vue";

const { addError, addAlert } = useNotificationsStore();
const reportResults = ref(null);

const filter = ref({
  flightID: null,
  startDate: null,
  endDate: null,
});

const applyFilter = async () => {
  const allowRequest =
    (filter.value.flightID !== null &&
      filter.value.from === null &&
      filter.value.to === null) ||
    (filter.value.flightID === null &&
      filter.value.from !== null &&
      filter.value.to !== null);

  if (!allowRequest) {
    addAlert("You can only search by fligth id OR date range");
    filter.value = {
      flightID: null,
      from: null,
      to: null,
    };
    return;
  }

  const { res, err } = await api.getAmenitiesReport({
    accessToken: Cookies.get("ACCESS_TOKEN"),
    payload: filter.value,
  });

  if (err !== null) {
    addError("Error, loading short summary: ", err);
    return;
  }

  reportResults.value = res;
};
</script>

<template>
  <UIHeader title="Amenities Report" />
  <UINav />
  <main class="main">
    <fieldset class="filters">
      <legend>Filter by</legend>
      <label class="field flight-id">
        <span class="label">Flight ID:</span>
        <input
          v-model="filter.flightID"
          class="input"
          type="text"
          placeholder="[ XXXXXX ]"
        />
      </label>
      <br />
      <label class="field">
        <span class="label">from: </span>
        <input
          v-model="filter.startDate"
          class="input"
          type="date"
          placeholder="[ XX/XX/XXXX ]"
        />
      </label>
      <label class="field">
        <span class="label">to: </span>
        <input
          v-model="filter.endDate"
          class="input"
          type="date"
          placeholder="[ XX/XX/XXXX ]"
        />
      </label>
      <UIButton class="make-report" @click="applyFilter">Make Report</UIButton>
    </fieldset>
    <div class="table-wrapper">
      <table v-if="reportResults?.amenities" class="table">
        <thead>
          <tr>
            <th v-if="reportResults.amenities">Amenities</th>
            <th v-for="amenity in reportResults?.amenities" :key="amenity">
              {{ amenity }}
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(stat, k, i) in reportResults?.data" :key="i">
            <td>{{ k }}</td>
            <td v-for="amount in stat" :key="amount">
              {{ amount || "0" }}
            </td>
          </tr>
        </tbody>
      </table>
      <div align="center" v-else>
        To generate report press the "Make Report" button
      </div>
    </div>
  </main>
</template>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
  padding: 1rem;
  gap: 1rem;
}

.field {
  display: inline-flex;
  align-items: center;
  margin-bottom: 1rem;
  gap: 1rem;
  margin-right: 5rem;
}
.make-report {
  display: inline-block;
}

.input {
  min-width: 12rem;
  flex-grow: 1;
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

thead {
  background-color: lightgray;
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
</style>
