<template>
  <div class="roomList">
    <roomItem v-for="(item, index) in roomData"
              :key="index"
              :itemName="item"
              :mobilizeData="mobilizeData[item]"
              :borrowData="borrowData[item]"></roomItem>
  </div>

</template>

<script>
import roomItem from './roomItem.vue'

export default {
  props: ['roomData', 'mobilizeData', 'borrowData'],
  components: {
    roomItem
  }
}
</script>

<style lang="less" scoped>
.roomList{
  width: 100vw;
  overflow: scroll;
}
</style>
