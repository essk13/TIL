<template>
  <div
    class="video-detail"
    @click="select(video)"
  >
    <img class="tumbnail" :src="video.snippet.thumbnails.default.url" :alt="video.snippet.title">
    <div class="video-description">
      <p class="title">{{ unescapeTitle }}</p>
      <p class="channel">{{ unescapeChannel }}</p>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  computed: {
    ...mapGetters([
      'unescapeTitle',
      'unescapeChannel'
    ])
  },
  methods: {
    ...mapActions([
      'select',
    ])
  }
}
</script>

<style>
.video-detail {
  margin: 10px 10px;
  display: flex;
}

.tumbnail {
  margin-right: 10px;
}

.video-description {
  text-align: left;
}

.title {
  font-size: 12px;
  font-weight: bold;
  margin: 0;
}

.channel {
  font-size: 8px;
  margin: 5px 0 0 0;
}
</style>