# -*- coding:utf-8 -*-
import pymysql
import xlrd
import  xlwt
host="localhost"
user="root"
passsword=""
database="上传银行"
c=[]
n=()
######增删改############################
def Db_to_excel(sql,param,name,name1):##（数据库的数据写入表格）
   #连接数据库
   con=pymysql.connect(host=host,user=user,password=passsword,database=database)
   #连接控制台
   cursor=con.cursor()
   #执行sql语句
   cursor.execute(sql,param)
   #提交
   con.commit()
   #获取信息
   a= cursor.fetchall()
   #写入excel表

   excel=xlwt.Workbook()
   sheet=excel.add_sheet(name)
   for r ,b in enumerate(a):
       for c,d in enumerate(b):
           sheet.write(r,c,d)
   #关闭资源
   excel.save(name1)
   cursor.close()
   con.close()
   #######查询###########################
def select(path,name,start=1):#path完整路径
    #获取表格信息
    wb = xlrd.open_workbook(filename=path, encoding_override=True)
    sheet = wb.sheet_by_name(name)
    # 获取行，列数据
    rows = sheet.nrows  # 多少行
    cols = sheet.ncols  # 多少列
    # 连接数据库
    con=pymysql.connect(host=host,user=user,password=passsword,database=database)
    # 连接控制台
    cursor=con.cursor()
    for i in range(start,rows):
        a=sheet.row_values(i)
        print(a)
        sql = "insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param = a
        cursor.execute(sql, param)
        print(n)
        #连接数据库
    # con=pymysql.connect(host=host,user=user,password=passsword,database=database)
    #连接控制台
    # cursor=con.cursor()
    #执行sql语句

    # for i in (c):
    #      print(i)
         # for l in i:
         #    print(l)
            # sql = "insert into users values(%s)"
            # param = [l]

            # cursor.execute(sql, param)
    #提交
    con.commit()
 # # #返回数据
 # #    return cursor.fetchall()
 # #关闭资源
    cursor.close()
    con.close()
# select("","","12月份衣服销售数据.xlsx","12月份各种服饰销售情况")