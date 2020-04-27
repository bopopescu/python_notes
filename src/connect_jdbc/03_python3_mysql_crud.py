# 打开数据库连接
import pymysql

'''
利用python3的mysql连接模块

'''

db = pymysql.connect("localhost", "root", "123456", "demo")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


def insert_one():
    # SQL 插入语句
    sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
           LAST_NAME, AGE, SEX, INCOME) \
           VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
          ('Mac', 'Mohan', 20, 'M', 2000)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    db.close()


def select_test01():
    # SQL 查询语句
    sql = "SELECT * FROM EMPLOYEE WHERE INCOME > %s"
    val = (1000)
    try:
        # 执行SQL语句
        cursor.execute(sql, val)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # 打印结果
            print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" %
                  (fname, lname, age, sex, income))
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()


def update():
    # SQL 更新语句
    sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    # insert_one()
    # select_test01()
    update()
