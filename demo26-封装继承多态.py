# 开发人:胡雪晴
# 开发时间: 2022/9/20 16:24
'''
面向对象的三大特征：
封装：提高程序的安全性
  将属性和方法封装到类中，在方法内部对属性进行操作，在类外部调用方法，这样无需关心方法内部的具体实现细节，从而隔离了复杂度
  如果属性不希望在类对象外部被访问，前边使用两个_
继承：提高代码的复用性
  语法结构：
  class 子类类名（父类1，父类2.。。）：
      pass
  如果一个类没有继承任何类，则默认继承object
  python支持多继承，定义子类时，必须在其构造函数中调用父类的构造函数
多态：提高程序的可扩展性和可维护性
  多态就是具有多种形态：即便不知道一个变量所引用的对象到底是什么类型，仍然可以通过这个变量调用方法，在运行过程中根据变量所引用的对象类型，动态决定调用哪个对象中的方法
'''
#继承的代码实现
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print('姓名:{0},年龄:{1}'.format(self.name,self.age))
#定义子类
class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)#从父类继承name,age
        self.stu_no=stu_no
class Teacher(Person):
    def __init__(self,name,age,teacheryear):
        super().__init__(name,age)#从父类继承name,age
        Teacher.teacheryear=teacheryear
stu1=Student('Jack',20,'2014090990')
tea1=Teacher('Mary',40,14)
stu1.info()
tea1.info()
#多态
class Animal(object):
    def eat(self):
        print('动物会吃东西')
class Dog(Animal):
    def eat(self):
        print('狗吃肉')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')
class Person():
    def eat(self):
        print('人吃五谷杂粮')
def food(living):
    living.eat()
food(Animal())
food(Dog())
food(Cat())#Dog Cat类重写了继承Animal类的eat方法 继承关系
food(Person())#Person对象不存在继承关系，也有eat（）方法 ，所以会调用自己的eat（）方法

