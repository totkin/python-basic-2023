from pydantic import BaseModel, Field


class User(BaseModel):
    id: int = Field(..., example=123)
    username: str = Field(
        example="john",
        min_length=3,
        max_length=20,
    )
