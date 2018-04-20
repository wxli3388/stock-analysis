import MySQLdb as mysql

conn = mysql.connect(host='localhost',port=3306,user='root',passwd='0921346555',db='stock',charset='utf8')
cursor = conn.cursor()
cursor.execute('SELECT * FROM stockdata LIMIT 10')
results = cursor.fetchall()

for row in results:
    print(row)
