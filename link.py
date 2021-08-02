import mysql.connector

my_db = mysql.connector.connect(user="abdul-malik", password="@8-2fermENt2020", host="127.0.0.1", database="LC_Online", auth_plugin="mysql_native_password")
my_cursor = my_db.cursor()
xy = my_cursor.execute("select * from Register")

for i in my_cursor:
    print(i)

