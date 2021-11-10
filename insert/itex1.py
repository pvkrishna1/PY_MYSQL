
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root123",
    database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name,address) VALUES (%s,%s)"
val = ("John","Highway1")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount,"record inserted.")