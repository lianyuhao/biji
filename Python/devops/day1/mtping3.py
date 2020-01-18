# import threading
# import  subprocess
#
# class Ping:
#     def __init__(self,host):
#         self.host=host
#
#     def __call__(self):
#         result=subprocess.run('ping -c2 %s &>/dev/null' % self.host,shell=True)
#         if result.returncode==0:
#             print('%s:up'% self.host)
#         else:
#             print('%s:down'% self.host)
#
# if __name__ == '__main__':
#     ips=['176.121.202.%s' % i for i in range(1,255)]
#     for ip in ips:
#         t=threading.Thread(target=Ping(ip))
#         t.start()



# import  subprocess
# import  threading
#
# class Ping:
#     def __init__(self,host):
#
#         self.host=host
#
#     def __call__(self):
#         resutl=subprocess.run('ping  -2c %s &>/dev/null' % self.host,shell=True)
#
#         if resutl.returncode==0:
#             print('%s:up' % self.host)
#
#         else:
#             print('%s:down' % self.host)
#
# if __name__ == '__main__':
#     ips=['176.121.202.%s' % i for i in range(1,255)]
#     for ip in ips:
#         t=threading.Thread(target=Ping(ip))
#         t.start()