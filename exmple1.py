
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "krishna",
    password = "krishna",
    port = 3306
)

print(mydb)