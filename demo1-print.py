# 开发人:胡雪晴
# 开发时间: 2022/9/9 8:53
# print()输出函数
# 输出数字
print(4.44)
# 输出字符串
print('hello,狗富贵')
print('hello,张富赢')
# 输出含有运算符的表达式
print(3 * 2)
# 将数据输出到文件中
fp = open('E:\胡雪晴测试专用\ceshi.txt', 'a+')  # a+ 没有文件就创建,有就在文件内容后面追加
print('hello world', file=fp)  # 不设置file= 代码执行之后会生成一个空文件,输出内容不写入文件中
fp.close()
# 使用,不进行换行输出 不使用,是换行输出
print('hello world', 'hello 狗富贵', 'hello 张富赢')
abcde = 345
print(abcde)
print('abcde')
print("abcde")
print('''abcde''')
print('abcde =', abcde)
# 输出内容换行 三引号回车 单双引号使用换行字符
print('''hello
狗富贵''')
print("""hello
狗富贵""")
print('hello\n狗富贵')
print("hello\n狗富贵")
