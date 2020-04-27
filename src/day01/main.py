import math

''' 这是多行注释，3个单引号 '''

if __name__ == '__main__':
    # 创建list的方法
    l = []
    for i in [1, 2, 3]:
        l.append(math.pow(i, 2))
    print(l)

    l1 = [math.pow(i, 2) for i in [1, 2, 3]]
    print(l1)

    # 可以利用type判断变量的类型
    print(type(l1))
    # 三元表达式
    v = 1 > 2 if print(3) else 4
    print(v)

