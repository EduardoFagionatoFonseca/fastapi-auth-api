from fastapi import Depends
from typing import Annotated
from  app.database.local import LocalDatabase
from app.database.users import UserRepo

database = LocalDatabase()

def get_database():
   return database

def get_user_repo(local_database: Annotated[LocalDatabase,
                                            Depends(get_database)]) -> UserRepo:
   return UserRepo(local_database)