# -*-coding:utf-8 -*-
"""
# File       : item.py
# Time       ：2022/11/30 14:25
# Author     ：Ya Potato
# File       ：
# Project    :PyCharm
"""
import json, time
import commentAPI, urlSource

class item():
    def __init__(self, file: str = None, type=None, **param):
        """
        :param file: JSON文件
        :param type: 类型
        :param param: None
        """
        self.file = file
        self.type = type

    def package(self):
        return json.load(open(self.file, "r", encoding="utf-8"))

    # JSON数据条目
    def numberDatas(self):   # JSON数据条目
        return len(self.package())

    # 字典遍历API数据，在编写代码时仅输出KEY，方便查阅
    def dictionary(self, x):
        """
        :param x: 输入字典类型
        :return: 在测试代码时仅输出KEY，方便查阅
        """
        return [i for i in x]

    # 将时间戳格式化
    def timeStamp(self, t: int):
        """
        :param t: 时间戳类型，如: 1669950065，输出：12-02
        :return: 返回格式为：月-日
        """
        return time.strftime("%m-%d", time.localtime(t))

    # 选择获取内容
    def optionPrint(self, numdata: int, option=True, type: str = None, **param):
        """
        :param numdata: 获取的电影数量
        :param option: 选择类型，默认为True将影片与评论总和在一起。若为False，仅输出影片内容。
        :param type: 数据类型
        :param param: None
        :return: 返回option的数据
        """
        if option is True:
            return commentAPI.commentAPI(self.file, numdata).completely_Detailed()

        else:
            return commentAPI.commentAPI(self.file, numdata).commentDeal()


if __name__ == "__main__":
    test = ("../data/package.json")
    # print(item(file=test).optionPrint(1))
    movie_Progress = item(test).package()
    print(movie_Progress["1"]["title"])


