# 开发人:胡雪晴
# 开发时间: 2022/9/19 10:59
'''
1.漏掉末尾冒号,如if语句 循环语句 else子句
2.缩进错误
3.把英文符号写成中文符号,如冒号 引号 括号
4.字符串拼接的时候,把字符串类型和数字拼一起
5.没有定义变量
6.=和==
7.索引越界问题
lst=[1,2,3,4]
lst[4]
'''


#python的异常处理机制(错误操作或者一些例外情况导致的程序异常)
#try...except
'''
try抛出异常会执行except块

try:
    可能会出现异常的代码
except 异常类型:
    异常处理代码
    
常见的异常类型:
ZeroDivisionError除零
IndexError序列中没有此索引
KeyError映射中没有这个键
NameError未声明/初始化对象
SyntaxError语法错误,如int a=20
ValueError传入无效的参数,如a=int('hello')
'''
try:
    a=int(input('请输入被除数:'))
    b=int(input('请输入除数:'))
    print(a/b)
except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('只能输入数字')
#try...except...else
'''
如果try块中没有抛出异常,则执行else块,如果try中抛出异常,则执行except块
'''
try:
    a=int(input('请输入被除数:'))
    b=int(input('请输入除数:'))
    result=a/b
except BaseException as e:#不确定会出现什么异常用BaseException,as是取了个别名
    print('出错了',e)
else:
    print('计算结果为:',result)
#try...except...else...finally
'''finally块无论是否发生异常都会执行,能常用来释放try块中申请的资源'''
try:
    a=int(input('请输入被除数:'))
    b=int(input('请输入除数:'))
    result=a/b
except BaseException as e:
    print('出错了',e)
else:
    print('计算结果为:',result)
finally:
    print('谢谢使用!')

#traceback模块打印异常信息
import traceback#导出异常
try:
    print('开始')
    num=10/0
except:
    traceback.print_exc()