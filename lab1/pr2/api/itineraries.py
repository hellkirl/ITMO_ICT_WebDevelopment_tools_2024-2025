from fastapi import APIRouter, Depends
from sqlmodel import Session
from db.connection import get_session
from services.itineraries_service import (
    get_itineraries,
    add_itinerary,
    delete_itinerary,
)
from models.models import Itinerary

router = APIRouter(tags=["Itineraries"], prefix="/itineraries")


@router.get("/{trip_id}", response_model=list[Itinerary])
async def read_itineraries(
    trip_id: int,
    session: Session = Depends(get_session),
):
    itineraries = get_itineraries(session, trip_id)
    return itineraries


@router.post("/", response_model=Itinerary)
async def create_new_itinerary(
    itinerary: Itinerary,
    session: Session = Depends(get_session),
):
    new_itinerary = add_itinerary(session, itinerary)
    return new_itinerary


@router.delete("/{trip_id}/{itinerary_id}", response_model=bool)
async def remove_itinerary(
    trip_id: int,
    itinerary_id: int,
    session: Session = Depends(get_session),
):
    deleted = delete_itinerary(session, trip_id, itinerary_id)
    return deleted
