from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.exercises import router as exercises_router
from app.routes.student import router as student_router
from app.routes.dashboard import router as dashboard_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(exercises_router)
app.include_router(student_router)
app.include_router(dashboard_router)

@app.get("/")
def root():
    return {"message": "Adaptive Math AI API"}