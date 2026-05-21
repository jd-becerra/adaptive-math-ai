import os

from dotenv import load_dotenv

load_dotenv()

AI_API_URL = os.getenv("AI_API_URL")

AI_API_KEY = os.getenv("AI_API_KEY")

AI_MODEL = os.getenv("AI_MODEL")

BACKEND_PORT = int(
    os.getenv("BACKEND_PORT", 12000)
)