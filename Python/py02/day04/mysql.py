import pymysql

conn=pymysql.connect(
    host='192.168.1.11',port=3306,
    user='admin',passwd='262888',
    db='nsd1908',charset='utf8'
)

cur=conn.cursor()


# mk_dep = """CREATE TABLE  departments(
# dep_id  INT ,dep_name VARCHAR(50),
# PRIMARY KEY(dep_id))"""
#
# mk_emp="""CREATE TABLE employees(
# emp_id INT,emp_name VARCHAR(20),emai VARCHAR(50),dep_id INT ,
# PRIMARY KEY (emp_id),
# FOREIGN KEY (dep_id) REFERENCES departments(dep_id)
# )"""
#
# mk_sal="""CREATE TABLE salary(
# id INT, date DATE, emp_id INT, basic INT, awards INT,
# PRIMARY KEY(id),
# FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
# )"""
#
#
# cur.execute(mk_dep)
# cur.execute(mk_emp)
# cur.execute(mk_sal)

# insert1='INSERT INTO departments VALUES (%s,%s)'
# cur.executemany(insert1,[(1,'人事部'),(2,'运维部')])
# cur.executemany(insert1, [(2, '运维部'), (3, '开发部'), (4, '财务部'), (5, '测试部'), (6, '市场部')])


# update1='UPDATE departments SET dep_name=%s WHERE  dep_name=%s'
# cur.execute(update1,('人力资源部','人事部'))

# delete1 = 'DELETE FROM departments WHERE dep_name=%s'
# cur.execute(delete1, ('运维部',))

select1='SELECT * FROM departments'
cur.execute(select1)

result1=cur.fetchone()
print(result1)
print('*' *30)

result2=cur.fetchmany(2)
print(result2)
print('*'*30)

result3=cur.fetchall()
print(result3)



conn.commit()


cur.close()
conn.close()