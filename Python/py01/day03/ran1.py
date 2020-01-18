# import random
# a='abcdefghijklnmopqrstuvwxyz0123456789ABCDEFGHIJKLNMOPQRSTUVWXYZ'
# n=int(input('weishu:'))
# def pas(n):
#     #f=print(random.choice(a))
#     for i in range(n):
#         f=random.choice(a)
#         print(f,end='')
# if __name__ == '__main__':
#     pas(n)

# f=open('/tmp/passwd')
# data=f.read()
# print(data)
# f.close()

# f=open('/tmp/passwd')
# print(f.read(4))
# print(f.readline())

# f=open('/tmp/passwd')
# for i in f:
#     print(i,end='')

# from random import choice
# import string
#
# a=string.ascii_letters+string.digits
# def pas (n=8):
#     f=''
#     for i in  range(n):
#         ch=choice(a)
#         f +=ch
#     return f
# if __name__ == '__main__':
#     print(pas())

# f= open('/tmp/a.txt','w')
# f.write('hello world!\n')
# f.close()

# f=open('/tmp/a.txt','w')
# f.writelines(['fdhasjf\n','siodhsakodjfo\n'])
# f.close()

# f= open('/tmp/a.txt','wb')
# f.write(b'hoell\n')

# f= open('/tmp/a.txt','wb')
# b1='你哦好\n'
# f.write(b1.encode())

# with  open('/tmp/a.txt') as  f:
#     print(f.read())

# f= open('/tmp/passwd','rb')
# # f.seek(16,0)
# # print(f.read(5))
# f.seek(-6,2)
# print(f.read())

# src='/bin/ls'
# dst='/tmp/list1'
#
# # s=open(src,'rb')
# # d=open(dst,'wb')
# #
# # data=s.read()
# # d.write(data)
# # s.close()
# # d.close()
#
# src='/bin/ls'
# dst='/tmp/list2'
# s=open(src,'rb')
# d=open(dst,'wb')
#
# while 1:
#     data=s.read(4096)
#     if not data:
#         break
#     d.write(data)
#
# s.close()
# d.close()

# def mk_fib():
#     fib=[0,1]
#     n=int(input("sdjak:"))
#     for i in range(n-2):
#         fib.append(fib[-1]+fib[-2])
#     print(fib)
# mk_fib()

# def mk_fib(n):
#     fib=[0,1]
#     for i in range(n-2):
#         fib.append(fib[-1]+fib[-2])
#     return fib
# for i in :
#     print(mk_fib(i))

# import sys
# def copy(src,dst):
#     s=open(src,'rb')
#     d=open(dst,'wb')
#     while 1:
#         data=s.read(4096)
#         if not data:
#             break
#         d.write(data)
#     s.close()
#     d.close()
# copy(sys.argv[1],sys.argv[2])

# def pstar(n=30):
#     print('*'*n)
# pstar(60)

# print('hello world!')
# if 3>0:
#     print('ok')
#     print('yes')
#
# x,y=3,4
# print(x+y)

# num=input('fjsa:')
# print(num)
# print(type(num))
