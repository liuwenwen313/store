pc=["北京","上海","广东"]
GDP=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
pc.append("石家庄（河北）")
pc.append("太原（太原）")
pc.append("呼和浩特（内蒙）")
pc.append("辽宁（沈阳）")
pc.append("长春（吉林）")
pc.append("哈尔滨（黑龙江）")
pc.append("南京（江苏）")
pc.append("杭州（浙江）")
pc.append("合肥（安徽）")
pc.append("福州（福建）")
pc.append("南昌（江西）")
pc.append("济南（山东")
pc.append("郑州（河南）")
pc.append("武汉（湖北）")
pc.append("长沙（湖南）")
pc.append("南宁（广西）")
pc.append("海口（海南）")
pc.append("四川（成都）")
pc.append("贵阳（贵州）")
pc.append("云南（昆明）")
pc.append("拉萨（西藏）")
pc.append("陕西（西安）")
pc.append("甘肃（兰州）")
pc.append("西宁（青海）")
pc.append("宁夏（银川）")
pc.append("乌鲁木齐（新疆）")
pc.append("台北（台湾）")
pc.append("天津")
pc.append("重庆")
pc.append("香港")
pc.append("澳门")
print(pc)
pc.remove("广东")
print(pc)
pc.insert(1,"广东")
print(pc)
sum=GDP[0]+GDP[1]+GDP[2]+GDP[3]+GDP[4]+GDP[5]+GDP[6]+GDP[7]
av=sum/8
print("GDP前八城市总和为",sum)
print("GDP前八城市平均值为",av)