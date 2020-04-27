import json


def dict_to_str():
    # Python 字典类型转换为 JSON 对象
    data = {
        'no': 1,
        'name': 'Runoob',
        'url': 'http://www.runoob.com'
    }

    json_str = json.dumps(data)
    print("Python 原始数据：", repr(data))
    print("JSON 对象：", json_str)
    print(type(json_str))


def json_str_to_dict():
    # 将 JSON 对象转换为 Python 字典
    json_str = '{"no": 1, "name": "Runoob", "url": "http://www.runoob.com"}'
    data2 = json.loads(json_str)
    print(type(data2))  # 返回的dict
    print("data2['name']: ", data2['name'])
    print("data2['url']: ", data2['url'])


# 从文件读取json
def process_json_from_file():
    # 写入 JSON 数据
    data_str = ''
    with open('data.json', 'w') as f:
        json.dump(data_str, f)

    # 读取数据
    with open('data.json', 'r') as f:
        data = json.load(f)


if __name__ == '__main__':
    # dict_to_str()
    json_str_to_dict()
