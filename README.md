空闲教室查询网站-毕设版本
====
前文
----
工程施工中，不定时开发······<br>
本项目暂定开发框架为：Node.js（后端）+ Vue.js（前端框架,使用Vue-Cli脚手架,生产环境使用Element组件） + Python（数据抓取） + MySQL（数据库）<br>
初步开发目标为网站，后续根据工作量，可能增加App或微信小程序<br>

# 目录<br>
待施工<br>

# 项目路径<br>
待施工<br>

# 当前开发进度<br>
***
1.前端页面 逻辑初步搭建完毕,开始进行逻辑组件细节优化。<br>
***
2.Python数据爬取脚本已于2020.12.25全面完成。<br>
    (1)完成教学周课程是否为本周课程的正则匹配判定。<br>
    (2)2020.12.25更新：已完成对调停课、教室借用信息查询。<br>
***
3.开始着手进行页面UI美化。<br>
    (1)2020.12.25 暂定为UI初版。
***
4.后端数据接口：采用基于Node.js的Express框架搭建<br>
①2020.12.25 已更新空闲课时&&调停课Api接口<br>
②[空闲课时接口](http://api.ppsuc.production.cicidoll.top:3001/v1/classRoomData)
③[调停课信息接口](http://api.ppsuc.production.cicidoll.top:3001/v1/mobilizeBorrow)
[Github项目地址](https://github.com/cicidoll/ppsucClassRoomService)
***


# 项目分支说明<br>
    master分支为项目最初备份分支。
    test1分支为项目第一次开发备份点。
    temp1分支为当前开发环境下最新代码。
    production分支为预设生产环境代码分支

# 实例页面<br>
[页面链接](http://ppsuc.demo.cicidoll.top/)

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
