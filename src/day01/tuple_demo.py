# 元组的应用介绍
# 元组在创建之后就是不可变的，元组是不可变的序列
if __name__ == '__main__':
    t = (1, 2, 3, 4)
    print(len(t))

    print(t + (6, 7))

    print(t.index(2))
    # 统计2出现的次数
    print(t.count(2))
    print(t[0])

    # 下面会报错
    # t[2] = 1
