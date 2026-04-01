from app.database.local import LocalDatabase
from app.models.user import User

class UserRepo:
   def __init__(self, database: LocalDatabase) -> None:
      self.db = database

   async def list_users(self) -> list[User]:
      with self.db.connect() as conn:
         cursor = conn.cursor()
         cursor.execute("SELECT id, username, password, email FROM users")
         data = cursor.fetchall()
         users = [
            User(id_= user[0], username=user[1], password=user[2], email=user[3]) for user in data
            ]
         print(users)
         return users