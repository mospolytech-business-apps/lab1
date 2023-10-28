import { createRouter, createWebHistory } from "vue-router";
import { useUserRoleStore } from "@/store/userRole";

import AdminHomePage from "@/pages/AdminHomePage.vue";
import AmenitiesReportPage from "@/pages/AmenitiesReportPage.vue";
import ClientSurveyPage from "@/pages/ClientSurveyPage.vue";
import ClientSurveySummaryPage from "@/pages/ClientSurveySummaryPage.vue";
import LoginPage from "@/pages/LoginPage.vue";
import ManageFlightSchedulesPage from "@/pages/ManageFlightSchedulesPage.vue";
import ManageUsersPage from "@/pages/ManageUsersPage.vue";
import PurchaseAmenitiesPage from "@/pages/PurchaseAmenitiesPage.vue";
import SearchFlightSchedulesPage from "@/pages/SearchFlightSchedulesPage.vue";
import UserHomePage from "@/pages/UserHomePage.vue";

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
        const userRoleStore = useUserRoleStore();
        return userRoleStore.userRole === "admin"
          ? AdminHomePage
          : UserHomePage;
      },
    },
    {
      path: "/amenities-report",
      name: "amenities-report",
      component: AmenitiesReportPage,
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
      path: "/search-flight-schedules",
      name: "search-flight-schedules",
      component: SearchFlightSchedulesPage,
    },
    {
      path: "/client-survey",
      name: "client-survey",
      component: ClientSurveyPage,
    },
    {
      path: "/client-survey-summary",
      name: "client-survey-summary",
      component: ClientSurveySummaryPage,
    },
  ],
});

const accessList = {
  admin: [
    "/",
    "/manage-users",
    "/manage-flight-schedules",
    "/client-survey-summary",
    "/amenities-report",
  ],
  user: [
    "/",
    "/search-flight-schedules",
    "/purchase-amenities",
    "/client-survey",
  ],
};

router.beforeEach((to, from, next) => {
  const userRoleStore = useUserRoleStore();
  const userRole = userRoleStore.userRole;
  let nextCalled = false;

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