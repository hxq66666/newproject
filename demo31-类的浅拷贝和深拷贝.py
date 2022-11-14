# 开发人:胡雪晴
# 开发时间: 2022/9/21 16:39
class Cpu:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
#变量的赋值操作
cpu1=Cpu()
cpu2=cpu1
print(cpu1,id(cpu1))
print(cpu2,id(cpu2))#创建了一个实例对象,放在了两个变量中
#浅拷贝,拷贝源对象(Computer的实例对象),对象包含的子对象不拷贝,因此源对象与拷贝对象会引用同一个子对象
disk1=Disk()
print(disk1)
computer=Computer(cpu1,disk1)
import copy#浅拷贝
computer2=copy.copy(computer)#拷贝computer赋给computer2
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)

#深拷贝,deepcopy()函数
#拷贝源对象以及源对象包含的子对象(Disk的实例对象和Cpu的实例对象),因此源对象与拷贝对象所有子对象也不相同
import copy
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)