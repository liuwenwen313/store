import  unittest
import xlrd
from Calc import  Calc
from ddt import  ddt
from  ddt import  data
from  ddt import  unpack
class Excle:
    n=[]
    #获取工作簿
    wb=xlrd.open_workbook(filename="数据.xlsx",encoding_override=True)
    #通过wb获取选项卡
    sheet=wb.sheet_by_name("参数")
    rows=sheet.nrows
    cols=sheet.ncols
    for i in range(1,rows):
        n.append(sheet.row_values(i))
e=Excle()
a=e.n
@ddt#将测试类用ddt进行修饰
class CalcTest(unittest.TestCase):
    @data(*a)#将a数据导入
    @unpack#将数据源进行解包
    def test_Add(self,a,b,c):
        calc=Calc()
        sum=calc.add(a,b)
        self.assertEqual(c,sum)
