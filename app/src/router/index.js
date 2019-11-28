import Vue from 'vue'
import Router from 'vue-router'
import Products from '@/components/products/Products'
import Index from '@/components/Index'
import AddProducts from '@/components/products/AddProducts'
import EditProducts from '@/components/products/EditProducts'
import Providers from '@/components/myproviders/Providers'
import AddProvider from '@/components/myproviders/AddProvider'
 
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
  {
    path: '/products/add',
    name: 'AddProducts',
    component: AddProducts
  },
  {
    path: '/products/edit/:id',
    name: 'EditProducts',
    component: EditProducts
  },
  {
    path: '/providers',
    name: 'Providers',
    component: Providers
  },
  {
    path: '/providers/add',
    name: 'AddProviders',
    component: AddProvider
  },
 ]
})
