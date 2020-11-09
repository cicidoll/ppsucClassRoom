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
  height: 5vh;
  font-size: 14px;
  color: #657180;
  display: flex;
  flex-direction: row;

  .tabs-tab{
    display: flex;
    flex: 1;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-left: 0.1rem;
    margin-right: 0.1rem;
    padding: 4px 12px;
    margin-right: 6px;
    background-color: #fff;
    border: 1px solid #d7dde4;
  }
  .tabs-tab-active{
    color: #3399ff;
  }
}
</style>
