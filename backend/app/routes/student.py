from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def student_status() -> dict[str, str]:
    return {"status": "active"}
