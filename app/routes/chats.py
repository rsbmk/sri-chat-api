from fastapi import APIRouter

from app.decorators.limit import limiter
from app.modules.chats.dto import InputDTO
from app.modules.chats.inyections import chatService

router = APIRouter(
    prefix="/chats",
    tags=["chats"],
    responses={404: {"description": "Not found"}},
)


@limiter.limit("5/minute")
@router.post("/input")
async def input(body: InputDTO):
    response = await chatService.input(body)
    return response
