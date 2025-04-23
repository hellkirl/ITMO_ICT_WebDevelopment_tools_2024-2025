from typing import List
from fastapi import APIRouter, HTTPException
from models.schemas import Companion
from services.companions_service import (
    get_companions,
    create_companion,
    update_companion,
    delete_companion,
)

router = APIRouter(tags=["Companions"], prefix="/companions")


@router.get("/{trip_id}", response_model=List[Companion])
async def read_companions(trip_id: int):
    return get_companions(trip_id)


@router.post("/new", response_model=Companion)
async def create_new_companion(companion: Companion):
    return create_companion(companion)


@router.put("/{companion_id}", response_model=Companion)
async def update_existing_companion(companion_id: int, companion: Companion):
    updated = update_companion(companion_id, companion)
    if not updated:
        raise HTTPException(status_code=404, detail="Companion not found")
    return updated


@router.delete("/{companion_id}", response_model=Companion)
async def delete_existing_companion(companion_id: int):
    deleted = delete_companion(companion_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Companion not found")
    return deleted
