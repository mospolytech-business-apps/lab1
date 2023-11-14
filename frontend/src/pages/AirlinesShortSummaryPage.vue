<template>
  <UIHeader title="Airlines Short Summary" />
  <UINav />

  <img width="400" class="logo" src="@/assets/logo.png" alt="Amonic" />
  <main class="main">
    <fieldset class="last30">
      <legend>In last 30 days...</legend>
      <fieldset class="stat columns">
        <legend>Flights</legend>
        <p>Number confirmed:</p>
        <p>Number canceled:</p>
        <p>Average daily flight time</p>
        <p>[XXX]</p>
        <p>[XXX]</p>
        <p>[XXX] minutes</p>
      </fieldset>
      <fieldset class="stat">
        <legend>Top Customers (Number of purchases)</legend>
        <p>Dohn Doe (5 Tickets)</p>
        <p>Dohn Doe (3 Tickets)</p>
        <p>Dohn Doe (2 Tickets)</p>
      </fieldset>
      <fieldset class="stat columns">
        <legend>Number of passengers flying</legend>
        <p>Busiest day:</p>
        <p>Most quiet day:</p>
        <p>[dd/mm] with [XXX] flying</p>
        <p>[dd/mm] with [XXX] flying</p>
      </fieldset>
      <fieldset class="stat">
        <legend>Top AMONIC Airlines Offices (Revenue)</legend>
        <p>1. Abu Dhabi</p>
        <p>2. Bahrain</p>
        <p>3. Cairo.</p>
      </fieldset>
    </fieldset>
    <fieldset>
      <legend>Revenue from ticket sales</legend>
      <p>Yesterday: $[XXX]</p>
      <p>Two days ago: $[XXX]</p>
      <p>Three days ago: $[XXX]</p>
    </fieldset>
    <fieldset>
      <legend>Weakly report of percentage of empty seats</legend>
      <p>This week: [XX]%</p>
      <p>Last week: [XX]%</p>
      <p>Three weeks ago: [XX]%</p>
    </fieldset>
    <div class="bottom">
      <p>Report generated in [XX] seconds</p>
      <UIButton class="make-report" @click="$router.push('/')">
        <img src="@/assets/cross-icon.png" width="25" alt="Close icon" />
        Close
      </UIButton>
    </div>
  </main>
</template>

<script setup>
import UIHeader from "@/components/UIHeader.vue";
import UIButton from "@/components/UIButton.vue";
import UINav from "@/components/UINav.vue";
</script>

<style scoped>
p {
  margin-top: 0;
}
.main {
  padding: 1rem 2rem;
  display: flex;
  flex-direction: column;
  height: 100%;
  justify-content: space-between;
  overflow-y: scroll;
}

.logo {
  margin: 0 auto;
  margin-top: 1rem;
}

.last30 {
  display: grid;
  grid-template: 1fr 1fr / 1fr 1fr;
  padding: 1rem;
  row-gap: 0.5rem;
  column-gap: 1rem;
}

.stat > * {
  margin-bottom: 0.5rem;
}

.columns {
  column-count: 2;
  column-gap: 1rem;
}

.bottom {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-bottom: 1rem;
}
</style>
