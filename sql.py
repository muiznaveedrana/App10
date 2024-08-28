import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

cursor.execute("SELECT date FROM events WHERE Band = 'Lions'")
rows = cursor.fetchall()
print(rows)

cursor.execute("SELECT * FROM events WHERE City = 'Lion City'")
rows = cursor.fetchall()
print(rows)

new_rows = [('Cats', 'Cat City', '2022.9.20'), ('Monkeys', 'Monkey City', '2026.10.24')]
cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)

connection.commit()

cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)