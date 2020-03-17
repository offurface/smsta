import store from '@/store'

export default (to, from, next) => {
  if (to.name === 'login') {
    next()
    return
  }
  if (!store.getters['auth/check']) {
    store
      .dispatch('auth/refresh')
      .then(() => {
        next()
      })
      .catch(() => {
        next({
          name: 'login',
          query: { next: to.fullPath }
        })
      })
  } else {
    next()
  }
}
