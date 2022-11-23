import pymysql
from config import DevelomentConfigLocal as DevelomentConfig


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
    # cur.execute('CREATE DATABASE IF NOT EXISTS flask_db_remote')
    # conn.commit()
    # cur.execute('CREATE TABLE IF NOT EXISTS users (id int(11) NOT NULL AUTO_INCREMENT, username varchar(50) NOT NULL, password varchar(255) NOT NULL, email varchar(50) NOT NULL, fullname varchar(50) NOT NULL, role varchar(50) NOT NULL, PRIMARY KEY (id), UNIQUE KEY username (username), UNIQUE KEY email (email)) ENGINE=InnoDB DEFAULT CHARSET=utf8;')
    # conn.commit()
    # cur.execute('CREATE TABLE IF NOT EXISTS sessions (id int(11) NOT NULL AUTO_INCREMENT, user_id int(11) NOT NULL, token varchar(255) NOT NULL, created_at datetime NOT NULL, expired_at datetime NOT NULL, status varchar(50) NOT NULL, PRIMARY KEY (id), KEY user_id (user_id), CONSTRAINT sessions_ibfk_1 FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE ON UPDATE CASCADE) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=1;')
    # conn.commit()
    # cur.execute("INSERT INTO users (username, password, email, fullname, role) VALUES ('admin', 'pbkdf2:sha256:260000$l999FTgAfnN4E5Wx$485350051a7136b6cd38408d17f0fd0a0c5ebeba199a6d2a384cc0e31d7e17e9', 'digisoftworldcontacto@gmail.com', 'Administrador', 'dgsoft');")
    # conn.commit()
    # cur.execute('CREATE TABLE IF NOT EXISTS categories (id int(11) NOT NULL AUTO_INCREMENT, name varchar(50) NOT NULL, description varchar(255) NOT NULL, PRIMARY KEY (id)) ENGINE=InnoDB DEFAULT CHARSET=utf8;')
    # conn.commit()
    # cur.execute('CREATE TABLE IF NOT EXISTS products (id int(11) NOT NULL AUTO_INCREMENT, name varchar(50) NOT NULL, description varchar(255) NOT NULL, price int(11) NOT NULL, stock int(11) NOT NULL, category_id int(11) NOT NULL, image varchar(255) NOT NULL, PRIMARY KEY (id), KEY category_id (category_id), CONSTRAINT products_ibfk_1 FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE CASCADE ON UPDATE CASCADE) ENGINE=InnoDB DEFAULT CHARSET=utf8;')
    # conn.commit()
    # cur.execute('CREATE TABLE IF NOT EXISTS orders (id int(11) NOT NULL AUTO_INCREMENT, user_id int(11) NOT NULL, total int(11) NOT NULL, status varchar(50) NOT NULL, created_at datetime NOT NULL, PRIMARY KEY (id), KEY user_id (user_id), CONSTRAINT orders_ibfk_1 FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE ON UPDATE CASCADE) ENGINE=InnoDB DEFAULT CHARSET=utf8;')
    # conn.commit()
    # cur.execute('CREATE TABLE IF NOT EXISTS orders_detail (id int(11) NOT NULL AUTO_INCREMENT, order_id int(11) NOT NULL, product_id int(11) NOT NULL, quantity int(11) NOT NULL, price int(11) NOT NULL, PRIMARY KEY (id), KEY order_id (order_id), KEY product_id (product_id), CONSTRAINT orders_detail_ibfk_1 FOREIGN KEY (order_id) REFERENCES orders (id) ON DELETE CASCADE ON UPDATE CASCADE, CONSTRAINT orders_detail_ibfk_2 FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE ON UPDATE CASCADE) ENGINE=InnoDB DEFAULT CHARSET=utf8;')
    # conn.commit()
    # cur.execute('CREATE PROCEDURE IF NOT EXISTS change_status_expired_session() BEGIN SET @current_date = NOW(); SELECT *  FROM sessions  WHERE status = "logged" AND expired_at < @current_date; UPDATE sessions SET status = "expired" WHERE status = "logged" AND expired_at < @current_date; COMMIT; END')
    # conn.commit()
    # print tables available in the database
    tables = []
    cur.execute("SHOW TABLES")
    for table in cur:
        tables.append(table[0])
    print(tables)

    # print rows in the tables
    for table in tables:
        print(f"Table: {table}")
        cur.execute(f"SELECT * FROM {table}")
        for row in cur:
            print(row)
            



    # To close the connection
    conn.close()




# Driver Code
if __name__ == "__main__":
    mysqlconnect()
