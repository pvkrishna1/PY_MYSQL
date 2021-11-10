
import mysql.connector

db  = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root123"
)

res = db.cursor()

res.execute("CREATE DATABASE mydatabase")
