import mysql.connector

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
val = ("prathap", "27")

mydb.commit()

print("1 Record inserted, ID:", mycursor.lastrowid)