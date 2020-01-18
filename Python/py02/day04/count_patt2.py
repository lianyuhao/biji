import re



def count_patt(fname,patt):
    patt_dict={}
    cpatt=re.compile(patt)

    with open(fname) as fobj:
        for lien in fobj:
            m=cpatt.search(lien)
            if m:
                key=m.group()
                patt_dict[key]=patt_dict.get(key,0)+1
    return  patt_dict


if __name__ == '__main__':
    fname='access_log'
    ip='^(\d+\.){3}\d+'
    rb='Firefox|MSIE|Chrome'
    resutl1=count_patt(fname,ip)
    resutl2=count_patt(fname,rb)
    print(resutl1)
    print(resutl2)
