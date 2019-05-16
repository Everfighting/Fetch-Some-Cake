# 数据库操作类
import os
import time

import pymysql
# from .setting import  database
# for  i in database:
#     print(i)
# 报错
# ModuleNotFoundError: No module named '__main__.myconfig'; '__main__' is not a package




# 数据库相关配置
database = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123',
    'db': 'stu',
    'charset': 'utf8'

}


class Model:
    def __init__(self, tablename):
        self.conn = self.__connect()  # 连接数据库
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        self.tablename = tablename
        self.options = {
            'fields': '*',  # 字段列表
            'table': self.tablename,  # 表名
            'where': '',  # where条件
            'groupby': '',  # group by分组条件
            'having': '',  # having 分组过滤条件
            'orderby': '',  # order by排序条件
            'limit': ''  # limit 限制结果集
        }
        self.__cache_field()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    # 字段缓存
    # if 有缓存字段,直接写到content--->fields
    # if not,读取数据库中相应表的字段,一方面写到缓存文件中,一方面写到options下fields中
    def __cache_field(self):
        # 1.判断是否有表名，如果没有，不做字段缓存
        if not self.options['table']:
            return

        # 如果没有cache目录，则建立cache
        if not os.path.exists('./cache'):
            os.mkdir('./cache')

        # 如果有表名
        path = './cache/' + self.options['table'] + '.txt'
        content = ''  # 字段列表字符串
        if os.path.exists(path):
            with open(path, 'r') as fp:
                content = fp.read()
        else:
            # 文件不存在，查询表，取出字段列表，写入文件
            self.cursor.execute("desc " + self.options['table'])
            # data = self.query("desc " + self.options['table'])
            data = self.cursor.fetchall()
            if not data:  # 表中无任何数据
                exit()

            # 拼接字段列表
            for rec in data:
                content += rec['Field'] + ','
            content = content.rstrip(',')  # 去除最右边的所有连续逗号

            with open(path, 'w') as fp:  # 将缓存字段写入path对应的文件中
                fp.write(content)
        if self.options['fields'] == '*':  # 判断options中的fields的字段值
            self.options['fields'] = content

        self.cachefield = content  # 保存字段缓存
        print('读取缓存后cachefield:',content)


    # 连接数据库
    def __connect(self):
        conn = pymysql.connections.Connection(**database)
        return conn

    def field(self, fields):
        self.options['fields'] = fields
        print('field中的options下的field字段值:',self.options['fields'])
        return self

    def table(self, tablename):
        # print(tablename)
        self.options['table'] = tablename
        # 在此处调用了缓存字段函数,出错原因:当fields字段为*时,才给它能成 cachefield(全字段)
        # 其他情况,保持原本值
        self.__cache_field()
        return self

    def where(self, conditions):  # 当where 调用两次是走else条件
        # 判断options中where是否为空
        if not self.options['where']:  # 为空
            self.options['where'] = " WHERE " + conditions
        else:
            self.options['where'] += ' and ' + conditions
        return self

    def whereor(self, conditions):
        # 判断options中where是否为空
        if not self.options['where']:  # 为空
            self.options['where'] = " WHERE " + conditions
        else:
            self.options['where'] += ' OR ' + conditions
        return self

    # 分组
    def groupby(self, conditions):
        self.options['groupby'] = " GROUP BY " + conditions
        return self

    # having
    def having(self, conditions):
        if not self.options['having']:
            self.options['having'] = " HAVING " + conditions
        else:
            self.options['having'] += ' AND ' + conditions
        return self

    # 排序
    def orderby(self, conditions):
        self.options['orderby'] = " ORDER BY " + conditions
        return self

    # limit
    def limit(self, conditions):
        self.options['limit'] = " LIMIT " + conditions
        return self

    def select(self):
        sql = "SELECT {fields} FROM {table} {where} {groupby} {having} {orderby} {limit}"
        sql = sql.format(**self.options)  # 为啥会在options中又定义一个table呢?此处见端倪
        print("select中的options:",self.options)
        self.sql = sql  # 保存sql语句
        return self.query(sql)

    # 还原options条件
    def __init_options(self):
        self.options = {
            'fields': self.cachefield,  # 全部字段列表
            'table': self.tablename,  # 表名
            'where': '',  # where条件
            'groupby': '',  # group by分组条件
            'having': '',  # having 分组过滤条件
            'orderby': '',  # order by排序条件
            'limit': ''  # limit 限制结果集
        }

    # 可以进行原生的sql查询
    def query(self, sql):
        # self.__init_options()
        print('query中的options:',self.options)
        print('query中的sql:',sql)
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()  # 返回查询结果
        except Exception as e:
            print(e)
            return None  # 如果查询出错((1054, "Unknown column 'sn' in 'field list'"))，返回None

    # 给字符串添加单引号
    def __add_quote(self, data):
        for key in data:
            if isinstance(data[key], str):  # 只对每个键对应的值进行单引号处理
                data[key] = "'" + data[key] + "'"
        print('__add_quote()中的data:',data)

    # insert
    # data必须是字典
    def insert(self, data:dict):
        sql = "INSERT INTO {table}({fields}) values({value})"
        # sql 语句最后的成品: insert into user(sno,sname) values('9393','kdkd')
        # data中的数据{'sno':1,'sname':'jimmy'}

        # 1.把data中值为字符串的两边添加单引号
        self.__add_quote(data)

        # 2.获取字段列表和值列表
        fields = ''
        value = ''
        for key in data:
            fields += key + ','
            value += str(data[key]) + ','
        fields = fields.rstrip(',') # 去除最后的逗号
        value = value.rstrip(',')
        print('insert中的fields:',fields)
        print('insert中的value',value)
        # insert中的value '肥1', 180517, '女'
        # 没处理过的: insert中的value 肥1, 180517, 女 (报错)

        # 3.替换sql
        self.options['fields'] = fields
        self.options['value'] = value
        sql = sql.format(**self.options)  # 格式化sql语句
        print('insert中的sql:', sql)
        return self.execute(sql)

    def execute(self, sql):
        # self.__init_options()

        try:
            res = self.cursor.execute(sql)
            self.conn.commit()
            if res > 0:
                return True
            else:
                return '无此人 or 没有影响记录'
        except Exception as e:
            print(e)
            self.conn.rollback()
            return False

    # 删除记录
    def delete(self):
        sql = "DELETE FROM {table} {where}"
        sql = sql.format(**self.options)
        return self.execute(sql)

    # 修改
    # data必须是字典
    def update(self, data):
        self.__add_quote(data)

        s1 = ','.join([key + '=' + str(value) for key, value in data.items()])
        self.options['value'] = s1
        print(s1)

        sql = "UPDATE {table} SET {value} {where}".format(**self.options)
        print(sql)
        return self.execute(sql)


if __name__ == '__main__':
    model = Model('sc')  # 创建学生模型类

    # 出错原因:缓存文件和数据库中的字段不一致
    # 由student模型类变成course模型类,全文查询
    # res2=model.table('course').field('cn,sn').select()
    # if res2:
    #     print(res2)
    # else:
    #     print('数据库中无法找到相应记录')

    # 查看options中fields字段值
    # print(model.options['fields'])

    # 查看options配置
    # print(model.options)

    # print(model.conn,model.cursor) or exit()

    # 查询数据的某个用户
    # select * from user where uname='tom'
    # res1=model.table("student").field('sn,name,age').where('name="王菊"').select()
    # if res1:
    #     print(res1)
    # else:
    #     print('数据库无此用户')

    # print(model.query("select * from sc"))

    # print(model.sql)  # 必须在调用select()之后模型类才能有sql属性

    # 如果需要自定义field,那么cachefield(__init_options())不能使用

    # data = model.field("sex,count(sex)")\
    #     .table("student")\
    #     .groupby('sex')\
    #     .having("count(sex) > 1")\
    #     .select()
    # print(data)

    # data = model.field("sn,name")\
    #     .table("student")\
    #     .orderby('sn desc')\
    #     .limit('3')\
    #     .select()
    # print(data)
    # print(model.sql)

    # data = {'name': '肥1', 'sn': 180517, 'sex': '女'}
    # res4=model.table('student').insert(data)
    # print(res4)

    # 删除学号为:... 的学生
    # print(model.table('student').where("sn='180513'").delete())

    # 每次查询只能查一条数据,可能会交叉其中的数据
    from datetime import datetime
    res5=model.table('student')\
        .where("sn='180513'")\
        .update({
           # 因为是datetime.datetime类型,__add_quote()无法处理,so 我们在这里就需要转换
        'age':datetime(122,1,23).strftime('%Y-%m-%d %X'),

    })
    print(res5)


    # print(model.query("desc sc"))
