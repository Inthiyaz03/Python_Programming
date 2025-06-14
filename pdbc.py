import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="root"
                               ,database = "employee")

cursor = mydb.cursor()
cursor.execute("select * from employee")
res = cursor.fetchone()

for i in res:
    print(i,end="  ")