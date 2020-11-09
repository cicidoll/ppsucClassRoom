<template>

  <div id="app" v-cloak>
    <div id="banner">
      <span>17网二陈川毕设：去哪自习（施工中）</span>
    </div>

    <div id="body-content">
      <daySelect>
        <p slot="day1">周一</p>
        <p slot="day2">周二</p>
        <p slot="day3">周三</p>
        <p slot="day4">周四</p>
        <p slot="day5">周五</p>
      </daySelect>
    </div>

    <Collapse v-model="value">
      <Panel name="1">
        上午1、2节
        <p slot="content">
          {{roomData.am12}}
        </p>
      </Panel>
      <Panel name="2">
        上午3、4节
        <p slot="content">
          {{roomData.am34}}
        </p>
      </Panel>
      <Panel name="3">
        下午1、2节
        <p slot="content">
          {{roomData.pm12}}
        </p>
      </Panel>
      <Panel name="4">
        下午3、4节
        <p slot="content">
          {{roomData.pm34}}
        </p>
      </Panel>
    </Collapse>
    <buildingSelect id="building"></buildingSelect>
    <div id="footbar"></div>
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
