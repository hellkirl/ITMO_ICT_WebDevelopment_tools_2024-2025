from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from db.connection import get_session
from services.trips_service import get_trips, get_trip, create_trip, update_trip
from models.models import Trip

router = APIRouter(tags=["Trips"], prefix="/trips")


@router.get("/", response_model=list[Trip])
async def list_trips(session: Session = Depends(get_session)):
    return get_trips(session)


@router.get("/{trip_id}", response_model=Trip)
async def get_trip_by_id(trip_id: int, session: Session = Depends(get_session)):
    trip = get_trip(session, trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip


@router.post("/new", response_model=Trip)
async def create_new_trip(trip: Trip, session: Session = Depends(get_session)):
    return create_trip(session, trip)


@router.put("/{trip_id}", response_model=Trip)
async def update_existing_trip(
    trip_id: int, trip: Trip, session: Session = Depends(get_session)
):
    updated = update_trip(session, trip_id, trip)
    if not updated:
        raise HTTPException(status_code=404, detail="Trip not found")
    return updated
