# create / retrieve / update / delete
from tables import Emp, Students,Session
from sqlalchemy import distinct
from sqlalchemy import or_,desc,func

# 创建到数据库的会话实例
session = Session()

#第1题
print(38*"*")
print('\033[31;1m第一题:查询所有的学生\033[0m')
print('\033[32;1m%-8s %-5s\033[0m' % ('id','学生姓名'))
qset1 = session.query(Students).order_by(Students.id)
for data in qset1:
    print('\033[35;1m%-8s %-5s\033[0m' % (data.id, data.name))
print(38*"*")

#第2题
print(38*"*")
print('\033[31;1m第二题:查询学生姓名,语文\033[0m')
print('\033[32;1m%s:%s\033[0m' % ('学生姓名','语文成绩'))
qset2 = session.query(Students).order_by(Students.id)
for data in qset2:
    print('\033[35;1m%s:%s\033[0m' % (data.name, data.chinese))
    # print(data)
print(38*"*")

#第3题
print(38*"*")
print('\033[31;1m第三题:查询一个公司里面的工作岗位–清除重复数据\033[0m')
print('\033[32;1m公司职务\033[0m')
qset3 = session.query(Emp.job).distinct().all()
for data in qset3:
    print('\033[35;1m%s\033[0m' % data.job)
print(38*"*")

# 第4题
print(38*"*")
print('\033[31;1m第四题:在所有学生分数上加 10 分特长分\033[0m')
print('\033[32;1m%s:%s\033[0m' % ('学生姓名','总分+特长10分=最终得分'))
qset4 = session.query(Students).order_by(Students.id)
for data in qset4:
    dataz=data.chinese + data.english + data.math
    print('\033[35;1m%-5s:%s+%s=%s\033[0m' % (data.name, dataz,10,dataz+10))
print(38*"*")

#第5题
print(38*"*")
print('\033[31;1m第五题:查询姓名为’张小明’的学生成绩\033[0m')
print('\033[32;1m%s: %s: %s: %s: %s\033[0m' % ('学生姓名','语文','英语','数学','总分'))
qset5 = session.query(Students).filter(Students.name=='张小明')
for data in qset5:
    dataz=data.chinese + data.english + data.math
    print('\033[35;1m%-5s %s  %s  %s  %s\033[0m' % (data.name, data.chinese,data.english,data.math,dataz))
print(38*"*")

#第6题
print(38*"*")
print('\033[31;1m第六题:查询英语成绩大于等于 90 分的同学\033[0m')
print('\033[32;1m%s:  %s\033[0m' % ('学生姓名','英语>90'))
qset6 = session.query(Students).filter(Students.english>90).order_by(Students.id)
for data in qset6:
    print('\033[35;1m%-5s  %s\033[0m' % (data.name, data.english))
print(38*"*")

#第7题
print(38*"*")
print('\033[31;1m第七题:查询总分大于 200 分的所有同学\033[0m')
print('\033[32;1m%s:%s\033[0m' % ('学生姓名','总分'))
qset7 = session.query(Students).filter(Students.chinese+Students.english+Students.math>200)
for data in qset7:
    dataz=data.chinese + data.english + data.math
    print('\033[35;1m%s:%s\033[0m' % (data.name, dataz))
print(38*"*")

#第8题
print(38*"*")
print('\033[31;1m第八题:查询数学分数为 89 或者 90 或者 91 的同学\033[0m')
print('\033[32;1m%s:%s\033[0m' % ('学生姓名','数学分数'))
qset8 = session.query(Students).filter(Students.math.in_([89,90,91]))
for data in qset8:
    # dataz=data.chinese + data.english + data.math
    print('\033[35;1m%s:  %s\033[0m' % (data.name, data.math))
print(38*"*")

#第8题
print(38*"*")
print('\033[31;1m第八题:查询数学分数为 89 或者 90 或者 91 的同学\033[0m')
print('\033[32;1m%s:%s\033[0m' % ('学生姓名','数学分数'))
qset8 = session.query(Students).filter(or_(Students.math==89,Students.math==90,Students.math==91))
for data in qset8:
    # dataz=data.chinese + data.english + data.math
    print('\033[35;1m%s:  %s\033[0m' % (data.name, data.math))
print(38*"*")

#第9题
print(38*"*")
print('\033[31;1m第九题:查询英语分数在 80-90 之间的同学,包含 80 和 90\033[0m')
print('\033[32;1m%s:%s\033[0m' % ('学生姓名','英语分数'))
qset9 = session.query(Students).filter(Students.english>=80).filter(Students.english<=90)
for data in qset9:
    print('\033[35;1m%s:  %s\033[0m' % (data.name, data.english))
print(38*"*")


#第10题
print(38*"*")
print('\033[31;1m第十题:查询所有姓’李’的学生成绩\033[0m')
print('\033[32;1m%s:%s:%s:%s\033[0m' % ('学生姓名','语文分数','英语分数','数学分数'))
qset10 = session.query(Students).filter(Students.name.like('李%'))
for data in qset10:
    print('\033[35;1m%s:    %s     %s     %s\033[0m' % (data.name, data.chinese,data.english,data.math))
print(38*"*")

#第11题
print(38*"*")
print('\033[31;1m第十一题:查询所有名’李’字的学生成绩\033[0m')
print('\033[32;1m%s:%s:%s:%s\033[0m' % ('学生姓名','语文分数','英语分数','数学分数'))
qset11 = session.query(Students).filter(Students.name.like('%李'))
for data in qset11:
    dataz=data.chinese + data.english + data.math
    print('\033[35;1m%s:    %s     %s     %s\033[0m' % (data.name, data.chinese,data.english,data.math))
print(38*"*")

#第12题
print(38*"*")
print('\033[31;1m第十二题:查询所有姓李的学生,并且姓名只有两个字\033[0m')
print('\033[32;1m%s:%s:%s:%s\033[0m' % ('学生姓名','语文分数','英语分数','数学分数'))
qset12 = session.query(Students).filter(Students.name.like('李%')).filter(Students.name.like('__'))
for data in qset12:
    dataz=data.chinese + data.english + data.math
    print('\033[35;1m%s:    %s     %s     %s\033[0m' % (data.name, data.chinese,data.english,data.math))
print(38*"*")

#第13题
print(38*"*")
print('\033[31;1m第十三题:查询所有姓李的学生,并且姓名只有两个字\033[0m')
print('\033[32;1m%s:%s:%s:%s\033[0m' % ('学生姓名','语文分数','英语分数','数学分数'))
qset13 = session.query(Students).filter(Students.name.like('李%')).filter(Students.name.like('__'))
for data in qset13:
    dataz=data.chinese + data.english + data.math
    print('\033[35;1m%s:    %s     %s     %s\033[0m' % (data.name, data.chinese,data.english,data.math))
print(38*"*")

#第14题
print(38*"*")
print('\033[31;1m第十四题:查询所有姓名中包含’李’的学生成绩\033[0m')
print('\033[32;1m%s:%s:%s:%s\033[0m' % ('学生姓名','语文分数','英语分数','数学分数'))
qset14 = session.query(Students).filter(Students.name.contains('李'))
for data in qset14:
    dataz=data.chinese + data.english + data.math
    print('\033[35;1m%s:    %s     %s     %s\033[0m' % (data.name, data.chinese,data.english,data.math))
print(38*"*")

#第15题
print(38*"*")
print('\033[31;1m第十五题:查询所有姓’李’的学生成绩,但姓名必须是三个字符\033[0m')
print('\033[32;1m%s:%s:%s:%s\033[0m' % ('学生姓名','语文分数','英语分数','数学分数'))
qset15 = session.query(Students).filter(Students.name.like('李%')).filter(Students.name.like('___'))
for data in qset15:
    dataz=data.chinese + data.english + data.math
    print('\033[35;1m%s:    %s     %s     %s\033[0m' % (data.name, data.chinese,data.english,data.math))
print(38*"*")

#第16题
print(38*"*")
print('\033[31;1m第十六题:对数学成绩排序(降序)后输出\033[0m')
print('\033[32;1m%s:%s\033[0m' % ('学生姓名','数学分数'))
qset16 = session.query(Students).order_by(desc(Students.math))
for data in qset16:
#     dataz=data.chinese + data.english + data.math
    print('\033[35;1m%s:    %s\033[0m' % (data.name,data.math))
print(38*"*")

#第17题
print(38*"*")
print('\033[31;1m组合排序:第一参考数学,如果数学成绩一样根据语文排序\033[0m')
print('\033[32;1m%s:%s:%s\033[0m' % ('学生姓名','数学分数','语文分数'))
qset17 = session.query(Students).order_by(desc(Students.math)).order_by(desc(Students.chinese)).all()
for data in qset17:
#     dataz=data.chinese + data.english + data.math
    print('\033[35;1m%s:    %s:    %s\033[0m' % (data.name,data.math,data.chinese))
print(38*"*")

#第18题
print(38*"*")
print('\033[31;1m第十八题:对总分排序(降序)后输出\033[0m')
print('\033[32;1m%s:%s\033[0m' % ('学生姓名','总分数'))
qset18 = session.query(Students).order_by(desc(Students.chinese+Students.english+Students.math))
for data in qset18:
    dataz=data.chinese + data.english + data.math
    print('\033[35;1m%s:    %s\033[0m' % (data.name,dataz))
print(38*"*")

#第19题
print(38*"*")
print('\033[31;1m第十九题:对姓’李’的学生总分排序(降序)输出\033[0m')
print('\033[32;1m%s:%s\033[0m' % ('学生姓名','总分数'))
qset19 = session.query(Students).filter(Students.name.like('李%')).order_by(desc(Students.chinese+Students.english+Students.math))
for data in qset19:
    dataz=data.chinese + data.english + data.math
    print('\033[35;1m%s:    %s\033[0m' % (data.name,dataz))
print(38*"*")

#第20题
print(38*"*")
print('\033[31;1m第二十题:统计一个班级共有多少学生\033[0m')
qset20 = session.query(func.count(Students.id)).first()
print('\033[35;1m班级一共有%s个学生\033[0m' % qset20)
print(38*"*")

#第21题
print(38*"*")
print('\033[31;1m第二十一题:统计数学成绩大于 80 的学生有多少个\033[0m')
qset21 = session.query(func.count(Students.id)).filter(Students.math>80).first()
print('\033[35;1m班级一共有%s个学生\033[0m' % qset20)
print(38*"*")

#第22题
print(38*"*")
print('\033[31;1m第二十二题:统计总分大于 250 的人数有多少人\033[0m')
qset22 = session.query(func.count(Students.id)).filter(Students.chinese+Students.english+Students.math>250).first()
print('\033[35;1m班级一共有%s个学生\033[0m' % qset22)
print(38*"*")

#第23题
print(38*"*")
print('\033[31;1m第二十二题:统计一个班级数学总成绩\033[0m')
qset23 = session.query(func.sum(Students.math)).first()
print('\033[35;1m班级数学总成绩:%s\033[0m' % qset23)
print(38*"*")

#第24题
print(38*"*")
print('\033[31;1m第二十四题:统计一个班级语文、英语、数学各科的总成绩\033[0m')
qset241 = session.query(func.sum(Students.chinese)).first()
qset242 = session.query(func.sum(Students.english)).first()
qset243 = session.query(func.sum(Students.math)).first()
print('\033[35;1m班级语文总成绩:%s\033[0m' % qset241)
print('\033[35;1m班级英语总成绩:%s\033[0m' % qset242)
print('\033[35;1m班级数学总成绩:%s\033[0m' % qset243)
print(38*"*")

#第25题
print(38*"*")
print('\033[31;1m第二十五题:统计一个班级语文、英语、数学的成绩总和\033[0m')
qset251 = session.query(func.sum(Students.chinese)).first()
qset252 = session.query(func.sum(Students.english)).first()
qset253 = session.query(func.sum(Students.math)).first()
print('\033[35;1m班级语文、英语、数学的成绩总和:%s\033[0m' % (qset251[-1]+qset252[-1]+qset253[-1]))
print(38*"*")

#第26题
print(38*"*")
print('\033[31;1m第二十六题:统计一个班级语文成绩平均分\033[0m')
qset261 = session.query(func.avg(Students.chinese)).first()
print('\033[35;1m统计一个班级语文成绩平均分:%s\033[0m' % qset261)
print(38*"*")

#第27题
print(38*"*")
print('\033[31;1m第二十七题:求一个班级总分平均分\033[0m')
qset27 = session.query(func.avg(Students.chinese+Students.english+Students.math)).first()
print('\033[35;1m班级语文、英语、数学的成绩总和:%s\033[0m' % qset27)
print(38*"*")

#第28题
print(38*"*")
print('\033[31;1m第二十八题:求班级最高分和最低数学分数\033[0m')
qset281 = session.query(func.max(Students.math)).first()
qset282 = session.query(func.min(Students.math)).first()
print('\033[35;1m班级数学最高分:%s,班级数学最低分:%s\033[0m' % (qset281,qset282))
print(38*"*")

#第29题
print(38*"*")
print('\033[31;1m第二十九题:统计工资大于 15000 的每个工作岗位人数\033[0m')
qset291= session.query(func.count(Emp.ename)).filter(Emp.job=='董事长').filter(Emp.sal>15000).first()
qset292= session.query(func.count(Emp.ename)).filter(Emp.job=='经理').filter(Emp.sal>15000).first()
qset293= session.query(func.count(Emp.ename)).filter(Emp.job=='分析师').filter(Emp.sal>15000).first()
qset294= session.query(func.count(Emp.ename)).filter(Emp.job=='销售员').filter(Emp.sal>15000).first()
qset295= session.query(func.count(Emp.ename)).filter(Emp.job=='文员').filter(Emp.sal>15000).first()
print('\033[35;1m工资大于15000的董事长有%s位\033[0m' % qset291)
print('\033[35;1m工资大于15000的经理有%s位\033[0m' % qset292)
print('\033[35;1m工资大于15000的分析师有%s位\033[0m' % qset293)
print('\033[35;1m工资大于15000的销售员有%s位\033[0m' % qset294)
print('\033[35;1m工资大于15000的文员有%s位\033[0m' % qset295)
print(38*"*")

# #第30题
# print(38*"*")
# print('\033[31;1m第二十九题:统计工资大于 15000 的每个工作岗位人数,并且该工作岗位的人数大于等于 3\033[0m')
# qset301= session.query(Emp).filter(func.sum(Emp.sal,Emp.COMM)>15000)
# # qset302= session.query(func.count(Emp.ename)).filter(Emp.job=='经理').filter(Emp.sal>15000).first()
# # qset303= session.query(func.count(Emp.ename)).filter(Emp.job=='分析师').filter(Emp.sal>15000).first()
# # qset304= session.query(func.count(Emp.ename)).filter(Emp.job=='销售员').filter(Emp.sal>15000).first()
# # qset305= session.query(func.count(Emp.ename)).filter(Emp.job=='文员').filter(Emp.sal>15000).first()
# print(qset301)
# for data in qset301:
#     print('%s' % (data.ename))
# #     print(data)


# 确认
session.commit()

# 关闭
session.close()