import unittest
from HTMLTestRunner  import  HTMLTestRunner
# 1.创建测试集
suite = unittest.TestSuite()
# 2.让测试加载器自己加载所用用例
tests = unittest.defaultTestLoader.discover(r"D:\测试自动化\day03\day03\作业",pattern="nm*.py")
# 3.将所用例 放入测试集
suite.addTests(tests)
# 4.创建测试运行器
f = open(file="柠檬云测试报告.html", mode="w+", encoding ="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream = f,
    title="这是一个柠檬云测试报告！",
    verbosity=2,
    description="执行用例"
)
# 5.让运行器生成测试报告

runner.run(suite)
