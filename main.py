# -*-coding:utf-8 -*-
"""
# File       : main.py
# Time       ：2022/11/30 13:09
# Author     ：Ya Potato
# File       ：
# Project    :PyCharm
"""
"""这里为主方法"""
import requests, json, time, random, pprint
from method import commentAPI, urlSource, item, homePage

file = "./data/package.json"
# 获取到的影片总数量。
movie_Number = item.item(file=file).numberDatas()

# 此处为输入获取的电影数量。
user_Number = int(input("请输入所需爬取影片数量(1-{}):\n"
                        .format(movie_Number)))

#  对输入需要的影片数量进行异常判断。
if user_Number > movie_Number or user_Number < 1:
    print("影片有效数在{:3<}至{:3<}范围, 您输入{}量已超出该范围！"
          .format(1, movie_Number, movie_Number))

else:
    # 由于selenium获取界面响应最大影片数仅有三十部，故在此增加条件判断
    if user_Number > 30:
        homePage.gainPopular(30)  # 运行selenium，获取风云榜封面信息
    else:
        homePage.gainPopular(user_Number)

    # 保存数据
    saveFile = open("./data/QiYi_SaveData.json", "w", encoding="utf-8")
    movie_Progress = item.item(file=file).package()

    # 循环次数代表查找的电影数量。
    for i in range(1, user_Number + 1):
        # 打印输出影片爬取进程
        print("正在爬取第{}条影片：《{}》，请等待……"
              .format(i, movie_Progress[str(i)]["title"]))

        # 随机休眠3至7秒
        time.sleep(random.randint(3, 7))

        # 将影片与评论总和在一起。
        # 默认为True
        option = item.item(file=file).optionPrint(i)

        json.dump(option, saveFile, indent=4, ensure_ascii=False)

        # 格式化输出数据
        # pprint.pprint(option)

        print("该影片已爬取完毕，即将进行下一项进程。")
    saveFile.close()
    print("您所需数据爬全部爬取完成，数据文件存储在本目录data/QiYi_SaveData.json。")


