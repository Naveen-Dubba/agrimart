import sqlite3
import os

db_path = 'agrimart.db'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET image_url = 'assets/images/irrigation_stakes.png' WHERE code = 'RIPL028696'")
    cursor.execute("UPDATE products SET image_url = 'assets/images/product_shears.png' WHERE code = 'DBT24068'")
    cursor.execute("UPDATE products SET image_url = 'assets/images/manual_seeder.png' WHERE code = 'RIPL036747'")
    cursor.execute("UPDATE products SET image_url = 'assets/images/synthetic_oil.png' WHERE code = 'RIPL037653'")
    conn.commit()
    conn.close()
    print('Database updated successfully.')
else:
    print('Database not found.')
