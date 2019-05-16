# home-made_models.py

实现：自定义数据库的CRUD链式操作

#### init(tablename)

- conn:连接对象        __connect():return 连接对象
- cursor：游标对象
- tablename:表名
- cachefield:缓存的某标的所有字段
- options：参数选项
  - fields:字段列表,  **默认:*  **
  - table:表名,  **默认:tablename**
  - where:where条件
  - groupby:分组条件
  - having:分组的过滤条件
  - orderby:排序条件
  - limit:限制结果集
  - value(后面需要创建)
- __cache_field()用来缓存数据库中table(s)的field
  - 缓存该表下的所有字段---->options中的fields
  - cachefield=content(包含所有字段)
  - 返回值:return None,  exit()

#### del

- 关闭游标对象
- 关闭连接对象

#### field(fields)

- 更改options中的fields字段
- return self

#### table(tablename)

- 更改options中的table表名
- 重新加载下当前table下的缓存txt文件,__cache_field()
- return self

#### having(orderby,limit,where(or))-------conditions

- 判断options中是否存在having字段,order by 字段,limit字段,
- return self

#### select

- ```mysql
  sql = "SELECT {fields} FROM {table} {where} {groupby} {having} {orderby} {limit}"
  
  
  ```

- 加入self.sql
- return query(sql)

#### __init_options

- 直接初始化options中的参数
  - fields:cachefield
  - table:tablename

#### query(sql)

- 进行原生sql查询
  - 现进行参数初始化
  - 调用cursor.execute()执行sql语句
  - return cursor.fetchall();    return None

#### __add_quote(data)

- 给字符串添加单引号,有啥用,给数据库的相关操作时,需要在字符串两边加入单引号
- ![img](file:///C:\Users\Actions\AppData\Roaming\Tencent\Users\2602594534\TIM\WinTemp\RichOle\31X230V9AXJ(9BX1E2@YH)9.png)

#### insert(data:dict)

- ```mysql
  sql = "INSERT INTO {table}({fields}) values({value})"
  
  ```

- ```mysql
  sql语句的成品: insert into user(sno,sname) values('9393','kdkd')
  ```

- ```
  data中的数据{'sno':1,'sname':'jimmy'}
  ```

- 为data两边增加单引号,获取data中的fields 和values
- 修改options中的fields和value
- 封装最后的sql语句
- 返回execute(sql)

#### execute(sql)

- 进行原生sql查询
- conn.commit()和conn.rollback()
- execute(sql) 处理完后返回  影响行数
- 返回True or False

#### delete()

- 进行原生sql 删除操作

- ```
  sql = "DELETE FROM {table} {where}"
  ```

- return execute(sql)

#### update(data)

- 进行原生sql 删除操作

- ```mysql
  sql = "UPDATE {table} SET {value} {where}".format(**self.options)
  s1 = ','.join([key + '=' + str(value) for key, value in data.items()])
          self.options['value'] = s1
  ```

- return execute(sql)