import getpass
import crypt
from ranpass import randpass

userdb={}

def zhu_ce():
    username=input('username:').strip()
    if username in userdb:
        print('请更换用户名,此用户名不可注册')
    else:
        password=getpass.getpass('password:')
        passwd=crypt.crypt(password,'$6$%s$' % randpass())
        userdb[username]=passwd

def deng_lu():
    username=input('username:')
    password = getpass.getpass('password:')
    passwd = crypt.crypt(password, userdb[username][:12])

    if userdb[username]!=passwd:
        print('登录失败')
    else:
        print('登录成功')

def show_menu():
    prompt='''(0)注册
(1)登录
(2)退出
请选择(0/1/2):'''

    cmds={'0':zhu_ce,'1':deng_lu}

    while 1:

        choice=input(prompt).strip()

        if choice not in '012':
            print('在输错,打你屁股')
            continue

        if choice=='2':
            print('已退出')
            break

        cmds[choice]()

if __name__ == '__main__':

    show_menu()
