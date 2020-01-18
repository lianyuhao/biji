# import json
#
# adict={'name':'tom','age':20}
# data=json.dumps(adict)
# print(type(data))
# print(data)
#
# jdata=json.loads(data)
# print(jdata)
# print(type(jdata))
# http://www.weather.com.cn/data/zs/101280101.html

# import requests
#
# r=requests.get('http://www.163.com')
# print(r.text)
#
# r=requests.get('https://i03picsos.sogoucdn.com/c2f73ee167629027')
# with open('/tmp/abcd.jpg','wb') as fobj:
#     fobj.write(r.content)

import requests
# url='http://www.weather.com.cn/data/zs/101280101.html'
# r=requests.get(url)
# r.encoding='utf8'
# print(r.json())

# url1='http://www.weather.com.cn/data/sk/101280101.html'
# r1=requests.get(url1)
# r1.encoding='utf8'
# print(r1.json())

# url2='http://www.weather.com.cn/data/cityinfo/101280101.html'
# r2=requests.get(url2)
# r2.encoding='utf8'
# print(r2.json())

# r=requests.get('http://www.jianshu.com')
# print(r.text)


# headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"}
# r=requests.get('http://www.jianshu.com',headers=headers)
# print(r.text)

# https://oapi.dingtalk.com/robot/send?access_token=49b14cbd69800cd0543baa0f36614aaa1b1b2bf48b47aa346bce0ad75e9dd8dc
url='https://www.kuaidi100.com/query'
params={'type':'yunda','postid':'4303568855784'}
r=requests.get(url,params=params)
print(r.json())

