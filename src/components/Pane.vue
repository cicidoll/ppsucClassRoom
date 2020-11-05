<template>

  <div class="pane" v-show="show">
    <slot></slot>
  </div>

</template>

<script>
export default {
  name: 'pane',
  data: function () {
    return {
      show: true
    }
  },
  props: {
    name: {
      type: String
    },
    label: {
      type: String,
      default: ''
    }
  },
  methods: {
    updateNav () {
      this.$parent.updateNav()
    }
  },
  watch: {
    label () {
      this.updateNav()
    }
  },
  mounted () {
    console.log(this.$parent)
    this.updateNav()
  }
}
</script>

<style scoped>
</style>
