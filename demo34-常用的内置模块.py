# 开发人:胡雪晴
# 开发时间: 2022/9/22 11:32
'''
sys 与Python解释器及其环境操作相关的标准库
time 提供与时间相关的各种函数的标准库
os 提供了访问操作系统服务功能的标准库
calendar 提供与日期相关的各种函数的标准库
urllib 用于读取来自网上(服务器)的数据标准库
json 用于使用JSON序列化和反序列化对象
re 用于在字符串中执行正则表达式匹配和替换
math 提供标准算数运算函数的标准库
decimal 用于进行精确控制运算精度,有效位数和四舍五入操作的十进制计算
logging 提供了灵活的记录事件,错误,警告和调试信息等日志信息的功能
'''
import sys
print(sys.getsizeof(24))#获取所占内存字节多少
import time
print(time.time())#秒
print(time.localtime(time.time()))

import urllib.request
print(urllib.request.urlopen('http://www.baidu.com').read())
