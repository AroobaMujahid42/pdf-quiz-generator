import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

MAX_CHARS_PER_CHUNK = 6000
MAX_TOTAL_CHARS = 120_000

DEFAULT_NUM_MCQ = 5
DEFAULT_NUM_SHORT = 5
MAX_QUESTIONS_PER_TYPE = 15

APP_TITLE = "QuizCraft AI"
APP_TAGLINE = "Turn any document into a quiz — instantly."

