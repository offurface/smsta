import axios from 'axios'

export const state = {
  groups: null,
  group: null
}

export const getters = {
  groups: state => state.groups,
  group: state => state.group
}

export const mutations = {
  setGroups(state, { data }) {
    state.groups = data
  },
  setGroup(state, { data }) {
    state.group = data
  }
}

export const actions = {
  loadGroups({ commit }) {
    return new Promise((resolve, reject) => {
      axios
        .get('system/groups/')
        .then(response => {
          const data = response.data
          commit('setGroups', { data })
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  loadGroup({ commit }, { pk }) {
    return new Promise((resolve, reject) => {
      axios
        .get('system/groups/' + pk + '/')
        .then(response => {
          const data = response.data
          commit('setGroup', { data })
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  }
}
