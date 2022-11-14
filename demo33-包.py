# 开发人:胡雪晴
# 开发时间: 2022/9/22 11:12
'''
将一组功能相近的模块组织在一个目录下
包与目录的区别
包:new python package 包含__init__.py文件的目录称为包
目录:new directory 目录里通常不包含__init__.py文件
'''
#包的导入  import 包名.模块名 [as 别名]
import package0.module0
from package0 import module0

print(package0.module0.a)
import package0.module1 as e
print(e.b)
#导入包下模块注意事项:使用import导入时 import只能跟包名或者模块名 使用from...import...导入包时 import可以跟包,模块,函数,变量
from package0.module1 import b
print(b)

