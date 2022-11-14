# 开发人:胡雪晴
# 开发时间: 2022/9/15 15:09
#
'''
列表存储的是一个对象的引用
列表元素按顺序有序排列
索引映射唯一数据
列表可以存储重复数
任意数据类型混存
根据需要动态分配和回收内存
'''
#创建
lst1=['hello',1.23,123]#使用中括号[]
lst2=list(['hello',1.23,123])#调用内置函数list()
print(lst1,id(lst1),type(lst1))

#获取指定元素的索引.index(元素值,start,stop)
lst1=[1.3333,
3.1415926,
'a',
123456,
'a','非官方的',
['my name is : ','hxq']]
print(lst1.index('a'))#多个相同元素只返回相同元素中第一个元素的索引
#元素在列表中不存在会抛出ValueError print(lst1.index('ab'))
print(lst1.index('a',1,3))#在指定的start和stop之间进行查找 在1到3(不包括3)查找

#获取列表中的指定元素
print(lst1[0])
print(lst1[2])
print(lst1[-1])
print(lst1[6][1])

#获取多个元素,切片操作 列表名[start:stop:step]
#step为正数
print(lst1[1:5])#默认步长为1
print(lst1[:5:])#默认start为0,步长为1
print(lst1[1::])#默认stop为最后,步长为1
print(lst1[1:5:2])
#step为负数
print(lst1[::-1])#将列表反过来
print(lst1[6::-1])
print(lst1[5:1:-1])

#判断列表元素在列表中是否存在 in和not in
print('a'in lst1)
print('a'not in lst1)

#列表元素的遍历 for-in
for i in lst1:
    print(i)

#列表元素的增删改
'''添加'''
lst0=[10,20,30]
print(lst0,id(lst0))
lst0.append(40)#.append()在列表末尾添加一个元素
print(lst0,id(lst0))
lst0.append(lst2)#.append()将lst2作为一个元素添加到lst0中
print(lst0,id(lst0))
lst0.extend(lst2)#.extend()在列表末尾至少添加一个元素 将lst2每个元素分别添加到lst0中
print(lst0,id(lst0))
lst0.insert(4,50)#.insert()在列表任意位置添加一个元素 在索引为4的地方添加元素50
print(lst0,id(lst0))
#切片 在列表任意位置至少添加一个元素
lst3=[30,3,3.3,'333']
lst0[5:]=lst3#把后面的元素切掉,放上lst3的元素
print(lst0,id(lst0))
'''删除'''
lst0.remove(30)#.remove()移除一个元素,重复元素只移除第一个
print(lst0,id(lst0))
lst0.pop()#.pop()删除指定索引位置上的元素,不指定索引则删除最后一个元素
print(lst0,id(lst0))
lst0.pop(0)
print(lst0,id(lst0))
#切片，可以删除不止一个元素，会产生一个新的列表
new_lst0=lst0[1:4]
print(new_lst0,id(new_lst0))
#不产生新的列表对象，而是删除原列表中的内容
lst0[1:4]=[]
print(lst0,id(lst0))
#clear()清空列表
lst0.clear()
print(lst0,id(lst0))
#del删除列表对象
del lst0
#print(lst0,id(lst0))
'''修改'''
#修改一个元素
lst=[10,20,30,40]
print(lst,id(lst))
lst[0]='10'
print(lst,id(lst))
#为指定切片赋予一个新值
lst[1:3]=[22,33,'44',55,66]
print(lst,id(lst))

#列表元素的排序操作
lst0=[10,3,5,66,345,98,7]
print(lst0,id(lst0))
lst0.sort()#调用sort（）方法，将所有元素默认按照从小到大排序 reverse默认False
print(lst0,id(lst0))
lst0.sort(reverse=True)#调用sort（）方法，指定reverse=True进行降序排序
print(lst0,id(lst0))
print(sorted(lst0),id(sorted(lst0)))#调用内置函数sorted（）会产生一个新的列表，原列表不发生改变
print(sorted(lst0,reverse=True),id(sorted(lst0,reverse=True)))#可以指定reverse=True进行降序排序

#列表生成式（生成列表的公式）:[表示列表元素的表达式 for 自定义变量 in 可迭代对象]
lst1=[i for i in range(1,10)]
print(lst1)
lst1=[i*i for i in range(1,10)]
print(lst1)
lst1=[i*2 for i in lst3]
print(lst1)
