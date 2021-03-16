import mysql.connector

conection = mysql.connector.connect(
    port=3307, user="root", password="secret",
    autocommit=True, database="classicmodels "
)
cursor = conection.cursor()
cursor.execute("SELECT * FROM employees limit 10")
for i in cursor:
    print(i)
cursor.close()
conection.close()
