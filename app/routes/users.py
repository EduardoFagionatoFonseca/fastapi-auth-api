from fastapi import APIRouter, Depends
from typing import Annotated
from app.models.user import User
from app.dependencies import get_user_repo

from app.database.users import UserRepo

router = APIRouter(prefix="/users")

@router.get("/", response_model=list[User])
async def get_users(user_repo: Annotated[UserRepo, Depends(get_user_repo)]):
   return await user_repo.list_users()

@router.post("/")
async def create_users(user: User, user_repo: Annotated[UserRepo, Depends(get_user_repo)]):
   return await user_repo.create_user(user)