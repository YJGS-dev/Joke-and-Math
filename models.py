from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4

class Joke(BaseModel):
    id: Optional[UUID] = uuid4()
    joke: str
