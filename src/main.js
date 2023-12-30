import Vue from 'vue'
import App from './App.vue'
import router from './router'
import '@/utils/element-ui'
import VueClipboard from 'vue-clipboard2'
Vue.config.productionTip = false
Vue.use(VueClipboard) // 复制内容组件
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
