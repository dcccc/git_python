#coding=utf-8
import MySQLdb
try:
	conn=mysql.connector.connect(user='fangliwen',passwd='prime1973',database='test',use_unicode=True)
	cur=conn.cursor()
except Exception, e:
	raise
else:
	pass
finally:
	pass


cur.execute('create database if not exists python')
cur.execute('create table if not exists test(id int,info varchar(20))')
value=[1,'hi rollen']
cur.execute('insert into python values(%s,%s)',value)
print cur.execute('select * from test')