# Python_Spider
爱奇艺风云榜视频信息及评论采集

本项目仅做学习使用。

# 一、准备工作
第三方库：
1. pprint
2. selenium
>pip install pprint
>pip install selenium

浏览器插件：
[ChromeDriver](https://chromedriver.chromium.org/)或 [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

---

# 二、文件介绍
1.  [[#main.py]] —— 主文件
	- 主要用来控制所需的视频数量
2.  [[#homePage.py]] —— 风云榜封面信息获取
	- selenium采集
3.  [[#urlSource.py]] —— 视频信息链接API资源
4.  [[#commentAPI.py]] —— 评论API调用
5.  [[#item.py]] —— 方法调用
6. [[#package.json]] —— 视频sign和timestamp信息存储
---

# 三、使用介绍
**适合人员：**
- 掌握Python基础
- 正在学习爬虫
- 对面向对象感兴趣
- 初步了解面向对象
- 学生、对程序感兴趣

**前提条件：**
1. 更新你的driver路径
	在homePage.py文件内，将第16行的drive路径修改为你自己的
2. 增加你感兴趣的视频**entity_id**、**sign**和**timestamp**信息存储到*package.json*内
3. 将method文件夹设为Sources

## package.json
[[Package.png]]
entity_id、sign和timestamp信息获取方式：[[conent.png]]
**这三个信息非常重要，将是后面程序获取评论信息的关键**

当然里面还有**title**（影片名称），这一点也是需要添加进去的（程序未设置无该信息自动跳过，反而这个是同样是必要选项，如不需要，请看[[#main.py]]介绍）。因为在main方法中，需要告诉用户

>为什么我会选择手动将这三个重要信息存储下来，而不是利用它网站特有的相关参数生成器？
>	*答：**entity_id**在网页源码中就可获取到，而**sign**和**timestamp**这两个参数是函数生成，当我在使用~JS逆向分析~的时候，我发现遇到了我目前还未涉及到的知识*
>
>这样的操作还是相当于手动获取我想要的信息，什么时候才能实现自动化？
>	*答：该项目作为我的期末大作业，目前我正在学习JS相关技术，待学成归来也许会重拾这个项目（仅做学习使用）*
---
## main.py
该方法用于控制所需的视频数量，如设置的数量超出[[#package.json]]文件则会提示：<u>影片有效数在{:3<}至{:3<}范围, 您输入{}量已超出该范围！</u>

经过判断后，若正常进入下一步，则会先调用[[#homePage.py]]的*selenium*获取风云榜影片信息内容。（并将其保存至QiYi_Rank_Data.json文件）

紧接着调用[[#item.py]]方法，将评论API所需的必要参数<u>channel_id</u>和<u>vedio_id</u>获取，然后采集评论信息。

当然，笔者在程序中设置了多个随机休眠（经过测试，采集30个视频信息需要30分钟），因笔者担心不断调试会导致网址监测到，当你在运行的时候可以先试着5个视频，若想多个且快速就将[[#main.py]]、[[#urlSource.py]]、[[#commentAPI.py]]内设置的随机休眠数调小即可。

---
## homePage.py
~~无需修改~~

## urlSource.py
~~无需修改~~

## commentAPI.py
~~无需修改~~

## item.py
~~无需修改~~
