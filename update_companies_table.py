import sqlite3

conn = sqlite3.connect("company_data.db")
cursor = conn.cursor()

columns_to_add = [
    ("heading", "TEXT"),
    ("description", "TEXT"),
    ("contact_person", "TEXT"),
    ("phone", "TEXT"),
    ("email", "TEXT"),
    ("address", "TEXT")
]

for col_name, col_type in columns_to_add:
    try:
        cursor.execute(f"ALTER TABLE companies ADD COLUMN {col_name} {col_type}")
        print(f"Added column: {col_name}")
    except sqlite3.OperationalError:
        print(f"Column already exists: {col_name}")

conn.commit()
conn.close()
print("Companies table updated successfully.")
