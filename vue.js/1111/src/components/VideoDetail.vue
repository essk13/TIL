<template>
  <div id="video-detail" v-if="selectedVideo">
    <div class="player">
      <iframe
        class="video-player"
        type="text/html"
        :src="videoURL"
        frameborder="0"
      >
      </iframe>
    </div>

    <div class="video-description">
      <p class="title">{{ unescapeTitle }}</p>
      <p class="channel">{{ unescapeChannel }}</p>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex'

export default {
  name: 'VideoDetail',
  computed: {
    ...mapState([
      'selectedVideo',
      'videoURL',
    ]),
    ...mapGetters([
      'unescapeTitle',
      'unescapeChannel',
    ])
  },
}
</script>

<style>
#video-detail {
  width: 80%;
  margin: 0 auto;
}

.player {
  width: 100%;
  height: 400px;
  margin-bottom: 10px;
}

.video-player {
  width: 100%;
  height: 100%;
}
</style>