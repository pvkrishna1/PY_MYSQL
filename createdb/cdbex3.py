import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root123",
    database = "mydatabase"
)



# connecting to the mydatabase