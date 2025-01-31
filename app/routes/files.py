from fastapi import APIRouter, File, UploadFile, BackgroundTasks, Request

from app.decorators.limit import limiter
from app.modules.files.inyections import service

router = APIRouter(
    prefix="/files",
    tags=["files"],
    responses={404: {"description": "Not found"}},
)


@limiter.limit("3/minute")
@router.post("/upload")
async def upload_file(
    background_tasks: BackgroundTasks,
    request: Request,
    file: UploadFile = File(...),
    type: str | None = None,
):
    if type != "text":
        return {"message": "Only text files are allowed"}

    file_path = await service.validate_file_text(file)
    background_tasks.add_task(service.upload_file_text, file_path)

    return {"message": "File uploaded successfully"}
