# import random
# num=random.randint(1,100)
# an=int(input('djskd:'))
# #while 1:
# if an>num:
#         print('da')
# elif an<num:
#         print('xiao')
# else:
#         print('dl')
# print(num)

# cj=int(input('sdjks:'))
#
# if cj>=90:
#     print('yx')
# elif cj>=80:
#     print('hao')
# elif cj>=70:
#     print('lian')
# elif cj>=60:
#     print('jg')
# else:
#     print('nl')

# from random import choice
# from string import ascii_letters,digits
# #all='qwerrtyuiopasdfghjklzxcvbnm132415647987'
# all=ascii_letters+digits
# def randpass(n=8):
#     #all='qwerrtyuiopasdfghjklzxcvbnm132415647987'
#     sou=''
#     for i in range(n):
#         ch=choice(all)
#         sou +=ch
#     return sou
#
# if __name__ == '__main__':
#     print(randpass())
#     print(randpass(6))

# from random import choice
# from string import printable
# all=printable
#
# def randpass(n=8):
#     sou = ''
#     for i in range(n):
#         ch=choice(all)
#         sou +=ch
#     return sou
#
# if __name__ == '__main__':
#     print(randpass())
#     print(randpass(9))

# from random import choice
# from string import hexdigits
# all=hexdigits
# def randpss(n=8):
#     sou=''
#     for i in range(n):
#         ch=choice(all)
#         sou +=ch
#     return sou
#
# if __name__ == '__main__':
#     print(randpss())
#     print(randpss(10))

# from random import choice
# from  string import  ascii_letters,digits
# all=ascii_letters+digits
#
# def randpass(n=8):
#     sou=''
#     for i in range(n):
#         ch=choice(all)
#         sou +=ch
#     return sou
# if __name__ == '__main__':
#     print(randpass())
#     print(randpass(10))
#     print(randpass(20))

# import  shutil
# f1=open('/bin/touch','rb')
# f2=open('/tmp/tch','wb')
#
# shutil.copyfileobj(f1,f2)
# f1.close()
# f2.close()
#
# shutil.copy('/etc/hosts','/tmp/')
# shutil.copy2('/etc/hosts','/tmp/zhuji')

# import shutil

# # f1= open('/etc/hosts','rb')
# # f2= open('/py/hs','wb')
# #
# # shutil.copyfileobj(f1,f2)
# #
# # shutil.copy('/etc/hosts','/tmp/')
# # shutil.copy2('/etc/hs','/pt/zhuji')
#
# shutil.copytree('/etc/security','/py/anquan')
# shutil.move('/py/anquan','/var/tmp/')
# shutil.chown('/py/anquan',user='tom',group='tom')

# import shutil
# shutil.copy('/etc/hosts','/py/tom')
# shutil.copy2(保留权限)
# shutil.move(移动)
# shutil.copytree(cp -r)
# shutil.chown('链接',user=,group=)
# shutil.rmtree('删除目录')

# import subprocess
# result= subprocess.run('ls /tmp',shell=True)
# print(result)
# import subprocess
# import shutil
# subprocess.run('ls')
# subprocess.run('ls /tmp',shell=True)

# shutil.rmtree('/var/tmp/anquan')
# import subprocess
#
# result=subprocess.run('ls /tmp',shell=True)
#
# print(result)
# print(result.args)
# print(result.returncode)

# import subprocess
# result=subprocess.run('id root;id zhangsan',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# print(result.stdout)
# print(result.stderr)
# print(result.stdout.decode())

