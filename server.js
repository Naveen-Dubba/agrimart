const express = require('express');
const cors = require('cors');
const db = require('./db');
const path = require('path');

const app = express();
const PORT = 3000; // Using 3000 for standard localhost web access

app.use(cors());
app.use(express.json());

// Serve static HTML/CSS files from the root directory!
app.use(express.static(__dirname));

// --- API ROUTES ---

// Get all products
app.get('/api/products', (req, res) => {
  db.all('SELECT * FROM products', [], (err, rows) => {
    if (err) return res.status(500).json({ error: err.message });
    res.json(rows);
  });
});

// Login
app.post('/api/auth/login', (req, res) => {
  const { email, password } = req.body;
  db.get('SELECT * FROM users WHERE email = ? AND password = ?', [email, password], (err, row) => {
    if (err) return res.status(500).json({ error: err.message });
    if (!row) return res.status(401).json({ error: 'Invalid email or password' });
    res.json({ id: row.id, name: row.name, email: row.email });
  });
});

// Register
app.post('/api/auth/register', (req, res) => {
  const { name, email, password } = req.body;
  if (!name || !email || !password) {
    return res.status(400).json({ error: 'Name, email, and password are required' });
  }
  db.run('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', [name, email, password], function(err) {
    if (err) {
      if (err.message.includes('UNIQUE')) {
        return res.status(400).json({ error: 'Email already exists' });
      }
      return res.status(500).json({ error: err.message });
    }
    res.json({ id: this.lastID, name, email });
  });
});

// Default route mapping to index.html is handled automatically by express.static
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
  console.log(`========================================`);
  console.log(`Agrimart Localhost running!`);
  console.log(`Click to open: http://localhost:${PORT}`);
  console.log(`========================================`);
});
