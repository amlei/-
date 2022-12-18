# -*-coding:utf-8 -*-
"""
# File       : homePage.py
# Time       ：2022/12/6 8:46
# Author     ：Ya Potato
# File       ：
# Project    :PyCharm
"""
import json
import random
import time

from selenium import webdriver

def gainPopular(num: int):
    driver = webdriver.Chrome(executable_path=r"D:\材料\Softpack\脚本\chromedriver_win32\chromedriver.exe")
    driver.get("https://www.iqiyi.com/ranks1/1/0?vfrm=pcw_dianying&vfrmblk=711219_dianying_fyb&vfrmrst=711219_dianying_fyb_tag1")  # 页面

    time.sleep(3)

    for i in range(2):
        driver.execute_script("var a = document.documentElement.scrollTop=10000")
        time.sleep(3)

    movieName = driver.find_elements_by_xpath('//div[@class="rvi__tit1"]')                  # 电影名
    newlyUpDateTime = driver.find_elements_by_xpath('//span[@class="erji__meta__txt"]')     # 实时更数据更新时间
    barrages = driver.find_elements_by_xpath('//span[@class="rvi__tag rvi__tag1"]')         # 弹幕
    rankDays = driver.find_elements_by_xpath('//span[@class="rvi__tag rvi__tag2"]')         # 霸榜
    contents = driver.find_elements_by_xpath('//span[@class="rvi__type__txt"]')             # 上映日期与类被主演
    timeTimeRank = driver.find_elements_by_xpath('//span[@class="rvi__No__txt"]')           # 排行

    dic = {"数据更新时间": newlyUpDateTime[0].text}
    for i in range(num):
        movie_Name_List = movieName[i].text
        cut = contents[i].text.split("/")

        playDate = cut[0]           # 上映日期
        classification = cut[1]     # 影片类型
        mainAct = cut[-1]           # 主演

        dic[movie_Name_List] = {
            "弹幕数": barrages[i].text,
            "霸榜天数": rankDays[i].text,
            "上映日期": playDate,
            "影片类型": classification,
            "主演": mainAct,
            "排行": timeTimeRank[i].text
               }

    time.sleep(random.randint(2, 4))
    driver.quit()

    with open("./data/QiYi_Rank_Data.json", "w", encoding="utf-8") as file:
        json.dump(dic, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    gainPopular(5)
