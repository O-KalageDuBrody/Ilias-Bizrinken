import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Table utilisateurs
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

# Table des réservations
c.execute('''
CREATE TABLE IF NOT EXISTS reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    nom TEXT,
    date TEXT,
    heure TEXT,
    personnes INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
''')

# Table des commandes
c.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    total REAL,
    adresse TEXT,
    telephone TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
''')

# Plats de chaque commande
c.execute('''
CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    plat_name TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(id)
)
''')

# Table des avis
c.execute('''
CREATE TABLE IF NOT EXISTS avis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    message TEXT
)
''')

conn.commit()
conn.close()