import Vue from 'vue'
import store from '@/store'
import Meta from 'vue-meta'
import routes from './routes'
import Router from 'vue-router'
import { sync } from 'vuex-router-sync'

Vue.use(Meta)
Vue.use(Router)

// const globalMiddleware = ['locale', 'auth']
const globalMiddleware = ['locale']

const routerMiddleware = resolveMiddleware(
  require.context('@/middleware', false, /.*\.js$/)
)

const router = createRouter()

sync(store, router)

export default router

function createRouter() {
  const router = new Router({
    scrollBehavior,
    mode: 'history',
    routes
  })

  router.beforeEach(beforeEach)
  router.afterEach(afterEach)

  return router
}

async function beforeEach(to, from, next) {
  const components = await resolveComponents(
    router.getMatchedComponents({ ...to })
  )

  if (components.length === 0) {
    return next()
  }

  const middleware = getMiddleware(components)

  callMiddleware(middleware, to, from, (...args) => {
    if (args.length === 0) {
      router.app.setLayout(components[0].layout || '')
    }

    next(...args)
  })
}

async function afterEach(to, from, next) {
  await router.app.$nextTick()
}

function callMiddleware(middleware, to, from, next) {
  const stack = middleware.reverse()

  const _next = (...args) => {
    if (args.length > 0 || stack.length === 0) {
      return next(...args)
    }

    const middleware = stack.pop()

    if (typeof middleware === 'function') {
      middleware(to, from, _next)
    } else if (routerMiddleware[middleware]) {
      routerMiddleware[middleware](to, from, _next)
    } else {
      throw Error(`Undefined middleware [${middleware}]`)
    }
  }

  _next()
}

function resolveComponents(components) {
  return Promise.all(
    components.map(component => {
      return typeof component === 'function' ? component() : component
    })
  )
}

function getMiddleware(components) {
  const middleware = [...globalMiddleware]

  components
    .filter(c => c.middleware)
    .forEach(component => {
      if (Array.isArray(component.middleware)) {
        middleware.push(...component.middleware)
      } else {
        middleware.push(component.middleware)
      }
    })

  return middleware
}

function scrollBehavior(to, from, savedPosition) {
  if (savedPosition) {
    return savedPosition
  }

  if (to.hash) {
    return { selector: to.hash }
  }

  const [component] = router.getMatchedComponents({ ...to }).slice(-1)

  if (component && component.scrollToTop === false) {
    return {}
  }

  return { x: 0, y: 0 }
}

function resolveMiddleware(requireContext) {
  return requireContext
    .keys()
    .map(file => [file.replace(/(^.\/)|(\.js$)/g, ''), requireContext(file)])
    .reduce(
      (guards, [name, guard]) => ({
        ...guards,
        [name]: guard.default
      }),
      {}
    )
}
