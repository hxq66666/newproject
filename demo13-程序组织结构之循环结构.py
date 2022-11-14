# 开发人:胡雪晴
# 开发时间: 2022/9/14 19:55
'''
while循环语法结构:
while 条件表达式:
    条件执行体(循环体)
'''
a=1
sum=0
while a<=100:
    if a%2==0:#等同于if not bool(a%2)
        sum+=a
    a+=1
print('1到100之间的偶数和:',sum)
'''
for-in循环语法结构:
for 自定义的变量 in 可迭代对象
    循环体
可迭代对象:字符串,序列
'''
for item in 'Python':#第一次取出为P,将P赋值给item并将item值输出
    print(item)
#range()可以产生一个整数序列,也是一个可迭代对象
for i in range(10):
    print(i)
#如果在循环体中不需要使用自定义变量,可将自定义变量写为"_"
for _ in range(5):
    print('人生苦短')
#计算1到100之间的偶数和
sum=0
for a in range(101):
    if not bool(a%2):
        sum+=a
print('1到100之间的偶数和:',sum)
print('100到999之间的水仙花数有:')
for a in range(100,1000):
    if a==(a//100)**3+(a%10)**3+((a//10)%10)**3:
        print(a)