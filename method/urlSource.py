# -*-coding:utf-8 -*-
"""
# File       : urlSource.py
# Time       ：2022/11/30 14:26
# Author     ：Ya Potato
# File       ：
# Project    :PyCharm
"""
import requests, json, time
import random, pprint
import item, commentAPI

class urlSource():
    def __init__(self, file: str, numdata: int = None, url: str = None, method=None, **param):
        """
        :param file: JSON文件
        :param numdata: 数据量
        :param url: 影片URL
        :param method: 请求方式，默认为None
        :param param: None
        """
        self.file = file
        self.numdata = numdata
        self.url = url
        self.method = method

    # 获得API所需数据
    def urlSet(self):
        entity_id = item.item(self.file).package()[str(self.numdata)]
        entity_id1 = (entity_id['entity_id'])
        timestamp = (entity_id['timestamp'])
        sign = (entity_id['sign'])
        vedio_url = "https://mesh.if.iqiyi.com/tvg/pcw/base_info?entity_id={}&timestamp={}&" \
                    "src=pcw_tvg&vip_status=0&vip_type=&auth_cookie=&device_id=ae3660a6667720a508f88610df39e64b&user_id=" \
                    "&app_version=3.0.0&sign={}".format(entity_id1, timestamp, sign)

        return vedio_url

    # 请求数据
    def jsonGet(self, url):
        """
        :param url: 将JSON读取出来，并将其字典格式
        :return: 将API返回为JSON格式
        """
        # 随机休眠2到5秒
        time.sleep(random.randint(2, 5))

        return json.loads(requests.get(url).text)

    # 向API数据转化为JSON格式
    def urlGet(self):
        return self.jsonGet(self.urlSet())

    # 获取数据
    def analy(self):
        contextJs = self.urlGet()['data']['base_data']                      # 使用urlGet()方法将内容信息获取到
        contextJs_Movie_Url = self.urlGet()['data']['template']['pure_data']['film_feature_bk']['videos'][0]

        dic = {}                                                            # 字典存储
        movie_Name = (contextJs['title'])                                   # 电影名称
        vedio_Rank = (contextJs['board_info']['board_txt'])                 # 影片排行
        movie_Desc = (contextJs['desc'])                                    # 影片简介
        timeHot = (contextJs['heat'])                                       # 实时热度
        page_Url = (contextJs_Movie_Url['page_url'])                        # 影片URL
        movie_Poll = contextJs_Movie_Url['score']                           # 电影评分
        vedio_Id = (contextJs['_id'])                                       # 评论API参数1
        channel_Id = (contextJs['channel_id'])                              # 评论API参数2

        # 将数据存储为字典，为便携评论API获取
        dic["movie"] = {
            "data":
                {
                    "电影名称": movie_Name,
                    "影片排行": vedio_Rank,
                    "影片简介": movie_Desc,
                    "实时热度": timeHot,
                    "影片URL": page_Url,
                    "电影评分": movie_Poll,
                    "vedio_id": vedio_Id,
                    "channel_id": channel_Id,
                }
        }

        return dic

if __name__ == "__main__":
    file = "../data/package.json"
    dataNumber = int(item.item(file).numberDatas())
    test = urlSource(file, 1)
    # print(test)
    print(test.analy())

