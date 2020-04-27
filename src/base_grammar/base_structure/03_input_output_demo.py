def test_str_format():
    print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
    print('{0} 和 {1}'.format('Google', 'Runoob'))
    print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
    # 占位符和关键字参数可以任意组合
    print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))


def test_input():
    str = input("请输入：")
    print("你输入的内容是: ", str)


# 读写文件

def test_write_to_file():
    # 打开一个文件. 以写的模式打开文件
    f = open("foo.txt", "w")

    num = f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
    print('写入文件的字符个数', num)
    # 关闭打开的文件
    f.close()

def test_read_from_file():
    # 打开一个文件
    f = open("foo.txt", "r")

    str = f.read()
    print(str)

    # 关闭打开的文件
    f.close()

# f.readline() 会从文件中读取单独的一行。换行符为 '\n'。
# f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
def test_read_from_file01():
    # 打开一个文件
    f = open("/tmp/foo.txt", "r")

    str = f.readline()
    print(str)

    # 关闭打开的文件
    f.close()
# 迭代一个文件
def test_read_from_file02():
    # 打开一个文件
    f = open("foo.txt", "r")

    for line in f:
        print(line, end='')

    # 关闭打开的文件
    f.close()

if __name__ == '__main__':
    # test_str_format()
    # test_input()
    # test_write_to_file()
    # test_read_from_file()
    # test_read_from_file01()
    test_read_from_file02()