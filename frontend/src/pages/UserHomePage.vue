<template>
  <div class="container">
    <h1>AMONIC Airlines Automation System</h1>

    <div class="time-spent-section">
      <h2>Time spent on system</h2>
      <p>{{ timeSpent }}</p>
    </div>

    <div class="number-of-crashes-section">
      <h2>Number of crashes</h2>
      <p>{{ numberOfCrashes }}</p>
    </div>

    <div class="crashes-table-section">
      <h2>Crashes</h2>
      <table class="table">
        <thead>
          <tr>
            <th>Date</th>
            <th>Login time</th>
            <th>Logout time</th>
            <th>Time spent on system</th>
            <th>Unsuccessful logout reason</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="crash in crashes" :key="crash.id">
            <td>{{ crash.date }}</td>
            <td>{{ crash.loginTime }}</td>
            <td>{{ crash.logoutTime }}</td>
            <td>{{ crash.timeSpentOnSystem }}</td>
            <td>{{ crash.unsuccessfulLogoutReason }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'TimeSpentOnSystemPage',
  data() {
    return {
      timeSpent: '00:19:03',
      numberOfCrashes: 1,
      crashes: [
        {
          id: 1,
          date: '02/13/2017',
          loginTime: '17:15',
          logoutTime: '18:45',
          timeSpentOnSystem: '1:30',
          unsuccessfulLogoutReason: 'Power outage',
        },
      ],
    };
  },
});
</script>

<style>
.container {
  max-width: 960px;
  margin: 0 auto;
}

.time-spent-section,
.number-of-crashes-section,
.crashes-table-section {
  margin-bottom: 20px;
}

.table {
  width: 100%;
  border-collapse: collapse;
}

.table th,
.table td {
  border: 1px solid black;
  padding: 5px;
}
</style>
