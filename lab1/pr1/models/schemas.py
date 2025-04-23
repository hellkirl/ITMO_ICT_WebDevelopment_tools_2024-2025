import datetime
from enum import Enum
from typing import Annotated, Optional

from pydantic import BaseModel, Field, field_validator


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


class Account(BaseModel):
    id: int
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    password: Annotated[Optional[str], Field(exclude=True)] = None
    description: Optional[str] = None
    created_at: Optional[str] = None

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }


class Trip(BaseModel):
    id: int
    initiator: Optional[Account] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    vehicle: Optional[VehicleType] = None
    description: Optional[str] = None
    created_at: Optional[str] = None
    status: Optional[TripStatus] = None

    @field_validator("initiator", mode="before")
    def validate_initiator(cls, v):
        if isinstance(v, int):
            return {"id": v}
        elif isinstance(v, dict):
            if "username" in v or len(v) > 1:
                return v
            return {"id": v.get("id")}
        return v

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
            Account: lambda v: v.dict(),
        }


class Companion(BaseModel):
    id: int
    trip_id: int
    companion_id: Account
    status: CompanionStatus
    created_at: str

    @field_validator("trip_id", mode="before")
    def validate_trip_id(cls, v):
        return int(v)

    @field_validator("companion_id", mode="before")
    def validate_companion_id(cls, v):
        if isinstance(v, int):
            return {"id": v}
        elif isinstance(v, dict):
            if "username" in v or len(v) > 1:
                return v
            return {"id": v.get("id")}
        return v

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat()}


class Message(BaseModel):
    id: int
    trip_id: int
    sender_id: Account
    message: str
    created_at: str

    @field_validator("trip_id", mode="before")
    def validate_trip_id(cls, v):
        return int(v)

    @field_validator("sender_id", mode="before")
    def validate_companion_id(cls, v):
        if isinstance(v, int):
            return {"id": v}
        elif isinstance(v, dict):
            if "username" in v or len(v) > 1:
                return v
            return {"id": v.get("id")}
        return v


class Itinerary(BaseModel):
    id: int
    trip_id: int
    stop_number: int
    location: str
    arrival_date: Optional[str]
    departure_date: Optional[str]
    created_at: str
