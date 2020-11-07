<template>
    <div class="classes">
        <slot></slot>
    </div>
</template>
<script>
export default {
  name: 'Collapse',
  props: {
    accordion: {
      // 是否为手风琴模式，该模式下同时只能展开一个面板
      type: Boolean,
      default: false
    },
    value: {
      // 对应panel.vue展开的name，手风琴模式下为数组
      type: [Array, String]
    },
    simple: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      // 设置内部使用状态，用于实现v-model
      currentValue: this.value
    }
  },
  // computed: {
  //   classes () {
  //     return [
  //       `${prefixCls}`,
  //       {
  //         [`${prefixCls}-simple`]: this.simple
  //       }
  //     ];
  //   }
  // },
  mounted () {
    // 初始化时，设置isActive和index
    this.setActive()
  },
  methods: {
    /**
     * data由Panel传递，有两项
     * name，当前Panel的name或index的值
     * isActive，当前是否激活
     */
    setActive () {
      const activeKey = this.getActiveKey()
      this.$children.forEach((child, index) => {
        const name = child.name || index.toString()
        let isActive = false

        // 在两种模式下，判断当前Panel是否需要激活
        if (self.accordion) {
          isActive = activeKey === name
        } else {
          isActive = activeKey.indexOf(name) > -1
        }
        // 给当前Panel设置isActive和index，index为它在slot中的序列
        child.isActive = isActive
        child.index = index
      })
    },
    getActiveKey () {
      let activeKey = this.currentValue || []
      const accordion = this.accordion
      /**
       * value的类型可以是字符串或数组，
       * 为保证数据格式统一，将activeKey强行设置为数组因为不能保证用户设置的都是数组
       */
      if (!Array.isArray(activeKey)) {
        activeKey = [activeKey]
      }
      // 手风琴模式下，如果多设置了数组，也只取其第一项
      if (accordion && activeKey.length > 1) {
        activeKey = [activeKey[0]]
      }
      // 将activeKey转为字符串，因为用户设置的有可能是字符串数字，比较时类型会不一致
      for (let i = 0; i < activeKey.length; i++) {
        activeKey[i] = activeKey[i].toString()
      }
      return activeKey
    },
    toggle (data) {
      const name = data.name.toString()
      // 声明一个临时激活项列表
      let newActiveKey = []
      if (this.accordion) {
        /**
         * 手风琴模式下，同时只能激活一个面板
         * 如果当前未激活，就将它的name写入临时列表
         * 如果已激活，意味着关闭所有的面板，所以不用任何设置
         */
        if (!data.isActive) {
          newActiveKey.push(name)
        }
      } else {
        let activeKey = this.getActiveKey()
        const nameIndex = activeKey.indexOf(name)
        // 点击后切换关闭
        if (data.isActive) {
          if (nameIndex > -1) {
            activeKey.splice(nameIndex, 1)
          }
        // 点击后切换为展开
        } else {
          if (nameIndex < 0) {
            activeKey.push(name)
          }
        }
        newActiveKey = activeKey
      }
      // 更新currentValue会触发watch，从而调用setActive方法
      this.currentValue = newActiveKey
      this.$emit('input', newActiveKey)
      // this.$emit('on-change', newActiveKey)
    }
  },
  watch: {
    value (val) {
      // 从外部改变value时，更新内部的数据。
      this.currentValue = val
    },
    // 修改currentValue时，重新设置一遍状态
    currentValue () {
      this.setActive()
    }
  }
}
</script>

<style lang="less" scoped>
.classes{
  width: 100vw;
}
</style>
