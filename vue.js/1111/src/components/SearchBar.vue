<template>
  <div id="search-bar">
    <input
      type="text"
      placeholder=" Input keyword"
      v-model.trim="inputData"
      @keyup.enter="searchKeyword"
    >

    <button @click="searchKeyword">검색</button>
  </div>
</template>

<script>
import axios from 'axios'

const API_KEY = process.env.VUE_APP_API_KEY
const API_URL = "https://www.googleapis.com/youtube/v3/search"

export default {
  name: 'SearchBar',
  data () {
    return {
      inputData: null,
    }
  },
  methods: {
    searchKeyword () {
      if (this.inputData) {
        axios ({
            method: 'get',
            url: API_URL,
            params: {
              part: 'snippet',
              q: this.inputData,
              type: 'video',
              key: API_KEY,
            }
        })
          .then(res => {
            this.$store.dispatch('search', res.data.items)
            return console.log('검색 성공')
            })
          .catch(err => console.log(err))
      } else {
        alert('검색어를 입력하세요')
      }
    },

  }
}
</script>

<style scoped>
#search-bar {
  margin-bottom: 10px;
}

button {
  background: red;
  color: white;
  border: 0;
  border-radius: 5px;
  margin-left: 5px;
  padding: 1.5px 6px;
  font-size: 13px;
}

input {
  font-size: 13px;
  border: 0.5px solid black;
  border-radius: 5px;
}
</style>