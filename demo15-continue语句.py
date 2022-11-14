# 开发人:胡雪晴
# 开发时间: 2022/9/14 21:17
'''
结束当前循环 进入下一个循环 常与分支结构中的if一起使用
for...in...:
    ......
    if...:
        continue
    ...

while(条件):
    ......
    if...:
        continue
    ...
'''
#要求输出1到50之间5的倍数
for a in range(1,51):
    if not bool(a%5):
        print(a)
for a in range(1,51):
    if bool(a%5):
        continue
    print(a)
