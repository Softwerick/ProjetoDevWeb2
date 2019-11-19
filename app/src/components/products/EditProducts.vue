<template>
    <div>
        <Header />
        <b-container class="container">
            <b-row>
                <b-col></b-col>
                <b-col>
                    <h2>Editar produto</h2>
                    <b-form-input :placeholder="product.name" v-model="product.name" class="form"></b-form-input>
                    <b-form-input type="number" placeholder="Peso do produto" v-model="product.weight" class="form"></b-form-input>
                    <b-form-input type="number" placeholder="Preço do produto" v-model="product.price" class="form"></b-form-input>
                    <b-form-input type="number" placeholder="Quantidade em estoque" v-model="product.stock" class="form"></b-form-input>
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
    },
    data(){
        return{
            name: "",
            weight: "",
            price: "",
            stock: "",
            product: {}
        }
    },
    methods: {
        getProductInfo(){
            axios.request({
                baseURL: "http://localhost:8000",
                methods: "get",
                url: `/api/product/get/${this.$route.params.id}/`
            }).then(res => {
                this.product = res.data
            });
        },
        submit(){
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

</style>