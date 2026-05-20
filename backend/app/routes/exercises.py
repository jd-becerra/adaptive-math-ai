import json

from fastapi import APIRouter

from app.database import DATA_PATH
from app.models.schemas import Exercise

router = APIRouter()


@router.get("/", response_model=list[Exercise])
def list_exercises() -> list[Exercise]:
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)
