import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdb"
)

cursor=mydb.cursor()

sql = "INSERT INTO students (name, age)  VALUES (%s, %s)"
val = ("JOHN", "22")

cursor.execute(sql,val)

mydb.commit()

print(cursor.rowcount, "Record Inserted.")