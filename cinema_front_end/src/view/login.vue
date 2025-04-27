<template>
  <Row class="ml-10 mr-10">
    <Col :span="12" class="overflow-hidden">
      <img
        class="imgcss"
        src="https://mediafiles.cinema.com.hk/broadway/cmsimg/cinweb/webcms/images/4de53d9a3e9e189067c21a0d6a79e5de_1679394119.jpg"
        alt=""
      />
    </Col>
    <Col :span="8" :offset="2" align="center">
      <div class="flex justify-between mt-20 mb-5 mr-26 ml-12">
        <Space size="large">
          <a-button
            :type="bt1act ? 'primary' : 'default'"
            @click="switchLoginMode(1)"
          >
            会员登陆1
          </a-button>
          <a-button
            :type="bt2act ? 'primary' : 'default'"
            @click="switchLoginMode(2)"
          >
            会员登陆2
          </a-button>
          <a-button
            :type="bt3act ? 'primary' : 'default'"
            @click="switchLoginMode(3)"
          >
            会员登陆3
          </a-button>
        </Space>
      </div>
      <a-form
        :model="formState"
        name="normal_login"
        class="login-form"
        @finish="onFinish"
        @finishFailed="onFinishFailed"
      >
        <a-form-item
          name="username"
          :rules="[{ required: true, message: 'Please input your username!' }]"
        >
          <a-input
            v-model:value="formState.username"
            placeholder="用户名称/电子邮件"
          >
            <template #prefix>
              <UserOutlined class="site-form-item-icon" />
            </template>
          </a-input>
        </a-form-item>

        <a-form-item
          name="password"
          :rules="[{ required: true, message: 'Please input your password!' }]"
        >
          <a-input-password
            v-model:value="formState.password"
            placeholder="密码"
          >
            <template #prefix>
              <LockOutlined class="site-form-item-icon" />
            </template>
          </a-input-password>
        </a-form-item>

        <a-form-item>
          <a href="#">忘记密码</a>
        </a-form-item>

        <a-form-item class="mt-6">
          <a-button
            type="primary"
            class="login-form-button mr-5"
            @click="
              formState = {
                username: '',
                password: '',
                remember: true,
              }
            "
          >
            重置
          </a-button>
          <a-button
            :disabled="disabled"
            type="primary"
            html-type="submit"
            class="login-form-button ml-5"
          >
            登入
          </a-button>
        </a-form-item>

        <a-form-item>
          <a-form-item name="remember" no-style>
            <a-checkbox v-model:checked="formState.remember"
              >Remember me</a-checkbox
            >
          </a-form-item>
          <a class="login-form-forgot" href="">Forgot password</a>
        </a-form-item>
      </a-form>

      <a-button type="primary" class="ml-5">
        <template #icon>
          <FacebookOutlined style="all: initial" />
        </template>
        FaceBook登入
      </a-button>
      <br />
      (Facebook登入只適用於cinema.com.hk會員)
      <br />
      ---------- 或 ----------
      <br />
      <a-button
        type="primary"
        html-type="submit"
        class="login-form-button ml-5"
        danger
        @click="router.push('/register')"
      >
        成为会员
      </a-button>
    </Col>
  </Row>
</template>
<script lang="ts" setup>
  import { reactive, computed } from 'vue'
  import Icon, {
    UserOutlined,
    LockOutlined,
    FacebookOutlined,
  } from '@ant-design/icons-vue'
  import { Row, Col, Space } from 'ant-design-vue'
  import { ref } from 'vue'
  import router from '@/modules/router/router'

  const bt1act = ref(true)
  const bt2act = ref(false)
  const bt3act = ref(false)

  const resetBtn = () => {
    bt1act.value = false
    bt3act.value = false
    bt2act.value = false
  }

  const switchLoginMode = (mode: number) => {
    resetBtn()
    // change api
    if (mode === 1) {
      bt1act.value = true
    } else if (mode === 2) {
      bt2act.value = true
    } else {
      bt3act.value = true
    }
  }

  interface FormState {
    username: string
    password: string
    remember: boolean
  }
  const formState = reactive<FormState>({
    username: '',
    password: '',
    remember: true,
  })
  function onChange() {
    console.log('formState', formState)
  }

  const onFinish = (values: any) => {
    console.log('Success:', values)
  }

  const onFinishFailed = (errorInfo: any) => {
    console.log('Failed:', errorInfo)
  }
  const disabled = computed(() => {
    return !(formState.username && formState.password)
  })
</script>
<style scoped>
  #components-form-demo-normal-login .login-form {
    max-width: 300px;
  }
  #components-form-demo-normal-login .login-form-forgot {
    float: right;
  }

  .imgcss {
    width: 100%;
  }
</style>
