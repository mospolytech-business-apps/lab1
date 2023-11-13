<template>
  <div class="select-wrapper">
    <select
      :class="{
        placeholderUnderline: props.placeholder && props.placeholderUnderline,
        placeholderBlue: props.placeholder && props.placeholderBlue,
        placeholder: true,
      }"
      placeholder="Select an option"
      class="select"
      id="select"
    >
      <option v-if="props.placeholder" disabled selected value="">
        {{ props.placeholder }}
      </option>
      <slot />
    </select>
  </div>
</template>

<script setup>
const props = defineProps({
  placeholder: { type: String },
  placeholderBlue: { type: Boolean },
  placeholderUnderline: { type: Boolean },
});
</script>

<style>
.select {
  appearance: none;
  -webkit-appearance: none;
  width: 100%;
  font-size: 1rem;
  padding: 0.2em 0.5em 0.2em 0.5em;
  background-color: #fff;
  border: 1px solid #757575;
  border-radius: 0.15rem;
  color: #000;
  cursor: pointer;
}

.select-wrapper {
  position: relative;
}

.select-wrapper::after {
  content: "▾";
  position: absolute;
  display: block;
  width: 28px;
  height: 32px;
  padding-top: 0.3rem;
  padding-inline: 0.48rem;
  top: 0;
  right: 0;
  background-size: contain;
  pointer-events: none;
  border-left: 1px solid #757575;
}

.select-wrapper::before {
  content: "";
  position: absolute;
  display: block;
  width: 20px;
}

.placeholder {
  color: blue;
  padding-left: 0;
}

.placeholderBlue {
  color: blue;
}

.placeholderUnderline {
  text-decoration: underline;
}
</style>
