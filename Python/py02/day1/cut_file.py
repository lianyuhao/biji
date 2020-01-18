# from datetime import datetime
# t9=datetime.strptime('2019-05-15 09:00:00','%Y-%m-%d %H:%M:%S')
# t12=datetime.strptime('2019-05-15 12:00:00','%Y-%m-%d %H:%M:%S')
# with open('weblog.txt') as fobj:
#     for lien in fobj:
#         t=datetime.strptime(lien[:19],'%Y-%m-%d %H:%M:%S')
#         if t>t12:
#             break
#         if t>=t9:
#             print(lien,end='')

# try:
#     num = int(input('number:'))
#     result=100/num
#     print(result)
#     print('Done')
# except ValueError:
#     print('只接受数字')
# except ZeroDivisionError:
#     print('在输"0",打死你')
# except KeyboardInterrupt:
#     print('\nbeybey')
# except EOFError:
#     print('\nbeybey')

# try:
#     num=int(input('number:'))
#     resutl=100/num
#     print(resutl)
#     print('Done')
# except ValueError:
#     print('只接受数字')
#
# except ZeroDivisionError:
#     print('在输"0",打死你')
#
# except KeyboardInterrupt:
#     print('\nbeybey')
#
# except EOFError:
#     print('\nbeybey')

# try:
#     num=int(input('number:'))
#     resutl=100/num
#
# except (ValueError,ZeroDivisionError) as e:
#     print('只接受非零数字',e)
# except (KeyboardInterrupt,EOFError):
#     print('\nbeybey')
#
# print(resutl)
# print('Done')

# try:
#     num=int(input('number:'))
#     resutl=100/num
#
# except (ValueError,ZeroDivisionError) as e:
#     print('只接受非零数字',e)
# except (KeyboardInterrupt,EOFError):
#     print('\nbeybey')
#     exit(101)
# else:
#     print(resutl)
# print('Done')

# try:
#     num=int(input('number:'))
#     resutl=100/num
#
# except (ValueError,ZeroDivisionError) as e:
#     print('只支持非零的数字',e)
#
# except (KeyboardInterrupt,EOFError):
#     print('\nbeybey')
#     exit(101)
# else:
#     print(resutl)
# finally:
#     print('Done')
#
# with open('xxx') as f:
#     try:
#         f.read(10)
#     finally:
#         f.close()

# try:
#     num=int(input('number:'))
#     resutl=100/num
#
# except (ValueError,ZeroDivisionError) as e:
#     print('dsad',e)
# except (KeyboardInterrupt,EOFError):
#     print('beybey')
#     exit(101)
# else:
#     print(resutl)
# finally:
#     print('Done')

# raise ValueError
