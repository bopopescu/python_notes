import sys

# 测试if、循环、函数的写法与特性

def if_test():
    age = int(input("请输入你家狗狗的年龄: "))
    print("")
    if age <= 0:
        print("你是在逗我吧!")
    elif age == 1:
        print("相当于 14 岁的人。")
    elif age == 2:
        print("相当于 22 岁的人。")
    elif age > 2:
        human = 22 + (age - 2) * 5
        print("对应人类年龄: ", human)

    # 退出提示
    input("点击 enter 键退出")


def test_while():
    n = 100

    sum = 0
    counter = 1
    while counter <= n:
        sum = sum + counter
        counter += 1
    # while-else语法，进攻演示
    else:
        print('counter > n,counter = ', counter)
    print("1 到 %d 之和为: %d" % (n, sum))


# 测试for循环
def test_for():
    sites = ["Baidu", "Google", "Runoob", "Taobao"]
    for site in sites:
        if site == "Runoob":
            print("菜鸟教程!")
            break
        print("循环数据 " + site)
    # 集合判空的方式
    else:
        print("没有循环数据!")
    print("完成循环!")


def test_range():
    for i in range(4):
        print(i)
    # 指定区间值
    for i in range(0, 3):
        print(i)
    # 指定步长
    for i in range(0, 3, 1):
        print(i)
    a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
    for i in range(len(a)):
        print(i)
    # 利用range创建一个列表
    l = list(range(3))
    print(l)


# 测试pass关键字. pass不作任何逻辑
def test_pass():
    for letter in 'Runoob':
        if letter == 'o':
            pass
            print('执行 pass 块')
        print('当前字母 :', letter)

    print("Good bye!")


def test_iterator():
    list = [1, 2, 3, 4]
    it = iter(list)  # 创建迭代器对象
    for x in it:
        print(x, end=" ")

    list = [1, 2, 3, 4]
    it = iter(list)  # 创建迭代器对象
    while True:
        try:
            print(next(it))
        except StopIteration:
            sys.exit()


# 函数调用时，参数可不规定顺序
def test_function01(name, age):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 函数的默认参数值
def test_func02(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 测试不定长参数. 以元组的方式传入
def test_func03(arg1, *var_tuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(var_tuple)


# 参数两个 * , 表示传入的会转化为一个dict
def test_func04(arg1, **var_dict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(var_dict)


sum = lambda arg1, arg2: arg1 + arg2


def test_lambda(a, b):
    print(sum(a, b))


if __name__ == '__main__':
    # if_test()
    # test_while()
    # test_for()
    # test_range()
    # test_iterator()
    # age=50, name="runoob" 这种写法表示以关键字传入参数
    # test_function01(age=50, name="runoob")
    # test_func02(name='wangxi')
    # test_func03(1, 2, 3, 4, 4)
    # test_func04(1, a=1, b=2)
    test_lambda(1, 2)
