"""
A class representing a database client.

Attributes:
    connection (sqlite3.Connection): The connection to the SQLite database.
    cursor (sqlite3.Cursor): The cursor object for executing SQL queries.

Methods:
    execute(query, params=None): Executes an SQL query with optional
    parameters.
    fetch_all(query, params=None): Fetches all rows from the
    result of an SQL query with optional parameters.
    fetch_one(query, params=None): Fetches one row from the result of an SQL 
    query with optional parameters.
    close(): Closes the cursor and the database connection.
"""
import sqlite3


class dbClient:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.connection = sqlite3.connect('chatbot.db')
        self.cursor = self.connection.cursor()
        self.setup_tables()

    def execute(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()

    def fetch_all(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def setup_tables(self):
        file_chunk_table_create_query = '''CREATE TABLE IF NOT EXISTS 
        file_chunk_table (id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT, page_number INTEGER, chunk_id TEXT)'''

        self.cursor.execute(file_chunk_table_create_query)
