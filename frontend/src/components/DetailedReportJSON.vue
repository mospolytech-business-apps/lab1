<template>
  <main class="detailed-main">
    <h1 class="visually-hidden">Client Detailed Survey</h1>
    <label class="field">
      <span class="label">Time period: </span>
      <UISelect>
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
          <th>&lrm;&#x20;</th>
          <th
            :colspan="
              Object.keys(flags.gender).filter((k) => flags.gender[k]).length -
              1
            "
            v-show="
              Object.keys(flags.gender).some((k) => flags.gender[k]) &&
              flags.gender.__active
            "
          >
            Gender
          </th>
          <th
            :colspan="
              Object.keys(flags.age).filter((k) => flags.age[k]).length - 1
            "
            v-show="
              Object.keys(flags.age).some((k) => flags.age[k]) &&
              flags.age.__active
            "
          >
            Age
          </th>
          <th
            :colspan="
              Object.keys(flags.cabin).filter((k) => flags.cabin[k]).length - 1
            "
            v-show="
              Object.keys(flags.cabin).some((k) => flags.cabin[k]) &&
              flags.cabin.__active
            "
          >
            Cabin Type
          </th>
          <th
            :colspan="
              Object.keys(flags.airport).filter((k) => flags.airport[k])
                .length - 1
            "
            v-show="
              Object.keys(flags.airport).some((k) => flags.airport[k]) &&
              flags.airport.__active
            "
          >
            Destination airport
          </th>
        </tr>
        <tr>
          <th class="blank"></th>
          <th>Total</th>
          <th v-show="flags.gender.male && flags.gender.__active">Male</th>
          <th v-show="flags.gender.female && flags.gender.__active">Female</th>
          <th v-show="flags.age['18-24'] && flags.age.__active">18-24</th>
          <th v-show="flags.age['25-39'] && flags.age.__active">25-39</th>
          <th v-show="flags.age['40-59'] && flags.age.__active">40-59</th>
          <th v-show="flags.age['60+'] && flags.age.__active">60+</th>
          <th v-show="flags.cabin['economy'] && flags.cabin.__active">
            Economy
          </th>
          <th v-show="flags.cabin['business'] && flags.cabin.__active">
            Business
          </th>
          <th v-show="flags.cabin['first'] && flags.cabin.__active">First</th>
          <th v-show="flags.airport['AUH'] && flags.airport.__active">AUH</th>
          <th v-show="flags.airport['BAH'] && flags.airport.__active">BAH</th>
          <th v-show="flags.airport['DOH'] && flags.airport.__active">DOH</th>
          <th v-show="flags.airport['RYU'] && flags.airport.__active">RYU</th>
          <th v-show="flags.airport['CAI'] && flags.airport.__active">CAI</th>
        </tr>
      </thead>
      <tbody>
        <template v-for="(q, qk, qi) of data" :key="qk">
          <tr>
            <td class="meta-description">
              {{ qk }}
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
          <tr v-for="(r, rk, i) of q" :key="rk">
            <td class="meta">{{ rk }}</td>
            <td class="total">{{ calculateTotalForRow(qi, i) }}</td>
            <td v-show="isColumnShown(j)" v-for="(d, j) in r">{{ d }}</td>
          </tr>
        </template>
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
    <div class="flags">
      <div class="gender">
        <label class="filed">
          <input
            v-model="flags.gender['__active']"
            class="checkbox"
            type="checkbox"
          />
          <span class="label">Gender</span>
        </label>
        <UISelect :disabled="!flags.gender.__active" v-model="filters.gender">
          <option value="all">All genders</option>
          <option value="male">Male</option>
          <option value="female">Female</option>
        </UISelect>
      </div>
      <div class="age">
        <label class="filed">
          <input
            v-model="flags.age['__active']"
            class="checkbox"
            type="checkbox"
          />
          <span class="label">Age</span>
        </label>
        <UISelect :disabled="!flags.age.__active" v-model="filters.age">
          <option value="all">All ages</option>
          <option value="18-24">18-24</option>
          <option value="25-39">25-39</option>
          <option value="40-59">40-59</option>
          <option value="60+">60+</option>
        </UISelect>
      </div>
      <div class="cabin-type">
        <label class="filed">
          <input
            v-model="flags.cabin['__active']"
            class="checkbox"
            type="checkbox"
          />
          <span class="label">Cabin Type</span>
        </label>
        <UISelect :disabled="!flags.cabin.__active" v-model="filters.cabin">
          <option value="all">All types</option>
          <option value="economy">Economy</option>
          <option value="business">Business</option>
          <option value="first">First</option>
        </UISelect>
      </div>
      <div class="dest-airport">
        <label class="filed">
          <input
            v-model="flags.airport['__active']"
            class="checkbox"
            type="checkbox"
          />
          <span class="label">Destination Airport</span>
        </label>
        <UISelect :disabled="!flags.airport.__active" v-model="filters.airport">
          <option value="all">All airports</option>
          <option value="AUH">AUH</option>
          <option value="BAH">BAH</option>
          <option value="DOH">DOH</option>
          <option value="RYU">RYU</option>
          <option value="CAI">CAI</option>
        </UISelect>
      </div>
    </div>
  </main>
</template>

<script setup>
import UISelect from "@/components/UISelect.vue";
import { computed, ref, watch } from "vue";

const props = defineProps({
  report: Object,
});

const data = computed(() => props.report["July 2017"]);

const filters = ref({
  gender: "all",
  age: "all",
  cabin: "all",
  airport: "all",
});

const flags = ref({
  gender: { __active: true, male: true, female: true },
  age: {
    __active: true,
    "18-24": true,
    "25-39": true,
    "40-59": true,
    "60+": true,
  },
  cabin: {
    __active: true,
    economy: true,
    business: true,
    first: true,
  },
  airport: {
    __active: true,
    AUH: true,
    BAH: true,
    DOH: true,
    RYU: true,
    CAI: true,
  },
});

const updateFlags = (filterChanges) => {
  const enableAllFlagsForCategory = (flags, category) => {
    Object.keys(flags[category]).forEach((flag) => {
      if (flag !== "__active") {
        flags[category][flag] = true;
      }
    });
  };

  Object.keys(filterChanges).forEach((category) => {
    if (filterChanges[category] === "all") {
      enableAllFlagsForCategory(flags.value, category);
    } else {
      Object.keys(flags.value[category]).forEach((flag) => {
        if (flag !== "__active") {
          flags.value[category][flag] = false;
        }
      });
      flags.value[category][filterChanges[category]] = true;
    }
  });
};

const boolFlags = ref([]);

const isColumnShown = (col) => {
  boolFlags.value = [];
  for (const category of Object.values(flags.value)) {
    let categoryFlags = [];
    for (const [subKey, subValue] of Object.entries(category)) {
      if (subKey !== "__active") {
        if (category["__active"] === false) {
          categoryFlags.push(false);
        } else {
          categoryFlags.push(subValue);
        }
      }
    }
    boolFlags.value.push(...categoryFlags);
  }
  return boolFlags.value[col];
};

const calculateTotalForRow = (question, mark) => {
  let total = 0;
  const row = 7 * question + mark;

  const preparedData = Object.values(data.value)
    .map((q) => Object.values(q))
    .flat();

  total += preparedData[row]
    .map((v, i) => (boolFlags.value[i] ? v : 0))
    .reduce((a, b) => a + b, 0);

  return total;
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

.flags {
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
