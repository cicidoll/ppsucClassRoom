<template>
<div class="build-tabs">
    <div class="build-tab-bar" @click="getData()">
      铸剑楼
    </div>
    <div class="build-tab-bar" @click="getData()">
      中楼
    </div>
    <div class="build-tab-bar" @click="getData()">
      西配
    </div>
</div>
</template>

<script>
export default {
  name: 'buildingSelect',
  methods: {
    getData () {
      this.$parent.getData()
    }
  }
}
</script>

<style lang="less" scoped>
.build-tabs{
  position: absolute;
  width: 100vw;
  bottom: 5vh;
  display: flex;
  .build-tab-bar{
    flex: 1;
    text-align: center;
    border: solid 1px black;
  }
}
</style>
