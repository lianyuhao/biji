from random import randint,choice


def exam():
    cmds={'+':lambda x,y:x+y,'-':lambda x,y:x+y}
    nums=[randint(1,100) for i in range(2)]
    nums.sort(reverse=True)
    op= choice('+-')

    result=cmds[op](*nums)

    prompt='%s %s %s = '% (nums[0],op,nums[1])
    counter=0
    while counter<3:
        try:
            answer = int(input(prompt))
        except:
            print()
            continue

        if answer==result:
            print('very goot')
            break

        print('滚')
        counter+=1
    else:
        print('\033[31;1m正确答案: %s%s\033[0m' % (prompt, result))

def main():
    while 1:
        exam()
        try:
            yn=input('Coninue(y/n)?').strip()[0]
        except ImportError:
            print('重新输入')
            continue
        except (KeyboardInterrupt,EOFError):
            yn='n'
        if yn in 'nN':
            print('\n886')
            break

if __name__ == '__main__':
    main()