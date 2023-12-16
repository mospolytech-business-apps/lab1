<script setup>
import { api } from "@/api";
import { ref, onMounted } from "vue";
import Cookies from "js-cookie";
import { useNotificationsStore } from "@/stores/notifications.store";

import UIHeader from "@/components/UIHeader.vue";
import UIButton from "@/components/UIButton.vue";
import UINav from "@/components/UINav.vue";

const { addError } = useNotificationsStore();

const shortSummary = ref(null);
onMounted(async () => {
  const { res, err } = await api.getShortSummary(Cookies.get("ACCESS_TOKEN"));
  if (err !== null) {
    shortSummary.value = res;
    addError("Error, loading short summary: ", err);
    return;
  }

  shortSummary.value = res;
});
</script>

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
        <p>
          <b>{{ shortSummary?.flights?.average_daily_flight_time ?? "–" }}</b>
        </p>
        <p>
          <b>{{ shortSummary?.flights?.cancelled ?? "–" }}</b>
        </p>
        <p>
          <b>{{ shortSummary?.flights?.confirmed ?? "–" }}</b>
        </p>
      </fieldset>
      <fieldset class="stat">
        <legend>Top Customers (Number of purchases)</legend>
        <p v-for="(client, i) in shortSummary?.top_clients">
          {{ `${i + 1}. ` + client?.name ?? "–" }}
          <b> ({{ client?.flights ?? "–" }} </b>
          Tickets)
        </p>
      </fieldset>
      <fieldset class="stat columns">
        <legend>Number of passengers flying</legend>
        <p>Busiest day:</p>
        <p>Most quiet day:</p>
        <p>
          <b>
            {{
              shortSummary?.number_of_passengers?.quietest?.day?.replace(
                /-/g,
                "/"
              ) ?? "–"
            }}
          </b>
          with
          <b>
            {{ shortSummary?.number_of_passengers?.quietest?.flights ?? "–" }}
            planes
          </b>
          flying
        </p>
        <p>
          <b>
            {{
              shortSummary?.number_of_passengers?.busiest?.day?.replace(
                /-/g,
                "/"
              ) ?? "–"
            }}
          </b>
          with
          <b>
            {{ shortSummary?.number_of_passengers?.busiest?.flights ?? "–" }}
            planes
          </b>
          flying
        </p>
      </fieldset>
      <fieldset class="stat">
        <legend>Top AMONIC Airlines Offices (Revenue)</legend>
        <p v-for="(office, i) in shortSummary?.top_offices">
          {{ `${i + 1}. ` + office?.name ?? "–" }}
        </p>
      </fieldset>
    </fieldset>
    <fieldset>
      <legend>Revenue from ticket sales</legend>
      <p>
        Yesterday: <b>${{ shortSummary?.revenue?.yesterday ?? "–" }}</b>
      </p>
      <p>
        Two days ago: <b>${{ shortSummary?.revenue?.two_days_ago ?? "–" }}</b>
      </p>
      <p>
        Three days ago:
        <b>${{ shortSummary?.revenue?.three_days_ago ?? "–" }}</b>
      </p>
    </fieldset>
    <fieldset>
      <legend>Weakly report of percentage of empty seats</legend>
      <p>
        This week:
        <b>{{ shortSummary?.weekly_seats_empty?.this_week ?? "–" }}% </b>
      </p>
      <p>
        Last week:
        <b> {{ shortSummary?.weekly_seats_empty?.last_week ?? "–" }}% </b>
      </p>
      <p>
        Three weeks ago:
        <b> {{ shortSummary?.weekly_seats_empty?.two_weeks_ago ?? "–" }}% </b>
      </p>
    </fieldset>
    <div class="bottom">
      <p>
        Report generated in
        <b>{{ shortSummary?.report_generated_in }} </b> seconds
      </p>
      <UIButton class="make-report" @click="$router.push('/')">
        <img src="@/assets/cross-icon.png" width="25" alt="Close icon" />
        Close
      </UIButton>
    </div>
  </main>
</template>

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
