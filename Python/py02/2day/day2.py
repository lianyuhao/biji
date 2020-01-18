# def get_age(name,age):
#     print('%s is %s' % (name,age))

# if __name__ == '__main__':
#     get_age()

# def func1(*args):
#     print(args)
#
# def func2(**kwargs):
#     print(kwargs)
#
# def get_age(name,age):
#     print('%s is %s' % (name,age))

import random

# def plus():
#     print('0')
# def reduce():
#     print('1')
# def show_menu():
#     cmds={'0':plus,'1':reduce}
#
#     prompt='''(0)游戏开始
# (1)结束
# 请选择(0/1):'''
#
#
#     while 1:
#         choice=input(prompt).strip()
#
#         if choice not in ['0','1']:
#             print('无效输入,重新输入')
#             continue
#         if choice=='1':
#             print('\n886')
#             break
#         cmds[choice]()
#
# if __name__ == '__main__':
#     show_menu()

from random import randint,choice


def exam():
    nums=[randint(1,100) for i in range(2)]
    nums.sort(reverse=True)
    op= choice('+-*/')
    if op=='+':
        result=nums[0]+nums[1]
    elif op=='-':
        result=nums[0]-nums[1]
    elif op=='*':
        result=nums[0]*nums[1]
    else:
        result=nums[0]/nums[1]

    prompt='%s %s %s = '% (nums[0],op,nums[1])
    counter=0
    while counter<3:
        try:
            answer = int(input(prompt))
        except:
            print()
            continue

        if answer==result:
            print('very goot')
            break

        print('滚')
        counter+=1
    else:
        print('\033[31;1m正确答案: %s%s\033[0m' % (prompt, result))

def main():
    while 1:
        exam()
        try:
            yn=input('Coninue(y/n)?').strip()[0]
        except ImportError:
            print('重新输入')
            continue
        except (KeyboardInterrupt,EOFError):
            yn='n'
        if yn in 'nN':
            print('\n886')
            break

if __name__ == '__main__':
    main()