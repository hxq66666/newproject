# 开发人:胡雪晴
# 开发时间: 2022/9/19 15:07
#类的定义
class Student:#类名由一个或多个单词组成,每个单词首字母要大写,其余小写
    native_place='吉林'#直接写在类中方法外的变量称为类属性
    def __init__(self,name,age,weight):#__init__特殊的类实例方法，称为构造方法（或初始化方法）__init__() 方法可以包含多个参数，但必须包含一个名为 self 的参数，且必须作为第一个参数
        self.name=name#self.name实例属性,在这里进行了赋值操作,将局部变量name的值赋给了实例属性
        self.age=age
        self.__weight=weight#加两个下划线：__，weight不允许在类的外部被使用，但是可以在类的内部使用
    def st_age(self):#必须有参数 实例方法 类里定义称为方法 类外定义的称为函数
        print('%s的年龄是%d，体重是%f'%(self.name,self.age,self.__weight))#__weight不允许在类的外部被使用，但是可以在类的内部使用
    @staticmethod#定义静态方法,静态方法中不允许使用self
    def method():
        print('我使用了staticmethod方法修饰,所以我是静态方法')
    @classmethod#类方法
    def cm(cls):
        print('我使用了classmethod方法修饰,所以我是类方法')
def drink():#类外定义的是函数
    print('喝水')
#对象的创建/类的实例化 有了实例就可以调用类中的内容
#实例名=类名()
st1=Student('张三',20,65)#创建类的对象
print(id(st1))
print(type(st1))
print(st1)
print(id(Student))
print(type(Student))
print(Student)
st1.cm()#调用类方法:对象名.类方法名
Student.cm()#调用类方法：类名.类方法名
st1.method()#调用静态方法:对象名.静态方法名
Student.method()#调用静态方法：类名.静态方法名
print(st1.name)#访问实例属性
print(st1.age)
st1.st_age()#调用实例方法:对象名.实例方法名
Student.st_age(st1)#调用实例方法:类名.实例方法名(类的对象)  对象名.方法名()
print(st1.native_place)#访问类属性
print(Student.native_place)#访问类属性
Student.native_place='天津'
print(st1.native_place)
print(Student.native_place)
#动态绑定属性和方法
stu1=Student('李四',21,60)
stu2=Student('王二',20,70)#一个类可以创建多个该类的实例对象，每个实例对象的属性可以相同也可以不同
stu2.gender='女'#为stu2动态绑定属性
print(stu2.name,stu2.age,stu2.gender)
#print(stu1.name,stu1.age,stu1.gender)没有定义stu1的gender，会报错
stu1.drink=drink#为stu1动态绑定方法
stu1.drink()
#stu2.drink()报错，因为stu2没有绑定drink（）方法
#print(stu2.__weight)报错，因为__weight不允许在类的外部被使用
print(dir(stu2))#dir()函数可以查看指定对象所有的属性和方法
print(stu2._Student__weight)#在类的外部可以通过_类名__weight访问