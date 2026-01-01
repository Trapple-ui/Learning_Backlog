from pydantic import BaseModel

class ResourcesGet(BaseModel):
    title: str
    url: str
    duration: int
    type: str
    priority: int
    status: str
    note_text: str | None