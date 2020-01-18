# import time
# import subprocess
# import os
#
# def ping(host):
#
#
#     resutl=subprocess.run('ping -c2 %s &>/dev/null' % host, shell=True)
#
#     if resutl.returncode == 0 :
#         print('%s :up' %  host)
#
#     else:
#         print('%s :down' % host)
#
#
#
#
#
#
# if __name__ == '__main__':
#
#     ips=['176.121.202.%s' % i for i in range(1,255)]
#
#     for ip in ips:
#         ret_val=os.fork()
#         if not ret_val:
#             ping(ip)
#             exit()


# import subprocess
# import os
#
# def ping(host):
#
#     resutl=subprocess.run('ping -c2 %s &>/dev/null' % host,shell=True)
#
#     if resutl.returncode==0:
#         print('%s:通' % host)
#
#     else:
#         print('%s:不通' % host)
#
# if __name__ == '__main__':
#     ips= ['176.121.202.%s' % i for i in range(1,255)]
#     for ip in ips:
#         ret_val=os.fork()
#         if not ret_val:
#             ping(ip)
#             exit()


# import subprocess
# import threading
#
#
# def ping(host):
#     resutl=subprocess.run('ping -c2 %s &>/dev/null' % host,shell=True)
#
#     if resutl.returncode==0:
#         print('%s:up' % host)
#     else:
#         print('%s:down'%host)
#
#
#
# if __name__ == '__main__':
#     ips=['176.121.202.%s' % i for i in range(1,255)]
#     for ip in ips:
#         t=threading.Thread(target=ping,args=(ip,))
#         t.start()

# import subprocess
#
# def ping(host):
#     resutl=subprocess.run('ping -c2 %s &>/dev/null' % host,shell=True)
#
#     if resutl.returncode==0:
#         print('%s:up' % host)
#     else:
#         print('%s:down'% host)
#
# if __name__ == '__main__':
#
#     ips=['176.121.202.%s' % i for i in range(1,255)]
#
#     for ip in ips:
#         ping(ip)



