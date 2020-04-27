def times(x, y):
    return x * y,x

def intersect(s1, s2):
    result = []
    for i in s1:
        if i in s2:
            result.append(i)
    return result

if __name__ == '__main__':
    print(times(2,3))
    print(type(times('a',3)))

    print(intersect('aaa','aaba'))