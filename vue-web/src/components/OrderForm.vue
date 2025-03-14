<script setup lang="ts">
import {defineEmits, ref} from 'vue'
import type {IOrder} from "@/model/Order.ts";
import api from "@/config/axios.ts";
import {type IWaypoint, WaypointType} from "@/model/Waypoint.ts";

const orderNumber = ref<string>('')
const customer = ref<string>('')
const orderDate = ref<string>('')
const pickup = ref<string>('')
const delivery = ref<string>('')

const showPickup = ref<boolean>(false);
const showDelivery = ref<boolean>(false);

const emit = defineEmits(['createOrder'])

function prepareOrder() {
  const newOrder: IOrder = {
    number: +orderNumber.value,
    customer: customer.value,
    date: orderDate.value,
  }
  return newOrder;
}

const submitOrder = async () => {
  try {
    const {data} = await api.post<IOrder>('/orders/', prepareOrder());
    if (showPickup.value && pickup.value) {
      const pickupWaypoint: IWaypoint = {
        location: pickup.value,
        order: data.id!,
        type: WaypointType.PICKUP
      }
      await api.post<IWaypoint>(`/orders/${data.id!}/waypoints/`, pickupWaypoint);
    }
    if (showDelivery.value && delivery.value) {
      const deliveryWaypoint: IWaypoint = {
        location: delivery.value,
        order: data.id!,
        type: WaypointType.DELIVERY
      }
      await api.post<IWaypoint>(`/orders/${data.id!}/waypoints/`, deliveryWaypoint);
    }
    emit('createOrder', "ok");
  } catch (error: unknown) {
    if (error instanceof Error) {
      emit('createOrder', error.message);
      console.error(error.message);
    } else {
      console.error("An unknown error occurred", error);
      emit('createOrder', "An unknown error occurred");
    }
  }
  resetForm();
}

const resetForm = ()=> {
  orderNumber.value = ''
  customer.value = ''
  orderDate.value = ''
  pickup.value = ''
  delivery.value = ''
  showPickup.value = false
  showDelivery.value = false
}
</script>

<!-- ----------------------------------------------------------------------- -->

<template>
  <div class="order-form">
    <h2 class="form-title">🛒 New Order</h2>

    <form @submit.prevent="submitOrder" class="form-fields">
      <div class="form-field">
        <label for="orderNumber" class="form-label">Order number</label>
        <input
            id="orderNumber"
            type="text"
            v-model="orderNumber"
            class="form-input"
            placeholder="Insert order number"
            required
        />
      </div>

      <div class="form-field">
        <label for="customer" class="form-label">Customer name</label>
        <input
            id="customer"
            type="text"
            v-model="customer"
            class="form-input"
            placeholder="Insert Customer name"
            required
        />
      </div>

      <div class="form-field">
        <label for="orderDate" class="form-label">Date of order</label>
        <input
            id="orderDate"
            type="date"
            v-model="orderDate"
            class="form-input"
            required
        />
      </div>

      <button class="show-button" type="button" @click="() => {showPickup = !showPickup}">{{showPickup ? 'Remove Pickup' : 'Add Pickup' }}</button>
      <div class="form-field" v-if="showPickup">
        <label for="customer" class="form-label">Pickup location</label>
        <input
            id="pickup"
            type="text"
            v-model="pickup"
            class="form-input"
            placeholder="Pickup location"
        />
      </div>

      <button class="show-button" type="button" @click="() => {showDelivery = !showDelivery}">{{showDelivery ? 'Remove Delivery' : 'Add Delivery' }}</button>
      <div class="form-field" v-if="showDelivery">
        <label for="customer" class="form-label">Delivery location</label>
        <input
            id="delivery"
            type="text"
            v-model="delivery"
            class="form-input"
            placeholder="Delivery location"
        />
      </div>

      <button type="submit" class="submit-button">Create Order</button>
    </form>
  </div>
</template>

<style scoped>
.order-form {
  width: 100%;
  max-width: 500px;
  background-color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.form-title {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  text-align: center;
  margin-bottom: 20px;
}

.form-fields {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.form-field {
  display: flex;
  flex-direction: column;
}

.form-label {
  font-size: 14px;
  font-weight: 600;
  color: #555;
  margin-bottom: 8px;
}

.form-input {
  padding: 12px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 5px;
  outline: none;
  transition: border-color 0.3s;
}

.form-input:focus {
  border-color: #4caf50;
}
.show-button {
  padding: 12px;
  background-color: transparent;
  color: #25aac6;
  font-size: 16px;
  border: 2px solid #25aac6;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 20px;
  transition: background-color 0.3s, color 0.3s;
}

.show-button:hover {
  background-color: #25aac6;
  color: #fff;
}
.submit-button {
  padding: 12px;
  background-color: #4caf50;
  color: #fff;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 20px;
  transition: background-color 0.3s;
}

.submit-button:hover {
  background-color: #45a049;
}
</style>
