from pydantic import BaseModel

class UserDTO(BaseModel):
   id_: int
   username: str
   email: str
   