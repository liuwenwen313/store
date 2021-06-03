'''
柠檬云登录的自动化测试
1.准备需要的数据
'''
class Logindata:
    success_data=[
        {"username":"17320093059",
         "password":"liuwenwen313",
         "expect":"首页 - 柠檬云财税"}
    ]
    password_error_data = [
        {"username": "17320093059",
         "password": "liuwenwen3131",
         "expect": "用户名或密码错误，请重新输入"}
    ]
    username_error_data = [
        {"username": "17320093058",
         "password": "liuwenwen3131",
         "expect": "用户名或密码错误，请重新输入"}
    ]
    nousername_error_data = [
        {"username": "",
         "password": "liuwenwen3131",
         "expect": "柠檬云财务软件-永久免费的专业财务软件系统-智能生成资产负债表|现金流量表|利润表|科目汇总表-会计做账|记账表格-会计软件有哪些-出纳管理软件-企业财务管理系统"}
    ]