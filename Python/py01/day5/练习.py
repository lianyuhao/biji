# sum100=0
# for i in range(1,101):
#     sum100 +=i
# print(sum100)

# fib=[0,1]
# n=int(input('请输入:'))
# for i in range(n):
#     fib.append(fib[-1]+fib[-2])
# print(fib)

# n=int(input('请输入:'))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('%s*%s=%s' %(j,i,i*j),end=' ')
#     print()


# alist=[1,8,10,66,16,88,4]
# alist[3]=66
# print(alist)
#
# alist[2:4]=[1,2,3,5,10]
#
# print(alist)
#
# alist[3:3]=[10,20]
# print(alist)
#
# alist[-1]=200
# print(alist)
#
# blist=[1,666,10,11,16,88]
# blist[-1]=[1,2,3]
#
# print(blist)

# alist.append(10)
#
# print(alist)
#
# alist.insert(-2,10)
#
# print(alist)
#
# alist.count(10)
# print(alist.count(10))
# print(alist)
#
# alist.extend([100,200,300])
# print(alist)


# blist.append(666) #追加
# print(blist)
#
# blist.insert(1,666)
# print(blist)
#
# print(blist.count(666))
#
# blist.extend([666,66,6])
# print(blist)
#
# alist.pop()
# print(alist)
#
# blist.pop(-3)
# print(blist)
#
# blist.remove(666)
# print(blist)

# print(alist.pop())
# print(blist.pop())

# print(alist.remove())
# print(blist.remove())

# print(alist.index(88))
# print(blist.index(16))


# alist.sort()
# print(alist)

# alist.reverse()
# print(alist)
#
# # alist.sort()
# alist.sort();alist.reverse()
# print(alist)
#
#
# blist.sort()
# print(blist)
#
# blist.reverse()
# print(blist)
#
# blist.sort() ; blist.reverse()
# print(blist)
#
#
# blist.reverse()
# blist.sort()
# print(blist .)

# clist=alist.copy()
# print(clist)

# clist.clear()
# print(clist)
#
# print(blist)
# dlist=blist.copy()
# dlist.sort()
# print(dlist)

# dlist.clear()
# print(dlist)

# print(alist)
# print(clist)
#
# clist.append(10)
# print(alist)
# print(clist)
#
# atuple=(10,20,30,10,50,60,8)
# print(atuple)
#
# # print(atuple.count(10))
# #
# # print(atuple.index(50))
# # a=(20)
# # print(type(a))
#
# # a=(10,)
# # print(type(a))
# # print(len(a))
#
# a=([1,2],)
# print(a)
# print(type(a))
# print(len(a))
#
# stack=[]
#
# def push_it():
#     item=input('item to push:')
#     stack.append(item)
#
# def pop_it():
#     if stack:
#         print('\033[31;1mPopped %s\033[0m' % stack.pop())
#     else:
#         print('\033[31;1mEmpty stack\033[0m')
#
# def view_it():
#     print('\033[32;1m%s\033[0m' % stack)
#
# def show_menu():
#     prompt='''(0)push_it
# (1)pop_it
# (2)wiew_it
# (3)quit
# Please input you choice(0/1/2/3):'''
#
#     cmds={'0':push_it,'1':pop_it,'2':view_it}
#
#     while 1:
#         choice=input(prompt).strip()[0]
#         if choice not in '0123':
#             print('不在')
#             continue
#
#         if choice=='3':
#             break
#
#
#     cmds[choice]()
#
#
# if __name__ == '__main__':
#     show_menu()
# stack=[]
# def push_it():
#     '用于实现压栈功能'
#     data=input('数据:').strip()
#     if data:
#         stack.append(data)
#     else:
#         print('\033[31;1m输入为空\033[0m')
#
# def pop_it():
#     '用于实现出栈功能'
#     if stack:
#         print('\033[032;1m从列表中,弹出了\033[0m\033[034;1m"%s"\033[0m' % stack.pop())
#     else:
#         print('\033[031;1m列表为空\033[0m')
#
# def view_it():
#     '用于实现查询功能'
#     print("\033[32;1m%s\033[0m" % stack)
# def show_menu():
#     '用于在屏幕上打印菜单，根据用户选择，调用相关功能函数'
#     cmds={'0':push_it,'1':pop_it,'2':view_it}
#     prompt='''(0) 压栈
# (1) 出栈
# (2) 查询
# (3) 退出
# 请选择(0/1/2/3): '''
#     while 1:
#         choice=input(prompt).strip()
#         if choice not in ['0','1','2','3']:
#             print('<<混蛋输错了,不是让你选择"0123"了吗>>')
#             continue
#         # elif choice =='0':
#         #     push_it()
#         # elif choice=='1':
#         #     pop_it()
#         # elif choice=='2':
#         #     view_it()
#         if choice=='3':
#             print('\nbyebye')
#             break
#
#         cmds[choice]()
# if __name__ == '__main__':
#     show_menu()

# import crypt
# from random import choice
# from string import ascii_letters
# a=ascii_letters
# def randpass(n=8):
#     result=''
#     for i in range(n):
#         ch=choice(a)
#         result += ch
#     return result
#
#
# password=input('passwd:')
#
# haxi=crypt.crypt(password,'$6$%s$' % randpass() )
# print(haxi)

# aset=set('abc')
# print(aset)
#
# bset=set('bcd')
# print(bset)
#
# cset=set(['tom','jerry','bob'])
# print(cset)

# for name in  cset:
#     print(name)
#
# print-aset)

# cset.add('alist')
# print(cset)
# cset.remove('bob')
# print(cset)
# cset.update(['zhangsan','lishi'])
# print(cset)

# dset=aset | bset
# print(dset)
#
# aa = aset.issubset(dset)
# print(aa)
#
# bb = dset.issuperset(aset)
# print(bb)

# stack=[]
#
# def push_it():
#     imte=input('数据:')
#     stack.append(imte)
#
# def pop_it():
#     if stack:
#         print('出栈%s' % stack.pop())
#     else:
#         print('空')
#
# def vime_it():
#     print(stack)
#
# def show_menu():
#     primpt='''(0)压栈
# (1)出栈
# (2)查询
# (3)退出
# 请选择(0/1/2/3):'''
#     cmds={'0':push_it,'1':pop_it,'2':vime_it}
#
#     while 1:
#         choice = input(primpt).strip()
#         if choice  not in '0123':
#             print('混蛋,都让你不要输错了:')
#             continue
#         if choice=='3' :
#             break
#
#         cmds[choice]()
#
# if __name__ == '__main__':
#     show_menu()

stack=[]

def push_it():
    data=input('数据:')
    stack.append(data)

def pop_it():
    if stack:
        print('已删除%s' % stack.pop())
    else:
        print('数据已空')

def vime_it():
    print(stack)

def show_menu():
    promct=('''(0)添加
(1)删除
(2)查询
(3)退出
请输入(0/1/2/3):''')

    cmds={'0':push_it,'1':pop_it,'2':vime_it}

    while 1:
        choice=input(promct).strip()

        if choice not in '0123':
            print('都叫你,输对了你妹')
            continue
        if choice=='3':
            break

        cmds[choice]()

if __name__ == '__main__':
    show_menu()