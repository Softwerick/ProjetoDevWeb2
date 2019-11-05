<template>
 <section>
     <Header />
  <div> 
   <h1>Produtos</h1>
  </div>
  <div v-for="product in products" v-bind:key="product.id">
   <p>{{product.name}}</p>
   <p>{{product.author}}</p>
   <p>{{product.description}}</p>
   <b-btn class="red" @click="deleteProduct(product)">
    Apagar
   </b-btn>
   <hr>
  </div>
  <b-button @click="AddBook">Adicionar novo produto</b-button>
 </section>
</template>
<script>
import axios from 'axios'
import router from '@/router'
import Header from '@/components/Header'

export default {
 name: 'Products',
 components: {Header},
 data() {
  return {
   products: [],
  }
 },
 created() {
  this.all();
 },
 methods: {
     AddBook(){
         router.push('/products/add')
     },
  all () {
   axios.request({
    baseURL: 'http://localhost:8000',
    method: 'get',
    url: '/api/product/'
   }).then( response => {
     this.products = response.data
   });
  },
  deleteProduct(product) {
   if (confirm('Excluir ' + product.name)) {
    axios.delete(
     `http://localhost:8000/api/product/${product.id}`,
     {
      headers: {
       'Authorization': `Token ${this.$session.get("token")}`
      }
     }
    ).then ( response => {
     this.all()
     this.log.console(response)
    })
   }
  },
 }
}
</script>
