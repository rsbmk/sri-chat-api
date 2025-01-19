from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import files, chats

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_version_v1 = "v1"
prefix = f"/api/{api_version_v1}"

app.include_router(files.router, prefix=prefix)
app.include_router(chats.router, prefix=prefix)
