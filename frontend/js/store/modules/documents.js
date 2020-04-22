import axios from 'axios'

export const state = {

}

export const getters = {
}

export const mutations = {
}

export const actions = {
  groupCard({ commit }, { pk }) {
    return new Promise((resolve, reject) => {
      axios({
        url: 'documents/group-card/' + pk + '/',
        method: 'GET',
        responseType: 'blob'
      })
        .then(response => {
          const url = window.URL.createObjectURL(new Blob([response.data]))
          const link = document.createElement('a')
          link.href = url
          link.setAttribute('download', 'group-card.docx')
          document.body.appendChild(link)
          link.click()
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  }
}
