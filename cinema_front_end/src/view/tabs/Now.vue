<template>
  <div class="w-[747px] h-[870px]" align="center">
    <Row :justify="'space-between'" class="pl-5 pr-5" v-for="i in 3">
      <Col class="w-[170px] h-[230px] bg-red-500 mb-3" v-for="j in 4">
        test{{ i }} - {{ j }}
      </Col>
    </Row>
    <div class="w-[95%] text-3xl bg-yellow-50 pt-2 pb-2">更多电影</div>
  </div>
</template>
<script setup lang="ts">
  import { Card, Col, Row } from 'ant-design-vue'

  console.log('script')
</script>
<style></style>
