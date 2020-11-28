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

      <!-- <el-tabs v-model="activeName" :stretch="true" @tab-click="selectDay" style="padding-left: 20px;padding-right: 20px;">
        pane似乎无法添加@click事件，因此借用@tab-click事件，将pane的name传递过去。
        <el-tab-pane label="周一" name="1" ></el-tab-pane>
        <el-tab-pane label="周二" name="2" ></el-tab-pane>
        <el-tab-pane label="周三" name="3" ></el-tab-pane>
        <el-tab-pane label="周四" name="4" ></el-tab-pane>
        <el-tab-pane label="周五" name="5" ></el-tab-pane>
      </el-tabs> -->
      <div id="dayRadio">
        <el-radio-group v-model="daySelectFlag" @change="selectDay">
          <el-radio-button label="1">周一</el-radio-button>
          <el-radio-button label="2">周二</el-radio-button>
          <el-radio-button label="3">周三</el-radio-button>
          <el-radio-button label="4">周四</el-radio-button>
          <el-radio-button label="5">周五</el-radio-button>
        </el-radio-group>
      </div>

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
      <div id="test"></div>
    </div>

    <div id="buildingRadio">
      <el-radio-group v-model="buildingSelectFlag" @change="selectBuilding">
        <el-radio-button label="0">铸剑楼</el-radio-button>
        <el-radio-button label="1">中楼</el-radio-button>
        <el-radio-button label="2">西配</el-radio-button>
      </el-radio-group>
    </div>

  </div>

</template>

<script>
import axios from 'axios'

const apiUrl = 'http://localhost:3000/v1/test' // 传递教室数据的api服务器网址

export default {
  data () {
    return {
      // activeKey: '1',
      // activeNames: ['1'], // 内容选择器的标签指向器
      // activeName: '1', // 日期选择器的标签指向器
      daySelectFlag: '1', // 日期选择器的标签指向器
      buildingSelectFlag: '0', // 教学楼选择器的标签指向器
      allRoomAllDayData: {},
      roomAllDayData: {},
      roomData: {'am12': [], 'am34': [], 'pm12': [], 'pm34': []},
      value: '1',
      day: 1 // selectDay的默认起始
    }
  },
  methods: {
    getData () {
      // Make a request for a user with a given ID
      // GET request for remote image
      // 在axios中使用function () {}的写法，会导致this指向问题出错。
      // 解决方法：使用ES6箭头函数
      axios.get(apiUrl)
        .then((response) => {
          // handle success
          this.allRoomAllDayData = response['data']['data']
        })
        .then(() => {
          this.selectBuilding(0, 'zhuJian')
          this.selectDay(this.day)
        })
        .catch((error) => {
          // handle error
          console.log(error)
        })
    },
    selectBuilding (name) {
      let index = Number(name)
      let building
      switch (index) {
        case 0:
          building = 'zhuJian'
          break
        case 1:
          building = 'zhongLou'
          break
        case 2:
          building = 'XiPei'
          break
      }
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
    this.getData()
  }
}
</script>

<style lang="less" scoped>
#app {
  height: 100%;
  width: 100vw;
  display: flex;
  flex-direction: column;

  #banner {
    height: 6%;
    width: 100vw;
    background-color:#26b2f8;
    color: white;
    font-size: x-large;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
  }

  #body-content {
    height: 86%;
    width: 100vw;
    overflow: scroll;
  }

  #buildingRadio {
    height: 8%;
    width: 100vw;
    display: flex;
    justify-content: center;
  }
}
</style>
