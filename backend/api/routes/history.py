from fastapi import APIRouter, Depends

from auth.dependencies import get_current_user
from database.database import SessionLocal
from database.models import Chat

router = APIRouter()


@router.get("/history")
def history(
    current_user=Depends(get_current_user)
):

    db = SessionLocal()

    try:

        chats = db.query(Chat).filter(
            Chat.user_id == current_user.id
        ).order_by(
            Chat.id.desc()
        ).all()

        return [
            {
                "id": chat.id,
                "query": chat.query,
                "response": chat.response,
                "created_at": chat.created_at
            }
            for chat in chats
        ]

    finally:

        db.close()