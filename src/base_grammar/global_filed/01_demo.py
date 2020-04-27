total = 0  # 这是一个全局变量
num = 0


# 更多参考：https://www.runoob.com/python3/python3-namespace-scope.html
# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是重新定义的局部变量.
    print("函数内是局部变量 : ", total)
    return total


# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)


#
if __name__ == '__main__':
    # 调用sum函数
    sum(10, 20)
    print("函数外是全局变量 : ", total)

    fun1()
    print(num)
