from pydantic import BaseModel


class Exercise(BaseModel):
    id: int
    question: str
    difficulty: str
