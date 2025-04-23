from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from db.connection import get_session
from services.messages_service import get_messages, create_message
from models.models import Message

router = APIRouter(tags=["Messages"], prefix="/messages")


@router.get("/{trip_id}", response_model=list[Message])
async def get_trip_messages(session: Session = Depends(get_session), trip_id: int = 0):
    messages = get_messages(session, trip_id)
    if not messages:
        raise HTTPException(status_code=404, detail="Messages not found")
    return messages


@router.post("/", response_model=Message)
async def create_trip_message(
    message: Message, session: Session = Depends(get_session)
):
    created_message = create_message(session, message)
    if not created_message:
        raise HTTPException(status_code=400, detail="Error creating message")
    return created_message
