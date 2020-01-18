# username=input('请输入用户名:')
# password=input('请输入密码:')
#
# if username=='bob'and password=='123456':
#     print('Login successful')
# else:
#     print('Login inorrect')

# cj=int(input('请输成绩:'))
# if cj>=90:
#     print('优秀')
# elif cj>=80:
#     print('好')
# elif cj>=70:
#     print('良')
# elif cj>=60:
#     print('及格')
# else:
#     print('你要努力了')

# import random
# ren=input('请出拳(石头/剪刀/布):')
# pc=random.choice(['石头','剪刀','布'])
# print('ren:%s,ps:%s' % (ren,pc))
# if ren=='石头':
#     if pc=='石头':
#         print('平局')
#     elif pc=='剪刀':
#         print('你赢了')
#     else:
#         print('你输了')
# elif ren=='剪刀':
#     if pc=='石头':
#         print('你输了')
#     elif pc=='剪刀':
#         print('平局')
#     else:
#         print('你赢了')
# else:
#     if pc=='石头':
#         print('你赢了')
#     elif pc=='剪刀':
#         print('你输了')
#     else:
#         print('平局')

# import random
# quan=['石头','剪刀','布']
# win=[['石头','剪刀'],['剪刀','布'],['布','石头']]
# ind='''(0)石头
# (1)剪刀
# (2)布)
# 请选择:'''
# cwin=0
# pwin=0
# while 1:
#     pc = random.choice(quan)
#     inb = int(input(ind))
#     ren = quan[inb]
#     print('ren:%s,ps:%s' % (ren, pc))
#     if ren == pc:
#         print('平局')
#     elif [ren, pc] in win:
#         pwin +=1
#         print('你赢了')
#     else:
#         pwin +=1
#         print('你输了')
#     if pwin ==2 or cwin==2:
#         break
result = 0   # 定义用于存储结果的变量
counter = 1  # 定义计数器

# 计数器不断的自增，每个计数器的值都累加到result中
while counter <= 100:
    result += counter
    counter += 1

print(result)
name=input('请输入用户名:')
# password=input('请输入密码:')
#
# if username=='bob'and password=='123456':
#     print('Login successful')
# else:
#     print('Login inorrect')

# cj=int(input('请输成绩:'))
# if cj>=90:
#     print('优秀')
# elif cj>=80:
#     print('好')
# elif cj>=70:
#     print('良')
# elif cj>=60:
#     print('及格')
# else:
#     print('你要努力了')

# import random
# ren=input('请出拳(石头/剪刀/布):')
# pc=random.choice(['石头','剪刀','布'])
# print('ren:%s,ps:%s' % (ren,pc))
# if ren=='石头':
#     if pc=='石头':
#         print('平局')
#     elif pc=='剪刀':
#         print('你赢了')
#     else:
#         print('你输了')
# elif ren=='剪刀':
#     if pc=='石头':
#         print('你输了')
#     elif pc=='剪刀':
#         print('平局')
#     else:
#         print('你赢了')
# else:
#     if pc=='石头':
#         print('你赢了')
#     elif pc=='剪刀':
#         print('你输了')
#     else:
#         print('平局')

# import random
# quan=['石头','剪刀','布']
# win=[['石头','剪刀'],['剪刀','布'],['布','石头']]
# ind='''(0)石头
# (1)剪刀
# (2)布)
# 请选择:'''
# cwin=0
# pwin=0
# while 1:
#     pc = random.choice(quan)
#     inb = int(input(ind))
#     ren = quan[inb]
#     print('ren:%s,ps:%s' % (ren, pc))
#     if ren == pc:
#         print('平局')
#     elif [ren, pc] in win:
#         pwin +=1
#         print('你赢了')
#     else:
#         pwin +=1
#         print('你输了')
#     if pwin ==2 or cwin==2:
#         break
result = 0   # 定义用于存储结果的变量
counter = 1  # 定义计数器

# 计数器不断的自增，每个计数器的值都累加到result中
while counter <= 100:
    result += counter
    counter += 1

print(result)