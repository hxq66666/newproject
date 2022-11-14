# 开发人:胡雪晴
# 开发时间: 2022/9/14 21:36
'''
if条件表达式不成立时执行else
if...:
    ...
else:
    ...
没有遇到break时执行完循环体执行else
while/for...:
    ...
else:
    ...
'''
#for...else...遇break不执行else;不遇break执行完循环体后执行else
for i in range(3):
    pwd=input('请输入密码:')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print('对不起,密码输错超过三次')


a=0 #初始化变量
while a<3: #条件判断
    pwd=input('请输入密码:')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码错误') #条件执行体(循环体)
    a+=1 #改变变量
else:
    print('对不起,密码输错超过三次')