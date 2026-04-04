from app.database.local import LocalDatabase
from app.models.user import User
from app.models.DTO.userDto import UserDTO

class UserRepo:
   def __init__(self, database: LocalDatabase) -> None:
      self.db = database

   async def list_users(self) -> list[UserDTO]:
      with self.db.connect() as conn:
         cursor = conn.cursor()
         cursor.execute("SELECT id, username, email FROM users")
         data = cursor.fetchall()
         users: list[UserDTO] = []
         for user in data:
            users.append(UserDTO(id=user[0], username=user[1], email=user[2]))
         return users
      
   async def create_user(self, data) -> UserDTO:
      with self.db.connect() as conn:
         cursor = conn.cursor()
         cursor.execute(
            "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
            (data.username, data.password, data.email)
        )   
         conn.commit()
         cursor.execute("SELECT id, username, email FROM users WHERE username LIKE (?)",(data.username, ))
         fetched = cursor.fetchone()
         return UserDTO(id=fetched[0], username=fetched[1], email=fetched[2])
      # TODO remove id from insert and make it automatic as well as implement DTOS over the whole project.