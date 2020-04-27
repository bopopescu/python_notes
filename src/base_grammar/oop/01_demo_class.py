class MyClass:
    """一个简单的类实例"""
    i = 12345

    def f(self):
        return 'hello world'

    # 构造函数。在执行x = MyClass() 就会调用此方法
    def __init__(self, s):
        self.data = []
        self.s = s

    # self代表类的实例(不是python关键字，可以替换成任务单词)，而非类.
    # 在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self,
    # 且为第一个参数，self 代表的是类的实例
    # 注意：对象函数与main函数的缩进
    def print_func(self):
        print(self)
        print(self.__class__)
        print(self.data)
        print(self.s)


if __name__ == '__main__':
    # 实例化类
    x = MyClass('sss')

    # 访问类的属性和方法
    print("MyClass 类的属性 i 为：", x.i)
    print("MyClass 类的方法 f 输出为：", x.f())
    x.print_func()
