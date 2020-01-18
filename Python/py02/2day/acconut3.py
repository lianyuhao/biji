import time
import pickle
import os
def save(fname):
    amount=int(input('金额:'))
    comment=input('备注:')
    date=time.strftime('%Y-%m-%d')
    with open(fname,'rb') as fobj:
        records=pickle.load(fobj)
        balance=records[-1][-2] + amount


def cost(fname):
    print('1')

def query(fname):
    print('2')

def show_menu():
    cmds = {'0': save, '1': cost, '2': query}
    prompt='''(0)收入
(1)开销
(2)查询
(3)退出
请选择(0/1/2/3):'''
    fname='account.data'
    init_data=[['2020-01-09',0,0,10000,'init data']]
    if not os.path.exists(fname):
        with open(fname,'wb') as fobj:
            pickle.dump(init_data,fobj)

    while 1:
        choice=input(prompt).strip()
        if choice not in ['0','1','2','3']:
            print('错误输入,请重试')
            continue
        if choice==3:
            print('\n886')
            break

        cmds[choice](fname)

if __name__ == '__main__':
    show_menu()
