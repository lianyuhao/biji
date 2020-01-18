# import  hashlib
# import sys
#
#
# def check_md5(fname):
#     m=hashlib.md5()
#     with open(fname,'rb') as fobj:
#         while 1:
#             data=fobj.read(4096)
#             if not data:
#                 break
#             m.update(data)
#     return m.hexdigest()
#
# if __name__ == '__main__':
#     resutl=check_md5(sys.argv[1])
#     print(resutl)
#
#
# # import  sys
# # import hashlib
# #
# # def check_md5(fname):
# #     m=hashlib.md5()
# #     with open(fname,'rb') as fobj:
# #         while 1:
# #             data=fobj.read(4096)
# #             if not data:
# #                 break
# #             m.update(data)
# #         return m.hexdigest()
# #
# # if __name__ == '__main__':
# #     resutl=check_md5(sys.argv[1])
# #     print(resutl)
#
# # import tarfile
# # tar=tarfile.open('/tmp/nsd1909/demo/a.tar.gz','w:gz')
# # tar.add('/tmp/a.txt')
# # tar.add('/tmp/b.txt')
# # tar.close()
# #
# # tar=tarfile.open('/tmp/nsd1909/demo/a.tar.gz')
# # tar.extractall(path='/tmp/nsd1909/demo')
# # tar.close()
#
#
# # import tarfile
# #
# # tar=tarfile.open('/tmp/nsd1909/demo/b.tar.gz','w:gz')
# # tar.add('/tmp/a.txt')
# # tar.add('/tmp/b.txt')
# # tar.close()
# #
# # tar=tarfile.open('/tmp/nsd1909/demo/b.tar.gz')
# # tar.extractall(path='/tmp/nsd1909/demo')
# # tar.close()
# from time import strftime
# print(strftime('%a'))