import axios from 'axios'

export const state = {
  citizenships: null,
  nationalitys: null,
  nativeLanguages: null,
  trainingDirections: null
}

export const getters = {
  citizenships: state => state.citizenships,
  nationalitys: state => state.nationalitys,
  nativeLanguages: state => state.nativeLanguages,
  trainingDirections: state => state.trainingDirections
}

export const mutations = {
  setCitizenships(state, { data }) {
    state.citizenships = data
  },
  pushCitizenships(state, { data }) {
    state.citizenships.push(data)
  },
  setNationalitys(state, { data }) {
    state.nationalitys = data
  },
  pushNationalitys(state, { data }) {
    state.nationalitys.push(data)
  },
  setNativeLanguages(state, { data }) {
    state.nativeLanguages = data
  },
  pushNativeLanguages(state, { data }) {
    state.nativeLanguages.push(data)
  },
  setTrainingDirections(state, { data }) {
    state.trainingDirections = data
  },
  pushTrainingDirections(state, { data }) {
    state.trainingDirections.push(data)
  }
}

export const actions = {
  loadCitizenships({ commit }) {
    return new Promise((resolve, reject) => {
      axios
        .get('system/citizenship/')
        .then(response => {
          const data = response.data
          commit('setCitizenships', { data })
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  postCitizenship({ commit }, { citizenship }) {
    return new Promise((resolve, reject) => {
      axios
        .post('system/citizenship/', citizenship)
        .then(response => {
          const data = response.data
          commit('pushCitizenships', { data })
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  putCitizenship({ commit }, { pk, citizenship }) {
    return new Promise((resolve, reject) => {
      axios
        .put('system/citizenship/' + pk + '/', citizenship)
        .then(response => {
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  loadNationalitys({ commit }) {
    return new Promise((resolve, reject) => {
      axios
        .get('system/nationality/')
        .then(response => {
          const data = response.data
          commit('setNationalitys', { data })
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  postNationality({ commit }, { nationality }) {
    return new Promise((resolve, reject) => {
      axios
        .post('system/nationality/', nationality)
        .then(response => {
          const data = response.data
          commit('pushNationalitys', { data })
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  putNationality({ commit }, { pk, nationality }) {
    return new Promise((resolve, reject) => {
      axios
        .put('system/nationality/' + pk + '/', nationality)
        .then(response => {
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  loadNativeLanguages({ commit }) {
    return new Promise((resolve, reject) => {
      axios
        .get('system/native-language/')
        .then(response => {
          const data = response.data
          commit('setNativeLanguages', { data })
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  postNativeLanguage({ commit }, { nativeLanguage }) {
    return new Promise((resolve, reject) => {
      axios
        .post('system/native-language/', nativeLanguage)
        .then(response => {
          const data = response.data
          commit('pushNativeLanguages', { data })
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  putNativeLanguage({ commit }, { pk, nativeLanguage }) {
    return new Promise((resolve, reject) => {
      axios
        .put('system/native-language/' + pk + '/', nativeLanguage)
        .then(response => {
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  loadTrainingDirections({ commit }) {
    return new Promise((resolve, reject) => {
      axios
        .get('system/training-direction/')
        .then(response => {
          const data = response.data
          commit('setTrainingDirections', { data })
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  postTrainingDirection({ commit }, { trainingDirection }) {
    return new Promise((resolve, reject) => {
      axios
        .post('system/training-direction/', trainingDirection)
        .then(response => {
          const data = response.data
          commit('pushTrainingDirections', { data })
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  putTrainingDirection({ commit }, { pk, trainingDirection }) {
    return new Promise((resolve, reject) => {
      axios
        .put('system/training-direction/' + pk + '/', trainingDirection)
        .then(response => {
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  }
}
