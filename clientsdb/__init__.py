import sqlite3
import models.client as cl

class ClientsDB:
    def __init__(self, filename='clients.sqlite'):
        self._filename = filename
        self._conn = sqlite3.connect(filename)
        self._cursor = self._conn.cursor()
        query = """CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY,
            surname TEXT,
            name TEXT,
            email TEXT,
            city TEXT,
            postal_code INTEGER,
            address TEXT
        );"""
        self._cursor.execute(query)
        self._conn.commit()

    @property
    def clients(self):
        query = 'SELECT * FROM clients'
        self._cursor.execute(query)
        clients = self._cursor.fetchall()
        return clients

    def get_client_data(self, id: int):
        query = 'SELECT * FROM clients WHERE id = ?'
        self._cursor.execute(query, (id,))
        client = self._cursor.fetchone()
        return client

    def register_client(self, client: cl.Client):
        cl = client.data
        query = """INSERT INTO clients (surname, name, email, city, postal_code, address)
        VALUES (?, ?, ?, ?, ?, ?)"""
        self._cursor.execute(query, cl)
        self._conn.commit()
        return self._cursor.lastrowid
