# import wget
# import os
# import re
#
# def get_patt(fname,patt,charset='utf8'):
#     resutl=[]
#     cpatt=re.compile(patt)
#     with open(fname,encoding=charset) as fobj:
#         for line in fobj:
#             m=cpatt.search(line)
#             if m:
#                 resutl.append(m.group())
#     return resutl
#
#
#
#
#
# if __name__ == '__main__':
#     url='http://www.163.com'
#     down_dir='tmp/163'
#     fname='/tmp/163/163.html'
#     img_patt='(http|https)://[\w./-]+\.(jpg|jpeg|png|git)'
#
#
#     if not os.path.exists(down_dir):
#         os.mkdir(down_dir)
#
#     if not os.path.exists(fname):
#         wget.download(url,fname)
#     img_list = get_patt(fname, img_patt,'gbk')
#
#     for img_url in img_list:
#         wget.download(img_url,down_dir)


# import wget
# import os
# import re
#
#
# def get_patt(fname, patt, charset='utf8'):
#     resutl = []
#     cpatt = re.compile(patt)
#     with open(fname, encoding=charset) as fobj:
#         for line in fobj:
#             m = cpatt.search(line)
#             if m:
#                 resutl.append(m.group())
#     return resutl
#
#
# if __name__ == '__main__':
#     url = 'https://pic.sogou.com/pics/recommend?category=%C3%F7%D0%C7&from=home#%E5%85%A8%E9%83%A8/'
#     down_dir = '/tmp/sogou'
#     fname = '/tmp/sogou/sogou.html'
#     img_patt = '(http|https)://[\w./-]+\.(jpg|jpeg|png|git)'
#
#     if not os.path.exists(down_dir):
#         os.mkdir(down_dir)
#
#     if not os.path.exists(fname):
#         wget.download(url, fname)
#     img_list = get_patt(fname, img_patt, 'gbk')
#
#     for img_url in img_list:
#         wget.download(img_url, down_dir)


import os
import re
import  wget

def get_patt(fname,patt,charset='utf8'):
    resutl=[]
    cpatt=re.compile(patt)
    with open(fname,encoding=charset) as fobj:
        for lien in fobj:
            m=cpatt.search(lien)
            if m:
                resutl.append(m.group())
    return resutl

if __name__ == '__main__':

    url='http://www.163.com'
    down_dir='/tmp/163'
    fname='/tmp/163/163.html'
    img_patt='(http|https)://[\w./-]+\.(jpg|png|jpeg)'
    if not os.path.exists(down_dir):
        os.mkdir(down_dir)

    if not os.path.exists(fname):
        wget.download(url,fname)
    img_list=get_patt(fname,img_patt,'gbk')
    for img_url in img_list:
        wget.download(img_url,down_dir)
