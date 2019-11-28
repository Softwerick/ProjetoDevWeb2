<template>
    <div>
        <Header />
        <b-container class="container">
            <b-row>
                <b-col></b-col>
                <b-col>
                    <h2>Adicionar um fornecedor</h2>
                    <b-form-input placeholder="Nome do fornecedor" v-model="provider.name" class="form"></b-form-input>
                    <b-button @click="add" class="form" variant="primary" block>Adicionar fornecedor</b-button>                      
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
            provider: {},
        }
    },
    methods: {
        add(){
            axios.post("http://localhost:8000/api/provider/add/", this.provider, {
                headers: {
                    Authorization: `Token ${this.$session.get("token")}`
                }
            }).then(response => {
                router.push('/providers')
                alert(response)
            }).catch(e =>{
                alert(e)
            })
        },
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