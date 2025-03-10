<script setup lang="ts">
  import { defineProps } from 'vue'
  import type {IOrder} from "@/model/Order.ts";
  defineProps<{
    order: IOrder
  }>();
</script>

<template>
  <div class="order-card">
    <h1>Order #{{ order.number }}</h1>
    <div class="order-info">
      <p><strong>Customer:</strong> {{ order.customer }}</p>
      <p><strong>Date:</strong> {{ order.date }}</p>
    </div>
  </div>
</template>

<style scoped>
.order-card {
  background: #fff;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  padding: 1.2rem;
  margin-bottom: 1rem;
  max-width: 600px;
  transition: transform 0.2s ease-in-out;
}

.order-card:hover {
  transform: translateY(-2px);
}

h1 {
  font-size: 1.4rem;
  color: #333;
  margin-bottom: 0.8rem;
}

.order-info p {
  margin: 0.5rem 0;
  color: #555;
  font-size: 1rem;
}

.order-info strong {
  color: #222;
}
</style>
