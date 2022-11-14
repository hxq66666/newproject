# 开发人:胡雪晴
# 开发时间: 2022/9/21 17:18
#创建模块
#新建一个.py文件

#导入模块
import math#导入模块 import 模块名称
print(dir(math))
print(math.pi)
print(math.pow(2,3))#得到的数据类型是浮点型 pow()函数得到的数据类型是整型
print(math.ceil(9.0001))
print(math.floor(9.9999))
import math as e#导入模块 import 模块名称 [as 别名]
print(e.pi)
from math import pi#导入模块 from 模块名称 import 函数/变量/类
print(pi)
#导入自定义模块
#右键单击.py文件所属文件夹,选中Mark Directory as,选中Sources Root
import demo
print(demo.fac(9))
from demo import fib
print(demo.fib(9))

#以主程序的形式运行
'''
如果一个模块不是被导入其它程序中执行,那么它可能在解释器的顶级模块中执行,顶级模块的__name__变量值为'__main__'
执行当前文件,当前文件__name__变量值为'__main__'
若想确保当前文件的导入文件的输出不会显示在当前文件的执行结果中,需要给其导入文件的输出语句添加限制条件
if __name__ == '__main__':
    print...
'''

#第三方模块的安装 cmd:pip install 模块名 例如:pip install schedule
#第三方模块的使用 import 模块名
import schedule#schedule第三方模块
import time
def job():
    print('hello')
schedule.every(3).seconds.do(job)#每三秒执行以下job函数，job函数不会马上被执行，而是进入pending状态
while True:#只要不停止脚本，或者重启运行脚本的主机的话，该脚本将一直运行下去
    schedule.run_pending()#schedule.run_pending()函数的作用就是立即执行所有状态为pending的函数
    time.sleep(1)#每隔三秒执行一次job，休眠1秒