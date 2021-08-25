import  sqlite3

conn = sqlite3.connect("storage.db")
cur = conn.cursor()
conn.execute("PRAGMA FOREIGN_KEYS=1")

conn.execute("""CREATE TABLE Ingredients (
    supplier_id TEXT NOT NULL,
    supplier_name TEXT NOT NULL,
    supplier_contact TEXT NOT NULL,
    supplier_address TEXT NOT NULL,
    unit TEXT NOT NULL,
    unit_quantity INTEGER NOT NULL,
    quantity TEXT NOT NULL,
    cup_quantity INTEGER NOT NULL,
    price TEXT NOT NULL,
    supply_datetime DATETIME DEFAULT CURRENT_TIMESTAMP
)""")

conn.close()