# 开发人:胡雪晴
# 开发时间: 2022/9/16 16:22
'''不可变字符序列'''
#创建'' "" '''''' """"""
a="Python"
b="""Python"""
print(a,id(a),b,id(b))

#字符串的查询
s='hello hello World'
print(s.index('lo'))#index()查找子串第一次出现的位置,查找不到报错
print(s.find('lo'))#find()查找子串第一次出现的位置,查找不到返回-1
print(s.rindex('lo'))#rindex()查找子串最后一次出现的位置,查找不到报错
print(s.rfind('lo'))#rfind()查找子串最后一次出现的位置,查找不到返回-1
print(s.rfind('lol'))

#字符串大小写转换的操作方法,转换之后将会产生一个新的字符串
s1=s.upper()#upper()方法将所有字母转换成大写
print(s1)
s2=s.lower()#lower()方法将所有字母转换成小写
print(s2)
s3='Hello World'
s4=s3.swapcase()#swapcase()方法把大写转化成小写,把小写转化成大写
print(s4)
print(s.title())#title()方法把每个单词的首字母转换成大写,剩余转换成小写
print(s.capitalize())#capitalize()方法把第一个字符转换成大写,剩余转换成小写

#字符串内容对齐的操作方法
print(s.center(30,'*'))#center()居中对齐,填充符不写默认空格 长度为30,填充符为*
print(s.center(2,'*'))#长度不够输出原字符
print(s.ljust(30,'*'))#ljust()左对齐 填充符不写默认空格 长度不够输出原字符
print(s.rjust(30,'*'))#rjust()右对齐 填充符不写默认空格 长度不够输出原字符
print(s.zfill(30))#zfill()右对齐 只能指定长度 使用0作为填充符 长度不够输出原字符
print('-3344'.zfill(8))#填充符0添加到了-后面

#字符串劈分的操作方法
lst=s.split()#split()方法从左边开始劈分 会得到一个列表 默认劈分符是空格
print(lst)
lst=s.split(sep='l')#sep参数指定劈分符
print(lst)
lst=s.split(maxsplit=1)#maxsplit参数指定最大劈分次数,经过最大次劈分之后,剩余子串会单独作为一部分
print(lst)
lst=s.rsplit()#rsplit()方法从右边开始劈分 会得到一个列表 默认劈分符是空格
print(lst)
lst=s.rsplit(sep='l')#sep参数指定劈分符
print(lst)
lst=s.rsplit(sep=' ',maxsplit=1)#maxsplit参数指定最大劈分次数,经过最大次劈分之后,剩余子串会单独作为一部分
print(lst)

#字符串判断的方法
print(s.isidentifier())#isidentifier()判断是否为合法的标识符
print('张三_dsf3443_'.isidentifier())
print(s.isspace())#isspace()判断是否全部由空白字符组成(回车 换行 水平制表符)
print('\n\t\r'.isspace())
print('张三dsf'.isalpha())#isalpha()判断是否全部由字母组成
print('123四'.isdecimal())#isdecimal()判断是否全部由十进制数字组成
print('1234'.isdecimal())
print('123四'.isnumeric())#isnumeric()判断是否全部由数字(中文数字/阿拉伯数字/罗马数字)组成
print('张三123四aBc'.isalnum())#isalnum())判断是否全部由字母和数字组成

#字符串替换
print(s.replace('l','0',3))#replace(被替换的字符串,替换的字符串,最大替换次数)

#字符串合并
lst=['324','df','啥的']
tp=('fdgd','梵蒂冈')
print('#'.join(lst))
print(''.join(tp))#join()将元组或者列表中的字符串合并成一个字符串,元组或者列表不能有数字
print('%'.join('Python'))#join()将字符串每个元素用指定符号连接起来

#字符串的比较操作< <= > >= ==  !=比较的是原始值 ord()函数获取
print('ccapp'>'ccbla')#只比较第一个不同的字符,其他不比较
print(ord('a'),ord('b'))
print(chr(97),chr(98))#chr()函数可以获取原始值对应的字符

#字符串切片操作,会产生新的对象 字符串[start:stop:step]
print(s[:4])
print(s[7::-1])

#格式化字符串
name='张三'
age=20
print('我的名字是%s,我今年%d岁'%(name,age))#%作为占位符 %s字符串 %i或%d整数 %f浮点数
print('我的名字是{0},我今年{1}岁,我朋友也叫{0},今年也是{1}岁'.format(name,age))#{}作为占位符
print(f'我的名字是{name},我今年{age}岁')#f-string
print('%10d'%99)#10表示宽度
print('%.3f'%3.11415926)#保留三位小数
print('%10.3f'%3.11415926)#同时表示宽度和精度 总宽度为10,保留小数点后三位
print('{0:.3}'.format(3.1415936))#0是索引 指向format方法的参数 .3表示的是一共是三位数字
print('{0:.3f}'.format(3.1415936))#.3加f表示的是保留小数点后三位
print('{0:10.3f}'.format(3.1415936))#总宽度为10,保留小数点后三位
print('{0:10.3}'.format(3.1415936))

#字符串的编码和解码
#编码
s='天涯共此时'
print(s.encode(encoding='UTF-8'))
print(s.encode(encoding='GBK'))
#解码 编码解码格式要相同
byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))

