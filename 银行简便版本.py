import random
from DBUtils import select
from DBUtils import update
# 2.银行的名称写死
bank_name = "中国工商银行的昌平支行"
# 打印欢迎页面
def welcome():
    print("---------------------------------")
    print("-     中国工商银行账户管理系统V1.0     -")
    print("---------------------------------")
    print("-   1.开户                       -")
    print("-   2.存钱                       -")
    print("-   3.取钱                       -")
    print("-   4.转账                       -")
    print("-   5.查询                       -")
    print("-   6.Bye!                       -")
    print("----------------------------------")

# 银行的开户逻辑
def bank_addUser(account,username,password,country,province,street,door):
    # l利用sql判断是否已满
    sql = "select * from   users"
    #调用方法 select
    user=select(sql,[])
    if len(user) >=100 :
        return 3
    # 判断是否存在
    sql = "select 账号  from users  where 账号= %s;"
    param = [account]
    user=select(sql,param)
    if len(user) > 0:
        return 2
    #正常开户
    sql = "insert into users  values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param = [account,username, password, country, province, street, door,  0,  '中国工商银行的昌平支行']
    # #调用方法 update
    update(sql,param)
    return 1
# 用户开户方法
def addUser():
    # 随机获取账号
    li = ["1","2","3","4","5","6","7","8","9","0","a","b","c","e","f"]
    account = ""
    for i in range(8):
        index = random.randint(0, len(li) - 1)
        account = account + li[index]
    name = input("请输入用户名：")
    while True:
        password = input("请输入您的密码（6位数字）：")
        if len(password)==6:
            break
        else:
            print("请重新输入六位密码")
    print("接下来要输入您的地址信息：")
    country = input("\t输入国家：")
    province = input("\t输入省份：")
    street =  input("\t输入街道：")
    door = input("\t输入门牌号：")
    # 余额不允许第一次输入，需要存钱

    status = bank_addUser(account,name,password,country,province,street,door)
    if status == 1:
        print("恭喜开户成功！")
        info = '''
            ------------个人信息----------------
            账号：%s,
            用户名：%s,
            取款密码：%s,
            地址信息：
                国家：%s,
                省份：%s,
                街道：%s,
                门牌号：%s,
            余额：%s,
            开户行：%s
            -----------------------------------
        '''
        print(info % (account,name,password,country,province,street,door,0,bank_name))

    elif status == 2:
        print("对不起，该用户已存在！请稍后重试！！！")
    elif status == 3:
        print("对不起，该银行库已满，请携带证件到其他银行办理！！！")
    #取钱
    #银行取钱的逻辑
####cunq
#银行存钱的逻辑
def bank_savemoney(account,money):
    sql ="select 账号  from users  where 账号= %s;"
    param = [account]
    #调用select方法
    user=select(sql, param)
    if  len(user)>0:
        sql = "update  users set 余额=余额+ %s where 账号= %s"
        param = [money,account]
             ##调用方法update
        update(sql, param)  # (sql模板，param实际的填充参数)
        return 1
    else:
        return False
#存款的方式
def savemoney():
    account=input("请输入您的账号：")
    while True:
        money=input("请输入您的存款金额：")
        if money.isdigit():
            money = int(money)
            break
        else:
            print("您输入非法重新输入")
    status0=bank_savemoney(account,money)
    if status0 == 1:
      print("存款成功")
    if status0 == False:
       print("您输入的账号不存在")
   #取款的逻辑
def bank_getmoney (account,password,gmoney):
    # 账号是否存在
    sql="select 账号 from users where 账号 =%s"
    param=[account]
    user=select(sql,param)
    if len(user)>0:
# 密码是否正确
        sql="select 账号 from users where 账号 =%s and  密码 = %s"
        param=[account,password]
        user=select(sql,param)
        if len(user)>0:
            #正常取钱
            sql="select 账号 from users where 余额>=%s and  账号 =%s"
            param = [gmoney, account]
            user=select(sql,param)
            if len(user) >0:
               sql="update users set 余额=余额-%s where 账号 =%s"
               param=[gmoney,account]
               update(sql,param)
               return 0
            else:
                 return 3
        else:
            return 2
    else:
        return 1
#银行的取钱的方式
def getmoney():
    account = input("请输入用户账号:")
    password = input("请输入您的用户密码:")
    while True:
        gmoney = input("请输入您的取钱金额:")
        if gmoney.isdigit():
            gmoney = int(gmoney)
            break
        else:
            print("您输入非法重新输入")

    status1 =bank_getmoney (account,password,gmoney,)
    if status1==0:
     print("恭喜你，取款成功，")
    elif status1==1:
      print("账号不存在！")
    elif status1 == 2:
      print("密码不正确！")
    elif status1 == 3:
       print("您的余额不足！")
        ####转账

##########转账
#转账的逻辑
def bank_transfer(account1,account2,password,money):
    # 两个账号是不是存在
    sql="select 账号 from users where 账号=%s or 账号=%s"
    param=[account1,account2]
    user=select(sql, param)
    if len(user) == 2:
        # 转出账号密码是不是存在
        sql = "select 账号 from users where 密码=%s and 账号=%s"
        param = [password,account1]
        user=select(sql, param)
        if  len(user)>0:
            # 转出金额是不是足够
            sql = "select 账号 from users where 余额>=%s and 账号=%s"
            param = [money,account1 ]
            user=select(sql, param)
            if len(user)>0:
                # 正常转出
                sql = "update  users set 余额=余额- %s where 账号= %s "
                param = [money, account1]
                update(sql, param)
                #调用update方法
                sql = "update  users set 余额=余额+ %s where 账号= %s "
                param = [money, account2]
                update(sql, param)
                return 0
            else:
                return 3
        else:
            return  2
    else:
        return 1

#转账的方法
def transfer():
   account1=input("请输入转出钱的账号：")
   account2=input("请输入转入钱的账号：")
   password=input("请输入转出账号的密码：")
   while True:
        money=input("请输入您要转出的金额:")
        if money.isdigit():
            money = int(money)
            break
        else:
            print("您输入非法重新输入")

   status4=bank_transfer(account1,account2,password,money)
   if status4==0:
       print("转账成功")
   elif status4==1:
       print("您输入的账号不存在：")
   elif status4==2:
       print("您输入的密码错误：")
   elif status4==3:
       print("您的余额不足：")
####查询
#查询的逻辑
def bank_query(account,password):
    sql = "select 账号 from users where 账号=%s "
    param = [account]
    user=select(sql, param)
    if len(user) > 0:
        sql = "select * from users where  密码= %s and 账号 = %s"
        param = [password,account]
        user=select(sql, param)
        print(user)
        if len(user) > 0:

           ''' print("帐号:", user[0], ",用户名:", user[1], ", 密码:", user[2], ", 余额:", user[7], "元, 用户居住地址:",
                 user[3] + user[4] + user[5] + user[6],
                 ", 当前开户行为:", user[8])'''
           account=user[0][0]
           name=user[0][1]
           password=user[0][2]
           money= user[0][7]
           country=user[0][3]
           province=user[0][4]
           street=user[0][5]
           door=user[0][6]
           bank_name= user[0][8]
           info = '''
                       ------------个人信息----------------
                       账号：%s,
                       用户名：%s,
                       取款密码：%s,
                       地址信息：
                           国家：%s,
                           省份：%s,
                           街道：%s,
                           门牌号：%s,
                       余额：%s,
                       开户行：%s
                       -----------------------------------
                   '''
           print(info % (account, name, password,money ,country, province, street, door, bank_name))

           return 1
        else:
            return 3
    else:
        return 2
#查询的方法
def query():
    account=input("请输入您的账号：")
    password=input("请输入您的密码：")
    status5=bank_query(account,password)
    if status5==1:
        print("查询信息如上",)

    elif status5 == 2:
        print("您输入的用户不存在")
    elif status5 == 3:
        print("您输入的密码有误")

while True:
    welcome()
    num = input("请输入您的业务编号：")
    if num.isdigit():
        num = int(num)
        if num == 1:#开户
            addUser()
        elif num == 2:#存款
            savemoney()
        elif num == 3:#取款
            getmoney()
        elif num == 4:#转账
            transfer()
        elif num == 5:#查询
            query()
        elif num == 6:#退出
            print("拜拜了您嘞，欢迎下次光临！！！")
        else:
            print("输入非法！请重新输入！！！别瞎弄！！！")
    else:
        print("您输入非法！请重新输入！！！")

