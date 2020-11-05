<template>

<div>
  <div class="tabs">
    <div class="tabs-bar">
      <div
        :class="tabCls(item)"
        v-for="(item,index) in navList"
        :key="item.index"
        @click="handleChange(index)">
        {{ item.label }}
      </div>
    </div>

    <div class="tabs-content">
      <slot></slot>
    </div>
  </div>
</div>

</template>

<script>
export default {
  name: 'tabs',
  props: {
    value: {
      type: [String, Number]
    }
  },
  data: function () {
    return {
      currentValue: this.value,
      navList: []
    }
  },
  methods: {
    tabCls: function (item) {
      return [
        'tabs-tab',
        {
          'tabs-tab-active': item.name === this.currentValue
        }
      ]
    },
    handleChange: function (index) {
      var nav = this.navList[index]
      var name = nav.name
      this.currentValue = name
      this.$emit('input', name)
      this.$emit('on-click', name)
    },
    getTabs () {
      return this.$children.filter(function (item) {
        return item.$options.name === 'pane'
      })
    },
    updateNav () {
      this.navList = []
      var _this = this

      this.getTabs().forEach(function (pane, index) {
        _this.navList.push({
          label: pane.label,
          name: pane.name || index
        })
        if (!pane.name) pane.name = index
        if (index === 0) {
          if (!_this.currentValue) {
            _this.currentValue = pane.name || index
          }
        }
      })

      this.updateStatus()
    },
    updateStatus () {
      var tabs = this.getTabs()
      var _this = this
      tabs.forEach(function (tab) {
        return (tab.show = tab.name === _this.currentValue)
      })
    }
  },
  watch: {
    value: function (val) {
      this.currentValue = val
    },
    currentValue: function () {
      this.updateStatus()
    }
  }
}
</script>

<style scoped lang="less">
.tabs{
  width: 100vw;
  font-size: 14px;
  color: #657180;
  display: flex;
  flex-direction: column;

  .tabs-bar{
    width: 100vw;
    height: 5vh;
    display: flex;
    flex-direction: row;

    .tabs-tab{
      width: 25vw;
      display: flex;
      flex: 1;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      margin-left: 0.1rem;
      margin-right: 0.1rem;
      padding: 4px 16px;
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
  .tabs-content{
    padding: 8px 0;
  }
}

</style>
