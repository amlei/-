# -*-coding:utf-8 -*-
"""
# File       : commentAPI.py
# Time       ：2022/11/30 16:00
# Author     ：Ya Potato
# File       ：
# Project    :PyCharm
"""
import json, time, random
import pprint
import urlSource, item

class commentAPI():
    def __init__(self, file: str, numData: int, **param):
        """
        :param file: JSON文件
        :param numData: 影片数量
        :param param: None
        """
        self.file = file
        self.numData = numData
        self.urlSource = urlSource.urlSource(self.file, self.numData).analy()["movie"]["data"]  # URl数据资源
        self.channel_id = self.urlSource['channel_id']                           # 获取到评论API所需的channel_id和vedio_id
        self.vedio_id = self.urlSource['vedio_id']

    def APIurl(self):
        comment = "https://sns-comment.iqiyi.com/v3/comment/get_baseline_comments.action?agent_type=118&" \
                  "agent_version=9.11.5&authcookie=27nqDm2m3SF9PlUwm2HfS9eLtm3ZQyQfqraupibc8DMXRu4ieZuuF3JErem3m" \
                  "1fBm3jcuXIVMd3&business_type=17&channel_id={}&content_id={}&last_id=&need_vote=1&page_size=10&" \
                  "qyid=ae3660a6667720a508f88610df39e64b&sort=HOT&tail_num=1&"\
            .format(self.channel_id, self.vedio_id)                                     # API参数调整

        # 随机休眠2到5秒
        time.sleep(random.randint(2, 5))

        return urlSource.urlSource(self.file).jsonGet(comment)                       # 将API数据发送JSON格式数据转化为字典

    def commentDeal(self):
        dic = {"comment": {}}                                                           # 多条评论存储在一条影片中
        # 循环获取十条评论
        for i in range(0, 11):
            """
            在评论API中，有些评论无回复, 添加异常进行处理，若出现无回复的评论，则跳过该条回复评论。
            """
            try:
                APIData = self.APIurl()['data']['comments'][i]
                userName = (APIData['userInfo']['uname'])                               # 用户名
                comment_Content = (APIData['content'])                                  # 评论内容
                comment_Time = int(APIData['addTime'])                                  # 评论时间
                comment_Time_Deal = item.item().timeStamp(comment_Time)
                replySourceLocate = (APIData['replies'][0]['replySource']['location'])   # IP地点
                likes = (APIData['likes'])                                              # 点赞数

                """
                回复的评论信息
                """
                comment_Replies_APIData = APIData['replies'][0]
                comment_Replies = (comment_Replies_APIData['content'])                     # 评论回复
                comment_Replies_UserInfo = (comment_Replies_APIData['userInfo']['uname'])  # 回复该条评论的用户信息
                comment_Replies_UserInfo_Locate = (comment_Replies_APIData['location'])    # 回复该条评论的用户IP地点
                comment_Replies_UserInfo_Like = (comment_Replies_APIData['likes'])         # 回复该条评论的用户点赞数
                comment_AddTime = (comment_Replies_APIData['addTime'])                     # 回复该条评论的用户日期
                comment_AddTime_Deal = item.item().timeStamp(comment_AddTime)

                dic["comment"]["评论{:2<}".format(i + 1)] = {
                        "用户名": userName,
                        "评论内容": comment_Content,
                        "评论时间": comment_Time_Deal,
                        "IP地点": replySourceLocate,
                        "点赞数": likes,
                        "评论回复": {
                            "用户名": comment_Replies_UserInfo,
                            "评论时间": comment_AddTime_Deal,
                            "IP地点": comment_Replies_UserInfo_Locate,
                            "点赞数": comment_Replies_UserInfo_Like,
                            "回复内容": comment_Replies
                    }
                }

            except Exception as e:
                # 告知哪条评论无回复
                print("评论{:2<}".format(i) + "无回复内容,已跳过。")
                pass

        return dic

    # 将影片信息和评论总和
    def completely_Detailed(self):
        dic = {}

        dic[self.numData] = self.urlSource
        # 删除不需要的内容vedio_id和channel_id
        dic[self.numData].pop("vedio_id")
        dic[self.numData].pop("channel_id")
        dic[self.numData]["评论"] = self.commentDeal()['comment']

        return dic

if __name__ == "__main__":
    for i in range(1, 2):   # 循环次数代表查找的电影数量。
        # 随机休眠6至10秒
        time.sleep(random.randint(2, 4))
        test1 = commentAPI("../data/package.json", i).completely_Detailed()
        pprint.pprint(test1)



