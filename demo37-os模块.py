# 开发人:胡雪晴
# 开发时间: 2022/9/23 15:26
#os模块
#os模块与os.path模块用于对目录或文件进行操作
import os
os.system('notepad.exe')#打开记事本
os.system('calc.exe')#打开计算器
os.startfile('D:\\Program Files (x86)\\Tencent\\WeChat\\WeChat.exe')#直接调用可执行文件os.startfile(文件路径)

#os模块操作目录相关函数
print(os.getcwd())
print(os.listdir('../newproject'))#当前文件在newproject文件夹下,需要退两级到newproject文件夹的上级目录
#os.rmdir('newdir0')
#os.mkdir('newdir0')
#os.makedirs('A/B/newdir2.py')
#os.removedirs('A/B/newdir1')
os.chdir('E:\\胡雪晴测试专用\\newproject')
print(os.getcwd())
'''
getcwd()返回当前工作目录
listdir(path)返回指定路径下的文件和目录信息
mkdir(path[,mode])创建目录
makedirs(path1/path2...[,mode])创建多级目录
rmdir(path)删除目录
removedirs(path1/path2...)删除多级目录
chdir(path)将path设置为当前目录
walk(path)遍历整个目录包括子目录下的所有文件
'''
#获取指定目录下的所有py文件
import os
pathnow=os.getcwd()
lst=os.listdir(pathnow)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)
import os
path=os.getcwd()
lst_files=os.walk(path)
for dirpath,dirname,filename in lst_files:
    print(dirpath)
    print(dirname)
    print(filename)
    print('--------------------------------------')