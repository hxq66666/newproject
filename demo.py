# 开发人:胡雪晴
# 开发时间: 2022/9/22 10:44
def fun(a,b):
    c=a+b#c是函数体内的变量，为局部参数，a和b是形参，作用范围也是函数内部，相当于局部变量
    print(c)


#递归函数(函数体内调用了该函数本身)
#使用递归函数计算阶乘n!
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
if __name__=='__main__':
    print(fac(6))
#递归函数计算斐波那契数列(1,1,2,3,5,8,13...后面一个数是前两项之和)第n项
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
if __name__ == '__main__':
    print(fib(7))
for i in range(1,8):
    if __name__ == '__main__':
        print(fib(i))
