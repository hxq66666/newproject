# 开发人:胡雪晴
# 开发时间: 2022/9/9 10:54
#浮点型数据加法运算
from decimal import Decimal #decimal 模块
print(Decimal('1.1')+Decimal('2.2'))
#布尔类型
f1=True
f2=False
print(f1,type(f1),f2,type(f2))
#布尔类型可进行整数运算 True表示1.False表示0
print(f1+1,f2+1)
print(f1+f2,type(f1+f2))
#数据类型转换和拼接
#字符串str和整型int数据不能用连接符+连接,需要进行数据类型转换
#print('我的名字是:'+name+',我今年'+age+'岁.')
name='狗富贵'
age=29
print('我的名字是:',name,',我今年',age,'岁.')#字符串str和整型int数据能用,连接
print('我的名字是:'+name+',我今年'+str(age)+'岁.')#将int类型通过str()函数转换成str类型
#int()
#将str转换成int()类型,前提是字符串必须为整数串,小数串和非数字串不能转
s0='1234'
print(s0,type(s0),int(s0),type(int(s0)))
#将float转换成int()类型,截取整数部分,舍掉小数部分
s1=3.1415926
print(s1,type(s1),int(s1),type(int(s1)))
#将bool转换成int()类型,转换值为0和1
s2=True
print(s2,type(s2),int(s2),type(int(s2)))
#float()
#字符串中的数据如果是非数字串,则不允许转换成float()
#整数转换成浮点数,末尾为.0
s3=3
print(s3,type(s3),float(s3),type(float(s3)))
#字符串拼接
#拼接符+
abcd = '123' + '456' + '789'
print(abcd)
#相同字符串拼接用*
abc = 'we' * 3
print(abc)
print('we' * 3)