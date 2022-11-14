# 开发人:胡雪晴
# 开发时间: 2022/9/21 15:16
#__dict__获得类对象或者实例对象所绑定的所有属性和方法的字典
print(dir(object))#查看object类对象的属性和方法
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
class D(A):
    pass
c=C('Mary',20)
print(c.__dict__)#实例对象会获取属性字典
print(C.__dict__)#类对象会获取方法字典
#__class__
print(c.__class__)#输出对象所属的类
#__bases__
print(C.__bases__)#输出C类父类类型的元素
#__base__
print(C.__base__)#输出定义时离C类最近的父类
#__mro__
print(C.__mro__)#查看类的层次结构
#A.__subclasses__()
print(A.__subclasses__())#查看子类