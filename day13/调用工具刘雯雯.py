# #数据库的写入列表
from 表格连接数据库工具 import Db_to_excel     #导入方法
from 表格连接数据库工具 import  select
# sql="select * from bank  "
# param=[]
# name="nam"
# name1="1.xls"
# Db_to_excel(sql,param,name,name1)
path=r"上传银行.xls"
name="bank"
select(path,name,start=0)