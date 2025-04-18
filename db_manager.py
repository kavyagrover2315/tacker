import sqlite3

def create_table():
    conn = sqlite3.connect("clothes.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY,
            item_name TEXT,
            category TEXT,
            size TEXT,
            quantity INTEGER,
            price REAL,
            last_updated TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_item(item_name, category, size, quantity, price, last_updated):
    conn = sqlite3.connect("clothes.db")
    c = conn.cursor()
    c.execute("INSERT INTO inventory (item_name, category, size, quantity, price, last_updated) VALUES (?, ?, ?, ?, ?, ?)",
              (item_name, category, size, quantity, price, last_updated))
    conn.commit()
    conn.close()

def view_items():
    conn = sqlite3.connect("clothes.db")
    c = conn.cursor()
    c.execute("SELECT * FROM inventory")
    data = c.fetchall()
    conn.close()
    return data

def update_quantity(item_id, quantity, last_updated):
    conn = sqlite3.connect("clothes.db")
    c = conn.cursor()
    c.execute("UPDATE inventory SET quantity=?, last_updated=? WHERE id=?", (quantity, last_updated, item_id))
    conn.commit()
    conn.close()

def delete_item(item_id):
    conn = sqlite3.connect("clothes.db")
    c = conn.cursor()
    c.execute("DELETE FROM inventory WHERE id=?", (item_id,))
    conn.commit()
    conn.close()
