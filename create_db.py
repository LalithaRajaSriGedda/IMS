import sqlite3  

def create_db():
    con = sqlite3.connect(database=r'ims.db')
    con.execute("PRAGMA foreign_keys = ON;")  # Enable foreign key constraints
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS employee(
            eid INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, 
            email TEXT, 
            gender TEXT, 
            contact TEXT, 
            dob TEXT, 
            doj TEXT, 
            pass TEXT, 
            utype TEXT, 
            address TEXT, 
            salary TEXT
        )
    """)
    con.commit()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS supplier(
            invoice INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, 
            contact TEXT, 
            desc TEXT
        )
    """)
    con.commit()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS category(
            cid INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT
        )
    """)
    con.commit()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS product(
            pid INTEGER PRIMARY KEY AUTOINCREMENT, 
            supplier_id INTEGER, 
            category_id INTEGER, 
            name TEXT, 
            price REAL, 
            qty INTEGER, 
            status TEXT,
            FOREIGN KEY (supplier_id) REFERENCES supplier(invoice) ON DELETE SET NULL,
            FOREIGN KEY (category_id) REFERENCES category(cid) ON DELETE SET NULL
        )
    """)
    con.commit()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS cart_table(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            product_id INTEGER, 
            quantity INTEGER, 
            FOREIGN KEY (product_id) REFERENCES product(pid) ON DELETE CASCADE
        )
    """)
    con.commit()

    con.close()
create_db()
