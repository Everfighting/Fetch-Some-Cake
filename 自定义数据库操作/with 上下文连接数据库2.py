import pymysql


config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123',
    'charset': 'utf8',
    'db': 'stu'
}

create_table_sql = """
create TABLE t_mv(id int PRIMARY KEY auto_increment, name VARCHAR(255), image_path VARCHAR(255));
"""

exists_table_sql = """
select table_name from information_schema.tables where TABLE_NAME = %s
"""

insert_sql = """
insert t_mv(name, image_path) values (%s, %s)
"""

class DB():
    def __init__(self):
        self.conn = pymysql.connect(**config)
    
        with self.conn as cursor:  
            # cursor ：<pymysql.cursors.Cursor object at 0x7f13b7f95128>
            cursor.execute(exists_table_sql, 't_mv')
            if len(cursor.fetchall()) == 0:
                cursor.execute(create_table_sql)

        print('---init db ok---')

    def add(self, item):
        with self.conn as cursor:
            cursor.execute(insert_sql, args=(item['star_name'], item['images']))

        self.conn.commit()
