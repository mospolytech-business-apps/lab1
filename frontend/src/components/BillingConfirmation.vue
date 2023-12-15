<script setup>
import { ref } from "vue";
import { useTicketsStore } from "@/stores/tickets.store";
import { useNotificationsStore } from "@/stores/notifications.store";

import UIHeader from "@/components/UIHeader.vue";
import UIButton from "@/components/UIButton.vue";

const { addAlert } = useNotificationsStore();
const { issueTicket } = useTicketsStore();
const billingMethod = ref("credit-card");

const props = defineProps({
  open: { type: Boolean, required: true },
  passengers: { type: Array, required: true },
  returnTicketInfo: { type: Object, required: false },
  outboundTicketInfo: { type: Object, required: true },
  price: { type: Number, required: true },
});

const emit = defineEmits(["close", "ticketsCreated"]);

const close = () => {
  emit("close");
};

const ticketIssuer = () => {
  if (!billingMethod.value) {
    addAlert("Please select a payment method");
    return;
  }

  const bookingReference = Math.random().toString(36).substring(7);

  props.passengers.forEach((passenger) => {
    issueTicket({
      ...passenger,
      ...props.outboundTicketInfo,
      bookingReference: bookingReference,
    });
  });

  if (props.returnTicketInfo) {
    props.passengers.forEach((passenger) => {
      issueTicket({
        ...passenger,
        ...props.returnTicketInfo,
        bookingReference: bookingReference,
      });
    });
  }

  emit("ticketsCreated");
};
</script>

<template>
  <div v-if="props.open" class="billing-modal">
    <UIHeader title="Billing confirmation" :closeButtonHandler="close" />
    <main class="main">
      <div class="payment">
        <p class="total-amount">
          Total amount: <b>${{ parseInt(props.price) }}</b>
        </p>
        <div class="payment-method">
          <p>Paid using:</p>
          <label class="field">
            <input
              type="radio"
              v-model="billingMethod"
              value="credit-card"
              name="payment-method"
            />
            <span class="label">Credit card</span>
          </label>
          <label class="field">
            <input
              type="radio"
              v-model="billingMethod"
              value="cash"
              name="payment-method"
            />
            <span class="label">Cash</span>
          </label>
          <label class="field">
            <input
              type="radio"
              v-model="billingMethod"
              value="voucher"
              name="payment-method"
            />
            <span class="label">Voucher</span>
          </label>
        </div>
      </div>
      <div class="actions">
        <UIButton @click="ticketIssuer">
          <img
            src="src/assets/check-mark-icon.png"
            width="20"
            alt="Checkmark icon"
          />
          <span>Issue tickets</span>
        </UIButton>
        <UIButton @click="close" class="cancel-icon">
          <img src="src/assets/cross-icon.png" width="20" alt="Cross icon" />
          <span>Cancel</span>
        </UIButton>
      </div>
    </main>
  </div>
</template>

<style scoped>
.billing-modal {
  position: absolute;
  top: 50%;
  left: 50%;
  background-color: white;
  min-width: 40%;
  transform: translate(-50%, -50%);
  border: 1px solid black;
  box-shadow: 0 0 2rem black;
}

.main {
  display: flex;
  flex-direction: column;
  align-items: start;
  gap: 3rem;
  width: 100%;
  background-color: white;
  padding: 2rem 4rem;
  overflow: scroll;
}

.cancel-icon:hover {
  background-color: salmon;
}

.actions {
  display: flex;
  width: 100%;
  justify-content: center;
  gap: 2rem;
}

.payment {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.field {
  padding-inline-start: 5rem;
}

.payment-method {
  display: flex;
  flex-direction: column;
}
</style>
