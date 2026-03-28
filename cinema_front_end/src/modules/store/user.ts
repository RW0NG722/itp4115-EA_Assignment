import { message } from 'ant-design-vue'
import axios from 'axios'
import { defineStore } from 'pinia'
import router from '../router/router'

export const useUserStore = defineStore('user', {
  state: () => ({
    userInfo: {
      user_id: '',
      user_name: '',
      email: '',
      user_age: undefined,
      first_name: '',
      last_name: '',
      gender: '',
      birth_date: '',
      phone: '',
      email_subscription: '',
      occupation: '',
      income_level: '',
      work_location: '',
      residence_location: '',
    },
  }),
  getters: {
    getUserInfo: (state) => state.userInfo,
  },
  actions: {
    login(email: string, password: string) {
      return axios({
        method: 'post',
        // url: 'https://upgraded-zebra-69rjq7669x77cr767-5000.app.github.dev/login',
        url: 'http://localhost:5000/login',
        // url: 'http://54.174.200.10:35123/login',
        data: { email, password },
      })
        .then((res) => {
          const data = res.data
          if (data.code == 200) {
            console.log(data.data.user_name)
            this.setUserInfo(data.data)
            message.success('登录成功')
            router.push('/')
            return true
          } else {
            message.error(data.message || '登录失败')
            return false
          }
        })
        .catch((err) => {
          console.error(err)
          message.error('网络错误，请稍后重试')
          return false
        })
    },
    setUserInfo(userInfo: any) {
      this.userInfo = userInfo
    },
    setUserName(username: string) {
      this.username = username
    },

    setToken(token: string | null) {
      this.token = token
    },
  },
})
