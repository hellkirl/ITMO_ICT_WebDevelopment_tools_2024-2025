from typing import List

from fastapi import APIRouter, HTTPException
from models.schemas import Trip
from services.trips_service import get_trips, get_trip, create_trip, update_trip

router = APIRouter(tags=["Trips"], prefix="/trips")


@router.get("/", response_model=List[Trip])
async def read_trips():
    return get_trips()


@router.get("/{trip_id}", response_model=Trip)
async def read_trip(trip_id: int):
    trip = get_trip(trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip


@router.post("/new", response_model=Trip)
async def create_new_trip(trip: Trip):
    return create_trip(trip)


@router.put("/{trip_id}", response_model=Trip)
async def update_existing_trip(trip_id: int, trip: Trip):
    updated = update_trip(trip_id, trip)
    if not updated:
        raise HTTPException(status_code=404, detail="Trip not found")
    return updated
