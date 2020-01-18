from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date,Numeric,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# 创建连接到数据库的引擎
engine = create_engine(
    # mysql+pymysql://用户名:密码@服务器/数据库?参数
    'mysql+pymysql://admin:262888@183.56.208.89/lianxi?charset=utf8',
    encoding='utf8',
    # echo=True  # 在屏幕上输出日志
)

# 创建一个会话类，用于客户端到服务器的会话连接
Session = sessionmaker(bind=engine)

# 创建实体类（与表关联的类）的基类
Base = declarative_base()

# 创建实体类
class Emp(Base):
    __tablename__ = 'emp'  # 定义库中关联的表
    empno = Column(Integer, primary_key=True,autoincrement=False)
    ename = Column(String(50))
    job = Column(String(50))
    mgr = Column(Integer,index=True)
    hiredate = Column(Date)
    sal = Column(Numeric(7,2))
    COMM = Column(Numeric(7,2))
    deptno = Column(Integer)


    # def __str__(self):
    #     return "[%s: %s]" % (self.dep_id, self.dep_name)

class Students(Base):
    __tablename__ = 'Students'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(20))
    chinese = Column(Float)
    english = Column(Float)
    math = Column(Float)

# class Salary(Base):
#     __tablename__ = 'salary'
#     id = Column(Integer, primary_key=True)
#     date = Column(Date)
#     emp_id = Column(Integer, ForeignKey('employees.emp_id'))
#     basic = Column(Integer)
#     awards = Column(Integer)

if __name__ == '__main__':
    # 如果库中没有相关的表则创建，如果已存在，只是映射，不会再创建一遍
    Base.metadata.create_all(engine)