from fastapi import FastAPI
from app.routes import files, chats

app = FastAPI()

api_version_v1 = "v1"
prefix = f"/api/{api_version_v1}"

app.include_router(files.router, prefix=prefix)
app.include_router(chats.router, prefix=prefix)
