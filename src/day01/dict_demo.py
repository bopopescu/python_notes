# python的dict是hash，元素时无序的
if __name__ == '__main__':
    d = {'a': 1, 'b': 2}
    print(d)
    print(d['a'])
    d['a'] += 1
    print(d)

    # 创建空dict. dict的key是无序的
    d1 = {}
    d1['b'] = 100
    d1['a'] = 2
    d1['b'] = 200
    print('d1 = {0}'.format(d1))
    print('d1 = ', d1)
    # dict的嵌套
    d2 = {'a': {'c': 100}, 'b': [4, 5]}
    print(d2)
    print(d2['a']['c'])
    print(d2['b'][1])

    l = list(d1.keys())
    l.sort()
    for key in l:
        print(key, '=>', d1[key])

    # 字典获取默认值
    v = d1.get('aa', 0)
    print(v)
    # 获取值
    keys = list(d1.keys())
    print(keys)
    print(d1.values())
    print(d1.items())
    # 判断值是否存在于dict中
    print(2 in d1)
