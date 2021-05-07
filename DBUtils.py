import pymysql
host="localhost"
user="root"
passsword=""
database="银行数据库"
######增删改############################
def update(sql,param):
   #连接数据库
   con=pymysql.connect(host=host,user=user,password=passsword,database=database)
   #连接控制台
   cursor=con.cursor()
   #执行sql语句
   cursor.execute(sql,param)
   #提交
   con.commit()
   #关闭资源
   cursor.close()
   con.close()
   #######查询###########################
def select(sql,param):
     #连接数据库
     con=pymysql.connect(host=host,user=user,password=passsword,database=database)
     #连接控制台
     cursor=con.cursor()
     #执行sql语句
     cursor.execute(sql,param)
     #提交
     con.commit()
     #返回数据
     return cursor.fetchall()
     #关闭资源
     cursor.close()
     con.close()