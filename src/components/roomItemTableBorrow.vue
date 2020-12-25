<template>
  <el-table
    stripe
    :data="tableData"
    style="width: 100%">
    <el-table-column
      prop="borrowDate"
      label="借用日期">
    </el-table-column>
    <el-table-column
      prop="borrowTime"
      label="借用时间">
    </el-table-column>
    <el-table-column
      prop="borrowReason"
      label="借用事由">
    </el-table-column>
  </el-table>
</template>

<script>
export default {
  props: ['itemData'],
  data () {
    return {
      tableData: this.itemData
    }
  }
}
</script>
