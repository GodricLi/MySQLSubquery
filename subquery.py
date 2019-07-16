# _*_ coding=utf-8 _*_

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='123', database='db1')
cursor = conn.cursor()

# 使用IN的子查询：
# 查询平均年龄在25岁以上的部门名
sql = """select name from department where id in
        (select dep_id from emp group by dep_id having avg(age)>25);    
    """
cursor.execute(sql)
res = cursor.fetchall()
print(res)

# 查看技术部员工姓名
sql2 = """
        select name from emp where dep_id in(
            select id from department where name='技术'
        );
    """

cursor.execute(sql2)
print(cursor.fetchall())

# 查看员工人数不足1人的部门名
sql3 = """
        select name from department where id not in(
            select distinct dep_id from emp
        );
            
    """
cursor.execute(sql3)
print(cursor.fetchall())
print(type(cursor.fetchall()))

# 2.带比较运算符的子查询
# 查询大于所有人平均年龄的员工名与年龄
sql4 = """
        select name,age from emp where age >(
            select avg (age) from emp
        );
"""
cursor.execute(sql4)
print(cursor.fetchall())

"""3 带EXISTS关键字的子查询
    EXISTS关字键字表示存在。在使用EXISTS关键字时，内层查询语句不返回查询的记录。
    而是返回一个真假值。True或False
    当返回True时，外层查询语句将进行查询；当返回值为False时，外层查询语句不进行查询
"""
# True
sql5 = "select * from emp where exists (select id from department where name='技术');"
# False
sql6 = "select * from emp where exists (select id from department where name='IT');"

cursor.execute(sql5)
print(cursor.fetchall())
