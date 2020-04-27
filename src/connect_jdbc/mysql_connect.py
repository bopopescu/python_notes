import mysql.connector


def get_mysql_connect():
    mydb = mysql.connector.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        passwd="123456",  # 数据库密码
        database="demo"
    )
    print('连接已建立database = {} connect = {}'.format('demo', mydb))
    return mydb


if __name__ == '__main__':
    print(get_mysql_connect)
