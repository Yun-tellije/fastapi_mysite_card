from fastapi import APIRouter
from backend.services.service_chat import ChatService

router = APIRouter(
    tags=["Chat"],
)


@router.post("/") # http://127.0.0.1:8000/chat/
async def send_message(chat: dict) -> dict:
    print(f"전달 받은 챗: {chat}")
    
    ChatService().send_chat(chat)
    
    return {"status": {"code": 200, "message": "success"}}