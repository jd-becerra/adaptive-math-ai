from fastapi import FastAPI

from app.routes.dashboard import router as dashboard_router
from app.routes.exercises import router as exercises_router
from app.routes.student import router as student_router

app = FastAPI(title="Adaptive Math AI")
app.include_router(exercises_router, prefix="/exercises", tags=["exercises"])
app.include_router(student_router, prefix="/student", tags=["student"])
app.include_router(dashboard_router, prefix="/dashboard", tags=["dashboard"])


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Adaptive Math AI backend is running"}
