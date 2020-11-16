from lxml import etree
from urllib import parse
import requests
import json
import re
from interval import Interval

baseUrl = 'http://121.194.213.115/swyt/jxcdkbcx.php' #基于校园内网地址进行爬取
ua = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'

# http://121.194.213.72/ 教务处网站 获取实时教学周
week = 10

urlDic = {
    'xnxq':"'2020-20211'"#查询日期,默认为2020-2021第一学期
    #'jxcdmc'为教室get请求头
    #  "%CD%C5%D6%FD%BD%A3%C2%A5"是由"团铸剑楼"gbk编码得来
}
classRoomNumZhuJian = ['101','102','104','105','106','108','110','111','112',
            '201','202','204','205','206','207','208','210',
            '301','302','303','304','305','306','307','308','309',
            '401','402','403','404','405','406','407','408','409','410','411',
            '501','502','503','504','505','506','507','508','509','510','511']#铸剑楼教室

classRoomNumZhong = ['103','104','107','110','112','113',
            '203','204','205','206','207','208','210','211',
            '303','304','305','306','307','308',
            '407','408',
            '503','504','505','506','507','510',
            '603','607',
            '703','704','705','707','708']#中楼教室

classRoomNumXi = ['102','103','104','105','106','109',
            '202','203','204','205','206','209',
            '302','303','304','305','306','309',
            '402','403','404','405','406','409',
            '502','503','504','505','506','509',]#西配楼教室

#测试用教室号
# classRoomNumZhuJian = ['101']#铸剑楼教室
# classRoomNumZhong = ['103']#中楼教室
# classRoomNumXi = ['102']#西配楼教室

pathPool = [#上午1、2节
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
    "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[6]/text()",
]

# 定义一个变量
jsontext = {'data':[]}

#生成当前教学楼所有教室的url池，以便下一步爬取
def creatUrlPool(roomNumSelect):
    urlPool = [] #url池, 存放需要遍历的url        
    if roomNumSelect is classRoomNumZhuJian:
        for roomNum in roomNumSelect:
            urlPool.append("{}?{}&jxcdmc=%27%CD%C5%D6%FD%BD%A3%C2%A5{}%27".format(baseUrl,parse.urlencode(urlDic),roomNum))#铸剑楼拼接字符串
    elif roomNumSelect is classRoomNumZhong:
        for roomNum in roomNumSelect:
            urlPool.append("{}?{}&jxcdmc=%27%CD%C5%D3%FD%BE%AF%D6%D0%C2%A5{}%27".format(baseUrl,parse.urlencode(urlDic),roomNum))#中楼拼接字符串
    elif roomNumSelect is classRoomNumXi:
        for roomNum in roomNumSelect:
            urlPool.append("{}?{}&jxcdmc=%27%CD%C5%D3%FD%BE%AF%CE%F7%C2%A5{}%27".format(baseUrl,parse.urlencode(urlDic),roomNum))#西配楼拼接字符串
    return urlPool

def RegStr(string):
    global week
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
    return 1 if week in Interval(numberList[0],numberList[1]) else 0


#开始爬取
def getResponse(roomNumSelect):
    am12, am34, pm12, pm34 = [], [], [], []
    urlPool = creatUrlPool(roomNumSelect)

    for classRoomIndex,url in enumerate(urlPool):
        with requests.get(url,headers={'User-agent':ua}) as response:
            content = response.text #HTML内容
            html = etree.HTML(content)

            count = 0
            for path in pathPool:
                pathTemp = html.xpath(path)
                count+=1
                pathFlag = 1#默认置1

                # max(list, key=len, default='')
                #检测文本
                if len(pathTemp)==0:
                    pathFlag=0
                else:
                    pathTemp = max(pathTemp, key=len, default='')
                    pathFlag = RegStr(pathTemp)

                #结果检测完毕
                #append(0)为占位符,表示有课
                if count<=5:
                    if pathFlag==0:#pathFlag为0，代表无课
                        am12.append(int(roomNumSelect[classRoomIndex]))
                    else:#pathFlag不为0，代表有课。向结果数组添加0，以示占位。
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

    if roomNumSelect is classRoomNumZhuJian:
        jsontext['data'].append( {'zhuJian': {'am12':am12, 'am34':am34, 'pm12':pm12, 'pm34':pm34}} )
    elif roomNumSelect is classRoomNumZhong:
        jsontext['data'].append( {'zhongLou': {'am12':am12, 'am34':am34, 'pm12':pm12, 'pm34':pm34}} )
    elif roomNumSelect is classRoomNumXi:
        jsontext['data'].append( {'XiPei': {'am12':am12, 'am34':am34, 'pm12':pm12, 'pm34':pm34}} )
    
    

roomList = [classRoomNumZhuJian, classRoomNumZhong, classRoomNumXi]
for roomNumSelect in roomList:
    getResponse(roomNumSelect)

#将得到的数据保存为本地json文件
# jsondata = json.dumps(jsontext,indent=4,separators=(',', ': '))
jsondata = json.dumps(jsontext)
f = open('classRoomData.json','w')
f.write(jsondata)
# f.write(jsontext)
f.close()

#path更新于2020/09/09
#周一到周五上午 1、2节课的path如下：
# //table[@class='table table-bordered table-striped table-condensed']//tr[1]//td[2]/text()
# //table[@class='table table-bordered table-striped table-condensed']//tr[1]//td[3]/text()
# //table[@class='table table-bordered table-striped table-condensed']//tr[1]//td[4]/text()
# //table[@class='table table-bordered table-striped table-condensed']//tr[1]//td[5]/text()
# //table[@class='table table-bordered table-striped table-condensed']//tr[1]//td[6]/text()
#周一到周五上午 3、4节课的path如下：
# //body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[2]/text()
# //body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[3]/text()
# //body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[4]/text()
# //body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[5]/text()
# //body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[6]/text()
#周一到周五下午 1、2节课的path如下：
# /html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[2]/text()
# /html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[3]/text()
# /html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[4]/text()
# /html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[5]/text()
# /html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[6]/text()
#周一到周五下午 3、4节课的path如下：
# /html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[2]/text()
# /html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[3]/text()
# /html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[4]/text()
# /html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[5]/text()
# /html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[6]/text()
