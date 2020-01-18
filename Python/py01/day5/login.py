# import getpass
# userdb={}
#
# def register():
#     username=input('username:')
#     if username in userdb:
#         print('\033[31;1m%s用户已存在\033[0m'%username)
#     else:
#         password=input('password:')
#         userdb[username]=password
#
# def login():
#     username=input('username:')
#     password=getpass.getpass('password:')
#     if userdb.get(username)!=password:
#         print('\033[31;1m登录失败\033[0m')
#     else:
#         print('\033[32;1m登录成功\033[0m')
#
#
# def shou_menu():
#     cmds={'0':register,'1':login}
#     prompt='''(0)注册
# (1)登录
# (2)退出
# 请选择(0/1/2):'''
#     while 1:
#         choice=input(prompt).strip()
#         if choice not in ['0','1','2']:
#             print('混蛋输错了')
#             continue
#         if choice=='2':
#             print('\nbyebye')
#             break
#         cmds[choice]()
#
#
# if __name__ == '__main__':
#     shou_menu()

