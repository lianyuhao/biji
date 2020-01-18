# for i in  e(1,10):
#     for j in range(1,i+1):
#         print('%d×%d=%d' % (j,i,j*i),end=' ')
#     print('')
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('hello',end=' ')
#     print('')
#
# for i in range(1,20):
#     for j in range(1,i+1):
#         print('%d×%d=%d' %(j,i,j*i),end=' ')
#     print('')

# import tushare
# import datetime
# now = datetime.datetime.now()
# print(now)

# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if( i != k ) and (i != j) and (j != k):
#                 print (i,j,k)

# f= open('/tmp/passwd')
# # data=f.read()
# # print(data)
# # data=f.read()
# # print(data)
# for line in f:
#     print(line,end='')
# f.close()

# f=open('/tmp/timg.jpg','rb')
# print(f.read(4096),end='')
# f.close()

# f=open('/tmp/a.txt','w','rb')
# f.write('hello world!\n')
# print(f)

# f=open('/tmp/b.txt','wb')
# f.write(b'Hello world!\n')
# b1='566.你好!\n'
# f.write(b1.encode())
# f.close()

# with open('/tmp/passwd',) as f:
#     print(f.readline())
#     f.readline()

# with open('/tmp/passwd') as f:
#     print(f.readlines(),end=' ')

# f=open('/tmp/passwd','rb')
# f.seek(16,0)
# print(f.readline(5))

# f=open('/tmp/passwd','rb')
# f.seek(-5,2)
# print(f.readline(4))

# f=open('/bin/ls','rb')
# data=f.read()
# g=open('/tmp/list','wb')
# g.write(data)
#
# f.close()
# g.close()

# src_fname = '/bin/ls'
# dst_fname = '/tmp/list2'
# src_fobj = open(src_fname,'rb')
# dst_fobj = open(dst_fname,'wb')
#
# while 1:
#     data =src_fobj.read(4096)
#     if not  data:
#     #if len(data) ==0
#     #if data == b""
#         break
#     dst_fobj.write(data)
#
# src_fobj.close()
# dst_fobj.close()

# src_fname='/bin/ls'
# dst_fname='/tmp/list3'
#
# src_fo=open(src_fname,'rb')
# dst_fo=open(dst_fname,'wb')
#
# while 1:
#     data=src_fo.read(4096)
#     if len(data)==0:
#     if data ==b'':
#     if not  data :
#         break
#     dst_fo.write(data)
#
# src_fo.close()
# dst_fo.close()
# def mk_fib():
#     fib = [0, 1]
#
#     n = int(input('长度: '))
#     for i in range(n - 2):
#         fib.append(fib[-1] + fib[-2])
#
#     print(fib)
# mk_fib()
# mk_fib()

# def mk_f():
#     fia=[0,1,2]
#     n=int(input('长度:'))
#     for i in range(n-2):
#         fia.append(fia[-1]+fia[-2])
#     return fia
# alist=mk_f()
# print(alist)
# blist= [i * 2 for i in alist]
# print(blist)

# def mk_fib():
#     fib=[0,1]
#     n=int(input('长度:'))
#     for i in range(n - 2):
#         fib.append(fib[-1]+fib[-2])
#
#     return fib
# alist=mk_fib()
# print(alist)
# blist=[i*2 for i in  alist]
# print(blist)

# def mk_fib():
#     fib=[1,2]
#     n=int(input('长度:'))
#     for i in range(n -2):
#         fib.append(fib[-1]+fib[-2])
#
#     return fib
# alist = mk_fib()
# print(alist)
# blist=[i*2 for i in alist]
# print(blist)

# def mk_fib(n):
#     fib=[0,1]
#     #n=int(input('长度:'))
#     for i in range(n -2):
#         fib.append(fib[-1]+fib[-2])
#     return fib
# for i in [5,8,6,10,20]:
#     print(mk_fib(i))

# def mk_fib(n):
#     fib=[0,1]
#     for i in range(n-2):
#         fib.append(fib[-1]+fib[-2])
#     return fib
# for i in [12,13,14,15]:
#     print(mk_fib(i))

# import sys
# print(sys.argv)
#
# src_fname = '/bin/ls'
# dst_fname = '/tmp/list2'
# src_fobj = open(src_fname,'rb')
# dst_fobj = open(dst_fname,'wb')
#
# while 1:
#     data =src_fobj.read(4096)
#     if not  data:
#     #if len(data) ==0
#     #if data == b""
#         break
#     dst_fobj.write(data)
#
# src_fobj.close()
# dst_fobj.close()

# import sys
# print(sys.argv)
#
# src_fname = sys.argv[1]
# dst_fname = sys.argv[2]
# src_fobj = open(src_fname,'rb')
# dst_fobj = open(dst_fname,'wb')
#
# while 1:
#     data =src_fobj.read(4096)
#     if not  data:
#         break
#     dst_fobj.write(data)
#
# src_fobj.close()
# dst_fobj.close()
# import sys
#
# def copy(src_fname,dst_fname):
#     src_fobj = open(src_fname,'rb')
#     dst_fobj = open(dst_fname,'wb')
#     while 1:
#         data= src_fobj.read(4096)
#         if not data :
#             break
#         dst_fobj.write(data)
#     src_fobj.close()
#     dst_fobj.close()
#
# copy(sys.argv[1],sys.argv[2])

# import sys
# def cp(src_fname,dst_fname):
#     src_fobj=open(src_fname,'rb')
#     dst_fobj=open(dst_fname,'wb')
#     while 1:
#         data=src_fobj.read(4096)
#         if not data:
#             break
#         dst_fobj.write(data)
#
#     src_fobj.close()
#     dst_fobj.close()
# cp(sys.argv[1],sys.argv[2])

def pstar(n=30):
    print('*'*n)

print(pstar())
print(pstar(60))


