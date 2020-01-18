# create / retrieve / update / delete
from tables import Emp, Students,Session
from sqlalchemy import distinct

# 创建到数据库的会话实例
session = Session()

#第1题
# print(38*"*")
# print('\033[31;1m第一题:\033[0m')
# print('\033[32;1m%-8s %-5s\033[0m' % ('id','学生姓名'))
# qset1 = session.query(Students)
# for data in qset1:
#     print('\033[35;1m%-8s %-5s\033[0m' % (data.id, data.name))
# print(38*"*")

# #第2题
# print(38*"*")
# print('\033[31;1m第二题:\033[0m')
# print('\033[32;1m%s:%s\033[0m' % ('学生姓名','语文成绩'))
# qset2 = session.query(Students)
# for data in qset2:
#     print('\033[35;1m%s:%s\033[0m' % (data.name, data.chinese))
#     # print(data)
# print(38*"*")

# #第3题
# print(38*"*")
# print('\033[31;1m第三题:\033[0m')
# print('\033[32;1m公司职务\033[0m')
# qset3 = session.query(Emp.job).distinct().all()
# for data in qset3:
#     print('\033[35;1m%s\033[0m' % data.job)
# print(38*"*")

#第4题
print(38*"*")
print('\033[31;1m第四题:\033[0m')
print('\033[32;1m%s:%s:%s:%s\033[0m' % ('学生姓名','语文','英语','数学'))
qset4 = session.query(Students)
for data in qset4:
    print('\033[35;1m%-5s:%s:%s:%s\033[0m' % (data.name, data.chinese,data.english,data.math))
print(38*"*")
# 确认
session.commit()

# 关闭
session.close()