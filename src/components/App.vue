<template>

  <div id="app" v-cloak>
    <div id="banner">
      <span>17网二陈川-毕设<br>
              去哪学<br>
            （施工中···）</span>
    </div>

    <div id="body-content">
      <daySelect>
        <p slot="day1">周一</p>
        <p slot="day2">周二</p>
        <p slot="day3">周三</p>
        <p slot="day4">周四</p>
        <p slot="day5">周五</p>
      </daySelect>
      <Collapse v-model="value">
        <Panel name="1">
          <p>上午1、2节</p>
          <p>{{roomData.am12.length}}</p>
          <ul slot="content">
            <li v-for="(item, index) in roomData.am12" :key="index">
              {{item}}
            </li>
          </ul>
        </Panel>
        <Panel name="2">
          <p>上午3、4节</p>
          <p>{{roomData.am34.length}}</p>
          <p slot="content">
            {{roomData.am34}}
          </p>
        </Panel>
        <Panel name="3">
          <p>上午空闲教室</p>
          <p>{{computed (roomData.am12, roomData.am34).length}}</p>
          <p slot="content">
            {{computed (roomData.am12, roomData.am34)}}<br>
            测试<br>
            测试<br>
            测试<br>
            测试<br>
            测试<br>
            测试<br>
            测试<br>
            测试<br>
            测试<br>
            测试<br>
            测试<br>
            测试<br>
            测试<br>
          </p>
        </Panel>
        <Panel name="4">
          <p>下午1、2节</p>
          <p>{{roomData.pm12.length}}</p>
          <p slot="content">
            {{roomData.pm12}}
          </p>
        </Panel>
        <Panel name="5">
          <p>下午3、4节</p>
          <p>{{roomData.pm34.length}}</p>
          <p slot="content">
            {{roomData.pm34}}
          </p>
        </Panel>
        <Panel name="6">
          <p>下午空闲教室</p>
          <p>{{computed (roomData.pm12, roomData.pm34).length}}</p>
          <p slot="content">
            {{computed (roomData.pm12, roomData.pm34)}}
          </p>
        </Panel>
      </Collapse>
      <div id="footbar"></div>
    </div>
    <buildingSelect id="building"></buildingSelect>
  </div>

</template>

<script>
import buildingSelect from './BuildingSelect.vue'
import daySelect from './DaySelect.vue'

import Collapse from './Collapse.vue'
import Panel from './Panel.vue'

// const axios = require('axios')

export default {
  data: function () {
    return {
      // activeKey: '1',
      allRoomAllDayData: {},
      roomAllDayData: {},
      roomData: {'am12': [], 'am34': [], 'pm12': [], 'pm34': []},
      value: '1',
      day: 1
    }
  },
  components: {
    daySelect,
    buildingSelect,
    Collapse,
    Panel
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
    selectDay (day) {
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
</style>
