import random

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(tags=["Users"])


class User(BaseModel):
    id: int
    name: str


class CreateUser(BaseModel):
    name: str


class UpdateUser(CreateUser):
    pass


Users = list[User]
MaybeUser = None | User


fake_db: list[User] = [User(id=1, name="Tidras")]


@router.get("/users", status_code=200, response_model=Users)
def list_users() -> Users:
    return fake_db


@router.post("/users", status_code=201)
def create_user(payload: CreateUser) -> None:
    if payload.name not in [u.name for u in fake_db]:
        fake_db.append(User(id=random.randint(2, 100), name=payload.name))


@router.get("/users/{user_id}", status_code=200, response_model=MaybeUser)
def get_user(user_id: int) -> MaybeUser:
    found = next((u for u in fake_db if u.id == user_id), None)
    if not found:
        raise HTTPException(status_code=404, detail="User not found")
    return found


@router.put("/users/{user_id}", status_code=200)
def update_user(user_id: int, payload: UpdateUser) -> None:
    for user in fake_db:
        if user.id == user_id:
            user.name = payload.name
