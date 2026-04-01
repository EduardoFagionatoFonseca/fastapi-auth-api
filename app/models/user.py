from pydantic import BaseModel

class User(BaseModel):
   id_: int
   username: str
   password: str
   email: str
   