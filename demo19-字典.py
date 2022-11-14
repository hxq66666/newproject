# 开发人:胡雪晴
# 开发时间: 2022/9/15 17:24
'''
无序可变序列,以键值对的方式存储数据,key不允许重复,value可以重复
字典中的key必须是不可变对象
字典也可以根据需要动态得伸缩
字典会浪费较大的内存,是一种使用空间换时间的数据结构
'''
#创建
scores={'张三':100,'李四':90,'王五':45}#{}
ages=dict(name='李四', age=60)#内置函数dict()
print(scores,type(scores))
print(ages,type(ages))
dt0=dict()#空字典
dt1={}#空字典
print(dt0,dt1,type(dt0),type(dt1))

#字典中元素的获取
print(scores['张三'])#[键],输入一个不存在的键报错
print(scores.get('张三'))#get(键)方法 输入一个不存在的键运行结果为None
print(scores.get('麻子'))

#判断指定键在字典中是否存在 in和not in
print('张三'in scores)
print('张三'not in scores)

#字典元素的增删改
#key是不可变对象,只能改变value
'''增加'''
scores['陈六']=78
print(scores)
'''修改'''
scores['陈六']=80
print(scores)
'''删除'''
del scores['张三']#删除指定的键值对

print(scores)
scores.clear()#清空字典
print(scores)

#获取字典视图
scores={'张三':100,'李四':90,'王五':45}
keys=scores.keys()#keys()获取字典所有key
print(keys,type(keys))
print(list(keys))#将视图转成列表
values=scores.values()#values()获取字典所有value
print(values,type(values))
items=scores.items()#items()获取字典所有键值对
print(items,type(items))
print(list(items))#转化之后的列表元素由元组组成

#字典元素的遍历for-in
for i in scores:
    print(i)#键
for i in scores:
    print(i, scores[i])#键值
for i in scores:
    print(i,scores[i],scores.get(i))#键值

#键不能重复,一旦重复会覆盖,值可以重复
d0={'name':'jack','name':'李迪'}
print(d0)
d1={'name':'jack','age':20,'score':20}
print(d1)

#字典生成式
#{表示字典key的表达式:表示字典value的表达式 for 自定义表示key的变量,自定义表示value的变量 in 可迭代对象}
sales=['水果','蔬菜','肉类']
prices=[20,10,50,90]
d2={s:p for s,p in zip(sales,prices)}
print(d2)#生成的时候以数据少的为基准

