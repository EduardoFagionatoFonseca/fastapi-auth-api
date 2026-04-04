import sqlite3
from contextlib import contextmanager

class LocalDatabase():
   def __init__(self, file_name='movex.db'):
      self.file_name = file_name
      self.init_db()

   @contextmanager
   def connect(self):
      conn = sqlite3.connect(self.file_name)
      try:
         yield conn
      except Exception as e:
         conn.rollback()
         print(e)
      finally:
         conn.close()

   def init_db(self):
      with self.connect() as conn:
         cursor = conn.cursor()
         cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        email TEXT NOT NULL)""")
         conn.commit()
