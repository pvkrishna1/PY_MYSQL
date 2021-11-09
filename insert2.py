import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
val = [
    ('peter', '24'),
    ('amy', '10'),
    ('prasad', '22'),
    ('michel', '30'),
    ('me', '25')
]

mycursor.executemany(sql,val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

