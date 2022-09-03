import { createRouter, createWebHashHistory } from 'vue-router'
import School from '../components/test/School.vue'
import Ele from '@/components/test/Ele.vue'
import LessTest from '@/components/test/LessTest.vue'
import Axios from '@/components/test/Axios.vue'
const routes = [
  {
    path: '/',
    redirect: '/decetion'
  },
  {
    path: '/decetion',
    component: () => import('@/pages/Decetion.vue')
  },
  {
    path: '/school',
    component: School
  },
  {
    path: '/ele',
    component: Ele
  },
  {
    path: '/less',
    component: LessTest
  },
  {
    path: '/axios',
    component: Axios
  }
  // {
  //   path: '/decetion',
  //   name: 'decetion',
  //   component: () => import('@/views/Decetion.vue')
  // }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
