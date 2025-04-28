import axios from 'axios'
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    userName: '',
    userAge: undefined,
  }),
  getters: {
    getUserInfo: (state) => state,
    getUserName: (state) => state.userName,
    getUserAge: (state) => state.userAge,
  },
  actions: {
    login(userName: string, password: string) {
      axios({
        method: 'post',
        url: '/api/login',
        data: { userName, password },
      })
      // if success
      this.userName = userName
      this.userAge = 18
    },
    setUserInfo(userInfo: any) {
      this.userInfo = userInfo
    },
    setToken(token: string | null) {
      this.token = token
    },
  },
})
