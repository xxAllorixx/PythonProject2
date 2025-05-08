from pydantic import BaseModel, Field
from typing import Annotated, Optional

class Book(BaseModel):
    id: int
    title: str
    author: str
    review: Optional[Annotated[int, Field(ge=1, le=5)]] = None