<template>
     <h1>Administrator Home Page</h1>
    <div class="list" align="center">
        <router-link to="/manage-users">Manage Users</router-link>
        <router-link to="/manage-flight-schedules">Manage Flight Schedules</router-link>
        <router-link to="/client-survey-summary">Client Survey Summary</router-link>
        <router-link to="/amenities-report">Amenities Report</router-link>
    </div>
</template>

<script setup>
defineOptions({
    name: 'AdminHomePage',
})
</script>

<style scoped>

.list {
    display: flex;
    flex-direction: column;
}
</style>
