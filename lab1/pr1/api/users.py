from typing import List

from fastapi import APIRouter, HTTPException
from models.schemas import Account
from services.users_service import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user,
)

router = APIRouter(tags=["Users"], prefix="/users")


@router.get("/", response_model=List[Account], response_model_exclude={"password"})
async def read_users():
    accounts = get_all_users()
    return accounts


@router.get("/{user_id}", response_model=Account, response_model_exclude={"password"})
async def read_user(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/new", response_model=Account, response_model_exclude={"password"})
async def create_new_user(user: Account):
    return create_user(user)


@router.put("/{user_id}", response_model=Account, response_model_exclude={"password"})
async def update_existing_user(user_id: int, user: Account):
    updated = update_user(user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated


@router.delete(
    "/{user_id}", response_model=Account, response_model_exclude={"password"}
)
async def delete_existing_user(user_id: int):
    deleted = delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted
