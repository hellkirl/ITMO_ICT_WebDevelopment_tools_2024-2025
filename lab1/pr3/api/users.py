from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from db.connection import get_session
from services.users_service import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user,
)
from models.models import Account

router = APIRouter(tags=["Users"], prefix="/users")


@router.get("/", response_model=list[Account], response_model_exclude={"password"})
async def list_users(session: Session = Depends(get_session)):
    return get_all_users(session)


@router.get("/{user_id}", response_model=Account, response_model_exclude={"password"})
async def read_user(user_id: int, session: Session = Depends(get_session)):
    user = get_user_by_id(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/new", response_model=Account, response_model_exclude={"password"})
async def create_new_user(user: Account, session: Session = Depends(get_session)):
    return create_user(session, user)


@router.put("/{user_id}", response_model=Account, response_model_exclude={"password"})
async def update_existing_user(
    user_id: int, user: Account, session: Session = Depends(get_session)
):
    updated = update_user(session, user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated


@router.delete(
    "/{user_id}", response_model=Account, response_model_exclude={"password"}
)
async def delete_existing_user(user_id: int, session: Session = Depends(get_session)):
    deleted = delete_user(session, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted
