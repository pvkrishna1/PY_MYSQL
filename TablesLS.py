import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdb"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)