from sqlalchemy  import  create_engine, Column, Integer, String,ForeignKey,DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker

# 创建连接到数据库的引擎
engine = create_engine(
    'mysql+pymysql://admin:262888@192.168.1.11/tedu1908?charset=utf8',
    encoding='utf8',
    # echo=True)
)

Session = sessionmaker(bind=engine)

#创建实体类(与表关联的类)的基类
Base = declarative_base()


#创建实体类
class Departments(Base):
    __tablename__ = 'departments'
    dep_id = Column(Integer,primary_key=True)
    dep_name= Column(String(20),unique=True)

    def __str__(self):
        return '{%s:%s}' % (self.dep_id,self.dep_name)

class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20))
    email=Column(String(50))
    dep_id=Column(Integer,ForeignKey('departments.dep_id'))

class Salary(Base):
    __tablename__ = 'salary'
    sal_id = Column(Integer, primary_key=True)
    date = Column(DATE)
    emp_id=Column(Integer,ForeignKey('employees.emp_id'))
    basic=Column(Integer)
    awards=Column(Integer)

if __name__ == '__main__':
    Base.metadata.create_all(engine)