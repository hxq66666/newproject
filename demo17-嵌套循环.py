# 开发人:胡雪晴
# 开发时间: 2022/9/15 14:26
'''
循环结构中又嵌套了另外的完整的循环结构,其中内层循环作为外层循环的循环体执行
while...:
    ...
    for...:
        ...
    else:
        ...
    ...
'''
#输出一个三行四列的矩形
for i in range(3): #行表,执行三次,一次是一行
    for j in range(4):
        print('*',end='\t') #不换行输出
    print() #打行
#打印一个直接三角形
for i in range(1,10):
    for j in range(i):
        print('*',end='\t')
    print()
#输出九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+'*'+str(j)+'='+str(i*j),end='\t')
    print()
'''
二重循环中的break和continue用于控制本层循环
while...:
    ...
    for...:
        ...
        if...:
            break/continue
        ...
    else:
        ...
    ...
'''
for i in range(2):
    for j in range(1,10):
        if j%2==0:#j=2时跳出内层循环 执行下一轮外层循环
            break
        print(j,end='\t')#内层循环的输出语句
    print()
for i in range(2):
    for j in range(1,10):
        if j%2==0:
            continue #j=2.4.6.8时跳出本次循环,继续执行内层的下一轮循环
        print(j,end='\t')#内层循环的输出语句
    print()