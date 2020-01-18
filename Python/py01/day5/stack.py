# stack=[]
#
# def push_it():
#     data=input('数据:')
#     stack.append(data)
#
# def pop_it():
#     if stack:
#         print(stack.pop())
#     else:
#         print('空')
#
# def vime_it():
#     print(stack)
#
# def nums_it():
#     ncmd={'0':push_it,'1':pop_it,'2':vime_it}
#     prompt='''(0) 压栈
# (1) 出栈
# (2) 查询
# (3) 退出
# 请选择(0/1/2/3): '''
#
#     while 1:
#         choice=input(prompt).strip()
#         if choice not in ['0','1','2','3']:
#             print('输错了,混蛋')
#             continue
#         # elif choice=='0':
#         #     push_it()
#         # elif choice=='1':
#         #     pop_it()
#         # elif choice=='2':
#         #     vime_it()
#         if choice=='3':
#             print('byebye')
#             break
#         ncmd[choice]()
#
#
#
#
# if __name__ == '__main__':
#     nums_it()

# adict=dict(['ab',('name','tom'),['age',20]])
# print(adict)
#
# bdict=dict([('name','bob'),('age','23')])
# print(bdict)
#
# cdict={}.fromkeys(('bod','alist'),23)
# print(cdict)
#
# for key in adict:
#     print(key,adict[key])
#
# adict['email']='tom@.com'
# print(adict)
#
# adict['age']=22
# print(adict)
#
# print(len(adict))
#
# print(hash(10))
# print(hash('aaa'))
# # print(hash(adict))
#
# print(adict.get('name'))
# print(adict.get('dsds'))
#
# print(adict.get('name','not faname'))
# print(adict.get('pheom','not fname'))
#
# # print(adict.keys())
# # print(adict.values())
# # print(adict.items())
#
# print(list(adict.keys()))
# print(list(adict.values()))
# print(list(adict.items()))
#
# print(adict.pop('a'))
# print(adict)

# import getpass
#
# userdb={}
#
# def zhu_ce():
#     username=input('user:').strip()
#     if username in userdb:
#         print('用户已存在')
#     else:
#         passwd=input('passwd:')
#         userdb[username]=passwd
#
# def deng_lu():
#     username = input('user:').strip()
#     passwd = getpass.getpass('passwd:')
#     if userdb[username] !=passwd:
#         print('登录失败')
#
#     else:
#         print('登录成功')
#
#
# def show_menu():
#     cmds={'0':zhu_ce,'1':deng_lu,}
#     pojb='''(0)注册
# (1)登录
# (2)退出
# 请选择(0/1/2):'''
#     while 1:
#         choice=input(pojb).strip()
#         if choice not in ['0','1','2']:
#             print('输错了混蛋')
#             continue
#         if choice=='2':
#             print('\nbyebye')
#             break
#         cmds[choice]()
#
# if __name__ == '__main__':
#     show_menu()

import getpass

# userdb={}
#
# def zhu_ce():
#     username=input('user:').strip()
#     if username in userdb:
#         print('用户%s已存在' % username)
#     else:
#         password=input('password:')
#         userdb[username]=password
#
# def dong_lu():
#     username=input('username:')
#     password=input('password:')
#     if userdb[username]!=password:
#         print('登录失败')
#     else:
#         print('登录成功')
#
# def show_meun():
#     promit=('''(0)注册用户
# (1)登录用户
# (2)退出
# 请选择(0/1/2):''')
#     cmds={'0':zhu_ce,'1':dong_lu}
#
#     while 1:
#         choice=input(promit).strip()
#
#         if choice not in '012':
#             print('\n张晋,在输错弹你小鸡鸡\n')
#             continue
#         if choice=='2':
#             break
#
#         cmds[choice]()
#
#
# if __name__ == '__main__':
#     show_meun()

# userdb={'tom':"123456"}
