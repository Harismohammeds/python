import sqlite3
connection=sqlite3.connect("Haris.db")
cursor=connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR(20)NOT NULL,
               age INTEGER,
               gender VARCHAR(10),
               email VARCHAR(50)UNIQUE,
               phone_no VARCHAR(15)UNIQUE,
               address TEXT)
               """)
# cursor.execute("""
# INSERT INTO student(name,age,gender,email,phone_no,address)
#             VALUES("Rahul",21,"male","rahul@gmail.com","4353636363","bgg street")
# """)
# cursor.execute("""
# UPDATE student
#                SET email="ardra@gmail.com",name="Ardra" WHERE id=1
#                """)
cursor.execute("""
DELETE FROM student WHERE name="Akash"
               """)
cursor.execute("SELECT * from student")
rows=cursor.fetchall()
for row in rows:
    print(row)



connection.commit()
connection.close()