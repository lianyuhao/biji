from  dbconn import  Departments,Employees,Salary,Session


#创建到数据库的会话实例
session=Session()
hr=Departments(dep_id=1,dep_name='人事部')
ops=Departments(dep_id=2,dep_name='运维部')
dev=Departments(dep_id=3,dep_name='开发部')
qa=Departments(dep_id=4,dep_name='测试部')
marker=Departments(dep_id=5,dep_name='市场部')
sales=Departments(dep_id=6,dep_name='销售部')
# session.add_all([hr,ops,dev,qa,marker,sales])

# u1=Employees(
#     emp_id=1,emp_name='涂文良',
#     email='twl@163.com',dep_id=2
# )
#
# u2=Employees(
#     emp_id=2,emp_name='刘昌艳',
#     email='lcy@qq.com',dep_id=3
# )
# session.add_all([u1,u2])

# qset1=session.query(Departments)
#
# print(qset1)
#
# for dep in qset1:
#     print(dep.dep_id,dep.dep_name)
#
# qset2=session.query(Employees.emp_name, Employees.email)
# print(qset2)
# for data in qset2:
#     print(data)
# qset3 = session.query(Departments).order_by(Departments.dep_id)
# for  dep in qset3:
#     print(dep.dep_id,dep.dep_name)

# qset4 = session.query(Departments).filter(Departments.dep_id>1)\
#     .filter(Departments.dep_id<5).order_by(Departments.dep_id)
# for dep in qset4:
#     print(dep.dep_id,dep.dep_name)

# qset5=session.query(Employees).filter(Employees.email.like('%.com'))
# for emp in qset5:
#     print(emp.emp_name,emp.email)

# qset6 = session.query(Departments).filter(Departments.dep_name.in_(['人事部','市场部']))
#
# for dep in qset6:
#     print(dep.dep_id,dep.dep_name)

# qset7=session.query(Departments).filter(~Departments.dep_name.in_(['人事部','市场部']))
# # for dep in qset7:
#     print(dep.dep_id,dep.dep_name)
# qset7.all

# dep=qset7.first()
# print(dep)
# print(dep.dep_id,dep.dep_name)

# qset8=session.query(Employees.emp_name,Departments.dep_name).join(Departments)
#
# for data in qset8:
#     print(data)

# qset9 = session.query(Departments).filter(Departments.dep_name=='人事部')
# hr=qset9.first()
# print(hr)
# hr.dep_name='人力资源部'


#确认
session.commit()


#关闭
session.close()