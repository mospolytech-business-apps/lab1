<template>
  <main class="detailed-main">
    <h1 class="visually-hidden">Client Detailed Survey</h1>
    <label class="field">
      <span class="label">Time period: </span>
      <UISelect @update:modelValue="flagsPeriods">
        <option value="all">All period</option>
        <option value="july2017">July 2017</option>
        <option value="august2017">August 2017</option>
        <option value="september2017">September 2017</option>
      </UISelect>
    </label>
    <table class="table">
      <thead>
        <tr>
          <th class="blank"></th>
          <th></th>
          <th
            :colspan="
              Object.keys(flags.gender).filter((k) => flags.gender[k]).length
            "
            v-show="Object.keys(flags.gender).some((k) => flags.gender[k])"
          >
            Gender
          </th>
          <th
            :colspan="Object.keys(flags.age).filter((k) => flags.age[k]).length"
            v-show="Object.keys(flags.age).some((k) => flags.age[k])"
          >
            Age
          </th>
          <th colspan="3">Cabin Type</th>
          <th colspan="5">Destination airport</th>
        </tr>
        <tr>
          <th class="blank"></th>
          <th>Total</th>
          <th v-show="flags.gender.male">Male</th>
          <th v-show="flags.gender.female">Female</th>
          <th v-show="flags.age['18-24']">18-24</th>
          <th v-show="flags.age['25-39']">25-39</th>
          <th v-show="flags.age['40-59']">40-59</th>
          <th v-show="flags.age['60+']">60+</th>
          <th>Economy</th>
          <th>Business</th>
          <th>First</th>
          <th>AUH</th>
          <th>BAH</th>
          <th>DOH</th>
          <th>RYU</th>
          <th>CAI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="meta-description">
            Please rate our aircraft flown on AMONIC Airlines:
          </td>
          <td colspan="16" class="statistics">
            <span class="meta-wrapper">
              <div style="--dont-know: 14.2%" class="dont-know"></div>
              <div style="--poor: 14.2%" class="poor"></div>
              <div
                style="--needs-improvement: 14.2%"
                class="needs-improvement"
              ></div>
              <div style="--adequate: 14.2%" class="adequate"></div>
              <div style="--good: 14.2%" class="good"></div>
              <div style="--very-good: 14.2%" class="very-good"></div>
              <div style="--outstanding: 14.2%" class="outstanding"></div>
            </span>
          </td>
        </tr>
        <tr>
          <td class="meta">Outstanding</td>
          <td class="total">888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
        </tr>
        <tr>
          <td class="meta">Very good</td>
          <td class="total">888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
        </tr>
        <tr>
          <td class="meta">Good</td>
          <td class="total">888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
        </tr>
        <tr>
          <td class="meta">Adequate</td>
          <td class="total">888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
        </tr>
        <tr>
          <td class="meta">Needs improvement</td>
          <td class="total">888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
        </tr>
        <tr>
          <td class="meta">Poor</td>
          <td class="total">888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
        </tr>
        <tr>
          <td class="meta">Don't know</td>
          <td class="total">888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
        </tr>
        <tr>
          <td class="meta-description">
            How would you rate our flight amenities:
          </td>
          <td colspan="16" class="statistics">
            <span class="meta-wrapper">
              <div style="--dont-know: 14.2%" class="dont-know"></div>
              <div style="--poor: 14.2%" class="poor"></div>
              <div
                style="--needs-improvement: 14.2%"
                class="needs-improvement"
              ></div>
              <div style="--adequate: 14.2%" class="adequate"></div>
              <div style="--good: 14.2%" class="good"></div>
              <div style="--very-good: 14.2%" class="very-good"></div>
              <div style="--outstanding: 14.2%" class="outstanding"></div>
            </span>
          </td>
        </tr>
        <tr>
          <td class="meta">Outstanding</td>
          <td class="total">888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
        </tr>
        <tr>
          <td class="meta">Very good</td>
          <td class="total">888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
        </tr>
        <tr>
          <td class="meta">Good</td>
          <td class="total">888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
        </tr>
        <tr>
          <td class="meta">Adequate</td>
          <td class="total">888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
        </tr>
        <tr>
          <td class="meta">Needs improvement</td>
          <td class="total">888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
        </tr>
        <tr>
          <td class="meta">Poor</td>
          <td class="total">888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
        </tr>
        <tr>
          <td class="meta">Don't know</td>
          <td class="total">888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
          <td>888</td>
        </tr>
      </tbody>
    </table>
    <div class="labels">
      <p class="outstanding">Outstanding</p>
      <p class="very-good">Very Good</p>
      <p class="good">Good</p>
      <p class="adequate">Adequate</p>
      <p class="needs-improvement">Needs Improvement</p>
      <p class="poor">Poor</p>
      <p class="dont-know">Don't know</p>
    </div>
    <div class="flagss">
      <div class="gender">
        <label class="filed">
          <input
            v-model="filters.gender.active"
            class="checkbox"
            type="checkbox"
          />
          <span class="label">Gender</span>
        </label>
        <UISelect v-model="filters.gender.value">
          <option value="all">All genders</option>
          <option value="male">Male</option>
          <option value="female">Female</option>
        </UISelect>
      </div>
      <div class="age">
        <label class="filed">
          <input
            v-model="filters.age.active"
            @change="logState"
            class="checkbox"
            type="checkbox"
          />
          <span class="label">Age</span>
        </label>
        <UISelect v-model="filters.age.value">
          <option value="all">All ages</option>
          <option value="18-24">18-24</option>
          <option value="25-39">25-39</option>
          <option value="40-59">40-59</option>
          <option value="60+">60+</option>
        </UISelect>
      </div>
      <div class="cabin-type">
        <label class="filed">
          <input class="checkbox" type="checkbox" />
          <span class="label">Cabin Type</span>
        </label>
        <UISelect>
          <option value="all-types">All types</option>
          <option value="male">Economy</option>
          <option value="female">Business</option>
          <option value="female">First</option>
        </UISelect>
      </div>
      <div class="dest-airport">
        <label class="filed">
          <input class="checkbox" type="checkbox" />
          <span class="label">Destination Airport</span>
        </label>
        <UISelect>
          <option value="all-types">All airports</option>
          <option value="male"></option>
          <option value="female">AUH</option>
          <option value="female">BUH</option>
          <option value="female">DOH</option>
          <option value="female">RYU</option>
          <option value="female">CAI</option>
        </UISelect>
      </div>
    </div>
  </main>
</template>

<script setup>
import UISelect from "@/components/UISelect.vue";
import { ref, watch } from "vue";

const props = defineProps({
  report: Object,
});

const flags = ref({
  gender: { male: false, female: true },
  age: { "18-24": false, "25-39": false, "40-59": false, "60+": true },
});

const filters = ref({
  gender: {
    active: true,
    value: "male",
  },
  age: { active: true, value: "60+" },
});

const updateFlags = (filterChanges) => {
  Object.keys(filterChanges).foreach((category) => {
    if (filterChanges[category] === "all") {
      enableAllFlagsForCategory(flags.value, category);
    } else {
      object.keys(flags.value[category]).foreach((flag) => {
        flags.value[category][flag] = false;
      });
      flags.value[category][filterChanges[category]] = true;
    }
  });

  const enableAllFlagsForCategory = (flags, category) => {
    object.keys(flags[category]).foreach((flag) => {
      flags[category][flag] = true;
    });
  };
};

watch(filters, updateFlags, { deep: true });
</script>

<style scoped>
.detailed-main {
  margin-top: 1rem;
  margin-inline: 1rem;
  padding-bottom: 1rem;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  overflow-y: scroll;
  gap: 1rem;
}

.table {
  font-size: 0.8em;
}

.field {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

th,
td {
  text-align: center;
}

.meta {
  text-align: end;
}
.statistics {
}

.blank {
  border: 0;
}

.table-heading {
  display: flex;
  font-weight: bold;
  margin-bottom: 0.5rem;
  border-bottom: 2px solid black;
  justify-content: space-between;
}

thead th {
  border: 2px solid black;
  padding-inline-start: 0.25rem;
  text-align: center;
}

tbody tr:nth-child(2n + 3) {
  background-color: rgb(0, 50, 255, 0.1);
}

tbody tr:nth-child(8n + 1) {
  background-color: white;
}

th {
  font-weight: 600;
}

td {
  font-weight: 400;
}

.statistics {
}

.meta-description {
  text-align: start;
  font-weight: bold;
}

.meta-wrapper {
  height: 1.2ch;
  display: flex;

  & .dont-know {
    background-color: lightgrey;
    height: 100%;
    width: var(--dont-know);
  }

  & .poor {
    background-color: red;
    height: 100%;
    width: var(--poor);
  }

  & .needs-improvement {
    background-color: orange;
    height: 100%;
    width: var(--needs-improvement);
  }

  & .adequate {
    background-color: #ffabab;
    height: 100%;
    width: var(--adequate);
  }

  & .good {
    background-color: #dcff9c;
    height: 100%;
    width: var(--good);
  }

  & .very-good {
    background-color: #bdf556;
    height: 100%;
    width: var(--very-good);
  }

  & .outstanding {
    background-color: #77b800;
    height: 100%;
    width: var(--outstanding);
  }
}

.labels {
  margin-inline: auto;
  display: flex;
  gap: 2rem;

  & .outstanding {
    flex-grow: 1;
    position: relative;
    &::before {
      position: absolute;
      content: "";
      display: block;
      height: 12px;
      width: 12px;
      left: -1rem;
      top: 50%;
      transform: translateY(-50%);
      background-color: red;
    }
  }

  & .dont-know {
    flex-grow: 1;
    position: relative;
    &::before {
      position: absolute;
      content: "";
      display: block;
      height: 12px;
      width: 12px;
      left: -1rem;
      top: 50%;
      transform: translateY(-50%);
      background-color: lightgray;
    }
  }

  & .poor {
    position: relative;
    &::before {
      position: absolute;
      content: "";
      display: block;
      height: 12px;
      width: 12px;
      left: -1rem;
      top: 50%;
      transform: translateY(-50%);
      background-color: red;
    }
  }

  & .needs-improvement {
    position: relative;
    &::before {
      position: absolute;
      content: "";
      display: block;
      height: 12px;
      width: 12px;
      left: -1rem;
      top: 50%;
      transform: translateY(-50%);
      background-color: orange;
    }
  }

  & .adequate {
    position: relative;
    &::before {
      position: absolute;
      content: "";
      display: block;
      height: 12px;
      width: 12px;
      left: -1rem;
      top: 50%;
      transform: translateY(-50%);
      background-color: #ffabab;
    }
  }

  & .good {
    position: relative;
    &::before {
      position: absolute;
      content: "";
      display: block;
      height: 12px;
      width: 12px;
      left: -1rem;
      top: 50%;
      transform: translateY(-50%);
      background-color: #dcff9c;
    }
  }

  & .very-good {
    position: relative;
    &::before {
      position: absolute;
      content: "";
      display: block;
      height: 12px;
      width: 12px;
      left: -1rem;
      top: 50%;
      transform: translateY(-50%);
      background-color: #bdf556;
    }
  }

  & .outstanding {
    position: relative;
    &::before {
      position: absolute;
      content: "";
      display: block;
      height: 12px;
      width: 12px;
      left: -1rem;
      top: 50%;
      transform: translateY(-50%);
      background-color: #77b800;
    }
  }
}

.table-wrapper {
  flex-grow: 1;
  width: 100%;
  overflow: scroll;
}
.table {
  width: 100%;
  border-collapse: collapse;
  overflow: scroll;
}

.total {
  font-weight: bold;
}

.flagss {
  display: flex;
  width: 100%;
  justify-content: center;
  gap: 5rem;
}

.age,
.gender,
.cabin-type,
.dest-airport {
  display: flex;
  align-items: center;
  gap: 1rem;
}
</style>
