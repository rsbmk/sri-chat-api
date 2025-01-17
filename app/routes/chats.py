from fastapi import APIRouter

from app.modules.chats.dto import InputDTO
from app.modules.chats.inyections import chatService

router = APIRouter(
    prefix="/chats",
    tags=["chats"],
    responses={404: {"description": "Not found"}},
)


@router.post("/input")
async def input(body: InputDTO):
    response = await chatService.input(body)
    return response
