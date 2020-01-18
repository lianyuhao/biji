# import  time
# print(time.time())
#
# print(time.ctime())
#
# print(time.localtime())

# t=time.localtime()
# print(t.tm_year)
# print(t.tm_yday)
# print(t.tm_wday)
# print(t.tm_hour)

# sou=0
#
# s1=time.time()
# for i in range(1,10000001):
#     sou +=i
# s2=time.time()
#
# print(sou)
# print(s2-s1)

# result=0
# a=time.time()
# for i in range(10000001):
#     result +=i
# b=time.time()
#
# print(result)
# print(b-a)

# print(time.sleep(3))

# print(time.strftime('%Y-%m-%d-%H-%M-%S'))
# print(time.strftime('%A'))
# print(time.strftime('%a'))


# t1=time.strptime('2020-01-08 10:30:00','%Y-%m-%d %H:%M:%S')
# print(t1)
#
# t=time.localtime()
# print(t)
#
# print(t>t1)
#
# t2='2020-01-09 10:30:00'
# t3=time.strptime(t2,'%Y-%m-%d %H:%M:%S')
# print(t3)
# print(t3>t)

# t9=time.strptime('2019-05-15 09:00:00','%Y-%m-%d %H:%M:%S')
# t12=time.strptime('2019-05-15 12:00:00','%Y-%m-%d %H:%M:%S')
#
# with open('weblog.txt') as fobj:
#     for lien in fobj:
#         t=time.strptime(lien[:19],'%Y-%m-%d %H:%M:%S')
#         if t9<=t<=t12:
#             print(lien,end='')

# t9=time.strptime('2019-05-15 09:00:00','%Y-%m-%d %H:%M:%S')
# t12=time.strptime('2019-05-15 12:00:00','%Y-%m-%d %H:%M:%S')
#
# with open('weblog.txt') as fobj:
#     for lien in fobj:
#         t=time.strptime(lien[:19],'%Y-%m-%d %H:%M:%S')
#         if t9<= t<=t12:
#             print(lien,end='')

# t9=time.strptime('2019-05-15 09:00:00','%Y-%m-%d %H:%M:%S')
# t12=time.strptime('2019-05-15 12:00:00','%Y-%m-%d %H:%M:%S')
# a=time.time()
# with open('weblog.txt') as fobj:
#     for lien in fobj:
#         t=time.strptime(lien[:19],'%Y-%m-%d %H:%M:%S')
#         if t9<=t<=t12:
#             print(lien,end='')
# b=time.time()
#
# print(b-a)

# t9=time.strptime('2019-05-15 09:00:00','%Y-%m-%d %H:%M:%S')
# t12=time.strptime('2019-05-15 12:00:00','%Y-%m-%d %H:%M:%S')
# a=time.time()
# with open('weblog.txt') as fobj:
#     for lien in fobj:
#         t=time.strptime(lien[:19],'%Y-%m-%d %H:%M:%S')
#         if t>t12:
#             break
#         if t>=t9:
#             print(lien,end='')
# b=time.time()
# print(b-a)

# import datetime
#
# print(datetime.datetime.now())

# from datetime import datetime
# print(datetime.now())
# t=datetime.now()
#
#
# print(t.year)
# print(t.month)
# print(t.day)
# print(t.hour)
# print(t.minute)
# print(t.second)
# print(t.m)
#
#
# print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#
# t2=datetime.strptime('2020-01-08 11:26:41','%Y-%m-%d %H:%M:%S')
# print(t2)

# from datetime import  datetime,timedelta
#
# days=timedelta(days=100,hours=1)
# t=datetime.now()
# print(t-days)
#
# print(t+days)

# from datetime import datetime,timedelta

# days=timedelta(days=100,hours=1)
# t=datetime.now()
# print(t-days)
# print(t+days)

# print(int('abc'))
# print(int('10'))


import os
import shutil
# print(os.listdir())

# os.mkdir('/tmp/aaa')
# print(os.listdir('/tmp'))

# # os.makedirs('/tmp/nsd1908/demo')
# # print(os.listdir('/tmp/nsd1908'))
#
# os.chdir('/tmp/nsd1908')
# print(os.getcwd())
#
# shutil.copy('/etc/hosts','hosts')
# os.mknod('test.txt')
# os.symlink('/etc/passwd','mima')
# print(os.listdir())

# os.makedirs('/tmp/nsd1909/demo')
# print(os.listdir('/tmp/nsd1909'))

# os.chdir('/tmp/nsd1909')
# print(os.getcwd())

# os.mknod('test.txt')
# shutil.copy('/etc/hosts','hosts')
# os.symlink('/etc/passwd','mima')

# print(os.listdir())

# os.chmod('hosts',0o600)
#
# print(0o644)
# # print(os.listdir('/tmp/nsd1909/hosts'))
# os.chmod('hosts',420)

# print(os.path.abspath('demo'))
# print(os.path.isabs('aaa/bbb'))
# print(os.path.isabs('/aaa/bbb'))
# print(os.path.isdir('demo'))
# print(os.path.isfile('hosts'))
# print(os.path.islink('mima'))
# print(os.path.ismount('/etc'))
# print(os.path.exists('/etc/hostname'))
# print(os.path.basename('/tmp/nsd1909/hosts'))
# print(os.path.dirname('/tmp/nsd1909/hosts'))
# print(os.path.split('/tmp/nsd1909/hosts'))
# print(os.path.join('/tmp/nsd1909','hosts'))

# print(os.path.basename('/tmp/nsd1909/hosts'))
# print(os.path.dirname('/tmp/nsd1909/hosts'))
# print(os.path.split('/tmp/nsd1909/hosts'))
# print(os.path.join('/tmp/nsd1909','hosts'))

# print(list(os.walk('/tmp/nsd1909')))
os.chdir('/tmp')
alist=list(os.walk('nsd1909'))
# print(alist[0])
# print(alist[1])
# print(alist[2])
# print(alist[3])

# for data in alist:
#     print(data)

# for path,folders,files in os.walk('nsd1909'):
#     print('%s:' %path)
#     for dir in  folders:
#         print(dir,end='\t')
#     for file in files:
#         print(file,end='\t')
#     print('\n')

# print(alist)
#
# import pickle
#
# shopping_list =['apple','banana','egg']
#
# with open('/tmp/a.txt','wb') as fojb:
#     pickle._dump(shopping_list,fojb)
#
# with open('/tmp/a.txt','rb') as fojb:
#     alist=pickle.load(fojb)
#
# print(type(alist))
#
# print(alist)

# import  pickle
# shouu_list=['apple','banana','egg']
#
# with open('/tmp/b.txt','wb') as fojb:
#     pickle.dump(shouu_list,fojb)
#
# with open('/tmp/b.txt','rb') as fojb:
#     alist=pickle.load(fojb)
# print(type(alist))
# print(alist)
