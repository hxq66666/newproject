# 开发人:胡雪晴
# 开发时间: 2022/9/23 14:48
with open('E:\胡雪晴测试专用\ceshi.txt','r') as file:
    print(file.read())#使用with语句就无需手动关闭文件file.close()
#文件复制
file2=open('E:\胡雪晴测试专用\ceshi2.png','wb')
file3=open('E:\胡雪晴测试专用\ceshi3.png','rb')
file2.write(file3.read())
file2.close()
file3.close()

with open('E:\胡雪晴测试专用\ceshi3.png','rb') as file3:
    with open('E:\胡雪晴测试专用\ceshi2.png','wb') as file2:
        file2.write(file3.read())