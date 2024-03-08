import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'login',
    meta: {
      title: '登录页'
    },
    component: () => import('@/views/login')
  },
  {
    path: '/',
    name: 'index',
    meta: {
      title: '订阅管理系统'
    },
    component: () => import('@/views/index')
  },
  {
    path: '/url/:name?',
    name: 'url',
    meta: {
      title: '订阅查看'
    },
    component: () => import('@/views/url')
  }
]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})
router.beforeEach((to, from, next) => {
  document.title = to.meta.title
  const token = JSON.parse(localStorage.getItem('token'))
  if (to.path !== '/login' && !token) { // 判断是否登录
    router.push('/login') // 如果没登录直接跳回登录页
  }
  next()
})

export default router
