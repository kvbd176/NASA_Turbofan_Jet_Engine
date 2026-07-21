from fastapi import APIRouter, Depends
from pydantic import BaseModel

from auth.dependencies import get_current_user
from database.database import SessionLocal
from database.models import Chat

from agents.rag_agent import RAGAgent
from llm.llm_service import generate_answer


router = APIRouter()


class ChatRequest(BaseModel):
    query: str


@router.post("/chat")
def chat(
    request: ChatRequest,
    current_user=Depends(get_current_user)
):

    try:

        # -----------------------------
        # User specific RAG retrieval
        # -----------------------------

        rag_agent = RAGAgent(
            current_user.id
        )

        retrieved_data = rag_agent.retrieve(
            request.query
        )


        context = f"""
        User ID: {current_user.id}

        Engine Analysis Data:
        {retrieved_data}
        """


    except Exception:

        context = f"""
        User ID: {current_user.id}

        No processed dataset available.
        The user has not uploaded or processed any engine dataset yet.
        """


    answer = generate_answer(
        context=context,
        question=request.query
    )


    # -----------------------------
    # Save chat history
    # -----------------------------

    db = SessionLocal()

    chat_record = Chat(
        user_id=current_user.id,
        query=request.query,
        response=answer
    )

    db.add(chat_record)
    db.commit()
    db.close()


    return {
        "answer": answer
    }