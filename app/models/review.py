from pydantic import BaseModel, Field
from typing import Annotated, Optional

class Review(BaseModel):
    review: Optional[Annotated[int, Field(ge=1, le=5)]]