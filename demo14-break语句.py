# 开发人:胡雪晴
# 开发时间: 2022/9/14 20:50
'''
用于结束循环,通常与分支结构if一起使用跳出循环
for...in...:
    ......
    if ...:
        break

while(条件):
    ......
    if ...:
        break
'''
#从键盘录入密码,最多录入三次,若果正确就结束循环
for a in range(3):
    pwd=input('请输入密码:')
    if pwd=='123456':
        print('密码正确')
        break
    else:
        print('密码错误')
a=0
while a <3:
    pwd=input('请输入密码:')
    if pwd=='123456':
        print('密码正确')
        break
    else:
        print('密码错误')
        a+=1