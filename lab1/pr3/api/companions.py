from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from db.connection import get_session
from services.companions_service import (
    get_companions,
    create_companion,
    delete_companion,
    update_companion,
)
from models.models import Companion

router = APIRouter(tags=["Companions"], prefix="/companions")


@router.get("/", response_model=list[Companion])
async def read_companions(
    trip_id: int,
    session: Session = Depends(get_session),
):
    companions = get_companions(session, trip_id)
    return companions


@router.post("/", response_model=Companion)
async def create_new_companion(
    companion: Companion,
    session: Session = Depends(get_session),
):
    try:
        new_companion = create_companion(session, companion)
        return new_companion
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{companion_id}", response_model=Companion)
async def remove_companion(
    companion_id: int,
    session: Session = Depends(get_session),
):
    try:
        deleted_companion = delete_companion(session, companion_id)
        if not deleted_companion:
            raise HTTPException(status_code=404, detail="Companion not found")
        return deleted_companion
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{companion_id}", response_model=Companion)
async def modify_companion(
    companion_id: int,
    companion: Companion,
    session: Session = Depends(get_session),
):
    try:
        updated_companion = update_companion(session, companion_id, companion)
        if not updated_companion:
            raise HTTPException(status_code=404, detail="Companion not found")
        return updated_companion
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
