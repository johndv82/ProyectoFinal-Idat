import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../components/LoginModal.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('../components/RegisterModal.vue')
  },
  {
    path: '/carrito',
    name: 'Carrito',
    component: () => import('../views/Carrito.vue')
  },
  {
    path: '/pedidos',
    name: 'Pedidos',
    component: () => import('../views/Pedidos.vue')
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
