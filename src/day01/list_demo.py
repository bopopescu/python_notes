# 介绍列表, 列表、dict是可改变的。与dict一致，都是引用类型
if __name__ == '__main__':
    # 列表常见操作
    l = [1, 'abc', 1.2]
    print(l)
    print(len(l))
    print(l[0])
    print(l[:2])
    print(l + [4, 5, 6])
    # 扩大列表，使用append方法
    print(l.append('wangxio'))
    # 删除索引为2的元素
    print(l.pop(2))
    l.__delitem__(0)
    print('l = ', l)
    l.insert(0, 'aa')
    # 按值移除元素
    l.remove('aa')
    print(l)

    # 列表的排序
    m = [5, 4, 3, 2]
    m.sort()
    print(m)
    m.reverse()
    print(m)
    print(2 in m)
    for i in m:
        print(i)
    m.extend([1,2,3,4])
    print('m = ', m)

    # 多维数组 及 列表解析表达式
    n = [[1, 2, 3], [3, 4, 5]]
    print(n[0][0])
    # 获取某列所有值. 把每一行的第一列取出来
    n1 = [row[1] for row in n]
    print(n1)
    n2 = [row[1] + 100 for row in n]
    n3 = [row[1] for row in n if row[1] > 2]  # 过滤
    print(n2)
    print(n3)
    doubles = [c * 2 for c in 'wa']
    print(doubles)
    # 列表每一行相加
    n4 = [sum(row) for row in n]
    print(n4)
    # 迭代
    print(next(n4.__iter__()))
    # 把每一行的和封装成list
    n5 = list(map(sum, n))
    print(n5)
    # 创建set. 注意：python的set是{1,2,3}，列表是[1,2,3]
    n6 = {sum(row) for row in n}
    print(n6)
    # 创建dict
    n7 = {i: sum(n[i]) for i in range(2)}
    print(n7)
