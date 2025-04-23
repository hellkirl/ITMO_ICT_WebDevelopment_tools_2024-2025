from models.schemas import Trip
from data import temp_db
from services.users_service import get_user_by_id


def get_trips() -> list[Trip]:
    trips = []
    trip_ids = set()
    for user in temp_db:
        for trip in user.get("trips", []):
            if trip["id"] in trip_ids:
                continue
            trip_copy = trip.copy()
            initiator = trip_copy.get("initiator")
            user_id = initiator["id"] if isinstance(initiator, dict) else initiator
            account = get_user_by_id(user_id)
            if account:
                trip_copy["initiator"] = account.model_dump()
            trips.append(Trip.model_validate(trip_copy))
            trip_ids.add(trip["id"])
    return trips


def get_trip(trip_id: int) -> Trip | None:
    for user in temp_db:
        for trip in user.get("trips", []):
            if trip["id"] == trip_id:
                initiator = trip.get("initiator")
                user_id = initiator["id"] if isinstance(initiator, dict) else initiator
                account = get_user_by_id(user_id)
                if account:
                    trip["initiator"] = account.model_dump()
                return Trip.model_validate(trip)
    return None


def create_trip(trip: Trip) -> Trip | None:
    for user in temp_db:
        initiator_id = (
            trip.initiator["id"] if isinstance(trip.initiator, dict) else trip.initiator
        )
        if user["id"] == initiator_id:
            user.setdefault("trips", []).append(trip.model_dump())
            return trip
    return None


def update_trip(trip_id: int, trip: Trip) -> Trip | None:
    for user in temp_db:
        for i, t in enumerate(user.get("trips", [])):
            if t["id"] == trip_id:
                user["trips"][i] = trip.model_dump()
                return trip
    return None
