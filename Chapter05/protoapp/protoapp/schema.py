from pydantic import BaseModel

class ItemSchema(BaseModel):
    name: str
    color: str


