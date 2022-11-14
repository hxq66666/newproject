# 开发人:胡雪晴
# 开发时间: 2022/9/17 16:02
'''
def 函数名(输入参数):
    函数体
    return xxx
'''


def calc(a, b):
    c = a + b
    return c


x = calc(10, 20)  # 位置实参
y = calc(b=10, a=20)  # 关键字实参
print(x, y)

def fun(arg1, arg2):
    print('arg1:', arg1)
    print('arg2:', arg2)
    arg1 = 100
    arg2.append(40)
    print('arg1:', arg1)
    print('arg2:', arg2)


n1 = 11
n2 = [10, 20, 30]
print('n1:', n1)
print('n2:', n2)
fun(n1, n2)
print('n1:', n1)  # 在函数调用过程中,进行参数的传递,如果是不可变对象,在函数体的修改不会影响实参的值 arg1的修改不影响n1
print('n2:', n2)  # 如果是可变对象,在函数体内得得修改会影响到实参的值 arg2的修改影响n2

'''
函数的返回值
1.如果函数没有返回值(函数执行完毕之后不需要要给调用处提供数据),return可以省略不写
2.函数返回值如果是1个,直接返回原类型的数据
3.函数的返回值如果是多个,返回结果为元组
'''


def fun(num):
    odd = []  # 存奇数
    even = []  # 存偶数
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even  # 函数返回多个值


print(fun([10, 15, 20, 25, 30, 35, 40, 45, 50]))  # 函数返回多个值时,结果为元组


def fun(a, b=10):  # 函数定义时,给形参设置默认值
    print(a, b)


fun(100)  # 设置默认值的形参可以不传参
fun(200, 300)


def fun(*a):  # 定义函数时,使用*定义个数可变的位置参数,结果为一个元组
    print(a)


fun(10)
fun(10, 20, 30, 40)


def fun(**x):  # 定义函数时,使用**定义个数可变的关键字参数,结果为一个字典
    print(x)


fun(a=10)
fun(a=10, b=20, c=30, d=40)


# def fun(*a,*b)和def fun(**a,**b)报错,个数可变的未知参数和关键字参数只能有一个
# 在一个函数定义的过程中,既有个数可变的关键字形参,又有个数可变的位置形参,要求把位置形参放前面def fun(*a,**b)

def fun(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


fun(1, 2, 3)  # 位置实参
lst = [10, 20, 30]
fun(*lst)  # 不加*会抛错,会将lst视为一个值传参给a,b和c没有传参
fun(a=100, b=200, c=300)  # 关键字实参
dict = {'a': 1000, 'b': 2000, 'c': 3000}
fun(**dict)  # 不加**会抛错,会将dict视为一个值传参给a,b和c没有传参


def fun(a, *, b, c):  # *指定*之后的参数必须使用关键字实参进行传参，*之前的参数随意
    print('a=', a)
    print('b=', b)
    print('c=', c)


fun(a=1, b=2, c=3)
fun(1, b=2, c=3)


# 函数定义时形参的顺序问题
def fun1(a, b, *, c, d, **arg1):
    pass


def fun2(*args2, **args1):
    pass


def fun3(a, b=10, *args2, **args1):
    pass


# 变量的作用域
def fun(a, b):
    c = a + b  # c是函数体内的变量，为局部参数，a和b是形参，作用范围也是函数内部，相当于局部变量
    print(c)


name = '狗富贵'  # name作用范围为函数内部和外部，是全局变量
print(name)


def fun0():
    print(name)


fun0()


def fun1():
    global age  # 函数内部定义的局部变量，使用global声明之后就变成全局变量
    age = 20
    print(age)


fun1()
print(age)  # 函数外部输出函数内部定义的age


# 递归函数(函数体内调用了该函数本身)
# 使用递归函数计算阶乘n!
def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)


print(fac(6))


# 递归函数计算斐波那契数列(1,1,2,3,5,8,13...后面一个数是前两项之和)第n项
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(7))
# 输出这个数量前七位数字
for i in range(1, 8):
    print(fib(i))
