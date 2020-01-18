# if 3>0:
#     print('yes')
#     print('ok')
#
# if 'to' in 'python':
#     print('true')
# else:
#     print('false')
#
# if -0.0:
#     print('任何值为0的数字都是False')
#
# if 0.001:
#     print('任何值为非0的数字都是True')
#
# if ' ':
#     print('空格也是一个字符,非空字符串为True')
#
# if [] :
#     print('任何空对象都是Flase')
#
# if not None :
#     print('None为flase,取反为true')
#
# if not 0 :
#     print('数字为0为flase,取反为true')
a,b=10,20
if a<=b:
    smaller=a
else:
    smaller=b
print(smaller)

a,b = 10,20
smaller = a if a <= b else b
print(smaller)

