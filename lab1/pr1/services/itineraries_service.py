from datetime import datetime
from models.schemas import Itinerary
from data import temp_db


def get_itineraries(trip_id: int) -> list[Itinerary]:
    itineraries = []
    for user in temp_db:
        for trip in user.get("trips", []):
            if trip.get("id") == trip_id:
                for itinerary in trip.get("itineraries", []):
                    itineraries.append(Itinerary.model_validate(itinerary))
    return itineraries


def add_itinerary(
    trip_id: int,
    stop_number: int,
    location: str,
    arrival_date: str,
    departure_date: str,
) -> Itinerary | None:
    for user in temp_db:
        for trip in user.get("trips", []):
            if trip.get("id") == trip_id:
                itinerary = {
                    "id": len(trip.get("itineraries", [])) + 1,
                    "trip_id": trip_id,
                    "stop_number": stop_number,
                    "location": location,
                    "arrival_date": arrival_date,
                    "departure_date": departure_date,
                    "created_at": datetime.now().isoformat(),
                }
                trip.setdefault("itineraries", []).append(itinerary)
                return Itinerary.model_validate(itinerary)
    return None


def delete_itinerary(trip_id: int, itinerary_id: int) -> bool:
    for user in temp_db:
        for trip in user.get("trips", []):
            if trip.get("id") == trip_id:
                for itinerary in trip.get("itineraries", []):
                    if itinerary["id"] == itinerary_id:
                        trip["itineraries"].remove(itinerary)
                        return True
    return False
