
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root123",
    database = "mydatabase",
)

mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address= 'Park Len 38'"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)