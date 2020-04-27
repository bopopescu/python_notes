from connect_jdbc import mysql_connect

mydb = mysql_connect.get_mysql_connect()
mycursor = mydb.cursor()


def insert_one():
    # 如果有 int类型值，那么仍然是 %s(通配符)，然后传入int类型即可
    sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
    # 注意：如果val是string类型，那么值必须使用 双引号。
    val = ("RUNOOB", "https://www.runoob.com")
    mycursor.execute(sql, val)
    mydb.commit()  # 数据表内容有更新，必须使用到该语句
    print(mycursor.rowcount, "记录插入成功。")


def insert_batch():
    sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
    val = [
        ('Google', 'https://www.google.com'),
        ('Github', 'https://www.github.com'),
        ('Taobao', 'https://www.taobao.com'),
        ('stackoverflow', 'https://www.stackoverflow.com/')
    ]
    mycursor.executemany(sql, val)
    mydb.commit()  # 数据表内容有更新，必须使用到该语句
    print(mycursor.rowcount, "记录插入成功。")


# 获取插入数据的最后一个id
def get_insert_id():
    sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
    val = ("Zhihu", "https://www.zhihu.com")
    mycursor.execute(sql, val)

    mydb.commit()

    print("1 条记录已插入, ID:", mycursor.lastrowid)


def select_test01():
    mycursor.execute("SELECT * FROM sites")

    myresult = mycursor.fetchall()  # fetchall() 获取所有记录
    # fetchone获取一条
    for x in myresult:
        print(x)


def select_test02():
    sql = "SELECT * FROM sites WHERE name = %s"
    # 需要加一个 ,
    na = ("RUNOOB",)
    mycursor.execute(sql, na)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


def update():
    sql = "UPDATE sites SET name = %s WHERE name = %s"
    val = ("菜鸟教程", "RUNOOB")

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, " 条记录被修改")


if __name__ == '__main__':
    # insert_one()
    # insert_batch()
    # get_insert_id()
    # select_test02()
    update()
