# import requests
# import json
#
# url= 'http://192.168.1.12/api_jsonrpc.php'
#
# headers={'Content-Type':'application/json'}
#
# data={
#     "jsonrpc": "2.0",
#     "method": "apiinfo.version",
#     "params": [],
#     "id": 1
# }
#
# r=requests.post(url,headers=headers,data=json.dumps(data))
# print(r.json())



import requests
import json

url='http://192.168.1.12/api_jsonrpc.php'
headers={'Content-Type':'application/json'}

# data={
#     "jsonrpc": "2.0",
#     "method": "apiinfo.version",
#     "params": [],
#     "id": 666
# }

#9870bcdf4972d7a19b720004cb54a0b7
# data={
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }

# data={
#     "jsonrpc": "2.0",
#     "method": "user.get",
#     "params": {
#         "output": "extend"
#     },
#     "auth": "9870bcdf4972d7a19b720004cb54a0b7",
#     "id": 1
# }

# data={
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "filter": {
#             "host": [
#
#             ]
#         }
#     },
#     "auth": "9870bcdf4972d7a19b720004cb54a0b7",
#     "id": 1
# }

# data={
#     "jsonrpc": "2.0",
#     "method": "host.delete",
#     "params": [
#         "13"
#     ],
#     "auth": "038e1d7b1735c6a5436ee9eae095879e",
#     "id": 1
# }

# data={
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 "Linux servers"
#             ]
#         }
#     },
#     "auth": "9870bcdf4972d7a19b720004cb54a0b7",
#     "id": 1
# }

# data={
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux"
#             ]
#         }
#     },
#     "auth": "9870bcdf4972d7a19b720004cb54a0b7",
#     "id": 1
# }

data={
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "nsd1908web1",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.4.254",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"
            }
        ],
        "templates": [
            {
                "templateid": "10001"
            }
        ],
        "macros": [
            {
                "macro": "{$USER_ID}",
                "value": "123321"
            }
        ],
        "inventory_mode": 0,
        "inventory": {
            "macaddress_a": "fjdskf",
            "macaddress_b": "ereriwer"
        }
    },
    "auth": "9870bcdf4972d7a19b720004cb54a0b7",
    "id": 1
}


r=requests.post(url,headers=headers,data=json.dumps(data))
print(r.json())

