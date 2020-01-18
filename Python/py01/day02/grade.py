# chengji=int(input('请输入成绩:'))
# if 70>=chengji> 60:
#     print('及格')
# elif 80>=chengji >70:
#     print('良')
# elif 90>=chengji >80:
#     print('好')
# elif 100>=chengji >90:
#     print('优秀')
# else:
#     print('你要努力了')

# cj=int(input('成绩:'))
# if cj>=90:
#     print('优秀')
# elif cj>=80:
#     print('好')
# elif cj>=70:
#     print('良')
# elif cj>=60:
#     print('及格')
# else:
#     print('你很努力了')
# import random
# a=random.choice('abcdef')
# print(a)
#
# import  random
# b=input('请出拳:')
# a=random.choice(['石头','剪刀','布'])
# print(a)
# if a==b :
#     print('平局')
# elif

# import random
# choices = ['石头','剪刀','布']
# a=random.choice(choices)
# b=input('请出拳(石头/剪刀/布):')
# print('You choice:%s,Computer Choice:%s' %(a,b))
# if b=='石头':
#     if a=='石头':
#         print('\033[32;1m平局\033[0m')
#     elif a=='剪刀':
#         print('\033[31;1mYou WIN!!\033[0m')
#     else:
#         print('\033[31;1mYou LOSE!!\033[0m')
# elif b=='剪刀':
#     if a=='石头':
#         print('\033[31;1mYou LOSE!!\033[0m')
#     elif a=='剪刀':
#         print('\033[31;1m平局\033[0m')
#     else:
#         print('\033[32;1mYou WIN!!\033[0m')
# else :
#     if a=='石头':
#         print('\033[31;1mYou WIN!!\033[0m')
#     elif a=='剪刀':
#         print('\033[31;1mYou LOSE!!\033[0m')
#     else:
#         print('\033[32;1m平局\033[0m')
# import random
# a=random.choice(['石头','剪刀','布'])
# b=input('请出拳(石头/剪刀/布):')
# print('You choice:%s,Computer Choice:%s' %(a,b))
# if b==a:
#     print('\033[32;1m平局\033[0m')
# elif b!=a :

# import random
# b=random.choice(['石头','剪刀','布'])
# a=input('请出拳(石头/剪刀/布):')
# c=[['石头','剪刀'],['剪刀','布'],['布','石头']]
# print('You choice:%s,Computer Choice:%s' %(a,b))
# if a==b:
#     print('\033[32;1m平局\033[0m')
# elif [a,b] in c :
#     print('\033[31;1m你赢了\033[0m')
# else:
#     print('\033[31;1m你输了\033[0m')

# import  random
# d=['石头','剪刀','布']
# b=random.choice(d)
# f=int(input("""(0) 石头
# (1) 剪刀
# (2) 布
# 请选择:"""))
# c=[['石头','剪刀'],['剪刀','布'],['布','石头']]
# a = d[f]
# print('You choice:%s,Computer Choice:%s' %(a,b))
# if a==b:
#      print('\033[32;1m平局\033[0m')
# elif [a,b] in c :
#     print('\033[31;1m你赢了\033[0m')
# else:
#     print('\033[31;1m你输了\033[0m')
#
# resule=0
# counter=1

# while counter <= 100:
#     resule +=counter
#     counter +=1
# print('sum is %d' % resule)


# import  random
# d=['石头','剪刀','布']
# c=[['石头','剪刀'],['剪刀','布'],['布','石头']]
# f=("""(0) 石头
# (1) 剪刀
# (2) 布
# 请选择:""")
# cwim=0
# pwim=0
# while cwim<2 and pwim < 2:
#     b = random.choice(d)
#     e=int(input(f))
#     a = d[e]
#     print('You choice:%s,Computer Choice:%s' %(a,b))
#     if a==b:
#          print('\033[32;1m平局\033[0m')
#     elif [a,b] in c :
#         cwim += 1
#         print('\033[31;1m你赢了\033[0m')
#     else:
#         pwim += 1
#         print('\033[31;1m你输了\033[0m')
#
# import  random
# d=['石头','剪刀','布']
# c=[['石头','剪刀'],['剪刀','布'],['布','石头']]
# f=("""(0) 石头
# (1) 剪刀
# (2) 布
# 请选择:""")
# cwim=0
# pwim=0
# while 1:
#     b = random.choice(d)
#     e=int(input(f))
#     a = d[e]
#     print('You choice:%s,Computer Choice:%s' %(a,b))
#     if a==b:
#          print('\033[32;1m平局\033[0m')
#     elif [a,b] in c :
#         cwim += 1
#         print('\033[31;1m你赢了\033[0m')
#     else:
#         pwim += 1
#         print('\033[31;1m你输了\033[0m')
#     if pwim == 2 or cwim == 2:
#         break

# result = 0
# counter = 0
# while counter<100:
#     counter +=1
#     #if counter %2 == 1:
#     if counter %2:
#        continue
#     result += counter
# print(result)

# import random
# mun=random.randint(1,100)
# counter=0
# while counter<7:
#     answer=int(input('请输入数字(1~100):'))
#     if answer < mun :
#         print('你猜小了')
#     elif answer >mun:
#         print('你猜大了')
#     else:
#         print('你猜对了')
#         break
#     counter +=1
# else:
#     print('正确答案是:%d' % mun )

# s1 = 'abc'
# for ch in s1:
#     print(ch)
# print('#' * 30)
#
# muns=[101,120,110]
# for i in muns:
#     print(i)
# print('*' * 30)
#
# users=('tom','jerry','bob')
# for user in users:
#     print(user)
# print('*' * 30)
#
# adict = {'name':'tom','age':20}
# for key in adict:
#     print(key,adict[key])
# print('*' * 50)

# for i in range(10):
#     print(i)
#
# list(range(10))
# result =0
# for i in range(1,10000001):
#     result += i
# print(result)

# fib=[0,1]
# n=int (input('长度:'))
# for i in range(n):
#     fib.append(fib[-1]+fib[-2])
# print(fib)
# ip=for i in range(255)
# print(192.168.1.ip)







