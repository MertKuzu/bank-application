import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "*",   # write here your local server password
    database = "bankappdb"
)