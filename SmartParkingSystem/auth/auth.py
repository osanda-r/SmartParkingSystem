# Authentication handler
import sqlite3
import hashlib

class AuthManager:
    def __init__(self, db="users.db"):
        self.conn = sqlite3.connect(db, check_same_thread=False)
        self._create_users_table()

    def _create_users_table(self):
        c = self.conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash TEXT
        )""")
        self.conn.commit()

    def signup(self, username, password):
        hashed = self._hash(password)
        c = self.conn.cursor()
        try:
            c.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, hashed))
            self.conn.commit()
            return True
        except:
            return False

    def login(self, username, password):
        hashed = self._hash(password)
        c = self.conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ? AND password_hash = ?", (username, hashed))
        return c.fetchone() is not None

    def _hash(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
