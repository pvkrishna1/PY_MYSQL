import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students ORDER BY name")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
    