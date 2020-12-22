from lxml import etree
from urllib import parse
import requests
import json
import re
from interval import Interval

from lxml.html import tostring
import html

class netSpider:
  def __init__(self):
    self.baseUrl = 'http://121.194.213.115/swyt/jxcdkbcx.php' #基于校园内网地址进行爬取
    self.ua = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
    self.week = 10# http://121.194.213.72/ 教务处网站 获取实时教学周
    self.urlDic = {
                    'xnxq':"'2020-20211'"#查询日期,默认为2020-2021第一学期
                    #'jxcdmc'为教室get请求头
                    #  "%CD%C5%D6%FD%BD%A3%C2%A5"是由"团铸剑楼"gbk编码得来
                  }
    # 写入json的文本变量              
    self.jsonText = {'data':[]}
    self.tiaoTingJieYongKeJsonText = { "tiaoTing": {"zhuJian":  [],
                                                    "zhongLou": [],
                                                    "XiPei":    [] },
                                        "jieYong": {"zhuJian":  [],
                                                    "zhongLou": [],
                                                    "XiPei":    [] } }
    # # 铸剑楼教室
    # self.classRoomNumZhuJian = ['101','102','104','105','106','108','110','111','112',
    #                             '201','202','204','205','206','207','208','210',
    #                             '301','302','303','304','305','306','307','308','309',
    #                             '401','402','403','404','405','406','407','408','409','410','411',
    #                             '501','502','503','504','505','506','507','508','509','510','511' ]
    # # 中楼教室
    # self.classRoomNumZhong = ['103','104','107','110','112','113',
    #                           '203','204','205','206','207','208','210','211',
    #                           '303','304','305','306','307','308',
    #                           '407','408',
    #                           '503','504','505','506','507','510',
    #                           '603','607',
    #                           '703','704','705','707','708']
    # # 西配楼教室                          
    # self.classRoomNumXi = [ '102','103','104','105','106','109',
    #                         '202','203','204','205','206','209',
    #                         '302','303','304','305','306','309',
    #                         '402','403','404','405','406','409',
    #                         '502','503','504','505','506','509',]

    #测试用教室号
    self.classRoomNumZhuJian = ['104']#铸剑楼教室
    self.classRoomNumZhong = ['103']#中楼教室
    self.classRoomNumXi = ['102']#西配楼教室
    # 具体课表在网页中的路径表示
    self.pathPool = [#上午1、2节
                    "//table[@class='table table-bordered table-striped table-condensed']//tr[1]//td[2]/text()",
                    "//table[@class='table table-bordered table-striped table-condensed']//tr[1]//td[3]/text()",
                    "//table[@class='table table-bordered table-striped table-condensed']//tr[1]//td[4]/text()",
                    "//table[@class='table table-bordered table-striped table-condensed']//tr[1]//td[5]/text()",
                    "//table[@class='table table-bordered table-striped table-condensed']//tr[1]//td[6]/text()",
                    #上午3、4节
                    "//body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[2]/text()",
                    "//body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[3]/text()",
                    "//body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[4]/text()",
                    "//body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[5]/text()",
                    "//body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[6]/text()",
                    #下午1、2节
                    "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[2]/text()",
                    "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[3]/text()",
                    "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[4]/text()",
                    "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[5]/text()",
                    "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[6]/text()",
                    #下午3、4节
                    "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[2]/text()",
                    "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[3]/text()",
                    "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[4]/text()",
                    "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[5]/text()",
                    "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[6]/text()"]
    
  #生成当前教学楼所有教室的url池，以便下一步爬取
  def creatUrlPool(self, roomNumSelect):
      # url池:存放需要遍历的url 
      urlPool = []        
      if roomNumSelect is self.classRoomNumZhuJian:
          for roomNum in roomNumSelect:
              # 铸剑楼拼接字符串
              urlPool.append("{}?{}&jxcdmc=%27%CD%C5%D6%FD%BD%A3%C2%A5{}%27".format(self.baseUrl,parse.urlencode(self.urlDic),roomNum))
      elif roomNumSelect is self.classRoomNumZhong:
          for roomNum in roomNumSelect:
              # 中楼拼接字符串
              urlPool.append("{}?{}&jxcdmc=%27%CD%C5%D3%FD%BE%AF%D6%D0%C2%A5{}%27".format(self.baseUrl,parse.urlencode(self.urlDic),roomNum))
      elif roomNumSelect is self.classRoomNumXi:
          for roomNum in roomNumSelect:
              # 西配楼拼接字符串
              urlPool.append("{}?{}&jxcdmc=%27%CD%C5%D3%FD%BE%AF%CE%F7%C2%A5{}%27".format(self.baseUrl,parse.urlencode(self.urlDic),roomNum))
      return urlPool

  def RegStr(self, string):
      Reg1 = r'\d-\d\d'
      Reg2 = r'\d-\d'
      if re.search(Reg1,string) is None:
          it = re.search(Reg2,string)
      else:
          it = re.search(Reg1,string)

      numberList = str(it.group()).split('-')
      for i in range(len(numberList)):
        numberList[i] = int(numberList[i])
      
      #若有课，返回1；无课，返回0
      return 1 if self.week in Interval(numberList[0],numberList[1]) else 0


  #开始爬取
  def getResponse(self, roomNumSelect, flag):
      am12, am34, pm12, pm34 = [], [], [], []
      urlPool = self.creatUrlPool(roomNumSelect)
      
      if roomNumSelect is self.classRoomNumZhuJian:
          roomSelect = "zhuJian"
      elif roomNumSelect is self.classRoomNumZhong:
          roomSelect = "zhongLou"
      elif roomNumSelect is self.classRoomNumXi:
          roomSelect = "XiPei"

      for classRoomIndex,url in enumerate(urlPool):
          with requests.get(url,headers={'User-agent':self.ua}) as response:
              # 要设置响应包的编码格式为gbk，不然会乱码！！！
              response.encoding = "gbk"
              content = response.text #HTML内容
              htmlContent = etree.HTML(content)

              if flag is True:
                  count = 0
                  for path in self.pathPool:
                      pathTemp = htmlContent.xpath(path)
                      count+=1
                      pathFlag = 1#默认置1

                      #检测文本
                      if len(pathTemp)==0:
                        # 如果该节点中长度为0，则说明没有课。
                          pathFlag=0
                      else:
                        # 长度不为0，说明有课。结合具体的教学周，查询本教室当前教学周是否有课
                          pathTemp = max(pathTemp, key=len, default='')
                          pathFlag = self.RegStr(pathTemp)

                      #结果检测完毕
                      #append(0)为占位符,表示有课
                      if count<=5:
                          if pathFlag==0:
                              # pathFlag为0，代表无课
                              am12.append(int(roomNumSelect[classRoomIndex]))
                          else:
                              # pathFlag不为0，代表有课。向结果数组添加0，以示占位。
                              am12.append(0)
                      elif 5<count<=10:
                          if pathFlag==0:
                              am34.append(int(roomNumSelect[classRoomIndex]))
                          else:
                              am34.append(0)
                      elif 10<count<=15:
                          if pathFlag==0:
                              pm12.append(int(roomNumSelect[classRoomIndex]))
                          else:
                              pm12.append(0)
                      elif 15<count<=20:
                          if pathFlag==0:
                              pm34.append(int(roomNumSelect[classRoomIndex]))
                          else:
                              pm34.append(0)
                  # 将教室查询有无课结果写入jsonText变量中          
                  self.jsonText['data'].append( \
                                                {roomSelect: {'am12':am12, \
                                                              'am34':am34, \
                                                              'pm12':pm12, \
                                                              'pm34':pm34 } } )
              else:
                  # 调停课信息处理，当小于当前教学周时，不将其记录。
                  def decodeHtml(content):
                      # 将xpath解析得到的Element节点，解码为字符串并返回。
                      return html.unescape(etree.tostring(content)\
                                                .decode('gbk'))\
                                                .replace("\t", "")\
                                                .replace("\n", "")
                  pathTiaoTingKe = ".//div[@class='row-fluid sortable'][2] \
                                    /div[@class='box span12']/div[@class='box-content'] \
                                    /table/tbody/tr"
                  pathJieYong = ".//div[@class='row-fluid sortable'][3] \
                                  /div[@class='box span12']/div[@class='box-content'] \
                                  /table/tbody/tr"
                  # 该数据列表的具体长度
                  tiaoTingTimes = len(htmlContent.xpath(pathTiaoTingKe))
                  jieYongTimes = len(htmlContent.xpath(pathJieYong))

                  # 开始处理调停课信息
                  # 1、需要记录数据如下：
                  
                  for index in range(tiaoTingTimes):
                      pathContent = htmlContent.xpath(pathTiaoTingKe)[index]
                      # 原教学周索引为9，现教学周索引为15
                      oldWeek = int(decodeHtml(pathContent[9])[4:-6])
                      newWeek = int(decodeHtml(pathContent[15])[4:-6])
                      # 检测原教学周与现教学周若早于当前教学周，直接跳过该组数据。
                      if (self.week >= max(oldWeek,newWeek)): continue
                      # className = 4 # 课程名字
                      # classes = 7 # 调课类别
                      # oldDate = 8 # 原上课日期
                      # oldTimes = 11 # 原节次
                      # oldRoom = 12 # 原教室
                      # newDate = 14 # 现上课日期
                      # newTimes = 17 # 现节次
                      # newRoom = 18 # 现教室
                      # self.tiaoTingKeJsonText["tiaoTing"][roomSelect] \
                      #   .append( \
                      #     {int(roomNumSelect[classRoomIndex]): { 'className': className, \
                      #                                            'classes': classes, \
                      #                                            'oldDate': oldDate, \
                      #                                            'oldTimes': oldTimes, \
                      #                                            'oldRoom': oldRoom, \
                      #                                            'newDate': newDate } } )

  def init(self, flag):
      #flag 控制行为：true-查询课时空闲 false-查询调停课信息
      roomList = [self.classRoomNumZhuJian] #测试用
      # roomList = [self.classRoomNumZhuJian, self.classRoomNumZhong, self.classRoomNumXi]
      for roomNumSelect in roomList:
          self.getResponse(roomNumSelect, flag)    
      # 将得到的数据保存为本地json文件
      # jsondata = json.dumps(jsontext,indent=4,separators=(',', ': ')) # json格式美化写入（可选）
      return 0
      if flag :
          jsonName = "classRoomData.json"
          jsondata = json.dumps(self.jsonText)
      else :
          jsonName = "tiaoTingJieYong.json"
          jsondata = json.dumps(self.tiaoTingJieYongKeJsonText)
      writeFile = open(jsonName,'w')
      writeFile.write(jsondata)
      writeFile.close()

# 创建对象
newGet = netSpider()
# 初始化，开始请求查询
newGet.init(False)