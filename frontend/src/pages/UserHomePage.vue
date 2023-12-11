<script setup>
import { onMounted, ref, computed } from "vue";
import UIHeader from "@/components/UIHeader.vue";
import NoLogoutModal from "@/components/NoLogoutModal.vue";
import { useUsersStore } from "@/stores/users.store";
import { useAuthStore } from "@/stores/auth.store";
const { currentUser, sendLogoutInformation } = useUsersStore();
const { me } = useAuthStore();

const isNoLogoutModalOpen = ref(false);

const loginLogoutTimes = ref(null);

const numberOfCrashes = computed(() => {
  if (!loginLogoutTimes.value) return null;

  return (
    Object.values(loginLogoutTimes.value).filter((times) => !times?.logout_time)
      .length - 1
  );
});

const timeSpentIn30Days = computed(() => {
  if (!loginLogoutTimes.value) return null;

  const thirtyDaysAgo = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000);

  const thirtyDaysAgoSessions = Object.entries(loginLogoutTimes.value)
    .filter(([date, times]) => {
      const dateObj = new Date(date);
      return dateObj >= thirtyDaysAgo && times;
    })
    .map(([date, times]) => ({
      loginTime: new Date(date),
      logoutTime: times.logout_time ? new Date(times.logout_time) : null,
    }));

  let timeSpent = 0;
  thirtyDaysAgoSessions.forEach(({ loginTime, logoutTime }) => {
    if (logoutTime) {
      timeSpent += logoutTime - loginTime;
    }
  });

  return formatTime(timeSpent);
});
const sessions = ref([]);

const formatTime = (timeInMilliseconds) => {
  const totalSeconds = Math.floor(timeInMilliseconds / 1000);
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;

  if (hours > 0) {
    return `${hours.toString().padStart(2, "0")}:${minutes
      .toString()
      .padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;
  } else {
    return `${minutes}:${(seconds < 10 ? "0" : "") + seconds}`;
  }
};

onMounted(() => {
  loginLogoutTimes.value = currentUser.login_logout_times;

  sessions.value = Object.entries(loginLogoutTimes.value).map(
    ([date, times]) => {
      return {
        id: date,
        date: date.split("T")[0].replace(/-/g, "/"),
        loginTime: new Intl.DateTimeFormat("en-US", {
          hour: "2-digit",
          minute: "2-digit",
          hour12: false,
        }).format(new Date(date)),
        logoutTime: times?.logout_time
          ? new Intl.DateTimeFormat("en-US", {
              hour: "2-digit",
              minute: "2-digit",
              hour12: false,
            }).format(new Date(times.logout_time))
          : null,
        timeSpentOnSystem: times?.logout_time
          ? formatTime(
              new Date(times.logout_time ?? Date.now()) - new Date(date)
            )
          : null,
        unsuccessfulLogoutReason: times?.error ?? null,
      };
    }
  );

  // exclude the current session
  sessions.value = sessions.value.slice(0, -1);

  // sort sessions by date and time
  sessions.value.sort((a, b) => {
    if (a.date > b.date) return 1;
    if (a.date < b.date) return -1;
    if (a.loginTime > b.loginTime) return 1;
    if (a.loginTime < b.loginTime) return -1;
    return 0;
  });

  if (
    sessions.value?.at(-1).logoutTime === null &&
    sessions.value?.at(-1).unsuccessfulLogoutReason === null
  ) {
    isNoLogoutModalOpen.value = true;
  }
});

const setLogoutInformation = async (reason) => {
  const lastSessionKey = Object.keys(currentUser.login_logout_times).sort(
    (a, b) => {
      if (a < b) return 1;
      if (a > b) return -1;
      return 0;
    }
  )[1];

  await sendLogoutInformation(reason, lastSessionKey);

  currentUser.value = await me();
  sessions.value.find(
    (session) => session.id === lastSessionKey
  ).unsuccessfulLogoutReason = reason;
};
</script>

<template>
  <UIHeader title="User Home Page" />
  <main class="main">
    <h1 class="title">
      Hi <b>{{ currentUser.firstName }}</b
      >, Welcome to ANOMIC Airlines
    </h1>
    <div class="metrics">
      <p>
        Time spent on system: <b>{{ timeSpentIn30Days || "–" }}</b>
      </p>
      <p>
        Number of crashes: <b>{{ numberOfCrashes || "–" }}</b>
      </p>
    </div>

    <div class="table-wrapper">
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
          <tr
            v-for="session in sessions"
            :key="session.id"
            :class="{
              crashed: session.logoutTime === null,
              row: true,
            }"
          >
            <td>{{ session.date || "–" }}</td>
            <td>{{ session.loginTime || "–" }}</td>
            <td>{{ session.logoutTime || "–" }}</td>
            <td>{{ session.timeSpentOnSystem || "–" }}</td>
            <td>{{ session.unsuccessfulLogoutReason || "–" }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="links">
      <router-link class="link" to="/purchase-amenities"
        >Purchase Amenities</router-link
      >
      <router-link class="link" to="/search-flights"
        >Search For Flights</router-link
      >
    </div>
    <NoLogoutModal
      :open="isNoLogoutModalOpen"
      :failedSession="sessions?.at(-1) ? sessions?.at(-1) : null"
      @updateReason="setLogoutInformation"
      @close="isNoLogoutModalOpen = false"
    />
  </main>
</template>

<style scoped>
.main {
  margin: 1rem;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.title {
  font-size: 1.5em;
  font-weight: 400;
}
.crashes-table-section {
  margin-bottom: 20px;
}

thead {
  background-color: lightgray;
  border-bottom: 2px solid black;
}

td,
th {
  border: 1px solid black;
  padding-inline-start: 0.25rem;
  text-align: start;
}

.table-wrapper {
  flex-grow: 1;
  width: 100%;
  border: 2px solid black;
  overflow: scroll;
}

.table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid black;
  overflow: scroll;
}

.crashed {
  background-color: salmon;
}

.metrics {
  display: flex;
  justify-content: end;
  gap: 3rem;
}

.links {
  display: flex;
}

.link {
  min-width: 25rem;
  margin: 1rem;
  padding: 1rem;
  border: 1px solid black;
  border-radius: 0.5rem;
  text-decoration: none;
  color: black;
  font-size: 1.5rem;
  font-weight: bold;
  transition: 0.3s;
}
</style>
