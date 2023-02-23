import sqlite3

connection = sqlite3.connect("carRental.db")
cursor = connection.cursor()
try:
    cursor.execute("CREATE TABLE cars (id INTEGER, name TEXT, seats INTEGER)")
except:
    print("Open")
cursor.execute(f"INSERT INTO cars VALUES ('{1}', 'Suzuki Van', {2})")
cursor.execute(f"INSERT INTO cars VALUES ('{2}', 'Toyota Corolla', {4})")
cursor.execute(f"INSERT INTO cars VALUES ('{3}', 'Honda CRV', {4})")
cursor.execute(f"INSERT INTO cars VALUES ('{4}', 'Suzuki Swift', {4})")
cursor.execute(f"INSERT INTO cars VALUES ('{5}', 'Mitsibishi Airtrek', {4})")
cursor.execute(f"INSERT INTO cars VALUES ('{6}', 'Nissan DC Ute', {4})")
cursor.execute(f"INSERT INTO cars VALUES ('{7}', 'Toyota Previa', {7})")
cursor.execute(f"INSERT INTO cars VALUES ('{8}', 'Toyota Hi Ace', {12})")
cursor.execute(f"INSERT INTO cars VALUES ('{9}', 'Toyota Hi Ace', {12})")

rows = cursor.execute("SELECT id, name, seats FROM cars").fetchall()
print(rows)

