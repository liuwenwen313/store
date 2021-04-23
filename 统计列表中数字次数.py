List = [1, 4, 7, 5, 8, 2, 1, 3, 4, 5, 9, 7, 6, 1, 10]
a = 0
c= 0
while c<len(List):
    b=0
    a=0
    while a < len(List):
        if List[c] == List[a]:
            b = b + 1
        a = a + 1
    c=c+1
    print(List[c-1], "出现的次数有", b)
