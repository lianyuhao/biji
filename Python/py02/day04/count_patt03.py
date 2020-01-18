
import re
class CountPass:
    def __init__(self,fname):
        self.fname=fname


    def count_patt(self,patt):
        patt_dict={}
        cpatt=re.compile(patt)

        with open(fname) as fobj:
            for line in fobj:
                m=cpatt.search(line)
                if m:
                    key=m.group()
                    patt_dict[key]=patt_dict.get(key,0)+1

        return patt_dict



if __name__ == '__main__':
    fname='access_log'
    ip='^(\d+\.){3}\d+'
    br='Firefox|MSIE|Chrome'
    cp=CountPass(fname)
    resutl1=cp.count_patt(ip)
    resutl2=cp.count_patt(br)
    print(resutl1)
    print(resutl2)