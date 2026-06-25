import sqlite3

conn = sqlite3.connect('agrimart.db')
cursor = conn.cursor()

products = [
    ('AM-CS-5800 Heavy Duty Chainsaw', 'CHAINSAW', 12500.00, 'assets/images/cat_chainsaw.png', 'RIPL058000'),
    ('Agrimate 4-Stroke Power Sprayer', 'SPRAYER', 14500.00, 'assets/images/cat_sprayer.png', 'RIPL045000'),
    ('Multipurpose Engine 6.5HP', 'ENGINE', 9500.00, 'assets/images/cat_engine.png', 'RIPL065000'),
    ('Organic Compost Fertilizer 50kg', 'FERTILIZER', 1200.00, 'assets/images/fertilizer_bag.png', 'RIPL050000')
]

for p in products:
    # Check if already exists
    cursor.execute("SELECT count(*) FROM products WHERE code = ?", (p[4],))
    if cursor.fetchone()[0] == 0:
        cursor.execute('INSERT INTO products (name, category, price, image_url, code) VALUES (?, ?, ?, ?, ?)', p)

conn.commit()
conn.close()
print("Products added to DB!")
