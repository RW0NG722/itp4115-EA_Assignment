<template>
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
      name="username"
      :rules="[{ required: true, message: 'Please input your username!' }]"
    >
      <a-input v-model:value="formState.username" />
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
      name="confirmPassword"
      :rules="[{ required: true, message: 'Please confirm your password!' }]"
    >
      <a-input-password v-model:value="formState.confirmPassword" />
    </a-form-item>

    <Divider />
    基本资料
    <a-form-item
      label="名"
      name="firstName"
      :rules="[{ required: true, message: 'Please input your first name!' }]"
    >
      <a-input v-model:value="formState.firstName" />
    </a-form-item>

    <a-form-item
      label="姓"
      name="lastName"
      :rules="[{ required: true, message: 'Please input your last name!' }]"
    >
      <a-input v-model:value="formState.lastName" />
    </a-form-item>
    <a-form-item label="性别" name="sex">
      <a-radio-group v-model:value="formState.sex">
        <a-radio :value="'男'">男</a-radio>
        <a-radio :value="'女'">女</a-radio>
      </a-radio-group>
    </a-form-item>
    <a-form-item label="出生日期" name="birthDate">
      <DatePicker v-model:value="birthDate" />
    </a-form-item>

    <Divider />
    联络资料
    <a-form-item
      label="手提电话"
      name="phone"
      :rules="[{ required: true, message: 'Please input your phone number!' }]"
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
      name="confirmEmail"
      :rules="[{ required: true, message: 'Please confirm your email!' }]"
    >
      <a-input v-model:value="formState.confirmEmail" />
    </a-form-item>
    <a-form-item
      label="接受电子宣传邮件"
      name="receiveEmail"
      :rules="[
        {
          required: true,
          message: 'Which method do you want to receive our email?',
        },
      ]"
    >
      <a-radio-group v-model:value="formState.receiveEmail">
        <a-radio :value="1">是(中文)</a-radio>
        <a-radio :value="2">是(英文)</a-radio>
        <a-radio :value="3">否</a-radio>
      </a-radio-group>
    </a-form-item>

    <Divider />
    其他资料
    <a-form-item label="职业" name="cereer">
      <a-cascader
        v-model:value="formState.cereer"
        :options="cereer"
        placeholder="Please select"
      />
    </a-form-item>

    <a-form-item label="入息" name="income">
      <a-cascader
        v-model:value="formState.income"
        :options="income"
        placeholder="Please select"
      />
    </a-form-item>
    <a-form-item label="工作地区" name="workArea">
      <a-cascader
        v-model:value="formState.workArea"
        :options="area"
        placeholder="Please select"
      />
    </a-form-item>
    <a-form-item label="居住地区" name="livingArea">
      <a-cascader
        v-model:value="formState.livingArea"
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
</template>
<script lang="ts" setup>
  import { DatePicker, Divider, message } from 'ant-design-vue'
  import { Dayjs } from 'dayjs'
  import { reactive, ref, watch } from 'vue'
  import axios from 'axios'

  interface FormState {
    username: string
    password: string
    confirmPassword: string
    firstName: string
    lastName: string
    sex: string
    birthDate: string
    phone: string
    email: string
    confirmEmail: string
    receiveEmail: number
    cereer: string
    income: string
    workArea: string
    livingArea: string
  }

  const birthDate = ref<Dayjs>()

  watch(birthDate, (newVal) => {
    if (newVal) {
      formState.birthDate = newVal.format('YYYY-MM-DD')
    } else {
      formState.birthDate = ''
    }
  })

  const formState = reactive<FormState>({
    username: '1',
    password: '2',
    confirmPassword: '3',
    firstName: '4',
    lastName: '5',
    sex: '1',
    birthDate: '',
    phone: '1',
    email: '1',
    confirmEmail: '1',
    receiveEmail: 1,
    cereer: '',
    income: '',
    workArea: '',
    livingArea: '',
  })

  const validateForm = () => {
    const { password, confirmPassword } = formState
    if (password !== confirmPassword) {
      message.error('两次输入的密码不一致')
      return false
    }
    return true
  }

  const onSubmit = () => {
    console.log('submit', formState)
  }
  const onFinish = (values: any) => {
    if (validateForm()) {
      return
    }
    // axios.post('http://localhost:5173/api/test', values).then((res) => {
    //   if (res.status === 200) {
    //     message.success('注册成功')
    //   } else {
    //     message.error('注册失败')
    //   }
    // })
    axios({
      method: 'post',
      url: 'http://localhost:5173/api/test',
      data: values,
    })
      .then((response) => {
        console.log('Response:', response.data)
        message.success('注册成功')
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
