<template>
  <div>
    <el-row>
      <el-radio-group v-model="daySelectFlag" @change="selectDay">
        <el-col :span="5">
          <el-radio-button label="1">周一</el-radio-button>
        </el-col>
        <el-col :span="5">
          <el-radio-button label="2">周二</el-radio-button>
        </el-col>
        <el-col :span="5">
          <el-radio-button label="3">周三</el-radio-button>
        </el-col>
        <el-col :span="5">
          <el-radio-button label="4">周四</el-radio-button>
        </el-col>
        <el-col :span="5">
          <el-radio-button label="5">周五</el-radio-button>
        </el-col>
      </el-radio-group>
    </el-row>
  </div>
</template>

<script>
export default {
  data () {
    return {
      daySelectFlag: '1' // 日期选择器的标签指向器
    }
  },
  methods: {
    selectDay (day) {
      this.$emit('selectDayFunc', day)
      this.daySelectFlag = day
    }
  }
}
</script>

<style lang="less" scoped>
.el-radio-group{
  width: 100%;
}
.el-col-5{
  width: 20%;
}
</style>
