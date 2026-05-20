from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def dashboard_summary() -> dict[str, int]:
    return {"total_students": 0, "total_exercises": 0}
