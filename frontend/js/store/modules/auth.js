import axios from 'axios'
import Cookies from 'js-cookie'
import jwtDecode from 'jwt-decode'
import * as types from '../mutation-types'

export const state = {
  payload: Cookies.get('payload') || null
}

export const getters = {
  payload: state => state.payload,
  user: state => jwtDecode(state.payload, { header: true }),
  check: state => state.payload !== null
}

export const mutations = {
  [types.LOGIN](state, { payload }) {
    const user = jwtDecode(payload, { header: true })
    const d = new Date(0)
    d.setUTCSeconds(user.exp)
    state.payload = payload
    Cookies.set('payload', payload, {
      expires: d
    })
  },

  [types.LOGOUT](state) {
    state.payload = null
    Cookies.remove('payload')
  }
}

export const actions = {
  login({ commit }, { username, password }) {
    return new Promise((resolve, reject) => {
      axios
        .post('auth/token/', { username, password })
        .then(response => {
          const payload = response.data.access.split('.')[1]
          commit(types.LOGIN, { payload })
          resolve(response)
        })
        .catch(error => {
          commit(types.LOGOUT)
          reject(error)
        })
    })
  },

  refresh({ commit }) {
    return new Promise((resolve, reject) => {
      axios
        .post('auth/refresh/')
        .then(response => {
          const payload = response.data.access.split('.')[1]
          commit(types.LOGIN, { payload })
          resolve(response)
        })
        .catch(error => {
          commit(types.LOGOUT)
          reject(error)
        })
    })
  },

  logout({ commit }) {
    return new Promise((resolve, reject) => {
      axios
        .post('auth/delete/')
        .then(response => {
          commit(types.LOGOUT)
          resolve(response)
        })
        .catch(error => {
          commit(types.LOGOUT)
          reject(error)
        })
    })
  }
}
