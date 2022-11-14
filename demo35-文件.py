# 开发人:胡雪晴
# 开发时间: 2022/9/22 16:06
#内置函数open（）创建读取文件 file=open(文件名,[打开模式默认只读，编码格式默认gbk])
file=open('E:\胡雪晴测试专用\ceshi.txt','r')
print(file.readlines())#结果是个列表
file.close()
fp = open('E:\胡雪晴测试专用\ceshi.txt','a+') #a+ 没有文件就创建,有就在文件内容后面追加
print('hello world',file=fp) #不设置file= 代码执行之后会生成一个空文件,输出内容不写入文件中
fp.close()
'''
常用的文件打开模式:
r 只读 文件指针在文件开头
w 只写 没有文件就创建,有就覆盖，文件指针在文件开头
a 以追加模式打开文件 没有文件就创建,文件指针在文件开头，有就在文件内容后面追加，文件指针在原文件末尾
b 以二进制方式打开文件，不能单独使用，需要与其他模式一起使用 rb或者wb
+ 读写方式打开文件，，不能单独使用，需要与其他模式一起使用 a+
'''
file1=open('E:\胡雪晴测试专用\ceshi0.txt','w')
file1.write('Python1')
file1.close()
#二进制文件:MP3音频文件，jpg文件 .doc文件 不能用记事本打开，数据内容用字节存储
file2=open('E:\胡雪晴测试专用\ceshi2.png','wb')
file3=open('E:\胡雪晴测试专用\ceshi3.png','rb')
file2.write(file3.read())
file2.close()
file3.close()

'''
文件对象的常用方法
read([size]) 从文件中读取size个字节或字符的内容返回。若不指定size，则读取全部内容
readline() 从文本文件中读取一行内容
readlines() 把文本文件中的每一行都作为独立的字符串对象，并将这些对象放入列表输出
writer(str) 将字符串str的内容写入文件按
writerlines(s_list) 将字符串列表s_list写入文件，不添加换行符
seek(offset[,whence]) 把文件指针移到新的位置，offset表示相对于whence的位置：
  offset：为正往结束方向移动，为负往开始方向移动
  whence：
    0：从文件头开始计算（默认值）
    1：从当前位置开始计算
    2：从文件结尾开始计算
tell() 返回文件指针的当前位置
flush() 把缓冲区的内容写入文件，但不关闭文件
close() 把缓冲区的内容写入文件，同时关闭文件，释放对象文件相关资源
'''
file=open('E:\胡雪晴测试专用\ceshi.txt','r')
print(file.read(4))
file.close()
file=open('E:\胡雪晴测试专用\ceshi.txt','r')
print(file.readline())
file.close()
file=open('E:\胡雪晴测试专用\ceshi.txt','r')
print(file.readlines())
file.close()
file=open('E:\胡雪晴测试专用\ceshi.txt','a')
file.write('你好中国')
file.close()
s_list=['hello','China']
file=open('E:\胡雪晴测试专用\ceshi.txt','a')
file.writelines(s_list)
file.close()
file=open('E:\胡雪晴测试专用\ceshi.txt','r')
file.seek(2)#offset=1遇汉字时会乱码，一个汉字占2个字节
print(file.read())
print(file.tell())
file.close()
