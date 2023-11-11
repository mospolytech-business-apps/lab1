<template>
  <UIHeader title="Flight Satisfaction Survey Reports" />
  <UINav class="menu">
    <button>View Results Summary</button>
    <button>View Detailed Summary</button>
    <button @click="$router.push('/')">Exit</button>
  </UINav>
  <main class="main">
    <h1 class="visually-hidden">Client Survey Summary</h1>
    <div class="table-container">
      <div class="table-heading">
        <p>Fieldwork June 2017-October 2017</p>
        <p>Sample Size: 1727 adults</p>
      </div>
      <table class="table">
        <thead>
          <tr>
            <th>Gender</th>
            <th>Female</th>
            <th>Male</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Age</td>
            <td>839</td>
            <td>888</td>
          </tr>
          <tr>
            <td>18-24</td>
            <td>440</td>
            <td>590</td>
          </tr>
          <tr>
            <td>25-39</td>
            <td>400</td>
            <td>300</td>
          </tr>
          <tr>
            <td>40-59</td>
            <td>221</td>
            <td>250</td>
          </tr>
          <tr>
            <td>60+</td>
            <td>178</td>
            <td>148</td>
          </tr>
        </tbody>
      </table>
    </div>
  </main>
</template>

<script setup>
import UIHeader from "@/components/UIHeader.vue";
import UINav from "@/components/UINav.vue";
</script>

<style lang="scss" scoped>
.main {
  margin: 1rem 1rem;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
  gap: 1rem;
}

.menu {
  display: flex;
  justify-content: left;
  gap: 0.25rem;
  min-height: 30px;
  border-bottom: 2px solid black;
}

.menu-btn {
  border-radius: 5px;
  background: 0;
  border: 0;
  cursor: pointer;
}
.menu-btn::first-letter {
  text-decoration: underline;
}
</style>
