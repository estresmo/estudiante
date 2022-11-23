import pymysql
from config import DevelomentConfigRemote as DevelomentConfig


def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host=DevelomentConfig.MYSQL_HOST,
        user=DevelomentConfig.MYSQL_USER,
        password=DevelomentConfig.MYSQL_PASSWORD,
        db=DevelomentConfig.MYSQL_DB,
    )

    cur = conn.cursor()
    cur.execute("select @@version")
    output = cur.fetchall()

    print(output)

    # print first row of all tables
    cur.execute("show tables")
    tables = cur.fetchall()
    for table in tables:
        cur.execute("select * from {}".format(table[0]))
        print('Table: {}'.format(table[0]))
        print(cur.fetchone())

    conn.close()


if __name__ == "__main__":
    mysqlconnect()
