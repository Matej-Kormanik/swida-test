<script setup lang="ts">
  import Order from "@/components/Order.vue";
  import api from "@/config/axios.ts";
  import {onMounted, ref, defineProps, watch} from "vue";
  import type {IOrder} from "@/model/Order.ts";

  const props = defineProps<{ refresh: number }>()

  const orders = ref<Array<IOrder>>([]);
  const error = ref<string|null>("");
  const loading = ref<boolean>(true);

  const orderNumberFilter = ref<string>("");
  const customerFilter = ref<string>("");

  const getFilters = () => {
    const params: Record<string, string> = {};
    if (orderNumberFilter.value.trim()) {
      params.number = orderNumberFilter.value.trim();
    }
    if (customerFilter.value.trim()) {
      params.customer = customerFilter.value.trim();
    }
    return params;
  }

  const resetFilters = () => {
    orderNumberFilter.value = "";
    customerFilter.value = "";
    getOrders();
  }

  const getOrders = async () => {
    try {
      const ordersResponse = await api.get<IOrder[]>('/orders/', {params: getFilters()});
      orders.value = ordersResponse.data;
    } catch (e) {
      error.value = "Error fetching orders";
      console.error(e);
    }
    finally {
      loading.value = false;
    }
  }
  watch(() => props.refresh, getOrders);
  onMounted(getOrders);
</script>

<!-- ----------------------------------------------------------------------- -->

<template>
  <div class="order-list">
    <div class="filters">
      <input v-model="orderNumberFilter" placeholder="Filter by Order Number" />
      <input v-model="customerFilter" placeholder="Filter by Customer" />
      <button @click="getOrders">Apply Filters</button>
      <button @click="resetFilters">Reset Filters</button>
    </div>

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
  .filters {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
  }

  .filters input {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }

  .filters button {
    padding: 8px 12px;
    background-color: #25aac6;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background 0.3s;
  }

  .filters button:hover {
    background-color: #1a8099;
  }
</style>
