import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    userName: '',
    userAge: undefined,
  }),
  getters: {
    getUserName: (state) => state.userName,
    getUserAge: (state) => state.userAge,
  },
  actions: {
    setUserInfo(userInfo: any) {
      this.userInfo = userInfo
    },
    setToken(token: string | null) {
      this.token = token
    },
  },
})
