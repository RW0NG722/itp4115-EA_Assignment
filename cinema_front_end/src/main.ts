import { createApp } from 'vue'
import App from './App.vue'
// import 'ant-design-vue/dist/reset.css'
import router from './modules/router/router'
import { createPinia } from 'pinia'
import './style.css'

const pinia = createPinia()
const app = createApp(App)

app.use(pinia)
app.use(router)
app.mount('#app')
