import store from '@/store'

export default (to, from, next) => {
  if (store.getters['auth/user'].isSuperUser) {
    next()
  } else {
    next({ name: 'home' })
  }
}
