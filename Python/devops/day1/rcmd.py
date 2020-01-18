# import paramiko
#
# def rcmd(host,user,passwd,command):
#     ssh=paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.connect(host,username=user,password=passwd)
#     stdin,stdout,stderr=ssh.exec_command(command)
#     out=stdout.read()
#     err=stderr.read()
#
#     if out:
#         print('\033[32;1m[%s] OUT:\n%s' % (host,out.decode()))
#
#     if err:
#         print('\033[31;1m[%s] ERR:\n%s' % (host,err.decode()))
#
#     ssh.close()
#
# if __name__ == '__main__':
#     rcmd('192.168.1.11','root','123456','id root; id zhsdas')
#
#     import paramiko
#
#
#     def rcmd(host, user, passwd, command):
#         ssh = paramiko.SSHClient()
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         ssh.connect(host, username=user, password=passwd)
#         stdin, stdout, stderr = ssh.exec_command(command)
#         out = stdout.read()
#         err = stderr.read()
#
#         if out:
#             print('\033[32;1m[%s] OUT:\n%s' % (host, out.decode()))
#
#         if err:
#             print('\033[31;1m[%s] ERR:\n%s' % (host, err.decode()))
#
#         ssh.close()
#
#
#     if __name__ == '__main__':
#         rcmd('192.168.1.11', 'root', '123456', 'id root; id zhsdas')




# import paramiko
#
# def rcmd(host,user,passwd,command):
#     ssh=paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.connect(host,username=user,password=passwd)
#     stdin,stdout,stderr=ssh.exec_command(command)
#     out=stdout.read()
#     err=stderr.read()
#
#     if out:
#         print('\033[32;1m[%s] OUT:\n%s' % (host,out.decode()))
#
#     if err:
#         print('\033[31;1m[%s] ERR:\n%s' % (host,err.decode()))
#
#     ssh.close()
#
# if __name__ == '__main__':
#     rcmd('192.168.1.11','root','123456','id root; id zhsdas')

import paramiko
import sys
import getpass
import os
import threading


def rcmd(host, user, passwd, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(command)
    out = stdout.read()
    err = stderr.read()

    if out:
        print('\033[32;1m[%s] OUT:\n%s' % (host, out.decode()))

    if err:
        print('\033[31;1m[%s] ERR:\n%s' % (host, err.decode()))

    ssh.close()


if __name__ == '__main__':
    # rcmd('192.168.1.11', 'root', '123456', 'id root; id zhsdas')
    if len(sys.argv) !=3:
        print("Usage: %s ipfile 'commands'" % sys.argv[0])
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('No such file:',sys.argv[1])
        exit(2)

    ipfile=sys.argv[1]
    cmds=sys.argv[2]
    passwd=getpass.getpass()
    with open(ipfile,'rb') as fobj:
        for lien in fobj:
            ip=lien.strip()
            t=threading.Thread(target=rcmd,args=(ip,'root',passwd,cmds))
            t.start()