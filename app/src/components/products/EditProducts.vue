<template>
    <div>
        <Header />
        <b-container class="container">
            <b-row>
                <b-col></b-col>
                <b-col>
                    <h2>Editar produto</h2>
                    <label>Nome do Produto</label>
                    <b-form-input :placeholder="product.name" v-model="product.name" class="form"></b-form-input>
                    <label>Peso do Produto</label>
                    <b-form-input type="number" label="enter your name" placeholder="Peso do produto" v-model="product.weight" class="form"></b-form-input>
                    <label>Preço do Produto</label>
                    <b-form-input type="number" placeholder="Preço do produto" v-model="product.price" class="form"></b-form-input>
                    <label>Quantidade em estoque</label>
                    <b-form-input type="number" placeholder="Quantidade em estoque" v-model="product.stock" class="form"></b-form-input>
                    <label>{{product.providers}}</label>
                    <b-form-select v-model="selected" multiple class="form">
                        <option v-for="provider in providers" :key="provider.id" :value="provider.id" @click="addProvider(provider.id)">{{ provider.name }}</option>
                    </b-form-select>
                    <b-button @click="submit" class="form" variant="primary" block>Editar produto</b-button>                      
                </b-col>
                <b-col></b-col>
            </b-row>
        </b-container>
    </div>
</template>


<script>
import Header from '@/components/Header'
import axios from "axios"
import router from '@/router'
export default {
    name: 'EditBook',
    components: {Header},
    created(){
        this.getProductInfo()
        this.getProviders()
    },
    data(){
        return{
            name: "",
            weight: "",
            price: "",
            stock: "",
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
        getProductInfo(){
            axios.request({
                baseURL: "http://localhost:8000",
                methods: "get",
                url: `/api/product/get/${this.$route.params.id}/`
            }).then(res => {
                this.product = res.data
            });
        },
        getProviders(){
            axios.request({
                baseURL: "http://localhost:8000",
                method: "get",
                url: "/api/provider/"
            }).then(response => {
                this.providers = response.data
            });
        },
        submit(){
            this.product.providers = this.productprovider
            axios.put(`http://localhost:8000/api/product/edit/${this.$route.params.id}/`, this.product, {
                headers: {
                    Authorization: `Token ${this.$session.get("token")}`
                }
            }).then(res => {
                router.push('/products')
                this.log.console(res)
            });
        }
    }
}
</script>


<style>
label{
    margin-top: 2%;
    float:left;
}
</style>