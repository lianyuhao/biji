import time
import os
import pickle as p


def spend_money(record,wallet):
    date=time.strftime('%Y-%m-%d %H:%M:%S')
    amount=int(input('金额:'))
    comment=input('备注:')

    with open('wallet','rb') as fobj:
        balance=p.load(fobj)-amount

    with open(wallet,'wb') as fobj:
        p.dump(balance,fobj)

    with open(record,'a') as fobj:
        fobj.write(date,amount,'n/a',balance,comment)

def save_money(record,wallet):
    date = time.strftime('%Y-%m-%d %H:%M:%S')
    amount = int(input('金额:'))
    comment = input('备注:')
    with open('wallet','rb') as fobj:
        balance=p.load(fobj)+amount

    with open(wallet,'wb') as fobj:
        p.dump(balance,fobj)

    with open(record,'a') as fobj:
        fobj.write(date,amount,'n/a',balance,comment)
def query(record,wallet):
    with open(record) as fobj:
        for line in fobj:
            print(line,end='')
    with open(wallet,'rb') as fobj:
        balance=p.load(fobj)

    print('当前余额:%s' %balance)

def show_menu():
    prompt='''(0)记录开销
(1)记录收入
(2)查询收支记录
(3)退出
请选择(0/1/2/3):'''
    cmds={'0':spend_money,'1':save_money,'2':query}
    record='record.txt'
    wallet='wallet.data'

    if not os.path.exists(wallet):
        with open(wallet,'wb') as fobj:
            p.dump(10000,fobj)
    while 1:
        try:
            choice=input(prompt).strip()
        except ImportError:
            continue
        except (KeyboardInterrupt, EOFError):
            print('\nBye-bye')
            choice = '3'

        if choice not in '0123':
            print('无效输入，请重试')
            continue

        if choice=='3':
            break
        cmds[choice](record,wallet)

if __name__ == '__main__':
    show_menu()