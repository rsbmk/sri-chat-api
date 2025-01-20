from fastapi.responses import StreamingResponse
from fastapi import APIRouter, Request

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
async def input(body: InputDTO, request: Request):
    async def stream_response():
        async for chunk in chatService.input(body):
            yield chunk

    return StreamingResponse(stream_response(), media_type="text/event-stream")
