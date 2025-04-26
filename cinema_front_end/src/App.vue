<template>
  <!-- <p class="text-3xl underline mb-4">
    <strong>Current route path:</strong> {{ $route.fullPath }}
  </p>
  <Button :type="type1" @click="handleLogin" class="mr-6"> Login </Button>
  <Button :type="type2" @click="handleIndex"> Index </Button> -->
  <main class="mt-4">
    <RouterView />
  </main>
</template>

<script setup lang="ts">
  import { Button, Calendar } from 'ant-design-vue'
  import { ButtonType } from 'ant-design-vue/es/button'
  import { ref } from 'vue'
  import router from './modules/router/router'
  const type1 = ref<ButtonType>('primary')
  const type2 = ref<ButtonType>('default')

  const handleLogin = () => {
    type1.value = 'primary'
    type2.value = 'default'
    router.push('/login')
  }

  const handleIndex = () => {
    type1.value = 'default'
    type2.value = 'primary'
    router.push('/index')
  }
</script>
