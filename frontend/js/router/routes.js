const Home = () =>
  import(/* webpackChunkName: "home" */ '@/pages/home').then(
    m => m.default || m
  )
const NotFound = () =>
  import(/* webpackChunkName: "404" */ '@/pages/errors/404').then(
    m => m.default || m
  )
const Login = () =>
  import(/* webpackChunkName: "login" */ '@/pages/auth/login').then(
    m => m.default || m
  )

export default [
  { path: '/', name: 'home', component: Home },
  { path: '/login/', name: 'login', component: Login },
  { path: '*', name: '404', component: NotFound }
]