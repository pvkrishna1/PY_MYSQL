
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root123",
    database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name,address) VALUES (%s,%s)"
val = [
    ('peter','Lowstreet4'),
    ('amy','apple st 652'),
    ('Hannah','Vally 345'),
    ('sandy','ocean blvd 2'),
    ('Betty','green grass 1'),
    ('Richard','Sky st 331'),
    ('Susan','One way 98'),
    ('Vicky','Yellow garden 2'),
    ('Ben','Park Len 38'),
    ('William','Central st 954'),
    ('Chuck','Main Road 989'),
    ('Viola','Sideway 1633')
]

mycursor.executemany(sql,val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")