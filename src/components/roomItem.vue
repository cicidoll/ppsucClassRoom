<template>
  <div class="roomItem">
    <div class="itemName">
      {{itemName}}
    </div>
    <div class="itemBody">
      <el-collapse accordion>
        <el-collapse-item>
          <template slot="title">
            &nbsp;&nbsp;&nbsp;调停课信息 {{mobilizeData.length}}条
          </template>
          <roomItemTableMobilize :itemData="mobilizeData"></roomItemTableMobilize>
        </el-collapse-item>
        <el-collapse-item>
          <template slot="title">
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
  border-radius: 30px;
  .itemName{
    width: 10vw;
    font-size: 18px;
    border: 1px solid blue;
    border-radius: 30px;
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
