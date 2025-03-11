<script setup lang="ts">
import {computed, defineProps} from "vue"

const props = defineProps<{
   msg: string
 }>();

const bannerText = computed(() =>
    props.msg === "ok" ? "✅Order successfully created!" : props.msg
);

const bannerClass = computed(() => props.msg === "ok" ? "banner success" : "banner error");
</script>

<!-- ----------------------------------------------------------------------- -->

<template>
  <div :class="bannerClass">
    {{ bannerText }}
  </div>
</template>

<!-- ----------------------------------------------------------------------- -->

<style scoped>
.banner {
  padding: 10px;
  margin: 10px 0;
  text-align: center;
  border-radius: 5px;
  font-weight: bold;
  transition: opacity 0.5s;
}

/* Green background for success */
.success {
  background-color: #4caf50;
  color: white;
}

/* Red background for error/other messages */
.error {
  background-color: #f44336;
  color: white;
}
</style>
