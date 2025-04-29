<template>
  <GlobalHeader />
  <div class="w-[100%] h-[100%]">
    <a-space class="ml-[15%]">
      <div class="w-[210px] h-[110px]">
        <a href="#/">
          <img src="/src/assets/index_logo.png" />
        </a>
      </div>
      <div class="w-[610px] h-[90px] border">广告位招租</div>
    </a-space>
    <div class="ml-50 mr-60 h-150 border">
      <a-row>
        <a-col :span="17" class="h-100">
          <a-row> 用户资料 </a-row>
          <a-row>
            <a-col :offset="4">用户名称</a-col>
            <a-col :offset="4">{{ 'userInfo' }}</a-col>
          </a-row>
          <template v-for="(item, index) in disc" :key="index">
            <a-row>
              <a-col :offset="4">{{ item }}</a-col>
              <a-col :offset="4">{{ 'userInfo' }}</a-col>
            </a-row>
          </template>
        </a-col>
        <a-col :span="1">
          <a-divider type="vertical" style="height: 90%" />
        </a-col>
        <a-col :span="6">
          <a-button type="primary" class="w-[90%] mb-3 mt-5">更改资料</a-button>
          <a-button type="primary" class="w-[90%]">修改密码</a-button>
        </a-col>
      </a-row>
    </div>
  </div>
</template>
<script lang="ts" setup>
  import { reactive } from 'vue'
  import GlobalHeader from '../GlobalHeader.vue'

  const disc = reactive({
    accountInfo: {
      userName: 'userName',
      registerDate: 'registerDate',
    },
    basicInfo: {
      firstName: 'firstName',
      lastName: 'lastName',
      sex: 'sex',
      birthDate: 'birthDate',
    },
    contact: {
      phone: 'phone',
      email: 'email',
      receiveEmail: 'receiveEmail',
    },
    other: {
      cereer: 'cereer',
      income: 'income',
      workArea: 'workArea',
      livingArea: 'livingArea',
    },
  })
</script>
