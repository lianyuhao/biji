import os
import pickle
from time import strftime

def save(fname):
    try:
        amount=int(input('金额:'))
        comment=input('备注:')
    except ValueError:
        print("无效输入")
        return
    except (KeyboardInterrupt,EOFError):
        print('\nBey886')
        exit()
    date=strftime('%Y-%m-%d')
    with open(fname,'rb') as fboj:
        records=pickle.load(fboj)
    balance=records[-1][-2]+amount
    line=[date,amount,0,balance,comment]
    records.append(line)
    with open(fname,'wb') as fboj:
        pickle.dump(records,fboj)
def cost(fname):
    try:
        amount = int(input('金额:'))
        comment = input('备注:')
    except ValueError:
        print('无效输入')
        return
    except (KeyboardInterrupt,EOFError):
        print('\n886')
        exit()
    date = strftime('%Y-%m-%d')
    with open(fname, 'rb') as fboj:
        records = pickle.load(fboj)
    balance = records[-1][-2] - amount
    line = [date, 0, amount, balance, comment]
    records.append(line)
    with open(fname, 'wb') as fboj:
        pickle.dump(records, fboj)
def  query(fname):
    with open(fname,'rb') as fboj:
        records=pickle.load(fboj)
        print('%-12s%-8s%-8s%-12s%-20s'% ('date','save','cost','balance','comment'))
        for lien in records:
            print('%-12s%-8s%-8s%-12s%-20s' % tuple(lien))

def show_menu():
    cmds={'0':save,'1':cost,'2':query}
    prompt="""(0)收入
(1)开销
(2)查询
(3)退出
请选择(0/1/2/3):"""
    fname='acconut.data'
    init_data=[['2020-01-09',0,0,10000,'init data']]
    if not os.path.exists(fname):
        with open(fname,'wb') as fobj:
            pickle.dump(init_data,fobj)
    while 1:
        try:
            choice=input(prompt).strip()
        except (KeyboardInterrupt,EOFError):
            choice='3'

        if choice not in ['0','1','2','3']:
            print('无效输入,请重试')
            continue

        if choice=='3':
            print('\nBeybey')
            break
        cmds[choice](fname)

if __name__ == '__main__':
    show_menu()