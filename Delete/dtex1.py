
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root123",
    database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Main Road 989'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount,"record(s) deleted")