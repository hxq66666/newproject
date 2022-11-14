# 开发人:胡雪晴
# 开发时间: 2022/9/9 9:39
#转义字符
# n:newline 换行
print('hello\n狗富贵')
#水平制表符 tab键 光标移动到下一组四个空格开始处
print('hello\t狗富贵')
print('helloooo\t狗富贵')
#回车 return
print('hello\r狗富贵')#输出结果是狗富贵 回车转义符后面的内容把前面的hello给覆盖掉了
#退一格
print('hello\b狗富贵')#把转义字符前面的一个字符退掉了
print('hello\b\b狗富贵')
# \\ \' \"
print('https:\\\\www\'.bili"bili.com/video')
#原字符
#使转义字符不起作用,在字符串前加上r或者R
print(r'hello\n狗富贵')
#注意事项:字符串最后字符不能是单个反斜线,双个可以
print(r'hello\n狗富贵\\')