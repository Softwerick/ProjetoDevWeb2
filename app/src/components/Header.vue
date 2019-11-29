<template>
    <div>
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand href="#" @click="mainPage">ShopTime</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav v-if="checkLogin">
        <b-nav-item active @click="productsPage">Produtos</b-nav-item>
        <b-nav-item @click="providerPage" active>Fornecedores</b-nav-item>
      </b-navbar-nav>

      <b-navbar-nav class="ml-auto">
        <b-nav-item v-if="!checkLogin" v-b-modal.modal-1 right>Login</b-nav-item>
        <b-nav-item class="headerbuttons" v-else>
          <b-dropdown id="dropdown-dropleft" dropleft class="headerbutton" :text="getUsername">
            <b-dropdown-item>Perfil</b-dropdown-item>
            <b-dropdown-item @click="logout">Logout</b-dropdown-item>
          </b-dropdown>
        </b-nav-item>
            <b-modal id="modal-1" title="Realizar Login" hide-footer>
                <b-form-input v-model="credentials.username" placeholder="Enter your name"></b-form-input>
                <b-form-input v-model="credentials.password" type="password" placeholder="Enter your password" class="mt-3"></b-form-input>
                <b-button class="mt-3" block variant="info" @click="login">Login</b-button>
            </b-modal>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>

<script>
import axios from 'axios'
import router from '../router'

export default {
    data(){
      return{
        credentials: {},
        logged: true

      }
    },
    computed:{
      checkLogin: function(){
        return this.$session.get('token')
      },
      getUsername: function(){
        return this.$session.get('username')
      }
    },
    methods: {
      login(){
          axios.post('http://localhost:8000/auth/token/login', this.credentials).then(res => {
            this.$session.start();
            this.$session.set('token', res.data.auth_token);
            this.$session.set('username', this.credentials.username)
            router.push('/products')
          }).catch(e => {
            alert("Usuário ou senha incorretos")
            this.log.console(e)
            router.push('/')
          })
      },
      logout(){
        this.$session.remove('token')
        this.$session.remove('username')
        router.push('/')
      },
      mainPage(){
        router.push('/')
      },
      productsPage(){
        router.push('/products')
      },
      providerPage(){
        router.push('/providers')
      }
    }
}
</script>

<style>
.btn-secondary{
  background-color: #17a2b8 !important;
}
</style>