# print([10+5 for i in range(10)])
#
# print([10+i for i in range(1,11)])
#
# print([10+i for i in range(10)])
#
# print(10+i for i in range(1,11)if i %2==1)

import re
# print(re.match('f..','food'))
#
# print(re.match('f..','seafood'))
#
# print(re.search('f..','seafood'))
#
# m=re.search('f..','seafood')
# print(m.group())

# print(re.findall('f..','seafood is food'))
#
# print(re.finditer('f..','seafood is food'))
#
# print(list(re.finditer('f..','seafood is food')))
#
# for m in re.finditer('f..','seafood is food'):
#     lien=m.group()
#     print(lien)


# print(re.split('-|\.','hello-world-how-are-you.tar.gz'))
#
# print(re.sub('X','tom','Hi X.Nice to meet you,X'))

# patt=re.compile('f..')
# m=patt.findall('seafood in food')
# print(m)

# class Role:
#     def __init__(self,name,weapon):
#         self.name=name
#         self.weapon=weapon
#
#     def show_me(self):
#         print('我是%s,我的武器是%s' % (self.name,self.weapon))
#
#     def say(self,words):
#         print(words)
#
# if __name__ == '__main__':
#     lb=Role('吕布','方天画戟')
#     print(lb.name,lb.weapon)
#     lb.show_me()
#     lb.say('人中吕布,马中赤兔')

# class Role:
#     def __init__(self,name,weapon):
#         self.name=name
#         self.weapon=weapon
#
#     def show_me(self):
#         print('我是%s,我的武器是%s'% (self.name,self.weapon))
#
#
#     def say(self,words):
#         print(words)
#
#
# class Warrior(Role):
#     def __init__(self,name,weapon,country):
#         Role.__init__(self,name,weapon)
#         self.country=country
#
#     def attack(self,target):
#         print('近身攻击:%s'%target)
#
# class Mage(Role):
#     def attack(self,target):
#         print('远程攻击:%s'%target)
#
#
# if __name__ == '__main__':
#     gy=Warrior('sdsd','jfdksfj','df')
#     gy.show_me()
#     gy.attack('吕布')

import os
import tarfile
import hashlib
import pickle
from time import strftime

def check_md5(fname):
    m=hashlib.md5()
    with open(fname,'rb') as fobj:
        while 1:
            data=fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()

def full_backup(src,dst,md5file):
    fname=os.path.basename(src)
    fname='%s_full_%s.tar.gz' % (fname,strftime('%Y%m%d'))
    fname=os.path.join(dst,fname)

    tar =tarfile.open(fname,'w:gz')
    tar.add(src)
    tar.close()

    md5dict={}
    for path, folders, files in os.walk(src):
        for file in files:
            key=os.path.join(path,file)
            md5dict[key]=check_md5(key)

        with open(md5file, 'wb') as fobj:
            pickle.dump(md5dict, fobj)

    def incr_backup(src, dst, md5file):
        # 拼接出备份文件的绝对路径
        fname = os.path.basename(src)  # security
        fname = '%s_incr_%s.tar.gz' % (fname, strftime('%Y%m%d'))
        fname = os.path.join(dst, fname)

        # 计算每个文件的md5值，将其保存到字典
        md5dict = {}
        for path, folders, files in os.walk(src):
            for file in files:
                key = os.path.join(path, file)
                md5dict[key] = check_md5(key)

        # 取出前一天的md5值
        with open(md5file, 'rb') as fobj:
            old_md5 = pickle.load(fobj)

        # 比较两个字典，新字典的key不在老字典中，或值不一样，都要备份
        tar = tarfile.open(fname, 'w:gz')
        for key in md5dict:
            if old_md5.get(key) != md5dict[key]:
                tar.add(key)
        tar.close()

        with open(md5file, 'wb') as fobj:
            pickle.dump(md5dict, fobj)

    if __name__ == '__main__':
        src = '/tmp/nsd1908/security'
        dst = '/tmp/nsd1908/backup'
        md5file = '/tmp/nsd1908/md5.data'
        if strftime('%a') == 'Mon':
            full_backup(src, dst, md5file)
        else:
            incr_backup(src, dst, md5file)



