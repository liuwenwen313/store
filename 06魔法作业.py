#����������һ����scores.txt���ļ��������к������������޶���������ĸ��˵ļ���ħ����ҵ�ĳɼ��������أ���Ϊ��Щħ����ҵ��һ���Ѷȣ����ڲ�ǿ��ͬѧ�Ǳ����Ͻ������Դ���Ͻ���ҵ�Ĵ�������һ�¡�
#�޶� 23 35 44
####ϣ������ͳ�����ĸ�ѧ����ħ����ҵ���ܵ÷֣�Ȼ����д��һ��txt�ļ���
#-*- coding:gbk-*-

num=0
s=open(file="scores.txt",mode="r+",encoding="GBK")
s2=open(file="sum.txt",mode="w+",encoding="GBK")
score=s.readlines()
for i in score:
    qg=i.replace("\n","").split(",")
    for i in qg:
        qg2 = i.replace(" ",",").split(",")
        name=qg2[0]
        del qg2[0]
        for i in qg2:
            i=int(i)
            num=num+i
        s2.write(name)
        s2.write(str(num))
        s2.write("\n")
s.close()
s2.close()
