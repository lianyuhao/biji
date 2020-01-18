# import  hashlib
#
# import sys
#
# def

import os
import tarfile
import pickle
import hashlib
from time import strftime
import che_md5
def full_backup(src,dst,md5file):
    fname=os.path.basename(src) #security
    fname='%s_full_%s.tar.gz' % (fname,strftime('%Y%m%d'))
    fname=os.path.join(dst,fname)

    tar=tarfile.open(fname,'w:gz')
    tar.add(src)
    tar.close()

    md5dict={}
    for path,folders, files in os.walk(src):
        for file in files:
            key=os.path.join(path,file)
            md5dict[key]=che_md5.check_md5(key)

    with open(md5file,'wb') as fobj:
        pickle.dump(md5dict,fobj)

def incr_backup(src,dst,md5file):
    fname = os.path.basename(src)  # security
    fname = '%s_incr_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)


    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = che_md5.check_md5(key)

    with open(md5file,'rb') as fobj:
        old_md5=pickle.load(fobj)

    tar=tarfile.open(fname,'w:gz')
    for key in md5dict:
        if old_md5.get(key) !=md5dict[key]:
            tar.add(key)
    tar.close()

    with open(md5file,'wb') as fobj:
        pickle.dump(md5dict,fobj)



if __name__ == '__main__':
    src='/tmp/nsd1908/security'
    dst='/tmp/nsd1908/backup'
    md5file='/tmp/nsd1908/md5.data'
    if strftime('%a')=='Mon':
        full_backup(src,dst,md5file)
    else:
        incr_backup(src,dst,md5file)
