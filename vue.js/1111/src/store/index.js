import Vue from 'vue'
import Vuex from 'vuex'
import _ from 'lodash'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    videoList: null,
    selectedVideo: null,
    videoURL: null,
  },
  mutations: {
    SEARCH_RESULT (state, videoList) {
      state.videoList = videoList
      state.selectedVideo = null
    },

    SELECT_VIDEO (state, video) {
      state.selectedVideo = video
      state.videoURL = `https://www.youtube.com/embed/${state.selectedVideo.id.videoId}?autoplay=1&mute=0`
    }
  },
  actions: {
    search ({ commit }, videoList) {
      commit('SEARCH_RESULT', videoList)
    },

    select ({ commit }, video) {
      commit('SELECT_VIDEO', video)
    }
  },
  getters: {
    unescapeTitle (state) {
       const title = _.unescape(state.selectedVideo.snippet.title)
       return title
    },

    unescapeChannel (state) {
       const channel = _.unescape(state.selectedVideo.snippet.channelTitle)
       return channel
    },
  }
})