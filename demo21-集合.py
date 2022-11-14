# 开发人:胡雪晴
# 开发时间: 2022/9/16 10:22
'''可变无序的序列
集合是没有value的字典'''
#创建
s0={'xcds','ghf',90,90,'ghf'}#{}元素不能重复,一旦重复会覆盖
s1=set({'34','热风',324})#set()
s2=set(range(1,5))#set函数可以将range() 列表 元组 字符串 集合类型的数据转换成集合类型
print(s0,type(s0),s1,type(s1),s2,type(s2))
s3=set()#不可以使用{}定义一个空集合,自己能使用set()函数
print(s3)

#判断集合元素在集合中是否存在 in和not in
print(90 in s0)
print(90 not in s0)

#集合元素的增删改
'''添加'''
s0.add(80)#add()添加一个元素
print(s0)
s0.update({5,'78h',8.8})#update()至少添加一个元素 update函数的参数可以使集合 列表 元组
print(s0)
'''删除'''
s0.remove(90)#remove()删除一个指定的元素,元素不存在则抛出异常
print(s0)
s0.discard(990)#discard()删除一个指定的元素,元素不存在不抛出异常
print(s0)
s0.pop()#pop()一次只删除一个任意元素,不能添加参数,具体删除哪个元素不确定
print(s0)
s0.clear()#clear()清空集合
print(s0)

#集合间的关系
#== != 元素相同就相等
s1={10,20,30}
s2={30,20,10}
print(s1!=s2)
#子集issubset()方法
s3={10,20}
s4={20,90}
print(s3.issubset(s1))#s3是s1的子集吗
print(s4.issubset(s1))
#超集issuperset()方法
print(s1.issuperset(s3))
print(s1.issuperset(s4))
#是否有交集,isdisjoint()方法,没有交集为True,有交集为False
s5={90,100}
print(s1.isdisjoint(s4))
print(s1.isdisjoint(s5))

#集合的数据操作
#交集
print(s1.intersection(s4))
print(s1&s4)
#并集
print(s1.union(s4))
print(s1|s4)
#差集
print(s1.difference(s4))
print(s1-s4)
#对称差集
print(s1.symmetric_difference(s4))

#集合生成式
#{表示集合元素的表达式 for 自定义变量 in 可迭代对象}
s={i*2 for i in range(10)}
print(s)