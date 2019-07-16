# _*_ coding=utf-8 _*_


import pymysql


conn = pymysql.connect(host='localhost',user='root',password='123',database='db1')


# 子查询结果作为一张表与表本身连接查询
# 查询每个职位最新入职的员工记录
sql = """
        select * from employee as t1
        inner join 
        (select post,max(hire_date) as max_date from employee group by post) as t2
        on t1.post=t2.post
        where t1.hire_date = t2.max_date;
        
    """