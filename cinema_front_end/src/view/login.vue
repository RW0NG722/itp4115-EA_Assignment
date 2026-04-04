<template>
  <GlobalHeader />
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
          name="email"
          :rules="[{ required: true, message: 'Please input your email!' }]"
        >
          <a-input
            v-model:value="formState.email"
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
                email: '',
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
            {{ isLocked ? `锁定 (${lockTime}s)` : '登入' }}
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
  import { useUserStore } from '@/modules/store/user'
  import GlobalHeader from './GlobalHeader.vue'

  const bt1act = ref(true)
  const bt2act = ref(false)
  const bt3act = ref(false)

  const resetBtn = () => {
    bt1act.value = false
    bt3act.value = false
    bt2act.value = false
  }

  const user = useUserStore()

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
    email: string
    password: string
    remember: boolean
  }
  const formState = reactive<FormState>({
    email: '',
    password: '',
    remember: true,
  })

  const loginAttempts = ref(0)
  const isLocked = ref(false)
  const lockTime = ref(0)
  let timer: any = null

  const startLockTimer = () => {
    if (timer) clearInterval(timer)
    isLocked.value = true
    lockTime.value = 60
    timer = setInterval(() => {
      lockTime.value -= 1
      if (lockTime.value <= 0) {
        clearInterval(timer)
        timer = null
        isLocked.value = false
        loginAttempts.value = 0
      }
    }, 1000)
  }

  const onFinish = async (values: any) => {
    if (isLocked.value) return
    const success = await user.login(values.email, values.password)
    if (!success) {
      loginAttempts.value += 1
      if (loginAttempts.value >= 3) {
        startLockTimer()
      }
    } else {
      loginAttempts.value = 0
    }
  }

  const onFinishFailed = (errorInfo: any) => {
    console.log('Failed:', errorInfo)
  }
  const disabled = computed(() => {
    return isLocked.value || !(formState.email && formState.password)
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
