<template>
    <div>
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand href="#">ShopTime</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="#">About</b-nav-item>
        <b-nav-item href="#">Help</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item v-b-modal.modal-1 right>Login</b-nav-item>
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
        credentials: {}
      }
    },
    methods: {
      login(){
          axios.post('http://localhost:8000/auth/token/login', this.credentials).then(res => {
            this.$session.start();
            this.$session.set('token', res.data.auth_token);
            router.push('/products')
          }).catch(e => {
            alert(e)
            router.push('/login/')
          })
      }
    }
}
</script>

<style>

</style>