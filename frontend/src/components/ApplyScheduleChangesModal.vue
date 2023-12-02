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
        <p>[XXX]</p>
        <p>[XXX]</p>
        <p>[XXX]</p>
      </fieldset>
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

const fileInput = ref(null);

const close = () => {
  emit("close");
};

const importData = async () => {
  console.log("Importing data");
  console.log(fileInput.value.files.length);

  if (fileInput.value.files.length > 0) {
    const file = fileInput.value.files[0];

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/api/schedules/import-csv/",
        {
          method: "POST",
          headers: {
            Authorization:
              "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNDI4MjcwLCJpYXQiOjE3MDEzNDE4NzAsImp0aSI6ImY0MzBiYzE0M2FkZTRlYjJiYWVlYzQ1ZWRkMzhiYjViIiwidXNlcl9pZCI6MTB9.EjLzblGVhmLClWIoClb_vUj7qPLgICG2GjqqZ2Hgux0",
          },
          body: formData,
        }
      );

      if (response.ok) {
        console.log("File uploaded successfully");
      } else {
        console.error("File upload failed");
      }
    } catch (error) {
      console.error("Error during fetch:", error);
    }
  } else {
    console.log("No file selected");
  }
};
</script>

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
  margin-top: 0.5rem;
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
