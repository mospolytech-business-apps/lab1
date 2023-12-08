<template>
  <UIHeader title="Amenities Report" />
  <UINav class="menu">
    <button @click="$router.push('/')">Exit</button>
  </UINav>
  <main class="main">
    <fieldset class="filters">
      <legend>Filter by</legend>
      <label class="field flight-id">
        <span class="label">Flight ID:</span>
        <input class="input" type="text" placeholder="[XXXXXX]" />
      </label>
      <br />
      <label class="field">
        <span class="label">from: </span>
        <input class="input" type="date" placeholder="[ XX/XX/XXXX ]" />
      </label>
      <label class="field">
        <span class="label">to: </span>
        <input class="input" type="date" placeholder="[ XX/XX/XXXX ]" />
      </label>
      <UIButton class="make-report" @click="applyFilter">Make Report</UIButton>
    </fieldset>
    <div class="table-wrapper">
      <table v-if="report.amenities" class="table">
        <thead>
          <tr>
            <th v-if="report.amenities">Amenities</th>
            <th v-for="amenity in report.amenities" :key="amenity">
              {{ amenity }}
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="stat in report.statistics" :key="flightClass">
            <td>{{ stat.class }}</td>
            <td v-for="amount in stat.data" :key="amount">
              {{ amount || "–" }}
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

<script setup>
import UIHeader from "@/components/UIHeader.vue";
import UIButton from "@/components/UIButton.vue";
import UINav from "@/components/UINav.vue";

import { computed, ref } from "vue";

const report = ref({});

const apiUrl = "src/data/report.json";
const fetchReport = async () => {
  try {
    const response = await fetch(apiUrl);
    report.value = await response.json();
    console.log(report.value);
  } catch (error) {
    console.error("Error fetching report:", error);
  }
};

function applyFilter() {
  fetchReport();
}
</script>

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
