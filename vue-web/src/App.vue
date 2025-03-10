<script setup lang="ts">
    import OrderList from "@/components/OrderList.vue";
    import OrderForm from "@/components/OrderForm.vue";
    import {ref} from "vue";

    const refreshTrigger = ref(0)
    const showBanner = ref(false);

    const refreshOrders = () => {
      refreshTrigger.value++;
      showBanner.value = true; // Zobrazíme banner

      // Skryť banner po 3 sekundách
      setTimeout(() => {
        showBanner.value = false;
      }, 3000);
    }
</script>

<!-- ----------------------------------------------------------------------- -->

<template>
  <h1>Order management system</h1>
  <div v-if="showBanner" class="banner">✅ Order successfully created!</div>



  <main>
    <OrderList :refresh="refreshTrigger"/>
    <OrderForm @orderCreated="refreshOrders"/>
  </main>


</template>

<!-- ----------------------------------------------------------------------- -->


<style scoped>
  main {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: space-between;
  }
  h1 {
    text-align: center;
    margin-bottom: 3rem;
    padding-top: 2.6rem;
    font-weight: 500;
  }
  .banner {
    background-color: #4caf50;
    color: white;
    padding: 10px;
    margin: 10px 0;
    text-align: center;
    border-radius: 5px;
    font-weight: bold;
    transition: opacity 0.5s;
  }

</style>
