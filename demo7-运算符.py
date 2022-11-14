# 开发人:胡雪晴
# 开发时间: 2022/9/9 12:00
#算术运算符
#加+ 减- 乘* 除/(结果是小数) 整除//(结果取整，一正一负向下取整) 取余% 幂**
print(9/3)
#整除//(结果取整，一正一负向下取整)
print(9//4)
print(-9//-4)
print(-9//4)
print(9//-4)
print(9.0//4)
#取余% 公式：余数=被除数-除数*商（整除的商）
print(9%4)
print(-9%-4)
print(-9%4)
print(9%-4)
print(9.0%4)
#幂**
print(9**4)

#赋值运算符 运算顺序从右往左，先计算等号右边的值然后赋值给等号左边
#支持链式赋值
a=b=c=2
print(a,id(a),b,id(b),c,id(c))
#支持参数赋值
a+=30 #a=a+30
print(a)
b-=10 #b=b-10
print(b)
c*=4 #c=c*4
print(c)
a/=5 #a=a/5
print(a,type(a))
a//=2 #a=a//2
print(a)
a%=2 #a=a%2
print(a,type(a))
#支持系列解包赋值,=变量个数和值的个数一致
a,b,c=10,20,30
print('交换之前:',a,b,c)
#交换
a,b,c=c,a,b
print('交换之后:',a,b,c)

#比较运算符(> < >= <= !=) 结果为bool类型
a,b=10,20
print('a大于b么？',a>b) #False
print('a不等于b么？',a!=b) #True
print('a等于b么？',a==b) #False
'''
=赋值运算符
==比较运算符，比较的是值
比较标识id()使用的是is
'''
a=10
b=10
print(a==b) #value
print(a is b) #id
print(a is not b) #id
print(id(a),id(b))
list1=[11,22,33,44]
list2=[11,22,33,44]
print(list1==list2) #value
print(list1 is list2) #id
print(list1 is not list2) #id
print(id(list1),id(list2))

#布尔运算符 and  or  not  in  not in
#and 只有同时为True 结果才为True
a,b=1,2
print(a==1and b==2)
print(a==1and b<2)
#or 只要一个为True，结果是True
print(a==1or b<2)
#not 运算数为True，结果为False；运算数为False，结果为True
f=True
print(not f)
#in和not in
s='hello world'
print('w'in s,'k'in s)
print('w'not in s,'k'not in s)
print(a not in range(0,100))

#位运算符 将数据转成二进制然后进行运算
#位与 &
print(4&8) #转化成二进制，对应数位都是1，数位才是1，否则为0
#4的二进制0100，8的二进制1000 结果是0000，对应结果十进制数0
#位或 |
print(4|8) #转化成二进制，对应数位都是0，结果数位才是0，否则为1
#4的二进制0100，8的二进制1000 结果是1100，对应十进制数12
#左移位运算符 << 高位溢出舍弃，低位补0 相当于*2
#右移位运算符 >> 低位溢出舍弃，高位补0 相当于//2
print(4<<1)#左移1位 4的二进制00000100，左移1位是00001000
print(4>>1)#右移一位 4的二进制00000100，右移位是00000010
print(-45>>1)

#运算符优先级
#**  (* / // %) (+ -) (<< >>) & | (> < <= >= == !=) and or =
#()>算术运算符>位运算符>比较运算符>布尔运算符>赋值运算符