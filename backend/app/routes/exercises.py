from fastapi import APIRouter
from app.models.schemas import Exercise
from app.services.ai_service import generate_variants

router = APIRouter(prefix="/exercises")

@router.post("/generate")
def generate_exercise(exercise: Exercise):

    variants = generate_variants(exercise.question)

    return {
        "original": exercise.question,
        "variants": variants
    }