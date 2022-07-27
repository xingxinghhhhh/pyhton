# import pymysql

# # 创建连接
# try:
#     conn = pymysql.connect(host="localhost",
#     port=3306,user="root",
#     password="root",
#     database="books")
#     print(conn)

# 获取游标
# cursor = conn.cursor()

# 执行sql
# 查询
# sql = "select * from t_book;"
# cursor.execute(sql)

# 增加
# sql1 = "insert into t_book(id,title,pub_date) values(4,'西游记','1986-01-01');"
# cursor.execute(sql1)

# 更新
# sql2 = "update t_book set title='东游记' where title = '西游记';"
# cursor.execute(sql2)

# 删除
# sql3 = "delete from t_book where title = '东游记';"
# cursor.execute(sql3)

# 获取查询结果的总记录数
# print(cursor.rowcount)

# 获取查询结果的第一条数据
# print(cursor.fetchone())

# 获取全部的查询结果
# print(cursor.fetchall())

# 关闭游标
# cursor.close()

# 关闭连接
# conn.close()



# import pymysql
# conn = None 
# cursor = None
# # 创建连接
# try:
#     conn = pymysql.connect(host="localhost",
#     port=3306,user="root",
#     password="root",
#     database="books",
#     autocommit=False)
#     print(conn)


#     cursor= conn.cursor()
#     sql = "insert into t_book(id,title,pub_date) values(4,'西游记','1986-01-01');"
#     cursor.execute(sql)
#     print(cursor.rowcount)
#     print("-" * 200)

#     raise Exception("出错了")


#     sql = "insert into t_hero(name,gender,book_id) values('孙悟空',1,4)"
#     cursor.execute(sql)
#     print(cursor.rowcount)

#     conn.commit()

# except Exception as e:
#     conn.rollback()
#     print(e)

# finally:
#     if cursor:
#         cursor.close()
#     if conn:
#         conn.close()