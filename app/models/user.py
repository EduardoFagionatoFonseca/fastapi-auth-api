from pydantic import BaseModel

class User(BaseModel):
   username: str
   password: str
   email: str
   

class UserWithoutPassword(BaseModel):
   id: int
   username: str
   email: str
   