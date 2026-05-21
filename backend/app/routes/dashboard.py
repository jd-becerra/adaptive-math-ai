from fastapi import APIRouter

router = APIRouter(prefix="/dashboard")

@router.get("/stats")
def stats():

    return {
        "students": 20,
        "average_score": 82,
        "hardest_topic": "Fractions"
    }