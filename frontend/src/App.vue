<template>
<div v-if="login">
  <nav class="navbar navbar-expand-lg bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#"><router-link to="/">Home</router-link></a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Empresa
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
              <li><a class="dropdown-item"><router-link to="/empresa/sedes">Sedes</router-link></a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled">Disabled</a>
          </li>
        </ul>
        <p :src="user_data">Sesión iniciada como {{user_data}} 
          <button class="btn btn-outline-danger my-2 my-sm-0" @click="doLogout">Cerrar Sesión</button>
        </p>
      </div>
    </div>
  </nav>
</div>
<div v-else>
<hr style="color:white;">
  <div class="row justify-content-md-center">
    <div class="col col-lg-8">
        <form v-on:submit.prevent="doLogin">
          <div class="card">
            <div class="card-header">
              Iniciar Sesión
            </div>
            <div class="card-body">
              <h5 class="card-title">Ingrese sus credenciales para empezar</h5>
              <p class="card-text">
                  
                    <label for="validationCustom01" class="form-label">Usuario</label>
                    <input type="text" class="form-control" id="validationCustom01" v-model="username" required>
                    <div class="valid-feedback">
                      Looks good!
                    </div>
                    <label for="validationCustom01" class="form-label">Contraseña</label>
                    <input type="password" class="form-control" id="validationCustom01" v-model="password" required>
                    <div class="valid-feedback">
                      Looks good!
                    </div>
                

              </p>
              <button type="submit" class="btn btn-primary">Iniciar Sesión</button>
            </div>
          </div>
        </form>
    </div>
  </div>
</div>
<router-view/>
</template>
<script>
import axios from 'axios'
export default{
  name: 'App',
  data() {
    return {
      login: false,
      username: '',
      password: '',
      user_data:''
    }
  },
  beforeCreate(){
    this.$store.commit('initializeStore')
    const access = this.$store.state.access
    if(access){
      axios.defaults.headers.common['Authorization'] = 'JWT ' + access
      this.login = true
    }else{
      axios.defaults.headers.common['Authorization'] = ''
      this.login = false

    }
  },
  mounted(){
    setInterval(()=>{
      this.getAcces()
    },59000)
  },
  methods:{
    getAcces(e){
      const accessData={
        refresh: this.$store.state.refresh,
      }
      axios.post('/api/v1/jwt/refresh/',accessData)
          .then(response=>{
            const access = response.data.access
            this.$store.commit('setAccess',access)
            axios.defaults.headers.common['Authorization']='JWT '+access
            localStorage.setItem('access',access)
          })
          .catch(error=>{
            console.log(error)
          })
    },
    doLogin(e){
      const loginData={
        username: this.username,
        password: this.password,
      }
      axios.post('/api/v1/jwt/create/',loginData)
          .then(response=>{
            const access = response.data.access
            this.$store.commit('setAccess',access)
            axios.defaults.headers.common['Authorization']='JWT '+access
            localStorage.setItem('access',access)
            this.login = true
            this.username='',
            this.password=''
          })
          .catch(error=>{
            console.log(error)
          })
      axios.get('/api/v1/users/me/')
          .then(response => {
            this.user_data = response.data.username
          })
          .catch(error => {
            console.log(error)
          })
    },
    doLogout(e){
      this.$store.commit('setAccess','')
      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem('access')
      this.user_data = ''
      this.login = false
    }
    }
  }

</script>
<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
