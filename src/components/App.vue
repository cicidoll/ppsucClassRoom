<template>

  <div id="app" v-cloak>
    <div id="banner">
      <span>去哪学</span>
    </div>

    <div id="body-content">
    <div class="block">
      <el-carousel trigger="click" height="130px">
        <el-carousel-item v-for="item in 4" :key="item">
          <h2 class="small" style="text-align: center;">
            &nbsp;开发中···&nbsp;<br>
            &nbsp;17网二陈川&nbsp;
          </h2>
        </el-carousel-item>
      </el-carousel>
    </div>

      <el-tabs v-model="activeName" :stretch="true" @tab-click="selectDay" style="padding-left: 20px;padding-right: 20px;">
        <!-- pane似乎无法添加@click事件，因此借用@tab-click事件，将pane的name传递过去。 -->
        <el-tab-pane label="周一" name="1" ></el-tab-pane>
        <el-tab-pane label="周二" name="2" ></el-tab-pane>
        <el-tab-pane label="周三" name="3" ></el-tab-pane>
        <el-tab-pane label="周四" name="4" ></el-tab-pane>
        <el-tab-pane label="周五" name="5" ></el-tab-pane>
      </el-tabs>

      <el-collapse >
        <el-collapse-item name="1">
          <template slot="title">
            上午1、2节&nbsp;&nbsp;&nbsp;&nbsp;{{roomData.am12.length}}间
          </template>
          <ul>
            <li v-for="(item, index) in roomData.am12" :key="index">
              {{item}}
            </li>
          </ul>
        </el-collapse-item>

        <el-collapse-item name="2">
          <template slot="title">
            上午3、4节&nbsp;&nbsp;&nbsp;&nbsp;{{roomData.am34.length}}间
          </template>
          <ul>
            <li v-for="(item, index) in roomData.am34" :key="index">
              {{item}}
            </li>
          </ul>
        </el-collapse-item>
        <el-collapse-item name="3">
          <template slot="title">
            上午空闲教室&nbsp;&nbsp;&nbsp;&nbsp;{{computed(roomData.am12, roomData.am34).length}}间
          </template>
          <ul>
            <li v-for="(item, index) in computed(roomData.am12, roomData.am34)" :key="index">
              {{item}}
            </li>
          </ul>
        </el-collapse-item>
        <el-collapse-item name="4">
          <template slot="title">
            下午1、2节&nbsp;&nbsp;&nbsp;&nbsp;{{roomData.pm12.length}}间
          </template>
          <ul>
            <li v-for="(item, index) in roomData.pm12" :key="index">
              {{item}}
            </li>
          </ul>
        </el-collapse-item>
        <el-collapse-item name="5">
          <template slot="title">
            下午3、4节&nbsp;&nbsp;&nbsp;&nbsp;{{roomData.pm34.length}}间
          </template>
        </el-collapse-item>
        <el-collapse-item name="6">
          <template slot="title">
            下午空闲教室&nbsp;&nbsp;&nbsp;&nbsp;{{computed (roomData.pm12, roomData.pm34).length}}间
          </template>
          <ul>
            <li v-for="(item, index) in computed (roomData.pm12, roomData.pm34)" :key="index">
              {{item}}
            </li>
          </ul>
        </el-collapse-item>
      </el-collapse>
      <div id="footbar"></div>
    </div>
    <buildingSelect id="building"></buildingSelect>
  </div>

</template>

<script>
import buildingSelect from './BuildingSelect.vue'

// const axios = require('axios')

export default {
  data () {
    return {
      // activeKey: '1',
      // activeNames: ['1'], // 内容选择器的标签指向器
      activeName: '1', // 日期选择器的标签指向器
      allRoomAllDayData: {},
      roomAllDayData: {},
      roomData: {'am12': [], 'am34': [], 'pm12': [], 'pm34': []},
      value: '1',
      day: 1
    }
  },
  components: {
    buildingSelect
  },
  methods: {
    // getData: function () {
    //   // Make a request for a user with a given ID
    //   // GET request for remote image
    //   axios({
    //     method: 'get',
    //     url: 'http://127.0.0.1:8081/data',
    //     responseType: 'json'
    //   }).then(function (response) {
    //     // handle success
    //     console.log(response)
    //     return response
    //   }).catch(function (error) {
    //     // handle error
    //     console.log(error)
    //   })
    // }
    getJsonData () {
      this.$http.get('static/classRoomData.json').then(res => {
        this.allRoomAllDayData = res.body['data']// 此处的res对象包含了json的文件信息和数据，我们需要的json数据存在于body属性中
        this.selectBuilding(0, 'zhuJian')
      }).then(() => {
        let tab = {name: this.day}
        this.selectDay(tab)
      })
    },
    selectBuilding (index, building) {
      this.roomAllDayData = this.allRoomAllDayData[index][building]
      let tab = {name: this.day}
      this.selectDay(tab)
    },
    selectDay (tab) {
      let day = tab.name
      day = Number(day)
      this.day = day
      let start = day - 1
      for (let list in this.roomAllDayData) {
        let res = []
        for (let i = start; i < this.roomAllDayData[list].length; i += 5) {
          if (this.roomAllDayData[list][i] !== 0) {
            res.push(this.roomAllDayData[list][i])
          }
        }
        this.roomData[list] = res
      }
    },
    computed (list1, list2) {
      let res = []
      let data1 = list1.slice(0)
      let data2 = list2.slice(0)
      while (data1.length !== 0 && data2.length !== 0) {
        if (data1[0] === data2[0]) {
          res.push(data1[0])
          data1.shift()
          data2.shift()
        } else if (data1[0] < data2[0]) {
          data1.shift()
        } else if (data1[0] > data2[0]) {
          data2.shift()
        }
      }
      return res
    }
  },

  created () {
    this.getJsonData()
  },

  mounted () {
    // this.selectBuilding(0, 'zhuJian')
    // console.log(this.allRoomAllDayData)
  }
}
</script>

<style lang="less" scoped>
#body-content {
  height: 83vh;
  width: 100vw;
  overflow: scroll;
}

.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 150px;
  margin: 0;
}
.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}
.el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
}
</style>
