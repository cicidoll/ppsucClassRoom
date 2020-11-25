<template>
  <div class="tabs-bar">
    <div :class="classes('1')" @click="changeDay('1')">
      <slot name="day1"></slot>
    </div>
    <div :class="classes('2')" @click="changeDay('2')">
      <slot name="day2"></slot>
    </div>
    <div :class="classes('3')" @click="changeDay('3')">
      <slot name="day3"></slot>
    </div>
    <div :class="classes('4')" @click="changeDay('4')">
      <slot name="day4"></slot>
    </div>
    <div :class="classes('5')" @click="changeDay('5')">
      <slot name="day5"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'daySelect',
  data () {
    return {
      // 默认为周一
      value: '1'
    }
  },
  methods: {
    changeDay (day) {
      // 改变值
      this.value = day
      this.$parent.selectDay(day)
    },
    classes (day) {
      return [
        'tabs-tab',
        this.value === day ? 'tabs-tab-active' : ''
      ]
    }
  }
}
</script>

<style scoped lang="less">
.tabs-bar{
  width: 100vw;
  height: 7vh;
  font-size: 14px;
  color: #303133;
  background-color: #d7dadfb2;
  display: flex;
  flex-direction: row;

  .tabs-tab{
    display: flex;
    flex: 1;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 4px 12px;
    border: 1px solid transparent;
    margin-top: -1px;
    color: #909399;
  }
  .tabs-tab-active{
    color: #409EFF;
    background-color: #fff;
    border-right-color: #DCDFE6;
    border-left-color: #DCDFE6;
  }
}
</style>
