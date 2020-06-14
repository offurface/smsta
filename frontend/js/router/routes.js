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
const Test = () =>
  import(/* webpackChunkName: "login" */ '@/pages/test').then(
    m => m.default || m
  )
const GroupsList = () =>
  import(
    /* webpackChunkName: "login" */ '@/pages/academic-group/groups-list'
  ).then(m => m.default || m)
const GroupsDetail = () =>
  import(
    /* webpackChunkName: "login" */ '@/pages/academic-group/groups-detail'
  ).then(m => m.default || m)
<<<<<<< HEAD
const StudentDetail = () =>
  import(
    /* webpackChunkName: "login" */ '@/pages/students/students-detail'
  ).then(m => m.default || m)
const CitizenshipList = () =>
  import(/* webpackChunkName: "login" */ '@/pages/reference/citizenship').then(
    m => m.default || m
  )
const NationalityList = () =>
  import(/* webpackChunkName: "login" */ '@/pages/reference/nationality').then(
    m => m.default || m
  )
const NativeLanguageList = () =>
  import(
    /* webpackChunkName: "login" */ '@/pages/reference/native-language'
  ).then(m => m.default || m)
const TrainingDirectionList = () =>
  import(
    /* webpackChunkName: "login" */ '@/pages/reference/training-direction'
  ).then(m => m.default || m)
=======
>>>>>>> 67a21e0101656c73c91ce74090c78357c1a279d4
export default [
  { path: '/', name: 'login', component: Login },
  { path: '/home/', name: 'home', component: Home },
  { path: '/test/', name: 'test', component: Test },
  { path: '/groups/', name: 'groups-list', component: GroupsList },
  {
    path: '/nationality/',
    name: 'nationality-list',
    component: NationalityList
  },
  {
    path: '/citizenship/',
    name: 'citizenship-list',
    component: CitizenshipList
  },
  {
    path: '/native-language/',
    name: 'native-language-list',
    component: NativeLanguageList
  },
  {
    path: '/training-direction/',
    name: 'training-direction-list',
    component: TrainingDirectionList
  },
  { path: '/groups/:pkGroup/', name: 'groups-detail', component: GroupsDetail },
  {
    path: '/groups/:pkGroup/students/:pkStudent/',
    name: 'students-detail',
    component: StudentDetail
  },
  { path: '*', name: '404', component: NotFound }
]
