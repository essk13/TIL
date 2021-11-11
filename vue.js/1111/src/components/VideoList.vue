<template>
  <div id="video-list" v-if="videoList">
    <video-list-item
      v-for="video in videoList"
      :key="video.id.vedioId"
      :video="video"
    >
    </video-list-item>
  </div>
</template>

<script>
import VideoListItem from './VideoListItem'

import { mapState } from 'vuex'

export default {
  name: 'VideoList',
  components: {
    VideoListItem
  },
  computed: {
    ...mapState([
      'videoList',
    ])
  }
}
</script>

<style>
#video-list {
  border: 1px solid black;
  margin: 10px auto;
  width: 80%;
}
</style>