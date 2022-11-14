# 开发人:胡雪晴
# 开发时间: 2022/9/20 17:22
#方法重写（子类想输出自己特有的，子类重写后的方法中可以通过super().XXX()调用父类中被重写的方法）
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print('姓名:{0},年龄:{1}'.format(self.name,self.age))
class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no
    def info(self):#方法重写
        super().info()#不写super().info()方法，结果只会输出stu_no
        print('学号:{0}'.format(self.stu_no))
class Teacher(Person):
    def __init__(self,name,age,teacheryear):
        super().__init__(name,age)
        Teacher.teacheryear=teacheryear
    def info(self):
        super().info()
        print('教龄:{0}'.format(self.teacheryear))
stu1=Student('Jack',20,'2014090990')
tea1=Teacher('Mary',40,14)
stu1.info()
tea1.info()