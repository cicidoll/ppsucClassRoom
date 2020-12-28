<template>

  <div id="app" v-cloak>
    <div id="banner">
      <leftDrawer></leftDrawer>
      <div id="title">去哪学</div>
      <rightSearch></rightSearch>
    </div>

    <div id="body-content">
      <div class="block">
        <el-carousel trigger="click" :height="carouselImageHeight + 'px'">
          <el-carousel-item v-for="imageItem in carouselImageUrl" :key="imageItem.id">
            <img ref="imageHeight" :src="imageItem.url" @load="imgLoad" />
          </el-carousel-item>
        </el-carousel>
      </div>

      <dayRadio @selectDayFunc="selectDay"></dayRadio>

      <el-collapse >
        <el-collapse-item name="1">
          <template slot="title">
            上午1、2节&nbsp;&nbsp;&nbsp;&nbsp;{{roomData.am12.length}}间
          </template>
          <roomList :roomData="roomData.am12"
                    :mobilizeData="buildingMobilizeRoom[buildingName]"
                    :borrowData="buildingBorrowRoom[buildingName]"></roomList>
        </el-collapse-item>

        <el-collapse-item name="2">
          <template slot="title">
            上午3、4节&nbsp;&nbsp;&nbsp;&nbsp;{{roomData.am34.length}}间
          </template>
          <roomList :buildingName="buildingName"
                    :roomData="roomData.am34"
                    :mobilizeData="buildingMobilizeRoom[buildingName]"
                    :borrowData="buildingBorrowRoom[buildingName]"></roomList>
        </el-collapse-item>
        <el-collapse-item name="3">
          <template slot="title">
            上午空闲教室&nbsp;&nbsp;&nbsp;&nbsp;{{computed(roomData.am12, roomData.am34).length}}间
          </template>
          <roomList :buildingName="buildingName"
                    :roomData="computed(roomData.am12, roomData.am34)"
                    :mobilizeData="buildingMobilizeRoom[buildingName]"
                    :borrowData="buildingBorrowRoom[buildingName]"></roomList>
        </el-collapse-item>
        <el-collapse-item name="4">
          <template slot="title">
            下午1、2节&nbsp;&nbsp;&nbsp;&nbsp;{{roomData.pm12.length}}间
          </template>
          <roomList :buildingName="buildingName"
                    :roomData="roomData.pm12"
                    :mobilizeData="buildingMobilizeRoom[buildingName]"
                    :borrowData="buildingBorrowRoom[buildingName]"></roomList>
        </el-collapse-item>
        <el-collapse-item name="5">
          <template slot="title">
            下午3、4节&nbsp;&nbsp;&nbsp;&nbsp;{{roomData.pm34.length}}间
          </template>
          <roomList :buildingName="buildingName"
                    :roomData="roomData.pm34"
                    :mobilizeData="buildingMobilizeRoom[buildingName]"
                    :borrowData="buildingBorrowRoom[buildingName]"></roomList>
        </el-collapse-item>
        <el-collapse-item name="6">
          <template slot="title">
            下午空闲教室&nbsp;&nbsp;&nbsp;&nbsp;{{computed (roomData.pm12, roomData.pm34).length}}间
          </template>
          <roomList :buildingName="buildingName"
                    :roomData="computed (roomData.pm12, roomData.pm34)"
                    :mobilizeData="buildingMobilizeRoom[buildingName]"
                    :borrowData="buildingBorrowRoom[buildingName]"></roomList>
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
import leftDrawer from './leftDrawer.vue'
import rightSearch from './rightSearch.vue'

const apiClassRoomUrl = 'http://api.ppsuc.production.cicidoll.top:3001/v1/classRoomData' // 传递教室数据的api服务器网址
const mobilizeBorrowUrl = 'http://api.ppsuc.production.cicidoll.top:3001/v1/mobilizeBorrow' // 调停课数据的api接口

export default {
  data () {
    return {
      // 1、教学楼选择
      buildingSelectFlag: '0', // 教学楼选择器的标签指向器
      buildingName: 'zhuJian', // 教学楼选择器的命名指向器
      // 2、日期选择
      day: 1, // selectDay的默认起始
      // 3、存放教室空闲课时数据
      allRoomAllDayData: {},
      roomAllDayData: {},
      roomData: {'am12': [], 'am34': [], 'pm12': [], 'pm34': []},
      // 4、调停课数据
      allBuildingMobilizeBorrowRoom: {'mobilize': { 'zhuJian': { '101': [], '102': [], '104': [], '105': [], '106': [], '108': [], '110': [], '111': [], '112': [], '201': [], '202': [], '204': [], '205': [], '206': [], '207': [], '208': [], '210': [], '301': [], '302': [], '303': [], '304': [], '305': [], '306': [], '307': [], '308': [], '309': [], '401': [], '402': [], '403': [], '404': [], '405': [], '406': [], '407': [], '408': [], '409': [], '410': [], '411': [], '501': [], '502': [], '503': [], '504': [], '505': [], '506': [], '507': [], '508': [], '509': [], '510': [], '511': [] }, 'zhongLou': {'103': [], '104': [], '107': [], '110': [], '112': [], '113': [], '203': [], '204': [], '205': [], '206': [], '207': [], '208': [], '210': [], '211': [], '303': [], '304': [], '305': [], '306': [], '307': [], '308': [], '407': [], '408': [], '503': [], '504': [], '505': [], '506': [], '507': [], '510': [], '603': [], '607': [], '703': [], '704': [], '705': [], '707': [], '708': []}, 'XiPei': { '102': [], '103': [], '104': [], '105': [], '106': [], '109': [], '202': [], '203': [], '204': [], '205': [], '206': [], '209': [], '302': [], '303': [], '304': [], '305': [], '306': [], '309': [], '402': [], '403': [], '404': [], '405': [], '406': [], '409': [], '502': [], '503': [], '504': [], '505': [], '506': [], '509': [] } }, 'borrow': { 'zhuJian': { '101': [], '102': [], '104': [], '105': [], '106': [], '108': [], '110': [], '111': [], '112': [], '201': [], '202': [], '204': [], '205': [], '206': [], '207': [], '208': [], '210': [], '301': [], '302': [], '303': [], '304': [], '305': [], '306': [], '307': [], '308': [], '309': [], '401': [], '402': [], '403': [], '404': [], '405': [], '406': [], '407': [], '408': [], '409': [], '410': [], '411': [], '501': [], '502': [], '503': [], '504': [], '505': [], '506': [], '507': [], '508': [], '509': [], '510': [], '511': [] }, 'zhongLou': {'103': [], '104': [], '107': [], '110': [], '112': [], '113': [], '203': [], '204': [], '205': [], '206': [], '207': [], '208': [], '210': [], '211': [], '303': [], '304': [], '305': [], '306': [], '307': [], '308': [], '407': [], '408': [], '503': [], '504': [], '505': [], '506': [], '507': [], '510': [], '603': [], '607': [], '703': [], '704': [], '705': [], '707': [], '708': []}, 'XiPei': { '102': [], '103': [], '104': [], '105': [], '106': [], '109': [], '202': [], '203': [], '204': [], '205': [], '206': [], '209': [], '302': [], '303': [], '304': [], '305': [], '306': [], '309': [], '402': [], '403': [], '404': [], '405': [], '406': [], '409': [], '502': [], '503': [], '504': [], '505': [], '506': [], '509': [] } }},
      buildingMobilizeRoom: {'zhuJian': { '101': [], '102': [], '104': [], '105': [], '106': [], '108': [], '110': [], '111': [], '112': [], '201': [], '202': [], '204': [], '205': [], '206': [], '207': [], '208': [], '210': [], '301': [], '302': [], '303': [], '304': [], '305': [], '306': [], '307': [], '308': [], '309': [], '401': [], '402': [], '403': [], '404': [], '405': [], '406': [], '407': [], '408': [], '409': [], '410': [], '411': [], '501': [], '502': [], '503': [], '504': [], '505': [], '506': [], '507': [], '508': [], '509': [], '510': [], '511': [] }, 'zhongLou': {'103': [], '104': [], '107': [], '110': [], '112': [], '113': [], '203': [], '204': [], '205': [], '206': [], '207': [], '208': [], '210': [], '211': [], '303': [], '304': [], '305': [], '306': [], '307': [], '308': [], '407': [], '408': [], '503': [], '504': [], '505': [], '506': [], '507': [], '510': [], '603': [], '607': [], '703': [], '704': [], '705': [], '707': [], '708': []}, 'XiPei': { '102': [], '103': [], '104': [], '105': [], '106': [], '109': [], '202': [], '203': [], '204': [], '205': [], '206': [], '209': [], '302': [], '303': [], '304': [], '305': [], '306': [], '309': [], '402': [], '403': [], '404': [], '405': [], '406': [], '409': [], '502': [], '503': [], '504': [], '505': [], '506': [], '509': [] }},
      buildingBorrowRoom: {'zhuJian': { '101': [], '102': [], '104': [], '105': [], '106': [], '108': [], '110': [], '111': [], '112': [], '201': [], '202': [], '204': [], '205': [], '206': [], '207': [], '208': [], '210': [], '301': [], '302': [], '303': [], '304': [], '305': [], '306': [], '307': [], '308': [], '309': [], '401': [], '402': [], '403': [], '404': [], '405': [], '406': [], '407': [], '408': [], '409': [], '410': [], '411': [], '501': [], '502': [], '503': [], '504': [], '505': [], '506': [], '507': [], '508': [], '509': [], '510': [], '511': [] }, 'zhongLou': {'103': [], '104': [], '107': [], '110': [], '112': [], '113': [], '203': [], '204': [], '205': [], '206': [], '207': [], '208': [], '210': [], '211': [], '303': [], '304': [], '305': [], '306': [], '307': [], '308': [], '407': [], '408': [], '503': [], '504': [], '505': [], '506': [], '507': [], '510': [], '603': [], '607': [], '703': [], '704': [], '705': [], '707': [], '708': []}, 'XiPei': { '102': [], '103': [], '104': [], '105': [], '106': [], '109': [], '202': [], '203': [], '204': [], '205': [], '206': [], '209': [], '302': [], '303': [], '304': [], '305': [], '306': [], '309': [], '402': [], '403': [], '404': [], '405': [], '406': [], '409': [], '502': [], '503': [], '504': [], '505': [], '506': [], '509': [] }},
      // 5、首页走马灯设置
      carouselImageUrl: [
        {id: 0, url: require('..\\..\\static\\image\\banner\\001.jpg')},
        {id: 1, url: require('..\\..\\static\\image\\banner\\002.jpg')},
        {id: 2, url: require('..\\..\\static\\image\\banner\\003.jpg')}
      ],
      carouselImageHeight: '' // 高度自适应
    }
  },
  components: {
    dayRadio,
    roomList,
    leftDrawer,
    rightSearch
  },
  methods: {
    getClassRoomData () {
      // 在axios中使用function () {}的写法，会导致this指向问题出错。
      // 解决方法：使用ES6箭头函数
      axios.get(apiClassRoomUrl)
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
    getMobilizeBorrow () {
      // 在axios中使用function () {}的写法，会导致this指向问题出错。
      // 解决方法：使用ES6箭头函数
      axios.get(mobilizeBorrowUrl)
        .then((response) => {
          // handle success
          this.allBuildingMobilizeBorrowRoom = response['data']
          this.buildingMobilizeRoom = this.allBuildingMobilizeBorrowRoom['mobilize']
          this.buildingBorrowRoom = this.allBuildingMobilizeBorrowRoom['borrow']
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
    },
    imgLoad () {
      this.$nextTick(() => {
        this.carouselImageHeight = this.$refs.imageHeight[0].height
      })
    }
  },
  created () {
    this.getClassRoomData()
    this.getMobilizeBorrow()
  },
  mounted () {
    this.carouselImageHeight = this.$refs.imageHeight[0].height
    window.addEventListener('resize', () => {
      this.carouselImageHeight = this.$refs.imageHeight[0].height
      this.imgLoad()
    }, false)
  }
}
</script>

<style lang="less" scoped>
#app {
  height: 100%;
  width: 100%;
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  display: flex;
  flex-direction: column;
  // 隐藏滚动条
  // ::-webkit-scrollbar {
  //   width: 0 !important;
  // }
  // ::-webkit-scrollbar {
  //   width: 0 !important;height: 0;
  // }

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
    .block{
      height: auto;
      width: auto;
      .el-carousel__container{
        height: 200px;
      }
      img {
        width: auto;
        height: auto;
        max-width: 100%;
        max-height: 100%;
      }
    }
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
