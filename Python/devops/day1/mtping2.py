# import subprocess
# import threading
#
# class Ping:
#     def __call__(self,host):
#         resutl=subprocess.run('ping -c2 %s &>/dev/null' % host,shell=True)
#         if resutl.returncode==0:
#             print('%s:up' % host)
#
#         else:
#             print('%s:down'% host)
#
# if __name__ == '__main__':
#     ips=['176.121.202.%s' % i for i in range(1,255)]
#     for ip in ips:
#         t=threading.Thread(target=Ping(),args=(ip,))
#         t.start()

import subprocess
import threading
class Ping:
    def __call__(self,host):
        resutl=subprocess.run('ping -c2 %s &>/dev/null' % host,shell=True)

        if subprocess.threading==0:
            print('%s:up' % host)
        else:

            print('%s:down' % host)

if __name__ == '__main__':

    ips=['176.121.202.%s' % i for i in range(1,255)]
    for ip in  ips:
        t=threading.Thread(target=Ping(),args=(ip,))
        t.start()