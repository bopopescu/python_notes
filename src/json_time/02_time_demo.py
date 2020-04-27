import time


def func01():
    ticks = time.time()
    print("当前时间戳为:", ticks)

    localtime = time.localtime(time.time())
    print("本地时间为 :", localtime)

    localtime = time.asctime(time.localtime(time.time()))
    print("本地时间为 :", localtime)


def time_format():
    # 格式化成2020-04-27 21:32:31形式
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(time.strftime("%Y-%m-%d", time.localtime()))

    # 格式化成Sat Mar 28 22:24:24 2016形式
    print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

    # 将格式字符串转换为时间戳
    a = "Sat Mar 28 22:24:24 2016"
    print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))


if __name__ == '__main__':
    # func01()
    time_format()
