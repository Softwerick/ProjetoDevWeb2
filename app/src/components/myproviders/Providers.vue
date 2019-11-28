<template>
 <section>
     <Header />
   <b-container>
   <h1>Fornecedores</h1>
   <div v-for="provider in providers" v-bind:key="provider.id">
    <h2>{{provider.name}}</h2>
   </div>
  <b-button @click="AddProvider">Adicionar novo fornecedor</b-button>
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
   providers: [],
  }
 },
 created() {
  this.all();
 },
 methods: {
     AddProvider(){
         router.push('/providers/add')
     },
  all () {
   axios.request({
    baseURL: 'http://localhost:8000',
    method: 'get',
    url: '/api/provider/'
   }).then( response => {
     this.providers = response.data
   });
  },
 }
}
</script>

<style>

</style>