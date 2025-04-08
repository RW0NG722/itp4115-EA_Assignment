import { createWebHashHistory, createRouter } from 'vue-router'

const routes = [
  {
    name: 'index',
    path: '/index',
    component: () => import('@/view/index.vue'),
  },
  {
    name: 'login',
    path: '/login',
    component: () => import('@/view/login.vue'),
  },
  {
    name: 'register',
    path: '/register',
    component: () => import('@/view/register.vue'),
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router
