<template>
  <div v-if="props.open" class="billing-modal">
    <UIHeader title="Billing confirmation" :closeButtonHandler="close" />
    <main class="main">
      <div class="payment">
        <p class="total-amount">Total amount: <b>[XXX]</b></p>
        <div class="payment-method">
          <p>Paid using:</p>
          <label class="field">
            <input type="radio" value="credit-card" name="payment-method" />
            <span class="label">Credit card</span>
          </label>
          <label class="field">
            <input type="radio" value="cash" name="payment-method" />
            <span class="label">Cash</span>
          </label>
          <label class="field">
            <input type="radio" value="voucher" name="payment-method" />
            <span class="label">Voucher</span>
          </label>
        </div>
      </div>
      <div class="actions">
        <UIButton @click="issueTicker">
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

<script setup>
import UIHeader from "@/components/UIHeader.vue";
import UIButton from "@/components/UIButton.vue";
import { ref } from "vue";

const props = defineProps({
  open: { type: Boolean, required: true },
});

const emit = defineEmits(["close"]);

const close = () => {
  emit("close");
};

const issueTicker = () => {
  alert("TODO: issue ticket");
};
</script>

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
