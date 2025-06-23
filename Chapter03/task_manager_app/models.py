from typing import Optional
from pydantic import BaseModel


class Task(BaseModel):
    title: str
    description: str
    status: str

class TaskWithID(Task):
    id: int


# Version 2
class TaskV2(BaseModel):
    title: str
    description: str
    status: str
    priority: str | None = "lower"

class TaskV2WithID(TaskV2):
    id: str