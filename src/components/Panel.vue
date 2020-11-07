<template>
  <div class="itemClasses">
    <div class="headerClasses" @click="toggle">
      <slot></slot>
    </div>
    <div class="contentClasses" v-show="isActive">
      <div class="boxClasses">
        <slot name="content"></slot>
      </div>
    </div>
  </div>
</template>

<script>
//依赖iView的图标组件，这里使用小箭头
// import Icon from '../icon/icon.vue';

//CSS的命名空间
//const prefixCls = 'ivu-collapse';
export default {
  name: 'Panel',
  // components: { Icon },
  props: {
    name: {
      //用于唯一识别当前面板
      type: String
    },
    hideArrow: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      // use index for default when name is null
      index: 0, 
      isActive: false,
      mounted: false
    }
  },
  //动态设置相关CSS类名
    // computed: {
    //     itemClasses () {
    //       return [
    //           `${prefixCls}-item`,
    //           {
    //               [`${prefixCls}-item-active`]: this.isActive
    //           }
    //       ]
    //     },
    //     headerClasses () {
    //         return `${prefixCls}-header`
    //     },
    //     contentClasses () {
    //         return `${prefixCls}-content`
    //     },
    //     boxClasses () {
    //         return `${prefixCls}-content-box`
    //     }
    // },
  methods: {
    toggle () {
      //访问父链（即collapse.vue）执行方法，稍后介绍
      this.$parent.toggle({
        //优先使用name，未定义时使用index
        //index和isActive都在collapse.vue中设置，稍后介绍
        name: this.name || this.index,
        isActive: this.isActive
      })
    }
  },
  mounted () {
    this.mounted = true
  }
}
</script>

<style lang="less" scoped>
.itemClasses{
  width: 100vw;
  background-color: grey;
  margin-bottom: 10px;
  .headerClasses{
    height: 5vh;
  }
  .contentClasses{
    width: 100vw;
    background-color: white;
  }
}
</style>
