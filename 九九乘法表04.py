a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in a:
    j = 9
    while j >= i:
        print('%d*%d=%-3d'%(i,j,i*j),end='\t')
        # %-3d 是控制输出结果占据3位，且从左面开始对齐
        j =j-1
    print( )
