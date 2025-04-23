from services.users_service import get_user_by_id
from models.schemas import Message
from data import temp_db


def get_messages(trip_id: int) -> list[Message]:
    messages = []
    for user in temp_db:
        for trip in user["trips"]:
            if trip["id"] == trip_id:
                for msg in trip["messages"]:
                    sender = get_user_by_id(user_id=msg["sender_id"])
                    messages.append(
                        Message(
                            id=msg["id"],
                            trip_id=trip["id"],
                            sender_id=sender,
                            message=msg["message"],
                            created_at=msg["created_at"],
                        )
                    )
    return messages


def create_message(message: Message) -> Message:
    for user in temp_db:
        for trip in user["trips"]:
            if trip["id"] == message.trip_id:
                trip["messages"].append(message.model_dump())
                return message
    return None
