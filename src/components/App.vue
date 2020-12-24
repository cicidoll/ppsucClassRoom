<template>

  <div id="app" v-cloak>
    <div id="banner">
      <leftDraw></leftDraw>
      <div id="title">去哪学</div>
      <rightSearch></rightSearch>
    </div>

    <div id="body-content">
      <div class="block">
        <el-carousel trigger="click" height="130px">
          <el-carousel-item v-for="item in 4" :key="item">
            <h3 class="small" style="text-align: center;">
              <a href="https://github.com/cicidoll/ppsucClassRoom" target="_blank">Github链接地址</a><br>
              &nbsp;开发中···联系方式：ayaseemt@qq.com&nbsp;<br>
              &nbsp;17网二陈川&nbsp;
            </h3>
          </el-carousel-item>
        </el-carousel>
      </div>

      <dayRadio @selectDayFunc="selectDay"></dayRadio>

      <el-collapse >
        <el-collapse-item name="1">
          <template slot="title">
            上午1、2节&nbsp;&nbsp;&nbsp;&nbsp;{{roomData.am12.length}}间
          </template>
          <roomList :buildingName="buildingName"
                    :roomData="roomData.am12"></roomList>
        </el-collapse-item>

        <el-collapse-item name="2">
          <template slot="title">
            上午3、4节&nbsp;&nbsp;&nbsp;&nbsp;{{roomData.am34.length}}间
          </template>
          <roomList :buildingName="buildingName"
                    :roomData="roomData.am34"></roomList>
        </el-collapse-item>
        <el-collapse-item name="3">
          <template slot="title">
            上午空闲教室&nbsp;&nbsp;&nbsp;&nbsp;{{computed(roomData.am12, roomData.am34).length}}间
          </template>
          <roomList :buildingName="buildingName"
                    :roomData="computed(roomData.am12, roomData.am34)"></roomList>
        </el-collapse-item>
        <el-collapse-item name="4">
          <template slot="title">
            下午1、2节&nbsp;&nbsp;&nbsp;&nbsp;{{roomData.pm12.length}}间
          </template>
          <roomList :buildingName="buildingName"
                    :roomData="roomData.pm12"></roomList>
        </el-collapse-item>
        <el-collapse-item name="5">
          <template slot="title">
            下午3、4节&nbsp;&nbsp;&nbsp;&nbsp;{{roomData.pm34.length}}间
          </template>
          <roomList :buildingName="buildingName"
                    :roomData="roomData.pm34"></roomList>
        </el-collapse-item>
        <el-collapse-item name="6">
          <template slot="title">
            下午空闲教室&nbsp;&nbsp;&nbsp;&nbsp;{{computed (roomData.pm12, roomData.pm34).length}}间
          </template>
          <roomList :buildingName="buildingName"
                    :roomData="computed (roomData.pm12, roomData.pm34)"></roomList>
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
import dayRadio from './dayRadio.vue'
import roomList from './roomList.vue'
import axios from 'axios'
import leftDraw from './leftDraw.vue'
import rightSearch from './rightSearch.vue'

const apiUrl = 'http://api.ppsuc.production.cicidoll.top:3001/v1/classRoomData' // 传递教室数据的api服务器网址

export default {
  data () {
    return {
      // 1、教学楼选择
      buildingSelectFlag: '0', // 教学楼选择器的标签指向器
      buildingName: 'zhuJian', // 教学楼选择器的命名指向器
      // 2、日期选择
      day: 1, // selectDay的默认起始
      // 3、存放教室数据
      allRoomAllDayData: {},
      roomAllDayData: {},
      roomData: {'am12': [], 'am34': [], 'pm12': [], 'pm34': []}
      // 4、左抽屉控制
      // drawer: false
      // direction: 'ltr'
    }
  },
  components: {
    dayRadio,
    roomList,
    leftDraw,
    rightSearch
  },
  methods: {
    getData () {
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
      switch (index) {
        case 0:
          this.buildingName = 'zhuJian'
          break
        case 1:
          this.buildingName = 'zhongLou'
          break
        case 2:
          this.buildingName = 'XiPei'
          break
      }
      this.roomAllDayData = this.allRoomAllDayData[index][this.buildingName]
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
  width: 100%;
  display: flex;
  flex-direction: column;
  // 隐藏滚动条
  ::-webkit-scrollbar {
    width: 0 !important;
  }
  ::-webkit-scrollbar {
    width: 0 !important;height: 0;
  }

  #banner {
    height: 30%;
    width: 100%;
    background-color:#26b2f8;
    color: white;
    padding: 1% 1%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-content: center;
    #title{
      font-size: xx-large;
      align-self: end;
      text-align: center;
    }
  }

  #body-content {
    // height: 86%;
    min-height: 90%;
    width: 100vw;
    overflow: scroll;

    .el-collapse-item ul li{
      list-style-type: none;
    }
  }

  #buildingRadio {
    width: 100vw;
    display: flex;
    justify-content: center;
  }
}
</style>
