<template>
  <el-table
    stripe
    :data="tableData"
    style="width: 100%">
    <el-table-column
      prop="className"
      label="教室名">
    </el-table-column>
    <el-table-column
      prop="classes"
      label="调课类别">
    </el-table-column>
    <el-table-column
      prop="oldDate"
      label="原上课日期">
    </el-table-column>
    <el-table-column
      prop="oldTimes"
      label="原节次">
    </el-table-column>
    <el-table-column
      prop="oldRoom"
      label="原教室">
    </el-table-column>
    <el-table-column
      prop="newDate"
      label="现上课日期">
    </el-table-column>
    <el-table-column
      prop="newTimes"
      label="现节次">
    </el-table-column>
    <el-table-column
      prop="newRoom"
      label="现教室">
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
