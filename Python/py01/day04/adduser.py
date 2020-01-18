# import sys
# import subprocess
# from randpass2 import randpass
#
# def add_user(user,passwd,fname):
#     result = subprocess.run('id %s &> /dev/null' %user,shell=True)
#     if result.returncode == 0:
#         print('用户已存在')
#         return
#





#     subprocess.run('useradd %s' % user ,shell=True)
#     subprocess.run('echo %s | passwd --stdin %s' % (passwd,user),shell= True)
#
#     info='username:%s\npassword:%s\n' % (user,passwd)
#
#     with open(fname,'a') as fboj:
#         fboj.write(info)
#
# if __name__ == '__main__':
#     user = sys.argv[1]
#     fname = sys.argv[2]
#     passwd = randpass()
#     add_user(user,passwd,fname)

#
# import sys
# import subprocess
# from randpass2 import  randpass
#
# def add_user(user,passwd,fname):
#     a_a=subprocess('id %s &> /dev/null' % user,shell=True)
#     if a_a.returncode == 0:
#         print("yhcz")
#         return
#     subprocess('useradd %s' % user ,shell=True)
#     subprocess('echo %s | passwd --stdin %s' % (passwd,user),shell=True)
#
#     info='dsjfsk:%s\ndsklfa:%s' % (user,passwd)
#
#     with open(fname,'a') as boj:
#         boj.write(info)
#
# if __name__ == '__main__':
#     user=sys.argv[1]
#     passwd=randpass()
#     fname=sys.argv[2]
#     add_user(user,passwd,fname)
    

