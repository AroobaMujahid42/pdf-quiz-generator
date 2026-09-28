import json
import re
from dataclasses import dataclass, field

from groq import Groq

from config import GROQ_API_KEY, GROQ_MODEL, MAX_CHARS_PER_CHUNK
from core.file_parser import chunk_text


class QuestionGenerationError(Exception):
    pass


@dataclass
class MCQQuestion:
    question: str
    options: list[str]
    correct_answer: str
    explanation: str = ""
    type: str = "mcq"


@dataclass
class ShortAnswerQuestion:
    question: str
    ideal_answer: str
    type: str = "short_answer"


@dataclass
class QuizResult:
    mcqs: list[MCQQuestion] = field(default_factory=list)
    short_answers: list[ShortAnswerQuestion] = field(default_factory=list)


SYSTEM_PROMPT = """You are an expert quiz-writer and instructional designer.
You generate high-quality exam-style questions strictly from the text provided by the user.
Never invent facts that aren't supported by the text.
Always respond with ONLY valid JSON — no markdown fences, no commentary, no preamble."""

USER_PROMPT_TEMPLATE = """From the SOURCE TEXT below, generate:
- {num_mcq} multiple-choice questions
- {num_short} short-answer questions

Requirements:
- MCQs must have exactly 4 options, only one correct.
- Include a one-sentence explanation for each MCQ's correct answer.
- Short-answer questions should require a 1-3 sentence response and include an ideal answer.
- Base every question strictly on the SOURCE TEXT. Do not use outside knowledge.
- Vary difficulty and cover different parts of the text.

Respond with ONLY this JSON structure, no other text:
{{
  "mcqs": [
    {{
      "question": "...",
      "options": ["...", "...", "...", "..."],
      "correct_answer": "...",
      "explanation": "..."
    }}
  ],
  "short_answers": [
    {{
      "question": "...",
      "ideal_answer": "..."
    }}
  ]
}}

SOURCE TEXT:
\"\"\"
{text}
\"\"\"
"""


def _get_client() -> Groq:
    if not GROQ_API_KEY:
        raise QuestionGenerationError(
            "No Groq API key found. Add GROQ_API_KEY to your .env file. "
            "Get a free key at https://console.groq.com"
        )
    return Groq(api_key=GROQ_API_KEY)


def _extract_json(raw_text: str) -> dict:
    cleaned = raw_text.strip()
    cleaned = re.sub(r"^```(?:json)?", "", cleaned).strip()
    cleaned = re.sub(r"```$", "", cleaned).strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", cleaned, re.DOTALL)
        if match:
            return json.loads(match.group(0))
        raise QuestionGenerationError("The AI response wasn't valid JSON. Please try again.")


def _call_model(client: Groq, text_chunk: str, num_mcq: int, num_short: int) -> dict:
    user_prompt = USER_PROMPT_TEMPLATE.format(
        num_mcq=num_mcq, num_short=num_short, text=text_chunk
    )

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.5,
        max_tokens=4000,
    )

    raw = response.choices[0].message.content
    return _extract_json(raw)


def _merge_into_result(data: dict, result: QuizResult) -> None:
    for mcq in data.get("mcqs", []):
        try:
            result.mcqs.append(
                MCQQuestion(
                    question=mcq["question"],
                    options=mcq["options"],
                    correct_answer=mcq["correct_answer"],
                    explanation=mcq.get("explanation", ""),
                )
            )
        except KeyError:
            continue

    for sa in data.get("short_answers", []):
        try:
            result.short_answers.append(
                ShortAnswerQuestion(
                    question=sa["question"],
                    ideal_answer=sa["ideal_answer"],
                )
            )
        except KeyError:
            continue


def generate_questions(text: str, num_mcq: int, num_short: int) -> QuizResult:
    client = _get_client()
    chunks = chunk_text(text, MAX_CHARS_PER_CHUNK)

    result = QuizResult()

    if len(chunks) == 1:
        data = _call_model(client, chunks[0], num_mcq, num_short)
        _merge_into_result(data, result)
        return result

    n_chunks = len(chunks)
    base_mcq = num_mcq // n_chunks
    extra_mcq = num_mcq % n_chunks
    base_short = num_short // n_chunks
    extra_short = num_short % n_chunks

    for i, chunk in enumerate(chunks):
        chunk_mcq = base_mcq + (1 if i < extra_mcq else 0)
        chunk_short = base_short + (1 if i < extra_short else 0)

        if chunk_mcq == 0 and chunk_short == 0:
            continue

        try:
            data = _call_model(client, chunk, chunk_mcq, chunk_short)
            _merge_into_result(data, result)
        except QuestionGenerationError:
            continue

    if not result.mcqs and not result.short_answers:
        raise QuestionGenerationError(
            "Couldn't generate any questions from this document. Please try again."
        )

    return result