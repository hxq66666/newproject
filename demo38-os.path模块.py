# 开发人:胡雪晴
# 开发时间: 2022/9/23 15:59
import os.path
print(os.path.abspath('demo38-os.path模块.py'))
print(os.path.exists('demo38-os.path模块.py'),os.path.exists('hello.py'))
print(os.path.exists('E:\\胡雪晴测试专用\\newproject'))
print(os.path.join('E:\\胡雪晴测试专用','demo38-os.path模块.py'))
print(os.path.split('E:\胡雪晴测试专用\newproject\demo38-os.path模块.py'))#将目录与文件拆分开
print(os.path.splitext('E:\胡雪晴测试专用\newproject\demo38-os.path模块.py'))#将文件名与后缀拆分开
print(os.path.basename('E:\胡雪晴测试专用\newproject\demo38-os.path模块.py'))#把文件名提取出来
print(os.path.dirname('E:\胡雪晴测试专用\\newproject\demo38-os.path模块.py'))#把目录提取出来
print(os.path.isdir('E:\胡雪晴测试专用\\newproject\demo38-os.path模块.py'))
print(os.path.isdir('E:\胡雪晴测试专用\\newproject'))
'''
abspath(path) 用于获取文件或目录的绝对路径
exists(path) 用于判断文件或目录是否存在,如果存在返回True,否则返回False
join(path,name) 将目录与目录或者文件名拼接起来
splitext() 分离文件名和扩展名
basename(path) 从一个目录中提取文件名
dirname(path) 从一个路径中提取文件路径,不包括文件名
isdir(path) 用于判断是否为路径
'''
#列出指定目录下的所有py文件
import os
pathnow=os.getcwd()
for filename in os.listdir(pathnow):
    splitname=os.path.splitext(filename)
    if '.py'in splitname:
        print(filename)


    


