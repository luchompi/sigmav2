import { createStore } from 'vuex'

export default createStore({
  state: {
    access:null,
    refresh:null,
  },
  getters: {
  },
  mutations: {
    initializeStore(state){
        if(localStorage.getItem('access')){
            state.access = localStorage.getItem('access')
            state.refresh = localStorage.getItem('refresh')
        }
        else{
          state.access = null
            state.refresh=null
        }
    },
    setAccess(state, access){
        state.access = access
        localStorage.setItem('access', access)
    },
      setRefreshToken(state, refresh){
        state.refresh = refresh
        localStorage.setItem('refresh', refresh)
      }
  },
  actions: {
  },
  modules: {
  }
})
