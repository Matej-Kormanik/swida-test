<script setup lang="ts">
import { ref } from 'vue'

const orderNumber = ref<string>('')
const customer = ref<string>('')
const orderDate = ref<string>('')

const submitOrder = () => {
  console.log('Objednávka odoslaná:', {
    orderNumber: orderNumber.value,
    customer: customer.value,
    orderDate: orderDate.value
  })
}
</script>

<template>
  <div class="order-form">
    <h2 class="form-title">🛒 Nová objednávka</h2>

    <form @submit.prevent="submitOrder" class="form-fields">
      <!-- Číslo objednávky -->
      <div class="form-field">
        <label for="orderNumber" class="form-label">Číslo objednávky</label>
        <input
            id="orderNumber"
            type="text"
            v-model="orderNumber"
            class="form-input"
            placeholder="Zadajte číslo objednávky"
            required
        />
      </div>

      <!-- Meno zákazníka -->
      <div class="form-field">
        <label for="customer" class="form-label">Meno zákazníka</label>
        <input
            id="customer"
            type="text"
            v-model="customer"
            class="form-input"
            placeholder="Zadajte meno zákazníka"
            required
        />
      </div>

      <!-- Dátum objednávky -->
      <div class="form-field">
        <label for="orderDate" class="form-label">Dátum objednávky</label>
        <input
            id="orderDate"
            type="date"
            v-model="orderDate"
            class="form-input"
            required
        />
      </div>

      <!-- Tlačidlo Odoslať -->
      <button
          type="submit"
          class="submit-button"
      >
        Odoslať objednávku
      </button>
    </form>
  </div>
</template>

<style scoped>
.order-form {
  width: 100%;
  max-width: 500px;
  margin: 50px auto;
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

.submit-button {
  padding: 12px;
  background-color: #4caf50;
  color: #fff;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.submit-button:hover {
  background-color: #45a049;
}
</style>
