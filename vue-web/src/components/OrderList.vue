<script setup lang="ts">
  import Order from "@/components/Order.vue";
  import api from "@/config/axios.ts";
  import {onMounted, ref, defineProps, watch} from "vue";
  import type {IOrder} from "@/model/Order.ts";

  const props = defineProps<{ refresh: number }>()

  const orders = ref<Array<IOrder>>([]);
  const error = ref<string|null>("");
  const loading = ref<boolean>(true);

  const getOrders = async () => {
    try {
      const ordersResponse = await api.get<IOrder[]>('/orders/');
      orders.value = ordersResponse.data;
    } catch (e) {
      error.value = "Error fetching orders";
      console.error(e);
    }
    finally {
      loading.value = false;
    }
  };
  watch(()=> props.refresh, getOrders)
  onMounted(getOrders);
</script>

<!-- ----------------------------------------------------------------------- -->

<template>
  <div class="order-list">
    <p v-if="loading">Loading...</p>
    <p v-if="error" class="error">{{ error }}</p>
    <Order
        v-else
        v-for="anOrder in orders"
        :key="anOrder.id"
        :order="anOrder"
    />
  </div>
</template>

<!-- ----------------------------------------------------------------------- -->


<style scoped>
  .order-list {
    min-width: 600px
  }
</style>
