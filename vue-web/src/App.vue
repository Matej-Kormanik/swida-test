<script setup lang="ts">
    import OrderList from "@/components/OrderList.vue";
    import OrderForm from "@/components/OrderForm.vue";
</script>

<!-- ----------------------------------------------------------------------- -->

<template>
  <h1>Order management system</h1>
  <main>
    <OrderList />
    <OrderForm />
  </main>


</template>

<!-- ----------------------------------------------------------------------- -->


<style scoped>
  main {
    max-width: 80vw;
    margin: 2rem auto;
  }
  h1 {
    text-align: center;
    margin-bottom: 3rem;
  }

</style>
