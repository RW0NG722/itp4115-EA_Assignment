<template>
  <div>
    <GlobalHeader />
    <a-form
      :model="formState"
      name="basic"
      labelAlign="left"
      :label-col="{ span: 3, offset: 1 }"
      :wrapper-col="{ span: 16 }"
      autocomplete="off"
      @finish="onFinish"
      @finishFailed="onFinishFailed"
    >
      账户资料
      <a-form-item
        label="用户名"
        name="user_name"
        :rules="[{ required: true, message: 'Please input your username!' }]"
      >
        <a-input v-model:value="formState.user_name" />
      </a-form-item>

      <a-form-item
        label="密码"
        name="password"
        :rules="[{ required: true, message: 'Please input your password!' }]"
      >
        <a-input-password v-model:value="formState.password" />
      </a-form-item>
      <a-form-item
        label="重新输入密码"
        name="confirm_password"
        :rules="[{ required: true, message: 'Please confirm your password!' }]"
      >
        <a-input-password v-model:value="formState.confirm_password" />
      </a-form-item>

      <Divider />
      基本资料
      <a-form-item
        label="名"
        name="first_name"
        :rules="[{ required: true, message: 'Please input your first name!' }]"
      >
        <a-input v-model:value="formState.first_name" />
      </a-form-item>

      <a-form-item
        label="姓"
        name="last_name"
        :rules="[{ required: true, message: 'Please input your last name!' }]"
      >
        <a-input v-model:value="formState.last_name" />
      </a-form-item>
      <a-form-item label="性别" name="gender">
        <a-radio-group v-model:value="formState.gender">
          <a-radio :value="'男'">男</a-radio>
          <a-radio :value="'女'">女</a-radio>
        </a-radio-group>
      </a-form-item>
      <a-form-item label="出生日期" name="birth_date">
        <DatePicker v-model:value="birth_date" />
      </a-form-item>

      <Divider />
      联络资料
      <a-form-item
        label="手提电话"
        name="phone"
        :rules="[
          { required: true, message: 'Please input your phone number!' },
        ]"
      >
        <a-input v-model:value="formState.phone" />
      </a-form-item>

      <a-form-item
        label="电邮"
        name="email"
        :rules="[{ required: true, message: 'Please input your email!' }]"
      >
        <a-input v-model:value="formState.email" />
      </a-form-item>
      <a-form-item
        label="确定电邮"
        name="confirm_email"
        :rules="[{ required: true, message: 'Please confirm your email!' }]"
      >
        <a-input v-model:value="formState.confirm_email" />
      </a-form-item>
      <a-form-item
        label="接受电子宣传邮件"
        name="email_subscription"
        :rules="[
          {
            required: true,
            message: 'Which method do you want to receive our email?',
          },
        ]"
      >
        <a-radio-group v-model:value="formState.email_subscription">
          <a-radio :value="1">是(中文)</a-radio>
          <a-radio :value="2">是(英文)</a-radio>
          <a-radio :value="3">否</a-radio>
        </a-radio-group>
      </a-form-item>

      <Divider />
      其他资料
      <a-form-item label="职业" name="occupation">
        <a-cascader
          v-model:value="formState.occupation"
          :options="cereer"
          placeholder="Please select"
        />
      </a-form-item>

      <a-form-item label="入息" name="income_level">
        <a-cascader
          v-model:value="formState.income_level"
          :options="income"
          placeholder="Please select"
        />
      </a-form-item>
      <a-form-item label="工作地区" name="work_location">
        <a-cascader
          v-model:value="formState.work_location"
          :options="area"
          placeholder="Please select"
        />
      </a-form-item>
      <a-form-item label="居住地区" name="residence_location">
        <a-cascader
          v-model:value="formState.residence_location"
          :options="area"
          placeholder="Please select"
        />
      </a-form-item>

      <a-form-item :wrapper-col="{ offset: 2, span: 16 }">
        <a-button type="primary" html-type="submit" @click="onSubmit"
          >Submit</a-button
        >
      </a-form-item>
    </a-form>
  </div>
</template>
<script lang="ts" setup>
  import { DatePicker, Divider, message } from 'ant-design-vue'
  import { Dayjs } from 'dayjs'
  import { reactive, ref, watch } from 'vue'
  import axios from 'axios'
  import GlobalHeader from './GlobalHeader.vue'
  import router from '@/modules/router/router'

  interface FormState {
    user_name: string
    password: string
    confirm_password: string
    first_name: string
    last_name: string
    gender: string
    birth_date: string
    phone: string
    email: string
    confirm_email: string
    email_subscription: number
    occupation: string
    income_level: string
    work_location: string
    residence_location: string
  }

  const birth_date = ref<Dayjs>()

  watch(birth_date, (newVal) => {
    if (newVal) {
      formState.birth_date = newVal.format('YYYY-MM-DD')
    } else {
      formState.birth_date = ''
    }
  })

  const formState = reactive<FormState>({
    user_name: '1',
    password: '1234',
    confirm_password: '1234',
    first_name: '4',
    last_name: '5',
    gender: '1',
    birth_date: '',
    phone: '1',
    email: '1',
    confirm_email: '1',
    email_subscription: 1,
    occupation: '',
    income_level: '',
    work_location: '',
    residence_location: '',
  })

  const validateForm = () => {
    const { password, confirm_password } = formState
    if (password !== confirm_password) {
      message.error('两次输入的密码不一致')
      return false
    }
    return true
  }

  const onSubmit = () => {
    console.log('submit', formState)
  }
  const onFinish = (values: any) => {
    if (!validateForm()) {
      return
    }
    axios({
      method: 'post',
      url: 'http://192.168.21.129:8088/signup',
      data: {
        ...values,
        income_level: formState.income_level[0],
        occupation: formState.occupation[0],
        residence_location:
          formState.residence_location[0] +
          '-' +
          formState.residence_location[1],
        work_location:
          formState.work_location[0] + '-' + formState.work_location[1],
      },
    })
      .then((response) => {
        console.log('Response:', response.data)
        message.success('注册成功')
        router.push('/login')
      })
      .catch((error) => {
        console.error('Error:', error)
        message.error('注册失败')
      })
    console.log('Success:', values)
  }

  const onFinishFailed = (errorInfo: any) => {
    console.log('Failed:', errorInfo)
  }

  const cereer = [
    {
      value: 'teacher',
      label: '教师',
    },
    {
      value: 'doctor',
      label: '医生',
    },
    {
      value: 'engineer',
      label: '工程师',
    },
  ]
  const income = [
    {
      value: 'low',
      label: '$5000以下',
    },
    {
      value: 'middle',
      label: '$5001-$10000',
    },
    {
      value: 'high',
      label: '$10001以上',
    },
  ]
  const area = [
    {
      value: 'hongkong',
      label: '香港区',
      children: [
        {
          value: 'central',
          label: '中西区',
        },
        {
          value: 'east',
          label: '东区',
        },
        {
          value: 'south',
          label: '南区',
        },
        {
          value: 'wanchai',
          label: '湾仔',
        },
      ],
    },
    {
      value: 'kowloon',
      label: '九龙区',
      children: [
        {
          value: 'kowlooncity',
          label: '九龙',
        },
        {
          value: 'guantang',
          label: '观塘',
        },
        {
          value: 'ssb',
          label: '深水埗',
        },
        {
          value: 'hdx',
          label: '黄大仙',
        },
        {
          value: 'yjw',
          label: '油尖旺',
        },
      ],
    },
    {
      value: 'newterritories',
      label: '新界区',
      children: [
        {
          value: 'tuenmun',
          label: '屯门',
        },
        {
          value: 'yuenlong',
          label: '元朗',
        },
        {
          value: 'chuenwan',
          label: '荃湾',
        },
        {
          value: 'xt',
          label: '西田',
        },
      ],
    },
  ]
</script>
