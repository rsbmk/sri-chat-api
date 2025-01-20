from slowapi.middleware import SlowAPIMiddleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import files, chats
from app.decorators.limit import limiter
from app.core.config import settings

app = FastAPI()
app.state.limiter = limiter

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.ALLOW_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SlowAPIMiddleware)


@app.get("/status")
async def status():
    return {"status": "ok"}


api_version_v1 = "v1"
prefix = f"/api/{api_version_v1}"

app.include_router(files.router, prefix=prefix)
app.include_router(chats.router, prefix=prefix)
