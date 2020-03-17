export const state = {
  items: [
    {
      name: 'Links',
      items: [
        {
          icon: 'fas fa-tachometer-alt',
          name: 'Django admin',
          url: '/dj-admin/'
        },
        {
          icon: 'mdi mdi-api',
          name: 'API',
          url: '/api/'
        },
        {
          icon: 'mdi mdi-login',
          name: 'Login',
          url: 'login',
          noReload: true
        }
      ]
    },
    {
      name: 'Documents',
      items: [
        {
          icon: 'mdi mdi-language-python',
          name: 'Django',
          url: 'https://www.djangoproject.com/'
        },
        {
          icon: 'mdi mdi-api',
          name: 'Django REST Framework',
          url: 'https://www.django-rest-framework.org/'
        },
        {
          icon: 'mdi mdi-bootstrap',
          name: 'Bootstrap',
          url: 'https://getbootstrap.com/'
        },
        {
          icon: 'mdi mdi-vuejs',
          name: 'Vue.js',
          url: 'https://ru.vuejs.org/'
        },
        {
          icon: 'mdi mdi-vuejs',
          name: 'Vuex',
          url: 'https://vuex.vuejs.org/ru/guide/'
        },
        {
          icon: 'mdi mdi-vuejs',
          name: 'Vue Router',
          url: 'https://router.vuejs.org/ru/'
        },
        {
          icon: 'mdi mdi-code-braces',
          name: 'Axios',
          url: 'https://github.com/axios/axios'
        },
        {
          icon: 'mdi mdi-jquery',
          name: 'JQuery',
          url: 'https://api.jquery.com/'
        },
        {
          icon: 'mdi mdi-color-helper',
          name: 'Lodash',
          url: 'https://lodash.com/'
        },
        {
          icon: 'mdi mdi-comment-alert',
          name: 'SweetAlert',
          url: 'https://sweetalert2.github.io/'
        },
        {
          icon: 'mdi mdi-material-design',
          name: 'Material design icons',
          url: 'https://cdn.materialdesignicons.com/4.9.95/'
        },
        {
          icon: 'fab fa-font-awesome-flag',
          name: 'Fontawesome icons',
          url: 'https://fontawesome.com/icons'
        }
      ]
    },
    {
      name: 'Recommend',
      items: [
        {
          icon: 'mdi mdi-vuejs',
          name: 'Vue Modal Component',
          url: 'https://github.com/euvl/vue-js-modal'
        },
        {
          icon: 'mdi mdi-vuejs',
          name: 'Vue Select2 Component',
          url: 'https://github.com/godbasin/vue-select2'
        },
        {
          icon: 'mdi mdi-layers-outline',
          name: 'Select2',
          url: 'https://select2.org/'
        },
        {
          icon: 'mdi mdi-image-area',
          name: 'Owl Carousel',
          url: 'https://owlcarousel2.github.io/OwlCarousel2/'
        },
        {
          icon: 'mdi mdi-mail',
          name: 'Fancybox',
          url: 'http://fancyapps.com/fancybox/3/'
        }
      ]
    }
  ]
}

export const getters = {
  items: state => state.items
}
