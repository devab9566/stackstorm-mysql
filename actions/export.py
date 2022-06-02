import MYSQLdb
import mysql.connector
import pandas as pd



mydb = mysql.connector.connect(
        host="localhost",
        port=1234,
        user="root",
        passwd="1234",
        db="db",

query= ('SELECT * FROM db')

mycursor=mydb.cursor
mydb = mycursor.fetchall()
df = pd.DataFrame(mydb)
df_csv = df.to_csv("G:\sample.csv" )
