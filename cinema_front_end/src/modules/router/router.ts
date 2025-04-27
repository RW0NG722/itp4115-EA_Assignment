import { createWebHashHistory, createRouter } from 'vue-router'

const routes = [
  {
    // 首页
    name: 'index',
    path: '/',
    component: () => import('@/view/index.vue'),
  },
  // {
  //   // 首页
  //   name: 'index',
  //   path: '/index',
  //   component: () => import('@/view/index.vue'),
  // },
  {
    // 登录页
    name: 'login',
    path: '/login',
    component: () => import('@/view/login.vue'),
  },
  {
    // 注册页
    name: 'register',
    path: '/register',
    component: () => import('@/view/register.vue'),
  },
  {
    // 注册页, 选择注册
    name: 'signup',
    path: '/signup',
    component: () => import('@/view/register.vue'),
  },
  {
    name: 'detail',
    path: '/detail',
    component: () => import('@/view/movieDetail.vue'),
  },
  {
    name: 'special',
    path: '/special',
    component: () => import('@/view/register.vue'),
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router
