import sqlite3
from hashlib import sha256
from os import urandom

DATABASE = 'my_database.db'

def create_connection():
    """Crea una conexión a la base de datos SQLite."""
    conn = sqlite3.connect(DATABASE)
    return conn

def create_user(username, email, hashed_password, salt):
    """Crea un nuevo usuario en la base de datos."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (username, email, password, salt)
        VALUES (?, ?, ?, ?)
    ''', (username, email, hashed_password, salt))
    conn.commit()
    conn.close()

def validate_user(username_or_email, password):
    """Valida el usuario basado en el nombre de usuario, correo electrónico y contraseña."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT email, password, salt FROM users WHERE username = ? OR email = ?
    ''', (username_or_email, username_or_email))
    user = cursor.fetchone()
    conn.close()
    if user:
        email, stored_password, salt = user
        hashed_password = hash_password(password, salt)
        return hashed_password == stored_password
    return False

def generate_salt():
    """Genera una nueva sal aleatoria."""
    return urandom(16).hex()

def hash_password(password, salt):
    """Genera un hash de la contraseña usando SHA-256 y una sal."""
    salted_password = password + salt
    return sha256(salted_password.encode()).hexdigest()
