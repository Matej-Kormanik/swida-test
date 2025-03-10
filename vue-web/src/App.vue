<script setup lang="ts">
    import OrderList from "@/components/OrderList.vue";
    import OrderForm from "@/components/OrderForm.vue";
    import {ref} from "vue";

    const refreshTrigger = ref(0)

    const refreshOrders = () => {
      refreshTrigger.value++;
    }
</script>

<!-- ----------------------------------------------------------------------- -->

<template>
  <h1>Order management system</h1>
  <main>
    <OrderList :refresh="refreshTrigger"/>
    <OrderForm @orderCreated="refreshOrders"/>
  </main>


</template>

<!-- ----------------------------------------------------------------------- -->


<style scoped>
  main {
    max-width: 1280px;
    margin: 2rem auto;
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

</style>
