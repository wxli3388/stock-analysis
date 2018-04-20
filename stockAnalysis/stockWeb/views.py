from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    import MySQLdb as mysql

    conn = mysql.connect(host='localhost',port=3306,user='root',passwd='0921346555',db='stock',charset='utf8')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM stockdata LIMIT 10')
    results = cursor.fetchall()

    return HttpResponse(results)