
import mysql.connector

mydb  = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root123",
    database = "mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE table1 ( name VARCHAR(255), address VARCHAR(255))")

#mycursor.execute("SHOW TABLES")
#for x in mycursor:
 #   print(x)