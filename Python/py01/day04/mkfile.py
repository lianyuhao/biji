# def get_fname():
#     '用于获取文件名'
# def get_content():
#     '获取文件内容'
# def wfile(fname,content):
#     '写入文件'
# if __name__ == '__main__':
#     fname=get_fname()
#     content=get_content()
#     wfile(fname,content)

# import os
# def get_fname():
#     while 1:
#         finame=input('请输入新文件名:')
#         if not os.path.exists(finame):
#             break
#         print('文件已存在,请重试')
#     return finame
#
# def get_content():
#     coutent =[]
#     print('请输入内容,在单独一行输入end结束.')
#     while 1:
#         line=input('(end to quit)>')
#         if line=='end':
#             break
#         coutent.append(line)
#     return coutent
#
# def wfile(fname,content):
#     with open(fname,'w') as fobj:
#         fobj.writelines(content)
#
#
# if __name__ == '__main__':
#     fname=get_fname()
#     content=get_content()
#     content=['%s\n' % line for line in content]
#     wfile(fname,content)
#
# import os
#
# def get_fname():
#     while 1:
#         finame=input('请输入文件名:')
#         if not os.path.exists(finame):
#             break
#         print('文件已存在,重试')
#     return finame
#
# def get_content():
#     content=[]
#     print('输入内容,在输入end结束')
#     while 1:
#         lien=input('end to quit>')
#         if lien == 'end':
#             break
#         content.append(lien)
#     return content
#
# def wfite(fname,content):
#     with open(fname,'w') as fobj:
#         fobj.writelines(content)
#
# if __name__ == '__main__':
#     fname=get_fname()
#     content=get_content()
#     content=['%s\n' % lien for lien in content]
#     wfite(fname,content)

# nums=[2,10,8,6]
# print(reversed(nums))
# print(list(reversed(nums)))
#
# for i in reversed(nums):
#     print(i,end=' ')
#
# print(sorted(nums))

# user=['tom','jerrp','alice','zhigang']
# print(enumerate(user))
# print(list(enumerate(user
#             )))
# for data in enumerate(user):
#     print(data)
#
# for i,name in enumerate(user):
#     print('%s %s'% (i,name))

# print('%s is %s yesrs old' % ('tom',20))
#
# print('Hi %s' % 'tom')
#
# print('%s is %d' % ('tom',20))
#
# print('%s is %d ye old' % ('tom',20.5))
#
# print('%f' % (5/3))
#
# print('%.2f' % (10/3))
#
# print('%5.2f' % (1000/3))
#
# print('%8s%8s' % ('tom',20))
#
# print('%s%s' % ('ni','mei'))
#
# print('%-8s%-8s' % ('tom',20))
#
# print('%e' % 1230000)
#
# print('%#o' % 10)
#
# print('%#x' % 10)

# print('%s' % 'tom')
#
# print('%d' % 2.5)
#
# print('%e' % 123)
#
# print('%f' %  (5/3))
#
# print('{} is {} yes lsods' .format('tom',20))
#
# print('{} is {} sdjkslssdsa' .format(20,'tom'))
#
# print('{1} is {0} sdskldl' .format(20,'ton'))
#
# print('{0[0]} is {0[1]} sdskldl' .format(['ton',20]))

# sou= int(input('fs:'))
#
# if 70>sou>=60:
#     print('jg')
# elif 80>sou>=70:
#     print('lian')
# elif 90>sou>=80:
#     print('hao')
# elif sou>=90:
#     print('yx')
# else:
#     print('nynll')

# import random
# all_choices=['shitou','jiandao','bu']
# pas=random.choice(all_choices)
# p=input('qcq:')
# print('you ch:%s,com ch:%s' % (p,pas))
# if p=='shitou':
#     if pas=='shitou':
#         print('pj')
#     elif pas=='jiandao':
#         print('nyl')
#     else:
#         print('nsl')
# elif p=='jiandao':
#     if pas=='shitou':
#         print('nsl')
#     elif pas=='jiandao':
#         print('pj')
#     else:
#         print('nyl')
# else:
#     if pas=='shitou':
#         print('nyl')
#     elif pas=='jiandao':
#         print('nsl')
#     else:
#         print('pj')

# import random
# all_choices=['shitou','jiandao','bu']
# all_list=[['shitou','jiandao'],['jiandao','bu'],['bu','shitou']]
#
# p='''(0) shitou
# (1) jiandao
# (2) bu
# asjd(0/1/2):'''
#
# con=random.choice(all_choices)
# ind=int(input(p))
# pla=all_choices[ind]
#
# print('yuo chdsdj:%s ,congfdj:%s' % (pla,con))
#
# if pla==con :
#     print('\033[32;1m pj \033[0m')
# elif [pla,con] in all_list:
#     print('\033[31;1m you win \033[0m')
# else:
#     print('\033[31;1m you sdshidsa \033[0m')

# import  random
# num=random.randint(1,10)
# ru=True
#
# while ru:
#     an=int(input('fhdsja:'))
#     if an>num :
#         print('dl')
#     elif an<num:
#         print('xl')
#     else:
#         print('cdl')
#         ru=False



























