from pydantic import BaseModel


class InputDTO(BaseModel):
    input: str
    thread_id: str | None = None
