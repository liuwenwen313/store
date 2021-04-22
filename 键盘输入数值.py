count =0
sum = 0
num1 =0
while count<10:
    count = count + 1
    print("第多少次运行：",count)
    num = input("请输入数字:")
    num =int(num)
    num1 = int(num1)
    sum = int(sum)
    sum= num+sum
    if num>num1:
        num1 = num
        print(num1)
print("求和结果：",sum)
print("最大值:",num1)
print("平均值",sum/10)