<template>
<div class="build-tabs">
    <div :class="classes(0)" @click="selectBuilding(0, 'zhuJian')">
      铸剑楼
    </div>
    <div :class="classes(1)" @click="selectBuilding(1, 'zhongLou')">
      中楼
    </div>
    <div :class="classes(2)" @click="selectBuilding(2, 'XiPei')">
      西配
    </div>
</div>
</template>

<script>
export default {
  name: 'buildingSelect',
  data () {
    return {
      // 默认为zhuJian
      value: 'zhuJian',
      index: 0
    }
  },
  methods: {
    selectBuilding (index, building) {
      this.index = index
      this.$parent.selectBuilding(index, building)
    },
    classes (index) {
      return [
        'build-tab-bar',
        this.index === index ? 'build-tab-bar-active' : ''
      ]
    }
  }
}
</script>

<style lang="less" scoped>
.build-tabs{
  // position: fixed;
  width: 100vw;
  height: 6vh;
  // bottom: 5vh;
  display: flex;
  .build-tab-bar{
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    border: solid 1px black;
  }
  .build-tab-bar-active{
    background-color: black;
    color: white;
  }
}
</style>
