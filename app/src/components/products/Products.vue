<template>
 <section>
     <Header />
   <b-container>
   <h1>Produtos</h1>
   <table style="width:100%">
     <tr>
       <th>Nome</th>
       <th>Peso</th>
       <th>Preço</th>
       <th>Quantidade em estoque</th>
       <th>Editar</th>
       <th>Excluir</th>
     </tr>
     <tr v-for="product in products" v-bind:key="product.id">
       <td>{{product.name}}</td>
       <td>{{product.weight}}</td>
       <td>{{product.price}}</td>
       <td>{{product.stock}}</td>
       <td @click="editProduct(product)"><i class="fas fa-pen icone"></i></td>
       <td @click="deleteProduct(product)"><i class="fas fa-times icone"></i></td>
     </tr>
   </table>
  <b-button @click="AddProduct">Adicionar novo produto</b-button>
  </b-container>
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
     AddProduct(){
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
  editProduct(product){
    router.push(`/products/edit/${product.id}`)
  }
 }
}
</script>

<style>
table{
	margin-top: 30px;
	margin-bottom: 30px;
	text-align: center;
	border: 2px solid black;
}
table *{
	border: 2px solid black;
}
.icone{
  border: none;
}
</style>