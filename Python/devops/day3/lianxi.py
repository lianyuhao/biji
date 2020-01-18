# from collections import namedtuple
# Point=namedtuple('Point',['x','y','z'])
# p1=Point(10,11,12)
# print(p1)
# print(p1.x)
# print(p1.y)
# print(p1.z)
#
# '- name: configure webservers
#   hosts: webservers
#   tasks:
#     - name: install web pkgs
#       yum:
#         name: [httpd, php, php-mysql]
#         state: present
#     - name: configure web serivce
#       service:
#         name: httpd
#         state: started
#         enabled: yes
# [
# {
#         name: configure dbservers,
#         hosts: dbservers,
#         tasks: [
#             {
#                 name: install db pkgs,
#                 yum: {
#                     name: mariadb-server,
#                     state: present
#                 }
#             },
#             {
#                 name: configure db serivce,
#                 service: {
#                     name: mariadb,
#                     state: started
#                     enabled: yes
#                 }
#             }
#         ]
#     },
#     {
#         name: configure webservers,
#         hosts: webservers,
#         tasks:
#         [
#             {
#                 name: install web pkgs,
#                 yum:
#                     {
#                         name: [httpd, php, php-mysql],
#                         state: present
#                     }
#             },
#             {
#                 name: configure web serivce,
#                 service:
#                     {
#                         name: httpd,
#                         state: started,
#                         enabled: yes
#                     }
#             }
#         ]
# }
# ]