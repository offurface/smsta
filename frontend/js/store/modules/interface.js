export const state = {
  sidebarItems: [
    {
      name: 'Основное',
      role: '',
      items: [
        {
          icon: 'mdi-home',
          name: 'Главная',
          to: '/home'
        },
        {
          icon: 'mdi-content-paste',
          name: 'Группы',
          to: '/groups'
        }
      ]
    }
  ]
}

export const getters = {
  sidebar: state => state.sidebarItems
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
