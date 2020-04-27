def test01():
    while True:
        try:
            x = int(input("请输入一个数字: "))
            break
        except ValueError:
            print("您输入的不是数字，请再次尝试输入！")
        finally:
            print('我是finally代码块')

# 抛出异常 利用raise关键字抛出
def test02():
    x = 10
    if x > 5:
        raise Exception('x 不能大于 5。x 的值为: {}'.format(x))

if __name__ == '__main__':
    # test01()
    test02()