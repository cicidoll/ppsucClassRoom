<template>
  <div class="tabs-bar">
    <div class="tabs-tab">
      <slot name="day1"></slot>
    </div>
    <div class="tabs-tab">
      <slot name="day2"></slot>
    </div>
    <div class="tabs-tab">
      <slot name="day3"></slot>
    </div>
    <div class="tabs-tab">
      <slot name="day4"></slot>
    </div>
    <div class="tabs-tab">
      <slot name="day5"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'daySelect',
  methods: {

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
    // border-top: 1px solid #3399ff;
    // border-bottom: 1px solid #fff;
  }
  .tabs-tab-active:before{
    // content: '';
    // display: block;
    // height: 1px;
    background: #3399ff;
    // position: absolute;
    // top: 0;
    // left: 0;
    // right: 0;
  }
}
</style>
