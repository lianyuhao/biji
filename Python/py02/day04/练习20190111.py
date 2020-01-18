import  os
import tarfile
import hashlib
import pickle
from time import  strftime

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
    fname='%s_full_%s.tar.gz' % (fname,strftime('%Y%m%%d'))
    fname=os.path.join(dst,fname)

    tar=tarfile.open(fname,'w:gz')
    tar.add(src)
    tar.close()


