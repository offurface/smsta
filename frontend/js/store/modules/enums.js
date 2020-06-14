import axios from 'axios'

export const state = {
  formTraining: null,
  paymentTraining: null,
  typeTraining: null,
  activeGroup: null,
  disabilityGroup: null,
  gender: null
}

export const getters = {
  formTraining: state => state.formTraining,
  paymentTraining: state => state.paymentTraining,
  typeTraining: state => state.typeTraining,
  activeGroup: state => state.activeGroup,
  disabilityGroup: state => state.disabilityGroup,
  gender: state => state.gender
}

export const mutations = {
  setFormTraining(state, { data }) {
    state.formTraining = data
  },
  setPaymentTraining(state, { data }) {
    state.paymentTraining = data
  },
  setTypeTraining(state, { data }) {
    state.typeTraining = data
  },
  setActiveGroup(state, { data }) {
    state.activeGroup = data
  },
  setDisabilityGroup(state, { data }) {
    state.disabilityGroup = data
  },
  setGender(state, { data }) {
    state.gender = data
  }
}

export const actions = {
  loadFormTraining({ commit }) {
    return new Promise((resolve, reject) => {
      axios
        .get('system/form-training/')
        .then(response => {
          const data = response.data
          commit('setFormTraining', { data })
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  loadPaymentTraining({ commit }) {
    return new Promise((resolve, reject) => {
      axios
        .get('system/payment-training/')
        .then(response => {
          const data = response.data
          commit('setPaymentTraining', { data })
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  loadTypeTraining({ commit }) {
    return new Promise((resolve, reject) => {
      axios
        .get('system/type-trainig/')
        .then(response => {
          const data = response.data
          commit('setTypeTraining', { data })
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  loadActiveGroup({ commit }) {
    return new Promise((resolve, reject) => {
      axios
        .get('system/active-group/')
        .then(response => {
          const data = response.data
          commit('setActiveGroup', { data })
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  loadDisabilityGroup({ commit }) {
    return new Promise((resolve, reject) => {
      axios
        .get('system/disability-group/')
        .then(response => {
          const data = response.data
          commit('setDisabilityGroup', { data })
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  loadGender({ commit }) {
    return new Promise((resolve, reject) => {
      axios
        .get('system/gender/')
        .then(response => {
          const data = response.data
          commit('setGender', { data })
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  }
}
