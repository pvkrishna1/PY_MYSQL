
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root123",
    database = "mydatabase"
)

mycursor = mydb.cursor()
sql = "DROP TABLE customers"

mycursor.execute(sql)
