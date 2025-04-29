import { message } from 'ant-design-vue'
import axios from 'axios'
import { userInfo } from 'os'
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    userInfo:{
      id: '',
      username: '',
      email: '',
      userAge: undefined,
      firstName:'',
      lastName: '',
      gender: '',
      birthDate:'',
      phone:'',
      receiveEmail:'',
      careea:'',
      income:'',
      workArea:'',
      livingArea:''
    },
    userId: '',
    username: '',
    email: '',
    userAge: undefined,
    first_name:'',
    last_name: '',
    gender: '',
    birth_date:'',
    phone:'',
    email_subscription:'',
    occupation:'',
    income_level:'',
    work_location:'',
    residence_location:''
  }),
  getters: {
    getUserInfo: (state) => state,
    getUserName: (state) => state.username,
    getEmail: (state)=> state.email,
    getUserAge: (state) => state.userAge,
    getUserFirstName: (state) => state.first_name,
    getUserLastName: (state) => state.last_name,
    getUserGender: (state) => state.gender,
    getUserBirthDate: (state) => state.birth_date,
    getUserEmailSub: (state) => state.email_subscription,
    getUserOccupation: (state) => state.occupation,
    getUserIncome: (state) => state.income_level,
    getUserWorkLocation: (state) => state.work_location,
    getUserResidenceLocation: (state) => state.residence_location,
  },
  actions: {
    login(email: string, password: string) {
      axios({
        method: 'post',
        url: 'https://upgraded-zebra-69rjq7669x77cr767-5000.app.github.dev/login',
        data: { email, password },
      }).then((res) => {
        const data = res.data
        if(data.code==200){
          console.log(data.data.username)
          this.setUserInfo(data.data)
          message.success("登录成功")
          console.log("oooo",this.getUserInfo)
        }
      })
      
    },
    setUserInfo(userInfo: any) {
      this.userInfo = userInfo
    },
    setUserName(username: string){
      this.username = username
    },

    setToken(token: string | null) {
      this.token = token
    },
  },
})
