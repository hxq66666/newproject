# 开发人:胡雪晴
# 开发时间: 2022/9/21 15:34
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __add__(self, other):#通过重写__add__（）方法，实现自定义对象的相加
        return self.name+other.name
    def __len__(self):#通过重写__len__(self)方法，让内置函数len（）的参数可以是自定义类型
        return len(self.name)
ps1=Person('易烊千玺11',19)
ps2=Person('李四',29)

#__add__（）
a=20
b=100
c=a+b#底层实际是c=a.__add__(b)
d=a.__add__(b)
print(c,d)
s0=ps1+ps2#实现了两个对象的加法运算，因为在Student类中编写了__add__（）特殊方法
s1=ps1.__add__(ps2)#实现了两个对象的加法运算，因为在Student类中编写了__add__（）特殊方法
print(s0,s1)

#__len__（）
lst=[11,22,33,44]
print(len(lst))#len()是内置函数
print(lst.__len__())
print(len(ps1))
print(ps1.__len__())

#__new__()用于创建对象 __init__()对创建的对象进行初始化 先创建再初始化
class Person:
    def __new__(cls, *args, **kwargs):#__new__()继承了object
        print('__new__()被调用执行了,cls的id为{0}'.format(id(cls)))
        obj=super().__new__(cls)#new中创建的对象就是self和ps0
        print('创建的对象的id为{0}'.format(id(obj)))
        return obj #返回的obj给了self
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('__init__()被调用执行了,self的id为{0}'.format(id(self)))
print('object类对象id为{0}'.format(id(object)))
print('Person类对象id为{0}'.format(id(Person)))
ps0=Person('张三',30)#创建实例对象
print('ps0这个实例对象id为{0}'.format(id(ps0)))
'''
先把Person给了new中的cls
然后把cls传给了object中的new去创建对象obj
然后将创建的对象赋值给了self
self初始化方法执行结束再把self付给ps0
'''