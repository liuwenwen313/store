a = [1,5,21,30,15,9,30,24,]
b=0
sum=0
b=int(b)
while b<len(a):
    if a[b]%5==0:
        sum = int(sum)
        sum =  a[b]
        sum =  a[b]+sum
        print("5的倍数有",a[b])
        print("5的倍数和为",sum)
    b=b+1