<template>
    <div>
        <Header />
        <b-container class="container">
            <b-row>
                <b-col></b-col>
                <b-col>
                    <h2>Adicionar um produto</h2>
                    <b-form-input placeholder="Nome do produto" v-model="product.name" class="form"></b-form-input>
                    <b-form-input type="number" placeholder="Peso do produto" v-model="product.weight" class="form"></b-form-input>
                    <b-form-input type="number" placeholder="Preço do produto" v-model="product.price" class="form"></b-form-input>
                    <b-form-input type="number" placeholder="Quantidade em estoque" v-model="product.stock" class="form"></b-form-input>
                    <b-form-select v-model="selected" multiple class="form">
                        <option v-for="provider in providers" :key="provider.id" :value="provider.id" @click="addProvider(provider.id)">{{ provider.name }}</option>
                    </b-form-select>
                    <b-button @click="add" class="form" variant="primary" block>Adicionar produto</b-button>                      
                </b-col>
                <b-col></b-col>
            </b-row>
        </b-container>
    </div>
</template>


<script>
import Header from '@/components/Header'
import router from '@/router'
import axios from 'axios'
export default {
    components: {Header},
    created(){
        this.getProviders()
    },
    data(){
        return{
            product: {},
            providers: [],
            selected: [],
            productprovider: []
        }
    },
    methods: {
        addProvider(pid){
            this.productprovider.push(pid)

        },
        add(){
            this.product.providers = this.productprovider
            axios.post("http://localhost:8000/api/product/add/", this.product, {
                headers: {
                    Authorization: `Token ${this.$session.get("token")}`
                }
            }).then(response => {
                router.push('/products')
                alert(response)
            }).catch(e =>{
                alert(e)
            })
        },

        getProviders(){
            axios.request({
                baseURL: "http://localhost:8000",
                method: "get",
                url: "/api/provider/"
            }).then(response => {
                this.providers = response.data
            });
        }
    }
}
</script>


<style>
.container{
    margin-top: 4%;
    text-align: center;
}
.form{
    margin-top: 3%;
}
</style>