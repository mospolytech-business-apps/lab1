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
          <p>Fieldwork June 2017-October 2017</p>
          <p>Sample Size: 1727 adults</p>
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
                <th>RYU</th>
                <th>CAI</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>888</td>
                <td>888</td>
                <td>888</td>
                <td>888</td>
                <td>888</td>
                <td>888</td>
                <td>888</td>
                <td>888</td>
                <td>888</td>
                <td>888</td>
                <td>888</td>
                <td>888</td>
                <td>888</td>
                <td>888</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </main>
  </template>
  <template v-else>
    <DetailedReportJSON :report="report" />
  </template>
</template>

<script setup>
import DetailedReportJSON from "@/components/DetailedReportJSON.vue";
import UIHeader from "@/components/UIHeader.vue";
import UINav from "@/components/UINav.vue";
import { ref } from "vue";

const isSummaryShown = ref(true);

// const downloadPDF = async () => {
//   try {
//     const response = await fetch("src/data/CaseStudy.pdf", {
//       responseType: "arraybuffer",
//     });

//     const buffer = await response.arrayBuffer();
//     const blob = new Blob([buffer], { type: "application/pdf" });
//     blob.saveAs(blob, "CaseStudy.pdf");
//   } catch (error) {
//     console.error(error);
//   }
// };

const report = ref(null);

const apiUrl = "src/data/summary-report.json";
const fetchReport = async () => {
  try {
    const response = await fetch(apiUrl);
    report.value = await response.json();
  } catch (error) {
    console.error("Error fetching report:", error);
  }
};

fetchReport();
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
