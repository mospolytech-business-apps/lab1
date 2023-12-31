<template>
  <UIHeader title="Flight Satisfaction Survey Reports" />
  <UINav>
    <button @click="isSummaryShown = true">View Results Summary</button>
    <button @click="isSummaryShown = false">View Detailed Summary</button>
    <button>
      <a class="btn" href="/src/data/CaseStudy.pdf" download
        >Download CaseStudy.pdf</a
      >
    </button>
  </UINav>
  <template v-if="isSummaryShown">
    <main class="main">
      <h1 class="visually-hidden">Client Survey Summary</h1>
      <div class="table-container">
        <div class="table-heading">
          <p>{{ period }}</p>
          <p>{{ amountOfSurveyed }}</p>
        </div>
        <div class="table-wrapper">
          <table class="table">
            <thead>
              <tr>
                <th colspan="2">Gender</th>
                <th colspan="4">Age</th>
                <th colspan="3">Cabin Type</th>
                <th colspan="5">Destination airport</th>
              </tr>
              <tr>
                <th>Male</th>
                <th>Female</th>
                <th>18-24</th>
                <th>25-39</th>
                <th>40-59</th>
                <th>60+</th>
                <th>Economy</th>
                <th>Business</th>
                <th>First</th>
                <th>AUH</th>
                <th>BAH</th>
                <th>DOH</th>
                <th>RUH</th>
                <th>CAI</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td v-for="mark in reportSummary">{{ mark }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </main>
  </template>
  <template v-else>
    <DetailedReportJSON :report="sortedReport" :summary="summary" />
  </template>
</template>

<script setup>
import DetailedReportJSON from "@/components/DetailedReportJSON.vue";
import UIHeader from "@/components/UIHeader.vue";
import UINav from "@/components/UINav.vue";
import { ref, onMounted, computed } from "vue";

const isSummaryShown = ref(true);
const report = ref(null);
const apiUrl = "src/data/summary-report.json";
const summary = ref(null);
const reportSummary = ref([]);
import { BACKEND_URL } from "@/config";

//let apiURL = "src/data/summary-report.json";

let apiURL = `${BACKEND_URL}/report`;

const period = ref(null);
const amountOfSurveyed = ref(null);

const setPeriod = () => {
  period.value = `Fieldwork ${Object.keys(report.value)[0]} – ${
    Object.keys(report.value)[Object.keys(report.value).length - 1]
  }`;
};

const sortedReport = computed(() => {
  console.log("report.value", report.value);
  const sortedReport = JSON.parse(JSON.stringify(report.value));

  for (const [t, time] of Object.entries(sortedReport)) {
    for (const [q, question] of Object.entries(time)) {
      for (const [m, mark] of Object.entries(question)) {
        sortedReport[t][q][m] = mark.sort((a, b) => b - a);
      }
    }
  }

  console.log("sortedReport", sortedReport);
  return sortedReport;
});

const fetchReport = async () => {
  try {
    const response = await fetch(apiURL);

    if (!response.ok) {
      throw new Error(`Error fetching report: ${response.status}`);
    }

    report.value = await response.json();

    const objectCount = response.headers.get("X-Object-Count");
    console.log("objectCount", objectCount, response.headers);

    if (objectCount) {
      amountOfSurveyed.value = `Sample Size: ${objectCount} adults`;
    } else {
      console.error("X-Object-Count header not found");
    }

    createSummary();
    createReportSummary();
    setPeriod();
  } catch (error) {
    console.error("Error fetching report:", error);
  }
};

const createSummary = () => {
  summary.value = {
    all: JSON.parse(JSON.stringify(Object.values(report.value)[0])),
  };

  for (const [t, time] of Object.entries(report.value)) {
    if (Object.keys(report.value)[0] === t) {
      continue;
    }
    for (const [q, question] of Object.entries(time)) {
      for (const [m, mark] of Object.entries(question)) {
        summary.value["all"][q][m] = summary.value["all"][q][m].map(
          (value, index) => value + mark[index]
        );
      }
    }
  }
};

const createReportSummary = () => {
  reportSummary.value = JSON.parse(
    JSON.stringify(Object.values(Object.values(summary.value["all"])[0])[0])
  );

  for (const [q, question] of Object.entries(summary.value["all"])) {
    for (const [m, mark] of Object.entries(question)) {
      for (const [i, value] of Object.entries(mark)) {
        reportSummary.value[i] += value;
      }
    }
  }
};

onMounted(fetchReport);
</script>

<style scoped>
.main {
  margin: 1rem 1rem;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
  gap: 1rem;
}

.table-container {
  width: 100%;
}

.table-heading {
  display: flex;
  font-size: 1.2em;
  font-weight: bold;
  margin-bottom: 0.5rem;
  border-bottom: 2px solid black;
  justify-content: space-between;
}
td,
th {
  border: 2px solid black;
  padding-inline-start: 0.25rem;
  text-align: center;
}

th {
  font-weight: 600;
}

td {
  font-weight: 400;
}

.table-wrapper {
  flex-grow: 1;
  width: 100%;
  border: 1px solid black;
  overflow: scroll;
}
.table {
  width: 100%;
  border-collapse: collapse;
  overflow: scroll;
}

.btn {
  display: block;
  color: inherit;
  text-decoration: none;
  padding: 0;
  margin: 0;
}
</style>
