<template>
    <div class="sedeList">
        <hr style="color:white;">
            <div class="row justify-content-md-center">
                <div class="col col-lg-8">
                    <div class="card" :aria-hidden="">
                        <div class="card-header">
                            Listado de Sedes
                        </div>
                        <div class="card-body">
                            <p class="card-text">                  
                            </p>
                        </div>                    
                    </div>
                </div>
            </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
name:'sedeList',
data() {
        return {
            login:false,
            loading:true,
            queryset:[],
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
        this.$router.push('/')
        console.log('no esta logueado')
    }
},
mounted(){
    this.getData()
},
methods: {
    getData(){
        axios.get('/api/v1/empresa/sedes/')
            .then(response=>{
                console.log(response.data)
                this.queryset = response.data
                this.loading = false
            })
            .catch(error=>{
                alert(error)
            })
    },
    }
}
</script>