from sqlmodel import Session, select
from models.models import Trip


def get_trips(session: Session) -> list[Trip]:
    statement = select(Trip)
    trips = session.exec(statement).all()
    return trips


def get_trip(session: Session, trip_id: int) -> Trip | None:
    statement = select(Trip).where(Trip.id == trip_id)
    trip = session.exec(statement).one_or_none()
    return trip


def create_trip(session: Session, trip: Trip) -> Trip:
    session.add(trip)
    session.commit()
    session.refresh(trip)
    return trip


def update_trip(session: Session, trip_id: int, trip: Trip) -> Trip | None:
    statement = select(Trip).where(Trip.id == trip_id)
    existing_trip = session.exec(statement).one_or_none()
    if existing_trip:
        for key, value in trip.dict().items():
            setattr(existing_trip, key, value)
        session.commit()
        session.refresh(existing_trip)
        return existing_trip
    return None
