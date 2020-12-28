<template>
  <div id="drawer">
    <el-button  class="el-icon-more" plain
                @click="drawer = true">
    </el-button>
    <el-drawer
      title="设置"
      :show-close="false"
      :visible.sync="drawer"
      :direction="direction"
      :wrapperClosable="true"
      :with-header="false">
      <div class="drawerContent">
        <h3>关于</h3>
        <h5>作者：17网二陈川</h5>
        <h5>联系方式：</h5>
        <h5>ayaseemt@qq.com</h5>
      </div>
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
  .drawerContent{
    background-color: #71d0ff;
    color: black;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
}
</style>
