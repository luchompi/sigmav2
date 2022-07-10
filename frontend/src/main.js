import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bootstrap5/src/css/bootstrap.min.css'
import 'bootstrap5/src/js/bootstrap.bundle.min.js'
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:8000'
createApp(App).use(store).use(router).mount('#app')
