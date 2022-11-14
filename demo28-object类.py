# 开发人:胡雪晴
# 开发时间: 2022/9/20 17:28
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):#__str__（）是父类object的方法 重写__str__（）
        return '我的名字是{0}，我今年{1}岁'.format(self.name,self.age)
stu=Student('张三',10)
print(dir(stu))#dir()函数可以查看指定对象所有的属性和方法
print(stu)#重写__str__（）之后，不再输出内存地址<__main__.Student object at 0x00000186DF627C70>，而是去调用重写之后的__str__（）
print(type(stu))