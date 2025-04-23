from services.users_service import get_user_by_id
from models.schemas import Companion
from data import temp_db


def get_companions(trip_id: int) -> list[Companion]:
    companions = []
    for user in temp_db:
        for trip in user.get("trips", []):
            if trip.get("id") == trip_id:
                for companion_data in trip.get("companions", []):
                    companion_id = get_user_by_id(companion_data.get("id"))
                    if companion_id:
                        companion_data["companion_id"] = companion_id.model_dump()
                    else:
                        companion_data["companion_id"] = {
                            "id": companion_data.get("id")
                        }
                    companion_obj = Companion.model_validate(companion_data)
                    companions.append(companion_obj)
                break
    return companions


def create_companion(companion: Companion) -> Companion | None:
    for user in temp_db:
        for trip in user.get("trips", []):
            trip_id_val = trip.get("id")
            companion_trip_id = (
                companion.trip_id.id
                if isinstance(companion.trip_id, dict)
                else companion.trip_id
            )
            if trip_id_val == companion_trip_id:
                trip.setdefault("companions", []).append(companion.model_dump())
                return companion
    return None


def update_companion(companion_id: int, companion: Companion) -> Companion | None:
    for user in temp_db:
        for trip in user.get("trips", []):
            companions = trip.get("companions", [])
            for i, comp in enumerate(companions):
                if comp["id"] == companion_id:
                    companions[i] = companion.model_dump()
                    return companion
    return None


def delete_companion(companion_id: int) -> Companion | None:
    for user in temp_db:
        for trip in user.get("trips", []):
            companions = trip.get("companions", [])
            for comp in companions:
                if comp["id"] == companion_id:
                    companions.remove(comp)
                    return Companion.model_validate(comp)
    return None
