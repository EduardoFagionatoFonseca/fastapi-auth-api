from app.database.local import LocalDatabase
from app.models.user import User
from app.models.DTO.userDto import UserDTO

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
            users.append(User(id_=user[0], username=user[1], password=user[2], email=user[3]))
         print(users)
         return users
      
   async def create_user(self, user) -> UserDTO | None:
      if not user: 
         return None
      with self.db.connect() as conn:
         cursor = conn.cursor()
         cursor.execute(
            "INSERT INTO users (id_, username, password, email) VALUES (?, ?, ?, ?)",
            (user.id_, user.username, user.password, user.email)
        )   
         conn.commit()
         return UserDTO(id_=user.id, username=user.username, email=user.email)
      # TODO remove id from insert and make it automatic as well as implement DTOS over the whole project.