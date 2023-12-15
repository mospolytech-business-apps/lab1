<script setup>
import UIHeader from "@/components/UIHeader.vue";
import UIButton from "@/components/UIButton.vue";
import Cookies from "js-cookie";

import { ref } from "vue";
import { useSchedulesStore } from "@/stores/schedules.store";
import { useNotificationsStore } from "@/stores/notifications.store";
const { importCSV } = useSchedulesStore();
const { addError } = useNotificationsStore();

const importStatistics = ref(null);

const props = defineProps({
  open: { type: Boolean, required: true },
});
const emit = defineEmits(["close"]);

const fileInput = ref(null);

const importData = async () => {
  if (fileInput.value.files.length > 0) {
    const file = fileInput.value.files[0];

    const formData = new FormData();
    formData.append("file", file, file.name);

    importStatistics.value = await importCSV(formData);
  } else {
    addError("No file selected");
  }
};

const close = () => {
  emit("close");
};
</script>

<template>
  <div v-if="props.open" class="modal">
    <UIHeader title="Apply Schedule Changes" :closeButtonHandler="close" />
    <main class="main" id="myModal">
      <label class="field">
        <span class="label">Please select the text file with the changes</span>
        <div class="file-input-wrapper">
          <input class="input" type="file" ref="fileInput" />
          <UIButton @click="importData">
            <img
              src="https://cdn.icon-icons.com/icons2/1122/PNG/512/downloaddownarrowsymbolinsquarebutton_79508.png"
              width="25"
              alt="Import icon"
            />
            Import
          </UIButton>
        </div>
      </label>
      <fieldset class="summary">
        <legend>Results</legend>
        <p>Success Changes Applied:</p>
        <p>Duplicate Records Discarded:</p>
        <p>Records with missing fields discarded:</p>
        <p>
          <b>{{ importStatistics?.success_count ?? "–" }}</b>
        </p>
        <p>
          <b>{{ importStatistics?.duplicate_count ?? "–" }}</b>
        </p>
        <p>
          <b>{{ importStatistics?.missing_fields_count ?? "–" }}</b>
        </p>
      </fieldset>
    </main>
  </div>
</template>

<style scoped>
.modal {
  position: absolute;
  top: 50%;
  left: 50%;
  background-color: white;
  min-width: 40%;
  min-height: 35%;
  transform: translate(-50%, -50%);
  border: 1px solid black;
  box-shadow: 0 0 2rem black;
}

.main {
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.summary {
  columns: 2;
  column-gap: 1rem;
  flex-grow: 1;
}

.summary > * {
  display: block;
  margin-top: 0.5rem;
  &:first-of-type {
    margin-top: 0;
  }
}

.field {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.file-input-wrapper {
  display: flex;
  gap: 1rem;
  padding-inline: 1rem;
}

.input {
  /* padding: 1rem 0.25rem; */
  border: 1px solid black;
  flex-grow: 1;
  border-radius: 0.25rem;
  padding-top: 0.25rem;
  padding-inline-start: 1rem;
}
.input::file-selector-button {
  display: none;
}
</style>
