<template>
  <div id="app">
    <header>
      <h1>Youtube PJT</h1>
      <search-bar></search-bar>
    </header>

    <section>
    <video-detail></video-detail>
    <video-list></video-list>
    </section>
  </div>
</template>

<script>
import SearchBar from './components/SearchBar'
import VideoDetail from './components/VideoDetail'
import VideoList from './components/VideoList'

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoDetail,
    VideoList
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
