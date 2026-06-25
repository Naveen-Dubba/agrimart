const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const dbPath = path.resolve(__dirname, 'agrimart.db');
const db = new sqlite3.Database(dbPath, (err) => {
  if (err) {
    console.error('Error opening database', err.message);
  } else {
    console.log('Connected to the SQLite database.');
    
    db.serialize(() => {
      db.run(`CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
      )`);

      db.run(`CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL,
        image_url TEXT,
        code TEXT
      )`);

      db.get('SELECT count(*) as count FROM products', (err, row) => {
        if (err) return console.error(err);
        
        if (row.count === 0) {
          console.log('Seeding initial products data...');
          const insertProduct = db.prepare('INSERT INTO products (name, category, price, image_url, code) VALUES (?, ?, ?, ?, ?)');
          insertProduct.run('AM - Deep Drip Irrigation Stakes', 'IRRIGATION', 1660.00, 'assets/images/irrigation_stakes.png', 'RIPL028696');
          insertProduct.run('AM-22338 Pruning Shears', 'PRUNER', 1795.00, 'assets/images/product_shears.png', 'DBT24068');
          insertProduct.run('AM-MVS-1P MANUAL VERTICLE SEEDER', 'MANUAL SEEDER', 1840.00, 'assets/images/manual_seeder.png', 'RIPL036747');
          insertProduct.run('OM PROSINT2EVO SYNTHETIC-2T-OIL', 'LUBRICANTS', 8400.00, 'assets/images/synthetic_oil.png', 'RIPL037653');
          insertProduct.run('AM-CS-5800 Heavy Duty Chainsaw', 'CHAINSAW', 12500.00, 'assets/images/cat_chainsaw.png', 'RIPL058000');
          insertProduct.run('Agrimate 4-Stroke Power Sprayer', 'SPRAYER', 14500.00, 'assets/images/cat_sprayer.png', 'RIPL045000');
          insertProduct.run('Multipurpose Engine 6.5HP', 'ENGINE', 9500.00, 'assets/images/cat_engine.png', 'RIPL065000');
          insertProduct.run('Organic Compost Fertilizer 50kg', 'FERTILIZER', 1200.00, 'assets/images/fertilizer_bag.png', 'RIPL050000');
          insertProduct.finalize();
        }
      });
    });
  }
});

module.exports = db;
