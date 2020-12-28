<template>
  <div class="roomItem">
    <div style="display: flex;justify-content: center;padding: -10%">
      <div class="itemName">
        {{itemName}}
      </div>
    </div>
    <div class="itemBody">
      <el-collapse accordion>
        <el-collapse-item  v-if="mobilizeData.length != 0">
          <template slot="title">
            &nbsp;&nbsp;&nbsp;调停课信息 {{mobilizeData.length}}条
          </template>
          <roomItemTableMobilize :itemData="mobilizeData"></roomItemTableMobilize>
        </el-collapse-item>
        <el-collapse-item v-if="borrowData.length != 0">
          <template slot="title" >
            &nbsp;&nbsp;&nbsp;借用教室信息 {{borrowData.length}}条
          </template>
          <roomItemTableBorrow :itemData="borrowData"></roomItemTableBorrow>
        </el-collapse-item>
      </el-collapse>
    </div>
  </div>
</template>

<script>
import roomItemTableMobilize from './roomItemTableMobilize.vue'
import roomItemTableBorrow from './roomItemTableBorrow.vue'

export default {
  props: ['itemName', 'mobilizeData', 'borrowData'],
  components: {
    roomItemTableMobilize,
    roomItemTableBorrow
  }
}
</script>

<style lang="less" scoped>
.roomItem{
  width: 100vw;
  overflow: hidden;
  display: flex;
  font-size: 16px;
  color: #303133;
  border: 1px solid #00d412;
  .itemName{
    width: 10vw;
    font-size: 18px;
    background-color: #26b2f8;
    color: black;
    // border-radius: 30px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .itemBody{
    width: 90vw;
  }
}

</style>
