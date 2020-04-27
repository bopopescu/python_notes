import math
import random

# 介绍数字与字符串的基本操作
if __name__ == '__main__':
    # 输出
    print('aa')
    # 运算相关
    i = 100 + 200
    print(i)
    pi = math.pi
    print(pi)
    print(math.fabs(-100))

    print(random.random())
    print(random.choice([0,1,2,3,4]))

    # 字符串相关操作
    s = 'wangxi'
    print(s[len(s) - 1])
    print(s[0])
    # 获取最后一个元素
    print(s[-1])
    # 切片遵从左闭右开
    print(s[0:3])
    print(s[0:])
    print(s[:-1])

    print(s.find('xi'))
    # 字符串的不可变性，只是创建了一个新的字符串输出
    print(s.replace('wa', 'WA'))
    # 分隔符分割字符串
    line = '  123,345,asd  '
    print(line.split(','))
    # 转换大小写
    print(s.upper())
    #判断是否数字和字母
    print(s.isalpha())
    print(s.isdigit())
    # 去掉两边空格
    print(line.strip())
    # 字符串占位符
    a = '%s,bb,%s' % (1, 2)
    b = '{0},bb,{1}'.format(100, 200)
    print(a)
    print(b)