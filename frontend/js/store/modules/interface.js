export const state = {
  sidebarItems: [
    {
      name: 'Меню',
      role: '',
      items: [
        {
          icon: 'mdi-home',
          name: 'Личный кабинет',
          to: '/home'
        },
        {
          icon: 'mdi-school',
          name: 'Академические группы',
          to: '/groups'
        },
        {
          icon: 'mdi-bookshelf',
          name: 'Гражданства',
          to: '/citizenship'
        },
        {
          icon: 'mdi-bookshelf',
          name: 'Национальности',
          to: '/nationality'
        },
        {
          icon: 'mdi-bookshelf',
          name: 'Языки',
          to: '/native-language'
        },
        {
            icon: 'mdi-bookshelf',
            name: 'Направления',
            to: '/training-direction'
        }
      ]
    }
  ],
  roles: [
    { id: 1, name: 'Тютор' },
    { id: 2, name: 'Контроль работы' },
    { id: 3, name: 'Администратор' }
  ]
}

export const getters = {
  sidebar: state => state.sidebarItems,
  getRole: state => id => {
    return state.roles.find(role => role.id === id)
  }
}

export const mutations = {
  // sidebarToggle(state) {
  //   state.sidebar = !state.sidebar
  // }
}

export const actions = {
  // incrementIfOddOnRootSum({ state, commit, rootState }) {
  //   if ((state.count + rootState.count) % 2 === 1) {
  //     commit('increment')
  //   }
  // }
}
