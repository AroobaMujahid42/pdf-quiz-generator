import streamlit as st

from core.question_generator import MCQQuestion, ShortAnswerQuestion, QuizResult
from ui.styles import question_card_delay
from config import APP_TITLE, APP_TAGLINE


def render_hero():
    st.markdown(
        f"""
        <div class="hero-container">
            <div class="hero-title">{APP_TITLE}</div>
            <div class="hero-subtitle">{APP_TAGLINE}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_stats(num_mcq: int, num_short: int, chars_processed: int):
    st.markdown(
        f"""
        <div style="margin-bottom: 1.2rem;">
            <span class="stat-pill">📝 {num_mcq} MCQs</span>
            <span class="stat-pill">✍️ {num_short} Short Answer</span>
            <span class="stat-pill">📄 {chars_processed:,} characters analyzed</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_mcq_card(q: MCQQuestion, index: int):
    options_html = ""
    for j, opt in enumerate(q.options):
        label = chr(65 + j)
        options_html += f'<div class="option-row"><strong>{label}.</strong> {opt}</div>'

    explanation_html = ""
    if q.explanation:
        explanation_html = f'<div class="explanation-box">💡 {q.explanation}</div>'

    st.markdown(
        f"""
        <div class="question-card" style="{question_card_delay(index)}">
            <span class="question-badge badge-mcq">Multiple Choice</span>
            <div class="question-text">{index + 1}. {q.question}</div>
            {options_html}
            <div class="correct-answer-box">✅ <strong>Correct answer:</strong> {q.correct_answer}</div>
            {explanation_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_short_answer_card(q: ShortAnswerQuestion, index: int):
    st.markdown(
        f"""
        <div class="question-card" style="{question_card_delay(index)}">
            <span class="question-badge badge-short">Short Answer</span>
            <div class="question-text">{index + 1}. {q.question}</div>
            <div class="correct-answer-box">✅ <strong>Ideal answer:</strong> {q.ideal_answer}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_quiz(quiz: QuizResult):
    if quiz.mcqs:
        st.subheader("📝 Multiple Choice Questions")
        for i, q in enumerate(quiz.mcqs):
            render_mcq_card(q, i)

    if quiz.short_answers:
        st.subheader("✍️ Short Answer Questions")
        for i, q in enumerate(quiz.short_answers):
            render_short_answer_card(q, i)


def render_loader(message: str):
    st.markdown(
        f"""
        <div style="text-align:center; padding: 1.5rem;">
            <div style="font-size: 1.05rem; color: #a5b4fc; animation: fadeInUp 0.4s ease-out;">
                {message}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )