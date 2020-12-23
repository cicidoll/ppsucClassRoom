<template>
  <div>
    <ul>
      <li v-for="(item, index) in roomData" :key="index">
        {{item}}
      </li>
    </ul>
  </div>

</template>

<script>
export default {
  props: ['buildingName', 'roomData']
}
</script>

<style lang="less" scoped>

</style>
