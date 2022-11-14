# 开发人:胡雪晴
# 开发时间: 2022/9/14 13:45
'''单分支结构
if 条件表达式:
    条件执行体
'''
money=1000
outmoney= int(input('请输入取款金额:'))
if money>=outmoney:
    money-=outmoney
    print('取款成功,剩余金额为:',money)
'''双分支结构
if 条件表达式:
    条件执行体1
else:
    条件执行体2
'''
money=1000
outmoney= int(input('请输入取款金额:'))
if money>=outmoney:
    money-=outmoney
    print('取款成功,剩余金额为:',money)
else:
    print('取款失败,余额不足')
'''
条件表达式简写if...else..
语法结构:
X if 判断条件 else Y
判断条件成立 执行左边 判断条件不成立 执行右边
'''
#使用条件表达式进行比较
num_a=int(input('请输入一个整数:'))
num_b=int(input('请输入另外一个整数:'))
print(str(num_a)+'大于等于'+str(num_b)  if num_a>=num_b else str(num_a)+'小于'+str(num_b))
'''
多分支结构,多选一执行
if 条件表达式:
    条件执行体1
elif 条件表达式2:
    条件执行体2
elif 条件表达式n:
    条件执行体n
else:
    条件执行体n+1
'''
score=int(input('请输入您的考试成绩:'))
if score>=90 and score<=100: #也可以写成90<=score<=100
    print('您的等级为A')
elif score>=80 and score<=89:
    print('您的等级为B')
elif score>=70 and score<=79:
    print('您的等级为C')
elif score>=60 and score<=69:
    print('您的等级为D')
elif score>=0 and score<=59:
    print('您的等级为E')
else:
    print('对不起,您的成绩有误,不在成绩的有效范围!')
'''
嵌套结构
if 条件表达式:
    if 内层条件表达式:
        内层条件执行体1
    else:
        内层条件执行体2
else:
    条件执行体
'''
isvip=input('是会员吗?Y/N')
monetary=int(input('请输入消费金额:'))
if isvip=='Y':
    if monetary>=200:
        monetary*=0.8
    elif 200>monetary>=100:
        monetary*=0.9
    else:
        monetary=monetary
    print('会员价:',monetary)
else:
    if monetary>=200:
        monetary*=0.95
    else:
        monetary = monetary
    print('非会员价:',monetary)