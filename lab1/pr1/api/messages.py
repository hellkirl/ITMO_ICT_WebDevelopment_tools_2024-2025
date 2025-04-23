from typing import List

from fastapi import APIRouter, HTTPException
from models.schemas import Message
from services.messages_service import get_messages, create_message

router = APIRouter(tags=["Messages"], prefix="/messages")


@router.get("/{trip_id}", response_model=List[Message])
async def read_messages(trip_id: int):
    messages_list = get_messages(trip_id)
    if messages_list is None:
        raise HTTPException(status_code=404, detail="Messages not found")
    return messages_list


@router.post("/new", response_model=Message)
async def create_new_message(message: Message):
    return create_message(message)
