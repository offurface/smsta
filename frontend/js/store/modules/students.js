import axios from 'axios'

export const state = {
  student: null
}

export const getters = {
  student: state => state.student
}

export const mutations = {
  setStudent(state, { data }) {
    state.student = data
  }
}

export const actions = {
  loadStudent({ commit }, { pk }) {
    return new Promise((resolve, reject) => {
      axios
        .get('system/students/' + pk + '/')
        .then(response => {
          const data = response.data
          commit('setStudent', { data })
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  putStudent({ commit }, { pk, student }) {
    return new Promise((resolve, reject) => {
      axios
        .put('system/students/' + pk + '/', student)
        .then(response => {
          const data = response.data
          commit('setStudent', { data })
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  }
}
