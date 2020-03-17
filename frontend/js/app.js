import Vue from 'vue'
import store from '@/store'
import router from '@/router'
import i18n from '@/plugins/i18n'
import App from '@/components/layout/App'

import '@/plugins'
import '@/components'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  i18n,
  store,
  router,
  ...App
})
/* eslint-enable no-new */
