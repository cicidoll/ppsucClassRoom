<template>

  <div id="app" v-cloak>
    <div id="banner">

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
        <p slot="content">测试1：
          内容<br>
          内容<br>
          内容<br>
          内容<br>
        </p>
      </Panel>
      <Panel name="2">
        上午3、4节
        <p slot="content">测试2：
          内容<br>
          内容<br></p>
      </Panel>
      <Panel name="3">
        下午1、2节
        <p slot="content">测试3：
          内容<br>
          内容<br></p>
      </Panel>
      <Panel name="4">
        下午3、4节
        <p slot="content">测试4：
          内容<br>
          内容<br></p>
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

const axios = require('axios')

export default {
  data: function () {
    return {
      // activeKey: '1',
      roomAllDayData: {},
      value: '1'
    }
  },
  components: {
    daySelect,
    buildingSelect,
    Collapse,
    Panel
  },
  methods: {
    getData: function () {
      // Make a request for a user with a given ID
      // GET request for remote image
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8081/data',
        responseType: 'json'
      }).then(function (response) {
        // handle success
        console.log(response)
        return response
      }).catch(function (error) {
        // handle error
        console.log(error)
      })
    }
  }
}
</script>
