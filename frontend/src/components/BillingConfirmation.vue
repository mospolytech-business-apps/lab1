<template>
  <div class="billing-confirmation">
    <div class="header">
      <h1>Billing Confirmation</h1>
    </div>

    <div class="main">
      <div class="billing-address">
        <h3>Billing Address</h3>
        <table>
          <tr>
            <th>Name</th>
            <td>{{ billingAddress.name }}</td>
          </tr>
          <tr>
            <th>Address</th>
            <td>{{ billingAddress.address }}</td>
          </tr>
          <tr>
            <th>City</th>
            <td>{{ billingAddress.city }}</td>
          </tr>
          <tr>
            <th>State</th>
            <td>{{ billingAddress.state }}</td>
          </tr>
          <tr>
            <th>Zip Code</th>
            <td>{{ billingAddress.zipCode }}</td>
          </tr>
        </table>
      </div>

      <div class="payment-method">
        <h3>Payment Method</h3>
        <table>
          <tr>
            <th>Type</th>
            <td>{{ paymentMethod.type }}</td>
          </tr>
          <tr>
            <th>Number</th>
            <td>{{ paymentMethod.number }}</td>
          </tr>
          <tr>
            <th>Expiration Date</th>
            <td>{{ paymentMethod.expirationDate }}</td>
          </tr>
        </table>
      </div>

      <div class="total-price">
        <h3>Total Price</h3>
        <p>$ {{ totalPrice }}</p>
      </div>
    </div>

    <div class="footer">
      <button type="button" @click="closeBillingConfirmation()">Close</button>
    </div>
  </div>
</template>

<script setup>
import { defineComponent } from "vue";

const BillingConfirmation = defineComponent({
  props: {
    billingAddress: {
      type: Object,
      required: true,
    },
    paymentMethod: {
      type: Object,
      required: true,
    },
    totalPrice: {
      type: Number,
      required: true,
    },
  },
  methods: {
    closeBillingConfirmation() {
      this.$emit("close");
    },
  },
});
</script>

<style scoped lang="scss">
.billing-confirmation {
  width: 500px;
  margin: 0 auto;
  padding: 15px;
}

.header {
  text-align: center;
}

.main {
  margin-top: 15px;
}

table,
th,
td {
  border: 1px solid black;
  border-collapse: collapse;
  padding: 5px;
}

th {
  background-color: #ccc;
}

.total-price {
  margin-top: 15px;
  text-align: right;
}

.footer {
  text-align: right;
  margin-top: 15px;
}
</style>
