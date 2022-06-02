import MySQLdb as dbapi
import sys
import csv

dbServer='localhost'
dbPass='supersecretpassword'
dbSchema='dbTest'
dbUser='root'

dbQuery='SELECT * FROM pbTest.Orders;'

db=dbapi.connect(host=dbServer,user=dbUser,passwd=dbPass)
cur=db.cursor()
cur.execute(dbQuery)
result=cur.fetchall()

c = csv.writer(open("temp.csv","wb"))
c.writerow(result)pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on 'localhost:8080' ([Errno 11001] getaddrinfo failed)")
