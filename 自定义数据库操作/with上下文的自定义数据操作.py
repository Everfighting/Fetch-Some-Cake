class DB:
    def __init__(self, host, user, password, db):
        self.host=host
        self.user=user
        self.password = password
        self.db = db    
        self.conn()
        
    def conn(self):
        self.connect = pymysql.Connect(host=self.host,
                                       port=3306,
                                       user=self.user,
                                       password=self.password,
                                       db=self.db,
                                       charset='utf8')
        
    def __enter__(self):
        return self.connect.cursor()
        
    
    def __exit__(self, exc, value, traceback):
    '''
    调用上下文管理器对象的_exit__()方法，并将异常类型、值及traceback信息作为参数传递给__exit__()方法。
    如果_exit__()返回值为false，则异常会被重新抛出；
         如果其返回值为true，异常被挂起，程序继续执行。

    
    '''
        print('------__exit__-------', exc, value)
        # exc -> pymysql.err.ProgrammingError
        # 在此方法中，是否可以处理掉exc异常对象？？？
        # traceback 的对象属性或方法有哪些 ？
        if exc:
            self.connect.rollback()
        else:
            self.connect.commit()
            self.connect.close()
			
"""
1.实例化数据库连接对象
2.利用python上下文要经历的__enter__(),
	__exit__()来获得数据库连接的cursor对象,执行原生sql查询
	和关闭cursor对象,和connect对象
"""
'''
·__enter__()：进入运行时的上下文，返回运行时上下文相关的对象，with语句中会将这个返回值绑定到目标对象。
              如上面的例子中会将文件对象本身返回并绑定到目标f。
·__exit__(exception_type,exception_value,traceback)：退出运行时的上下文，定义在块执行（或终止）之后上下文管理器应该做什么。
              它可以处理异常、清理现场或者处理with块中语句执行完成之后需要处理的动作。

'''

with DB('127.0.0.1', 'root', 'root', 'stu') as cursor:
	cursor.execute('select * from A2')
	for row in cursor.fetchall():
		print(row)

