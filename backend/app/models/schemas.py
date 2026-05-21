from pydantic import BaseModel

class Exercise(BaseModel):
    question: str


class StudentAnswer(BaseModel):
    topic: str
    question: str
    student_answer: str
    correct_answer: str