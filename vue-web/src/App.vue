<script setup lang="ts">
    import OrderList from "@/components/OrderList.vue";
    import OrderForm from "@/components/OrderForm.vue";
    import {ref} from "vue";
    import Banner from "@/ui/Banner.vue";

    const refreshTrigger = ref(0)
    const bannerMsg = ref<string|undefined>();

    const createOrderHandler = (msg: string) => {
      refreshTrigger.value++;
      bannerMsg.value = msg;
      setTimeout(() => {
        bannerMsg.value = undefined;
      }, 3000);
    }
</script>

<!-- ----------------------------------------------------------------------- -->

<template>
  <h1>Order management system</h1>
  <Banner v-if="bannerMsg" :msg="bannerMsg"/>

  <main>
    <OrderList :refresh="refreshTrigger"/>
    <OrderForm @createOrder="createOrderHandler"/>
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
</style>
