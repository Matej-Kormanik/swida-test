<script setup lang="ts">
import {defineProps, ref} from 'vue'
import type {IOrder} from "@/model/Order.ts";
import Modal from "@/ui/Modal.vue";
import {formatDate} from "@/config/utils.ts";

const props = defineProps<{ order: IOrder }>();

const showModal = ref(false);

const openModal = () => (showModal.value = true);
const closeModal = () => (showModal.value = false);
</script>

<template>
  <div class="order-card" @click="openModal">
    <h1>Order #{{ order.number }}</h1>
    <div class="order-info">
      <p><strong>Customer:</strong> {{ order.customer }}</p>
      <p><strong>Date:</strong> {{ formatDate(order.date) }}</p>
    </div>
  </div>

  <Modal :show="showModal" @close="closeModal">
    <div class="order-details">
      <div class="header">
        <h2>Order #{{ order.number }}</h2>
      </div>
      <div class="info">
        <p><strong>Customer:</strong> {{ order.customer }}</p>
        <p><strong>Date:</strong> {{ formatDate(order.date) }}</p>
      </div>
      <div class="waypoints">
        <h3>Waypoints</h3>
        <ul>
          <li v-for="waypoint in order.waypoints" :key="waypoint.id">
            <p><strong>Type:</strong> {{ waypoint.type }}</p>
            <p><strong>Location:</strong> {{ waypoint.location }}</p>
          </li>
        </ul>
      </div>
    </div>
  </Modal>
</template>

<style scoped>
.order-card {
  background: white;
  padding: 15px;
  margin-bottom: 1rem;
  border-radius: 8px;
  cursor: pointer;
  transition: 0.3s;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
.order-card:hover {
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
  border: 1px solid #333333;
}
.order-details {
  padding: 20px;
}
.header {
  background: #007bff;
  color: white;
  padding: 10px;
  border-radius: 8px;
  text-align: center;
  font-size: 18px;
  font-weight: bold;
}
.info p {
  font-size: 16px;
  margin: 5px 0;
}
.waypoints {
  margin-top: 15px;
}
.waypoints h3 {
  font-size: 18px;
  margin-bottom: 5px;
}
.waypoints ul {
  list-style-type: none;
  padding: 0;
}
.waypoints li {
  background: #f8f9fa;
  padding: 8px;
  margin-bottom: 5px;
  border-radius: 5px;
}
</style>
