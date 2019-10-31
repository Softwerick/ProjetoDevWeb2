import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import router from './router/index'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueSession from 'vue-session'

Vue.use(VueSession)

Vue.use(BootstrapVue)
Vue.config.performance = true;
Vue.config.productionTip = false;

new Vue({
  el: "#app",
  router,
  components: { App },
  render: h => h(App)
})
