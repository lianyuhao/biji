import  getpass
import  requests
import json
headers={'Content-Type': 'application/json;charset=utf-8'}
# data={
#     "msgtype": "text",
#     "text": {
#         "content": "你的server已经爆炸,赶紧买火车票跑路.天王盖地虎"
#     },
#     "at": {
#         "atMobiles": [
#             "156xxxx8827",
#             "189xxxx8325"
#         ],
#         "isAtAll": False
#     }
# }
#
# data = {
#     "msgtype": "link",
#     "link": {
#         "text": """这个即将发布的新版本，创始人xx称它为“红树林”。
# 而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是“红树林”？天王盖地虎""",
#         "title": "唯美清纯小姐姐",
#         "picUrl": "https://img03.sogoucdn.com/app/a/100520021/ba78c2ef618cbe36bd8a4157368316ff",
#         "messageUrl": "https://www.baidu.com"
#     }
# }

# data={
#      "msgtype": "markdown",
#      "markdown": {
#          "title":"春节放假通知",
#          "text": "## 2020年春节放假安排\n" +
#                  "> 一共放假七天,天王盖地虎" +
#                  "> ![screenshot](https://i04picsos.sogoucdn.com/107fd61ab6812959)\n"  +
#                  "> ###### 2020年1月14日发布 [详细信息](http://www.baidu.cn/) \n"
#      },
#     "at": {
#         "atMobiles": [
#             "156xxxx8827",
#             "189xxxx8325"
#         ],
#         "isAtAll": False
#     }
#  }

# data={
#     "feedCard": {
#         "links": [
#             {
#                 "title": "清纯小姐姐,天王盖地虎",
#                 "messageURL": "https://www.jianshu.com",
#                 "picURL": "https://img01.sogoucdn.com/app/a/100520021/eff6777fb42dda0cd8729759734f4ed7"
#             },
#             {
#                 "title": "性感小姐姐,天王盖地虎",
#                 "messageURL": "https://www.baidu.com",
#                 "picURL": "https://img04.sogoucdn.com/app/a/100520021/09612c5ea01b7b38f8b5287516c61b57"
#             }
#         ]
#     },
#     "msgtype": "feedCard"
# }

# data={
#     "actionCard": {
#         "title": "乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身",
#         "text": """![screenshot](http://images.china.cn/attachement/jpg/site1000/20130705/002564bb1f4313406ea811.jpg)
#  ### 乔布斯 20 年前想打造的苹果咖啡厅
#  Apple Store 的设计正从原来满满的科技感走向生活化，而其生活化的走向其实可以追溯到 20 年前苹果一个建立咖啡馆的计划天王盖地虎""",
#         "hideAvatar": "0",
#         "btnOrientation": "0",
#         "btns": [
#             {
#                 "title": "这狗不错哦",
#                 "actionURL": "https://www.dingtalk.com/"
#             },
#             {
#                 "title": "不感兴趣",
#                 "actionURL": "https://www.dingtalk.com/"
#             }
#         ]
#     },
#     "msgtype": "actionCard"
# }
#
#
# url='https://oapi.dingtalk.com/robot/send?access_token=49b14cbd69800cd0543baa0f36614aaa1b1b2bf48b47aa346bce0ad75e9dd8dc'
#
# r=requests.post(url,headers=headers,data=json.dumps(data))
# print(r.json())
#
# #'https://oapi.dingtalk.com/robot/send?access_token=49b14cbd69800cd0543baa0f36614aaa1b1b2bf48b47aa346bce0ad75e9dd8dc'


