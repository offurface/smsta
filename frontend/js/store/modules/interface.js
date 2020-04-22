export const state = {
  sidebarItems: [
    {
      name: 'Основное',
      role: '',
      items: [
        {
          icon: 'mdi-view-dashboard',
          name: 'Главная',
          to: '/home'
        },
        {
          icon: 'mdi-settings',
          name: 'Test',
          to: '/test'
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
