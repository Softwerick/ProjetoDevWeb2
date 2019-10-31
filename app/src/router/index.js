import Vue from 'vue'
import Router from 'vue-router'
import Products from '@/components/products/Products'
import Index from '@/components/Index'
 
Vue.use(Router)
 
export default new Router({
 routes: [
   {
     path: '/',
     name: 'Index',
     component: Index
   },   
   {
    path: '/products',
    name: 'Products',
    component: Products
  },
 ]
})
