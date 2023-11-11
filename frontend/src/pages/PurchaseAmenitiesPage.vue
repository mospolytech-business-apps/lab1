<template>
  <UIHeader title="Purchase Amenities" />
  <UINav class="menu">
    <button @click="$router.push('/')">Exit</button>
  </UINav>
  <main class="main">
    <div class="search-booking">
      <label class="field">
        <span class="label">Booking number: </span>
        <input class="input" placeholder="[XXXXXX]" type="text" />
      </label>
      <UIButton>OK</UIButton>
    </div>
    <fieldset>
      <legend>Flight list</legend>
      <div class="flight-list">
        <label class="field">
          <span class="booking-number">Choose your flights: </span>
          <div class="select-wrapper">
            <select name="select-flights" class="select-flights">
              <option value="">1107, AUH-DOH, 11/07/2017, 17:20</option>
              <option value="">1309, XYZ-ASD, 23/02/2011, 11:30</option>
              <option value="">2182, QWE-POI, 1/02/2018, 13:00</option>
            </select>
          </div>
        </label>
        <UIButton>Show Amenities</UIButton>
      </div>
    </fieldset>
    <div class="passenger-data">
      <p>Fullname: [XXXXXXXXXXXX]</p>
      <p>Passport number: [XXXXXXXXXXXX]</p>
      <br />
      <p>Your cabin class is: [XXXXXXXXXXXX]</p>
    </div>
    <fieldset>
      <legend>AMONIC Airlines Amenities</legend>
      <div class="amenities-list">
        <label class="field">
          <input type="checkbox" disabled checked />
          <span class="label">Soft Drinks (Free)</span>
        </label>
        <label class="field">
          <input type="checkbox" disabled checked />
          <span class="label">Wi-Fi 50 MB (Free)</span>
        </label>
        <label class="field">
          <input type="checkbox" />
          <span class="label">Next Seat Free (30$)</span>
        </label>
        <label class="field">
          <input type="checkbox" checked />
          <span class="label">WI-FI 250MB (50$)</span>
        </label>
        <label class="field">
          <input type="checkbox" />
          <span class="label">Extra Bag (15$)</span>
        </label>
        <label class="field">
          <input type="checkbox" />
          <span class="label">Laptop Rental (15$)</span>
        </label>
        <br />
      </div>
    </fieldset>
    <div class="bottom-section">
      <div class="summary">
        <p>Items selected:</p>
        <p>Duties and taxes:</p>
        <p>Total payable:</p>
        <p>[$XX]</p>
        <p>[$XX]</p>
        <p>[$XX]</p>
      </div>
      <div class="btns">
        <UIButton>Save and Confirm</UIButton>
        <UIButton @click="$router.push('/')">Exit</UIButton>
      </div>
    </div>
  </main>
  <AmenitiesReportModal :open="isAmenitiesReportModalOpen" />
</template>

<script setup>
import UIHeader from "@/components/UIHeader.vue";
import UIButton from "@/components/UIButton.vue";
import UINav from "@/components/UINav.vue";
import AmenitiesReportModal from "@/components/AmenitiesReportModal.vue";
import { ref } from "vue";

const isAmenitiesReportModalOpen = ref(false);
</script>

<style scoped>
.main {
  padding: 1rem;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-content: center;
  gap: 1rem;
}
.search-booking {
  display: flex;
  gap: 1rem;
  align-items: center;
  padding: 0.5rem;
  flex-wrap: wrap;
}

.field {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}
.label {
  font-size: 1em;
}

.input {
  padding: 0.25rem 0.5rem;
  border: 1px solid black;
  border-radius: 0.25rem;
}

.flight-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 1rem;
  padding-top: 0.5rem;
  padding-bottom: 0.75rem;
  padding-inline: 1rem;
  align-items: center;
}

.select-wrapper {
  padding: 0.25rem 0.5rem 0.25rem 0rem;
  border: 1px solid black;
  border-radius: 5px;
  background-color: white;
  cursor: pointer;
}
.select-flights {
  text-align-last: center;
  padding-inline-end: 2rem;
  outline: none;
  border: none;
}

.amenities-list {
  column-count: 2;
  column-gap: 1rem;
  padding: 0.5rem;
}

.passenger-data {
  padding: 0.25rem;
}
.passenger-data > * {
  margin: 0;
  margin-inline-end: 5%;
  display: inline-block;
  padding-block: 0.25rem;
}
.bottom-section {
  padding-inline: 0.25rem;
  padding-top: 2rem;
  display: flex;
  justify-content: space-between;
}
.summary {
  columns: 2;
  column-gap: 1rem;
}
.summary > * {
  margin: 0;
}
.btns {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
</style>
