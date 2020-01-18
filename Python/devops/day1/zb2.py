# import os
# import time
#
# ret_val=os.fork()
#
# if ret_val:
#     print('父进程')
#     result=os.waitpid(-1,0)
#     print(result)
#     time.sleep(5)
# else:
#     print('子进程')
#     time.sleep(10)
#     print('child done')


import  os
import time

ret_val=os.fork()

if ret_val:
    print('父进程')
    resutl=os.waitpid(-1,0)
    print(resutl)
    time.sleep(5)
else:
    print('子进程')
    time.sleep(20)
    print('child done')