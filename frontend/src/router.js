import { createRouter, createWebHistory } from "vue-router";
import { useUsersStore } from "@/stores/users.store";

import AdminHomePage from "@/pages/AdminHomePage.vue";
import ClientSurveyPage from "@/pages/ClientSurveyPage.vue";
import LoginPage from "@/pages/LoginPage.vue";
import ManageFlightSchedulesPage from "@/pages/ManageFlightSchedulesPage.vue";
import ManageUsersPage from "@/pages/ManageUsersPage.vue";
import PurchaseAmenitiesPage from "@/pages/PurchaseAmenitiesPage.vue";
import SearchFlightsPage from "@/pages/SearchFlightsPage.vue";
import UserHomePage from "@/pages/UserHomePage.vue";
import AmenitiesReportPage from "@/pages/AmenitiesReportPage.vue";
import AirlinesShortSummaryPage from "@/pages/AirlinesShortSummaryPage.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/login",
      name: "login",
      component: LoginPage,
    },
    {
      path: "/",
      name: "home",
      component: () => {
        const userStore = useUsersStore();
        return userStore.userRole === "admin" ? AdminHomePage : UserHomePage;
      },
    },
    {
      path: "/amenities-report",
      name: "amenities-report",
      component: AmenitiesReportPage,
    },
    {
      path: "/airlines-short-summary",
      name: "airlines-short-summary",
      component: AirlinesShortSummaryPage,
    },
    {
      path: "/manage-flight-schedules",
      name: "manage-flight-schedules",
      component: ManageFlightSchedulesPage,
    },
    {
      path: "/manage-users",
      name: "manage-users",
      component: ManageUsersPage,
    },
    {
      path: "/purchase-amenities",
      name: "purchase-amenities",
      component: PurchaseAmenitiesPage,
    },
    {
      path: "/search-flights",
      name: "search-flights",
      component: SearchFlightsPage,
    },
    {
      path: "/client-survey",
      name: "client-survey",
      component: ClientSurveyPage,
    },
  ],
});

const accessList = {
  admin: [
    "/",
    "/manage-users",
    "/manage-flight-schedules",
    "/client-survey",
    "/amenities-report",
    "/airlines-short-summary",
  ],
  user: ["/", "/search-flights", "/purchase-amenities", "/client-survey"],
};

router.beforeEach((to, from, next) => {
  let nextCalled = false;

  const userRole = useUsersStore().userRole;

  const redirect = () => {
    if (nextCalled) {
      return;
    }

    nextCalled = true;
    next();
  };

  if (!userRole && to.path !== "/login") {
    next("/login");
  } else if (
    userRole &&
    !accessList[userRole].includes(to.path) &&
    to.path !== "/404"
  ) {
    next("/");
  } else {
    redirect();
  }
});

export default router;
