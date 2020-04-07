import Vue from 'vue'
import store from '@/store'
import router from '@/router'
import i18n from '@/plugins/i18n'
import vuetify from '@/plugins/vuetify'
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
  vuetify,
  ...App
})
/* eslint-enable no-new */
