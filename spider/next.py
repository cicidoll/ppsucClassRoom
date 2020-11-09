from lxml import etree
from urllib import parse
import requests
# import dryscrape

# weekPath = '/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]'
weekPath = "//div[@id='calendar_contain']/text()"

weekUrl = 'http://121.194.213.72' #基于校园内网地址进行爬取
ua = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'

with requests.get(weekUrl,headers={'User-agent':ua}) as response:
    content = response.text #HTML内容
    html = etree.HTML(content)
    print(content)
    # pathTemp = html.xpath(weekPath)
    # print(pathTemp)