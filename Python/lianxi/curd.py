# create / retrieve / update / delete
from tables import Emp, Students,Session

# 创建到数据库的会话实例
session = Session()

# 执行增删改查操作
# hr = Emp(dep_id=1, dep_name='人事部')
# ops = Emp(dep_id=2, dep_name='运维部')
# dev = Emp(dep_id=3, dep_name='开发部')
# qa = Emp(dep_id=4, dep_name='测试部')
# market = Emp(dep_id=5, dep_name='市场部')
# sales = Emp(dep_id=6, dep_name='销售部')
# session.add_all([hr, ops, dev, qa, market, sales])
u1 = Emp(empno=1009, ename='曾阿牛',job='董事长',hiredate='2001-11-17',sal=50000.00,deptno=10)
u2 = Emp(empno=1004, ename='刘备',job='经理',mgr=1009,hiredate='2001-04-02',sal=29750.00,deptno=20)
u3 = Emp(empno=1006, ename='关羽',job='经理',mgr=1009,hiredate='2001-05-01',sal=28500.00,deptno=30)
u4 = Emp(empno=1007, ename='张飞',job='经理',mgr=1009,hiredate='2001-09-01',sal=24500.00,deptno=10)
u5 = Emp(empno=1008, ename='诸葛亮',job='分析师',mgr=1004,hiredate='2007-04-19',sal=30000.00,deptno=20)
u6 = Emp(empno=1013, ename='庞统',job='分析师',mgr=1004,hiredate='2001-12-03',sal=30000.00,deptno=20)
u7 = Emp(empno=1002, ename='黛绮丝',job='销售员',mgr=1006,hiredate='2001-02-20',sal=16000.00,COMM=3000.00,deptno=30)
u8 = Emp(empno=1003, ename='殷天正',job='销售员',mgr=1006,hiredate='2001-02-22',sal=12500.00,COMM=5000.00,deptno=30)
u9 = Emp(empno=1005, ename='谢逊',job='销售员',mgr=1006,hiredate='2001-09-28',sal=12500.00,COMM=14000.00,deptno=30)
u10 = Emp(empno=1010, ename='韦一笑',job='销售员',mgr=1006,hiredate='2001-09-08',sal=15000.00,COMM=0.00,deptno=30)
u11= Emp(empno=1012, ename='程普',job='文员',mgr=1006,hiredate='2001-12-03',sal=9500.00,deptno=30)
u12= Emp(empno=1014, ename='黄盖',job='文员',mgr=1007,hiredate='2002-01-23',sal=13000.00,deptno=10)
u13 = Emp(empno=1011, ename='周泰',job='文员',mgr=1008,hiredate='2007-05-23',sal=11000.00,deptno=20)
u14 = Students(id=1, name='张小明',chinese=89,english=98,math=90)
u15 = Students(id=2, name='李进',chinese=67,english=98,math=89)
u16 = Students(id=3, name='王五',chinese=87,english=78,math=77)
u17 = Students(id=4, name='李一',chinese=88,english=98,math=90)
u18 = Students(id=5, name='李来财',chinese=82,english=84,math=67)
u19 = Students(id=6, name='张进宝',chinese=55,english=85,math=45)
u20 = Students(id=7, name='黄蓉',chinese=85,english=75,math=80)
u21 = Students(id=8, name='张一李',chinese=75,english=65,math=30)
u22 = Students(id=9, name='何李',chinese=75,english=65,math=90)
u23 = Students(id=10, name='单',chinese=75,english=65,math=30)
u24 = Students(id=11, name='jack',chinese=75,english=65,math=40)
u25 = Students(id=12, name='marry',chinese=75,english=65,math=60)
# u2 = Emp(empno=1009, ename='曾阿牛',job='董事长',mgr=,hiredate=,sal=,COMM=,deptno=)
session.add_all([u1, u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15,u16,u17,u18,u19,u20,u21,u22,u23,u24,u25])
###############################################
# 查询时，query参数是类名，返回的是实例列表
# qset1 = session.query(Departments)
# print(qset1)   # qset1是sql语句，此时不查询数据库，取值时才查询
# for dep in qset1:
#     print(dep.dep_id, dep.dep_name)
###############################################
# 查询时，query参数是属性，返回的是属性构成的元组
# qset2 = session.query(Employees.emp_name, Employees.email)
# print(qset2)
# for data in qset2:
#     print(data)
###############################################
# 查询部门，按id排序
# qset3 = session.query(Departments).order_by(Departments.dep_id)
# for dep in qset3:
#     print(dep.dep_id, dep.dep_name)
###############################################
# 查询部门，根据id进行过滤
# qset4 = session.query(Departments).filter(Departments.dep_id>1)\
#     .filter(Departments.dep_id<5).order_by(Departments.dep_id)
# for dep in qset4:
#     print(dep.dep_id, dep.dep_name)
###############################################
# 查询email以.com结尾的用户
# qset5 = session.query(Employees).filter(Employees.email.like('%.com'))
# for emp in qset5:
#     print(emp.emp_name, emp.email)
###############################################
# 查询人力资源部和市场部
# qset6 = session.query(Departments)\
#     .filter(Departments.dep_name.in_(['人事部', '市场部']))
# for dep in qset6:
#     print(dep.dep_id, dep.dep_name)

###############################################
# 查询人事部和市场部以外的部门
# qset7 = session.query(Departments)\
#     .filter(~Departments.dep_name.in_(['人事部', '市场部']))
# for dep in qset7:
#     print(dep.dep_id, dep.dep_name)
###############################################
# all()返回所有值的列表
# print(qset7.all())
###############################################
# first()返回匹配内容的第一项
# dep = qset7.first()
# print(dep)
# print(dep.dep_id, dep.dep_name)
###############################################
# 多表查询，query中先写Employees.emp_name，join时写Departments
# query中先写Departments.dep_name，join时写Employees
# qset8 = session.query(Employees.emp_name, Departments.dep_name)\
#     .join(Departments)
# for data in qset8:
#     print(data)
###############################################
# 修改
# qset9 = session.query(Departments).filter(Departments.dep_name=='人事部')
# hr = qset9.first()
# print(hr)
# hr.dep_name = '人力资源部'
###############################################
# 删除
# qset10 = session.query(Departments).filter(Departments.dep_name=='销售部')
# sales = qset10.first()
# print(sales)
# session.delete(sales)


# 确认
session.commit()

# 关闭
session.close()