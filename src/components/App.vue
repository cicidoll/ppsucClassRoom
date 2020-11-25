<template>

  <div id="app" v-cloak>
    <div id="banner">
      <span>17网二陈川-毕设<br>
              去哪学<br>
            （施工中···）</span>
    </div>

    <div id="body-content">
      <!-- <daySelect>
        <p slot="day1">周一</p>
        <p slot="day2">周二</p>
        <p slot="day3">周三</p>
        <p slot="day4">周四</p>
        <p slot="day5">周五</p>
      </daySelect> -->
      <el-tabs v-model="activeName" @tab-click="selectDay">
        <!-- pane似乎无法添加@click事件，因此借用@tab-click事件，将pane的name传递过去。 -->
        <el-tab-pane label="周一" name="1" ></el-tab-pane>
        <el-tab-pane label="周二" name="2" ></el-tab-pane>
        <el-tab-pane label="周三" name="3" ></el-tab-pane>
        <el-tab-pane label="周四" name="4" ></el-tab-pane>
        <el-tab-pane label="周五" name="5" ></el-tab-pane>
      </el-tabs>

      <el-collapse v-model="activeNames">
        <el-collapse-item name="1">
          <template slot="title">
            上午1、2节(当前:{{roomData.am12.length}})
          </template>
          <ul>
            <li v-for="(item, index) in roomData.am12" :key="index">
              {{item}}
            </li>
          </ul>
        </el-collapse-item>

        <el-collapse-item name="2">
          <template slot="title">
            上午3、4节(当前：{{roomData.am34.length}})
          </template>
          <ul>
            <li v-for="(item, index) in roomData.am34" :key="index">
              {{item}}
            </li>
          </ul>
        </el-collapse-item>
        <el-collapse-item name="3">
          <template slot="title">
            上午空闲教室(当前：{{computed(roomData.am12, roomData.am34).length}})
          </template>
          <ul>
            <li v-for="(item, index) in computed(roomData.am12, roomData.am34)" :key="index">
              {{item}}
            </li>
          </ul>
        </el-collapse-item>
        <el-collapse-item name="4">
          <template slot="title">
            下午1、2节(当前：{{roomData.pm12.length}})
          </template>
          <ul>
            <li v-for="(item, index) in roomData.pm12" :key="index">
              {{item}}
            </li>
          </ul>
        </el-collapse-item>
        <el-collapse-item name="5">
          <template slot="title">
            下午3、4节(当前：{{roomData.pm34.length}})
          </template>
        </el-collapse-item>
        <el-collapse-item name="6">
          <template slot="title">
            下午空闲教室(当前：{{computed (roomData.pm12, roomData.pm34).length}})
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
      activeNames: ['1'], // 内容选择器的标签指向器
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
        this.selectDay(this.day)
      })
    },
    selectBuilding (index, building) {
      this.roomAllDayData = this.allRoomAllDayData[index][building]
      this.selectDay(this.day)
    },
    selectDay (tab) {
      let day = tab.name
      day = Number(day)
      this.day = day
      // console.log(this.day);
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
</style>
