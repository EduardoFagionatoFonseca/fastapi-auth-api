from app.database.local import LocalDatabase
from app.models.user import User

class UserRepo:
   def __init__(self, database: LocalDatabase) -> None:
      self.db = database

   async def list_users(self) -> list[User]:
      print("WORKING LIST USERSSSADASDAS")
      with self.db.connect() as conn:
         cursor = conn.cursor()
         cursor.execute("SELECT * FROM users")
         data = cursor.fetchall()
         users: list[User] = []
         for user in data:
            print(user)
            users.append(User(id_=1, username="edu",password='24',email='edasd'))
         print(users)
         return users
   