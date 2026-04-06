from app.database.local import LocalDatabase
from app.models.user import User, UserWithoutPassword

class UserRepo:
   def __init__(self, database: LocalDatabase) -> None:
      self.db = database

   async def list_users(self) -> list[UserWithoutPassword]:
      with self.db.connect() as conn:
         cursor = conn.cursor()
         cursor.execute("SELECT id, username, email FROM users")
         data = cursor.fetchall()
         users: list[UserWithoutPassword] = []
         for user in data:
            users.append(UserWithoutPassword(id=user[0], username=user[1], email=user[2]))
         return users
      
   async def create_user(self, data: User) -> UserWithoutPassword:
      with self.db.connect() as conn:
         cursor = conn.cursor()
         cursor.execute(
            "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
            (data.username, data.password, data.email)
        )   
         conn.commit()
         cursor.execute("SELECT id, username, email FROM users WHERE username LIKE (?)",(data.username, ))
         fetched = cursor.fetchone()
         return UserWithoutPassword(id=fetched[0], username=fetched[1], email=fetched[2])
      # TODO remove id from insert and make it automatic as well as implement DTOS over the whole project.

   async def  authenticate_user(self, data: User):
      with self.db.connect() as conn:
         cursor = conn.cursor()
         cursor.execute("SELECT username, password, email FROM users WHERE username LIKE (?)", (data.username,))
         fetched = cursor.fetchone()
         db_user =  User(username=fetched[0], password=fetched[1], email=fetched[2])
         if data.password != db_user.password:
            return {"msg": "wrong password"}
         if data.email != db_user.email:
            return {"msg": "wrong email"}
         else:
            return {"msg": "Logged in sucessfully!"}