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
      :rules="[{ required: true, message: 'Please input your password!' }]"
    >
      <a-input-password v-model:value="formState.password" />
    </a-form-item>

    <Divider />
    基本资料
    <a-form-item
      label="名"
      name="firstName"
      :rules="[{ required: true, message: 'Please input your username!' }]"
    >
      <a-input v-model:value="formState.username" />
    </a-form-item>

    <a-form-item
      label="姓"
      name="lastName"
      :rules="[{ required: true, message: 'Please input your password!' }]"
    >
      <a-input-password v-model:value="formState.password" />
    </a-form-item>
    <a-form-item label="性别" name="sex">
      <a-radio-group v-model:value="formState.remember">
        <a-radio :value="1">男</a-radio>
        <a-radio :value="2">女</a-radio>
      </a-radio-group>
    </a-form-item>
    <a-form-item label="出生日期" name="birthDate">
      <DatePicker />
    </a-form-item>

    <Divider />
    联络资料
    <a-form-item
      label="手提电话"
      name="phone"
      :rules="[{ required: true, message: 'Please input your username!' }]"
    >
      <a-input v-model:value="formState.username" />
    </a-form-item>

    <a-form-item
      label="电邮"
      name="email"
      :rules="[{ required: true, message: 'Please input your password!' }]"
    >
      <a-input-password v-model:value="formState.password" />
    </a-form-item>
    <a-form-item
      label="确定电邮"
      name="confirmEmail"
      :rules="[{ required: true, message: 'Please input your password!' }]"
    >
      <a-input-password v-model:value="formState.password" />
    </a-form-item>
    <a-form-item
      label="接受电子宣传邮件"
      name="receiveEmail"
      :rules="[{ required: true, message: 'Please input your password!' }]"
    >
      <a-radio-group v-model:value="value">
        <a-radio :value="1">是(中文)</a-radio>
        <a-radio :value="2">是(英文)</a-radio>
        <a-radio :value="3">否</a-radio>
      </a-radio-group>
    </a-form-item>

    <Divider />
    其他资料
    <a-form-item
      label="职业"
      name="cereer"
      :rules="[{ required: true, message: 'Please input your username!' }]"
    >
      <a-cascader
        v-model:value="value"
        :options="cereer"
        placeholder="Please select"
      />
    </a-form-item>

    <a-form-item
      label="入息"
      name="income"
      :rules="[{ required: true, message: 'Please input your password!' }]"
    >
      <a-cascader
        v-model:value="value"
        :options="income"
        placeholder="Please select"
      />
    </a-form-item>
    <a-form-item
      label="工作地区"
      name="workArea"
      :rules="[{ required: true, message: 'Please input your password!' }]"
    >
      <a-cascader
        v-model:value="value"
        :options="area"
        placeholder="Please select"
      />
    </a-form-item>
    <a-form-item
      label="居住地区"
      name="livingArea"
      :rules="[{ required: true, message: 'Please input your password!' }]"
    >
      <a-cascader
        v-model:value="value"
        :options="area"
        placeholder="Please select"
      />
    </a-form-item>

    <a-form-item :wrapper-col="{ offset: 2, span: 16 }">
      <a-button type="primary" html-type="submit">Submit</a-button>
    </a-form-item>
  </a-form>
</template>
<script lang="ts" setup>
  import { DatePicker, Divider } from 'ant-design-vue'
  import { reactive } from 'vue'

  interface FormState {
    username: string
    password: string
    remember: boolean
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

  const formState = reactive<FormState>({
    username: '',
    password: '',
    remember: true,
  })
  const onFinish = (values: any) => {
    console.log('Success:', values)
  }

  const onFinishFailed = (errorInfo: any) => {
    console.log('Failed:', errorInfo)
  }
</script>
