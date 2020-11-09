<template>
  <div class="tabs-bar">
    <div :class="classes('day1')" @click="changeDay('day1')">
      <slot name="day1"></slot>
    </div>
    <div :class="classes('day2')" @click="changeDay('day2')">
      <slot name="day2"></slot>
    </div>
    <div :class="classes('day3')" @click="changeDay('day3')">
      <slot name="day3"></slot>
    </div>
    <div :class="classes('day4')" @click="changeDay('day4')">
      <slot name="day4"></slot>
    </div>
    <div :class="classes('day5')" @click="changeDay('day5')">
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
      value: 'day1'
    }
  },
  methods: {
    changeDay (day) {
      // 改变值
      this.value = day
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
