<script setup>
import { ref, watchEffect, onMounted, computed } from "vue";
import { storeToRefs } from "pinia";
import { useCountriesStore } from "@/stores/countries.store";
import { useNotificationsStore } from "@/stores/notifications.store";
import { useUsersStore } from "@/stores/users.store";

import BillingConfirmation from "@/components/BillingConfirmation.vue";
import UIHeader from "@/components/UIHeader.vue";
import UIButton from "@/components/UIButton.vue";
import UISelect from "@/components/UISelect.vue";

const { allCountries } = storeToRefs(useCountriesStore());
const { getAllCountries } = useCountriesStore();
const { addAlert } = useNotificationsStore();
const { currentUser } = storeToRefs(useUsersStore());

const counties = ref([]);

const props = defineProps({
  open: { type: Boolean, required: true },
  numberOfPassengers: { type: Number, required: true },
  cabinType: { type: String, required: true },
  outboundChosenFlight: { type: Object, required: true },
  returnChosenFlight: { type: Object, required: false },
});

const passengers = ref([]);
const outboundTicketInfo = ref(null);
const returnTicketInfo = ref(null);

const totalPrice = computed(() => {
  let outboundPrice = props.outboundChosenFlight?.base_price ?? 0;
  let returnPrice = props.returnChosenFlight?.base_price ?? 0;

  if (props.cabinType === "First Class") {
    outboundPrice *= 1.3 * 1.35;
    returnPrice *= 1.3 * 1.35;
  }

  if (props.cabinType === "Business") {
    outboundPrice *= 1.3;
    returnPrice *= 1.3;
  }

  return (outboundPrice + returnPrice) * props.numberOfPassengers;
});

watchEffect(() => {
  passengers.value = Array.from({ length: props.numberOfPassengers }, () => ({
    firstName: null,
    lastName: null,
    birthdate: null,
    passportNumber: null,
    passportCountry: null,
    phoneNumber: null,
  }));
});

const isBillingConfirmationOpen = ref(false);

const openBillingConfirmationModal = () => {
  if (
    passengers.value.some((p) => {
      return Object.values(p).some((value) => value === null);
    })
  ) {
    addAlert("Please fill all passenger details");
    return;
  }

  isBillingConfirmationOpen.value = true;
};

const closeBillingConfirmationModal = () => {
  isBillingConfirmationOpen.value = false;
};

const emit = defineEmits(["close"]);

const close = () => {
  emit("close");
};

const newPassenger = ref({
  firstName: null,
  lastName: null,
  birthdate: null,
  passportNumber: null,
  passportCountry: null,
  phoneNumber: null,
});

watchEffect(() => {
  outboundTicketInfo.value = {
    user: currentUser.value.id,
    schedule: props.outboundChosenFlight?.id ?? null,
    cabinType: props.cabinType,
  };

  returnTicketInfo.value = props.returnChosenFlight
    ? {
        user: currentUser.value.id,
        schedule: props.returnChosenFlight?.id ?? null,
        cabinType: props.cabinType,
      }
    : null;
});

const selectPassenger = (passenger) => {
  selectedPassenger.value = passenger;
};

const selectedPassenger = ref(null);

const addPassenger = () => {
  const index = passengers.value.findIndex((passenger) => {
    return Object.values(passenger).every((value) => value === null);
  });

  if (index !== -1) {
    passengers.value[index] = { ...newPassenger.value };
    newPassenger.value = {
      firstName: null,
      lastName: null,
      birthdate: null,
      passportNumber: null,
      passportCountry: null,
      phoneNumber: null,
    };
  } else {
    addAlert("You have reached the maximum number of passengers");
  }
};

const removePassenger = () => {
  const index = passengers.value.findIndex(
    (p) => p === selectedPassenger.value
  );

  passengers.value[index] = {
    firstName: null,
    lastName: null,
    birthdate: null,
    passportNumber: null,
    passportCountry: null,
    phoneNumber: null,
  };
};

const handleTicketsCreated = () => {
  passengers.value = [];
  closeBillingConfirmationModal();
  emit("ticketsCreated");
};

onMounted(async () => {
  counties.value = allCountries.value.length
    ? allCountries.value
    : await getAllCountries();
});
</script>

<template>
  <div v-if="props.open" class="modal">
    <UIHeader title="Booking confirmation" :closeButtonHandler="close" />
    <main class="main">
      <fieldset class="details" v-if="props.outboundChosenFlight">
        <legend>Outbound flight details</legend>
        <p class="detail">
          From: <b>{{ props.outboundChosenFlight?.from }}</b>
        </p>
        <p class="detail">
          To: <b>{{ props.outboundChosenFlight?.to }}</b>
        </p>
        <p class="detail">
          Cabin Type: <b>{{ props.cabinType }}</b>
        </p>
        <p class="detail">
          Date:
          <b>{{ props.outboundChosenFlight?.date?.replace(/-/g, "/") }}</b>
        </p>
        <p class="detail">
          Flight number:
          <b>{{
            props.outboundChosenFlight?.flight_numbers?.reduce(
              (a, c, i) => a + (i ? " – " : "") + c,
              ""
            ) ?? "–"
          }}</b>
        </p>
      </fieldset>
      <fieldset class="details" v-if="props.returnChosenFlight">
        <legend>Return flight details</legend>
        <p class="detail">
          From: <b>{{ props.returnChosenFlight?.from }}</b>
        </p>
        <p class="detail">
          To: <b> {{ props.returnChosenFlight?.to }} </b>
        </p>
        <p class="detail">
          Cabin Type: <b>{{ props.cabinType }}</b>
        </p>
        <p class="detail">
          Date: <b>{{ props.returnChosenFlight?.date?.replace(/-/g, "/") }}</b>
        </p>
        <p class="detail">
          Flight number:
          <b>{{
            props.returnChosenFlight?.flight_numbers?.reduce(
              (a, c, i) => a + (i ? " – " : "") + c,
              ""
            ) ?? "–"
          }}</b>
        </p>
      </fieldset>
      <form @submit.prevent="addPassenger">
        <fieldset class="passenger-details">
          <legend>Passenger details</legend>
          <label class="field">
            <span class="label">Firstname</span>
            <input
              v-model="newPassenger.firstName"
              class="input"
              type="text"
              required
            />
          </label>
          <label class="field">
            <span class="label">Lastname</span>
            <input
              v-model="newPassenger.lastName"
              class="input"
              type="text"
              required
            />
          </label>
          <label class="field">
            <span class="label">Birthdate</span>
            <input
              v-model="newPassenger.birthdate"
              class="input"
              type="date"
              required
            />
          </label>
          <label class="field">
            <span class="label">Passport number</span>
            <input
              v-model="newPassenger.passportNumber"
              class="input"
              type="text"
              required
            />
          </label>
          <label class="field">
            <span class="label">Passport country</span>
            <UISelect
              v-model="newPassenger.passportCountry"
              class="input"
              placeholder=" "
              required
            >
              <option v-for="country in counties" :value="country.name">
                {{ country.name }}
              </option>
            </UISelect>
          </label>
          <label class="field">
            <span class="label">Phone</span>
            <input
              v-model="newPassenger.phoneNumber"
              class="input"
              placeholder="(___) ___ __-__"
              type="tel"
              required
            />
          </label>
          <UIButton class="passenger-details-btn">Add passenger</UIButton>
        </fieldset>
      </form>

      <div class="passengers-list">
        <p class="table-title">Passengers list</p>
        <div class="table-wrapper">
          <table class="table">
            <thead>
              <tr>
                <th>Firstname</th>
                <th>Lastname</th>
                <th>Birthdate</th>
                <th>Passport number</th>
                <th>Passport country</th>
                <th>Phone</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="passenger in passengers"
                :key="passenger.passportNumber"
                @click="selectPassenger(passenger)"
                :class="{
                  selected: passenger === selectedPassenger,
                  row: true,
                }"
              >
                <td>{{ passenger?.firstName ?? "–" }}</td>
                <td>{{ passenger?.lastName ?? "–" }}</td>
                <td>{{ passenger?.birthdate ?? "–" }}</td>
                <td>{{ passenger?.passportNumber ?? "–" }}</td>
                <td>{{ passenger?.passportCountry ?? "–" }}</td>
                <td>{{ passenger?.phoneNumber ?? "–" }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <UIButton class="remove-passenger" @click="removePassenger"
          >Remove passenger</UIButton
        >
        <div class="bottom-actions">
          <UIButton @click="close">
            <img src="src/assets/reload-icon.png" width="20" alt="Back icon" />
            <span>Back to search for filters</span>
          </UIButton>
          <UIButton @click="openBillingConfirmationModal">
            <img
              src="src/assets/check-mark-icon.png"
              width="20"
              alt="Confirm icon"
            />
            <span>Confirm booking</span>
          </UIButton>
        </div>
      </div>
    </main>
  </div>
  <BillingConfirmation
    :open="isBillingConfirmationOpen"
    :passengers="passengers"
    :outboundTicketInfo="outboundTicketInfo"
    :returnTicketInfo="returnTicketInfo"
    :price="totalPrice"
    @close="closeBillingConfirmationModal"
    @ticketsCreated="handleTicketsCreated"
  />
</template>

<style scoped>
.modal {
  position: absolute;
  top: 50%;
  left: 50%;
  background-color: white;
  min-width: 65%;
  transform: translate(-50%, -50%);
  border: 1px solid black;
  box-shadow: 0 0 2rem black;
}

.main {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  width: 100%;
  padding: 1rem 2rem;
  background-color: white;
  padding: 1rem;
  overflow: scroll;
}

.table-wrapper {
  flex-grow: 1;
  width: 100%;
  height: 20rem;
  border: 2px solid black;
  margin-bottom: 1rem;
  overflow: scroll;
}

.details {
  display: flex;
  width: 100%;
  gap: 4rem;
}
.detail {
  display: inline;
  gap: 0.25rem;
}
.table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid black;
  overflow: scroll;
}

.passenger-details {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  row-gap: 1rem;
  column-gap: 2rem;
}

.field {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.input {
  /* width: 100%; */
  min-width: 10rem;
  flex-grow: 1;
  height: min-content;
}

.label {
  flex-grow: 1;
  align-self: center;
  width: max-content;
  white-space: nowrap;
}

thead {
  background-color: lightgray;
  border-bottom: 3px solid black;
}

td,
th {
  border: 1px solid black;
  padding-inline-start: 0.25rem;
}

.passengers-list {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  width: 100%;
}
.table-title {
}

.passenger-details-btn {
  grid-column: -2 / -1;
  margin-left: auto;
}

.remove-passenger {
  margin-left: auto;
}
.remove-passenger:hover {
  background-color: salmon;
}

.bottom-actions {
  display: flex;
  justify-content: center;
  gap: 2rem;
}

.selected {
  box-shadow: inset 0 0 0 2px black;
}
</style>
