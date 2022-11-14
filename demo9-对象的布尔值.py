# 开发人:胡雪晴
# 开发时间: 2022/9/14 13:35
# False 数值0 None 空字符串 空元祖 空列表 空字典 空集合的布尔值为False
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool(())) #空元祖
print(bool(tuple())) #空元祖
print(bool([])) #空列表
print(bool(list())) #空列表
print(bool({})) #空字典
print(bool(dict())) #空字典
print(bool(set())) #空集合
print(bool(range(0)))
#其他对象的布尔值均为True
print(bool('hello world'))
age=int(input('请输入您的年龄:'))
print('您的年龄是:'+str(age) if age else '您的年龄输入有误,请重新输入!') #输入age大于0 if判断为True 执行左边
#输入age等于0 if判断为False 执行右边