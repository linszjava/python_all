# 操作数据库 Mysql
import pymysql
db = pymysql.connect(host='localhost',user='root',password='linsz99@',database='python_test',charset='utf8')
cur = db.cursor()
cur.execute('select * from t_user')
data = cur.fetchall() # 获取所有数据
print(data)
cur.close()

