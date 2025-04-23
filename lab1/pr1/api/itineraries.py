from datetime import datetime
from typing import List

from fastapi import APIRouter
from models.schemas import Itinerary
from data import temp_db

router = APIRouter(tags=["Itineraries"], prefix="/itineraries")


@router.get("/{trip_id}", response_model=List[Itinerary])
async def read_itineraries(trip_id: int):
    itineraries = []
    for user in temp_db:
        for trip in user["trips"]:
            if trip["id"] == trip_id:
                itineraries.extend(trip["itineraries"])
    return itineraries
