# from random import randint,choice
# def exam():
#     nums=[randint(1,100) for i in range(2)]
#     nums.sort(reverse=True)
#     op=choice('+-*/')
#     if op=='-':
#         resutl=nums[0]-nums[1]
#     elif op=='+':
#         resutl = nums[0] + nums[1]
#     elif op=='*':
#         resutl = nums[0] * nums[1]
#     else:
#         resutl = nums[0] / nums[1]
#
#     prompt='%s %s %s =' %(nums[0],op,nums[1])
#     counter=0
#     while counter<3:
#         answer=int(input(prompt))
#         if answer==resutl:
#             print('对')
#             break
#         print('滚')
#         counter+=1
#     else:
#         print('正确答案:%s%s' % (prompt,resutl))
#
#
# def main():
#     while 1:
#         exam()
#         try:
#             yn= input('请选择(y/n):').strip()[0]
#         except ImportError:
#             continue
#         except (KeyboardInterrupt,EOFError):
#             yn='Nn'
#         if yn in 'nN':
#             print('\n886')
#             break
#
# if __name__ == '__main__':
#     main()
#
# def add(x,y):
#     return x+y


# from random import  randint
#
# def func1(x):
#     return True if x %2==1 else False
#
# if __name__ == '__main__':
#     nums=[randint(1,100)for i in range(10)]
#     print(nums)
#     resutl=filter(func1,nums)
#     print(list(resutl))
#     resutl=filter(lambda x:True if x%2==1 else False,nums)
#     print(list(resutl))


# from random import  randint
#
# def func1(x):
#     return True if x%2==1 else False
#
# if __name__ == '__main__':
#     nums=[randint(1,100) for i in range(10)]
#     print(nums)
#     resutl=filter(func1,nums)
#     print(list(resutl))
#     resutl=filter(lambda x:True if x%2==1 else False,nums)
#     print(list(resutl))


# from random import  randint
#
# def func2(x):
#     return x*2
#
# if __name__ == '__main__':
#     nums=[randint(1,100)for i in range(10)]
#     print(nums)
#     resutl=map(func2,nums)
#     print(list(resutl))
#     resutl1=map(lambda x:x*2,nums)
#     print(list(resutl1))


# x=10
# def func1():
#     print(x)
#
# if __name__ == '__main__':
#     func1()

# def func2():
#     y=100
#     print(y)
#
# if __name__ == '__main__':
#     func2()


# x=10
# def func3():
#     x=200
#     print(x)
#
# func3()

# x=10
# def func4():
#     global x
#     x=100
#     print(x)
#
# func4()

# def add(a,b,c,d,e):
#     return a+b+c+d+e
# from functools import partial
# myadd=partial(add,10,20,30,40)
# print(myadd(3))
#
# print(int('10101100',base=2))

# from functools import  partial
# int2=partial(int,base=2)
# print(int2('1100001'))

# from functools import partial
# int2=partial(int,base=2)
# print(int2('11001100'))

# def func1(x):
#     if x ==1:
#         return 1
#
#     return x*func1(x-1)
#
# if __name__ == '__main__':
#     resutl=func1(5)
#     print(resutl)

# from random import randint,choice
#
# def qsort(seq):
#     if len(seq)<2:
#         return seq
#     middle=seq[0]
#     smaller=[]
#     larger=[]
#
#     for data in seq[1:]:
#         if data<=middle:
#             smaller.append(data)
#         else:
#             larger.append(data)
#
#     return qsort(smaller)+[middle]+qsort(larger)
#
#
#
# if __name__ == '__main__':
#     nums=[randint(1,100) for i in range(10)]
#     print(nums)
#     print(qsort(nums))


# def mygen():
#     yield 100
#     a=10
#     yield a
#     yield 1000
#
# if __name__ == '__main__':
#     mg=list(mygen())
#     print(mg)
#     mm=mygen()
#     for i in mm:
#         print(i)

# import sys
# sys.path.append()

import os
import pickle
from time import strftime

def save(fname):
    try:
        amount=int(input('有钱拿\033[031;1m( $ _ $ )\033[0m金额:'))
        comment=input('备注:')
    except ValueError:
        print('无效金额')
        return
    except (KeyboardInterrupt,EOFError):
        print('\n永别了')
        exit()

    date=strftime('%Y-%m-%d')
    with open(fname,'rb') as fobj:
        records=pickle.load(fobj)
    balance=records[-1][-2] + amount
    lien=[date,amount,0,balance,comment]
    records.append(lien)
    with open(fname,'wb') as fobj:
        pickle.dump(records,fobj)


def cost(fname):
    try:
        amount=int(input('没钱了\033[031;1m\(ˋ＾ˊ)\033[0m金额:'))
        comment=input('备注:')
    except ValueError:
        print('无效输入')
        return
    except (KeyboardInterrupt,EOFError):
        print('\n永别了兄弟')
        exit()
    date=strftime('%Y-%m-%d')
    with open(fname,'rb') as fobj:
        records=pickle.load(fobj)
        balance=records[-1][-2] - amount
        lien=[date,0,amount,balance,comment]
        records.append(lien)
        with open(fname,'wb') as fobj:
            pickle.dump(records,fobj)

def query(fname):
    with open(fname,'rb') as fobj:
        records=pickle.load(fobj)
    print('%-12s%-8s%-8s%-12s%-20s' % ('date','save','cost','balance','comment'))
    for lien in records:
        print('%-12s%-8s%-8s%-12s%-20s' % tuple(lien))


def show_menu():
    cmds={'0':save,'1':cost,'2':query}
    prompt='''(0)收入
(1)支出
(2)查询
(3)退出
请选择(0/1/2/3):'''
    fname = 'acconut.data'
    init_data = [['2019-01-09', 0, 0, 10000, 'init data']]
    if not os.path.exists(fname):
        with open(fname,'wb') as fobj:
            pickle.dump(init_data,fobj)
    while 1:
        try:
            choice=input(prompt).strip()
        except (KeyboardInterrupt,EOFError):
            choice='3'

        if choice not in ['0','1','2','3']:
            print('\033[33;1m不要输其他的,不然弹你\033[0m\033[31;1m小鸡鸡\033[0m\033[32;1m(＝^ω^＝)\033[0m')
            continue
        if choice=='3':
            print('\n\033[34;1m永别了兄弟\033[0m\033[32;1m(T_T)\033[0m')
            break
        cmds[choice](fname)

if __name__ == '__main__':
    show_menu()













