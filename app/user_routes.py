from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["Users"])


class User(BaseModel):
    id: int
    name: str


class CreateUser(BaseModel):
    name: str


class UpdateUser(CreateUser):
    pass


users: list[User] = [User(id=1, name="Tidras")]


@router.get("/users", status_code=200, response_model=list[User])
def list_users() -> list[User]:
    return users


@router.post("/users", status_code=201)
def create_user(payload: CreateUser) -> None:
    if payload.name not in [u.name for u in users]:
        users.append(payload)


@router.get("/users/{id}", status_code=200, response_model=Optional[User])
def get_user(user_id: int) -> Optional[User]:
    return next((user for user in users if user.id == user_id), None)


@router.put("/users/{id}", status_code=200, response_model=Optional[User])
def get_user(user_id: int, payload: UpdateUser) -> Optional[User]:
    for user in users:
        if user.id == user_id:
            user.name = payload.name
