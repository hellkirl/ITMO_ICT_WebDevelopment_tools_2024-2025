from enum import Enum
import datetime
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class TripStatus(str, Enum):
    planned = "planned"
    in_progress = "in_progress"
    completed = "completed"
    canceled = "canceled"


class VehicleType(str, Enum):
    car = "car"
    motorcycle = "motorcycle"
    bicycle = "bicycle"
    scooter = "scooter"
    train = "train"
    bus = "bus"
    plane = "plane"
    boat = "boat"
    walking = "walking"


class CompanionStatus(str, Enum):
    confirmed = "confirmed"
    pending = "pending"
    declined = "declined"
    canceled = "canceled"


class Account(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = Field(default=None, sa_column_kwargs={"nullable": True})
    description: Optional[str] = None
    created_at: Optional[datetime.datetime] = None
    trips: List["Trip"] = Relationship(back_populates="initiator")


class Trip(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    initiator_id: Optional[int] = Field(default=None, foreign_key="account.id")
    start_date: Optional[datetime.datetime] = None
    end_date: Optional[datetime.datetime] = None
    vehicle: Optional[VehicleType] = None
    description: Optional[str] = None
    created_at: Optional[datetime.datetime] = None
    status: Optional[TripStatus] = None

    initiator: Optional[Account] = Relationship(back_populates="trips")
    companions: List["Companion"] = Relationship(back_populates="trip")
    messages: List["Message"] = Relationship(back_populates="trip")
    itineraries: List["Itinerary"] = Relationship(back_populates="trip")


class Companion(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    trip_id: int = Field(foreign_key="trip.id")
    companion_id: int = Field(foreign_key="account.id")
    status: CompanionStatus
    created_at: datetime.datetime

    trip: Trip = Relationship(back_populates="companions")
    companion: Account = Relationship()


class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    trip_id: int = Field(foreign_key="trip.id")
    sender_id: int = Field(foreign_key="account.id")
    message: str
    created_at: datetime.datetime

    trip: Trip = Relationship(back_populates="messages")
    sender: Account = Relationship()


class Itinerary(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    trip_id: int = Field(foreign_key="trip.id")
    stop_number: int
    location: str
    arrival_date: Optional[datetime.datetime] = None
    departure_date: Optional[datetime.datetime] = None
    created_at: datetime.datetime

    trip: Trip = Relationship(back_populates="itineraries")
