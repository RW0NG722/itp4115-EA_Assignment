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
          <template v-for="(item, index) in accountInfoKeys" :key="index">
            <a-row>
              <a-col :span="5" :offset="4">{{ item }}</a-col>
              <a-col :span="5" :offset="4">{{ desc.accountInfo[item] }}</a-col>
            </a-row>
          </template>
          <a-row> Basic Info </a-row>
          <template v-for="(item, index) in basicInfoKeys" :key="index">
            <a-row>
              <a-col :span="5" :offset="4">{{ item }}</a-col>
              <a-col :span="5" :offset="4">{{ desc.basicInfo[item] }}</a-col>
            </a-row>
          </template>
          <a-row> Contact </a-row>
          <template v-for="(item, index) in contactKeys" :key="index">
            <a-row>
              <a-col :span="5" :offset="4">{{ item }}</a-col>
              <a-col :span="5" :offset="4">{{ desc.contact[item] }}</a-col>
            </a-row>
          </template>
          <a-row> Other </a-row>
          <template v-for="(item, index) in otherKeys" :key="index">
            <a-row>
              <a-col :span="5" :offset="4">{{ item }}</a-col>
              <a-col :span="5" :offset="4">{{ desc.other[item] }}</a-col>
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
  import { onMounted, reactive } from 'vue'
  import GlobalHeader from '../GlobalHeader.vue'
import { useUserStore } from '@/modules/store/user'
import dayjs from 'dayjs'

  const desc = reactive({
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
      career: 'career',
      income: 'income',
      workArea: 'workArea',
      livingArea: 'livingArea',
    },
  })

  const user = useUserStore()

  onMounted(()=>{
    const userData = user.getUserInfo
    desc.accountInfo.userName = userData.user_name
    desc.accountInfo.registerDate = dayjs().format('YY-MM-DD')
    desc.basicInfo.birthDate = userData.birth_date
    desc.basicInfo.firstName = userData.first_name
    desc.basicInfo.lastName = userData.last_name
    desc.basicInfo.sex = userData.gender
    desc.contact.email = userData.email
    desc.contact.phone = userData.phone
    desc.contact.receiveEmail = userData.email_subscription
    desc.other.career = userData.occupation
    desc.other.income = userData.income_level
    desc.other.livingArea = userData.residence_location
    desc.other.workArea = userData.work_location
  })

  const accountInfoKeys = Object.keys(desc.accountInfo);
  const basicInfoKeys = Object.keys(desc.basicInfo);
  const contactKeys = Object.keys(desc.contact);
  const otherKeys = Object.keys(desc.other);
</script>
