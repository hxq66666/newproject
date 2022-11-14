# 开发人:胡雪晴
# 开发时间: 2022/9/14 15:22
#range()的三种创建方式
r1=range(10)#等同于range(0,10),默认从0开始 默认步长为1
r2=range(2,10) #指定起始值 结束值,默认步长为1
r3=range(2,10,2) #指定起始值 结束值和步长
print(r1)
print(list(r1)) #list用于查看range对象中的整数序列
print(r2)
print(list(r2))
print(r3)
print(list(r3))
#判断指定的整数是否在序列中使用的是 in和not in
print(10 in r3)
print(10 not in r3)