# 测试私有变量的作用域
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


# 测试私有方法作用域
class Site:
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    def __foo(self):  # 私有方法
        print('这是私有方法')

    def foo(self):  # 公共方法
        print('这是公共方法')
        self.__foo()


# 私有字段或者方法在类外是无法访问的
if __name__ == '__main__':
    counter = JustCounter()
    counter.count()
    counter.count()
    print(counter.publicCount)
    # print(counter.__secretCount)  # 报错，实例不能访问私有变量

    x = Site('菜鸟教程', 'www.runoob.com')
    x.who()  # 正常输出
    x.foo()  # 正常输出
    # x.__foo()  # 报错
