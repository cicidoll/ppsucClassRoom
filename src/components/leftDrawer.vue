<template>
  <div id="drawer">
    <el-button  class="el-icon-more" plain
                @click="drawer = true">
    </el-button>
    <el-drawer
      title="我是标题"
      :show-close="false"
      :visible.sync="drawer"
      :direction="direction"
      :wrapperClosable="true"
      :with-header="false">
      <span>我来啦!</span>
    </el-drawer>
  </div>

</template>

<script>
export default {
  data () {
    return {
      drawer: false,
      direction: 'ltr'
    }
  }
}
</script>

<style lang="less" scoped>
#drawer{
  .el-icon-more{
    background-color:#48bcf7;
    color: white;
  }
}
</style>
