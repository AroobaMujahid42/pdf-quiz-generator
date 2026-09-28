import streamlit as st

from config import (
    APP_TITLE,
    DEFAULT_NUM_MCQ,
    DEFAULT_NUM_SHORT,
    MAX_QUESTIONS_PER_TYPE,
)
from core.file_parser import extract_text, UnsupportedFileError, EmptyDocumentError
from core.question_generator import generate_questions, QuestionGenerationError
from core.exporter import build_docx, build_pdf
from ui.styles import CUSTOM_CSS
from ui.components import render_hero, render_stats, render_quiz, render_loader


st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# --- Session state (survives Streamlit re-runs) ---
if "quiz" not in st.session_state:
    st.session_state.quiz = None
if "source_filename" not in st.session_state:
    st.session_state.source_filename = None
if "chars_processed" not in st.session_state:
    st.session_state.chars_processed = 0

# --- Sidebar ---
with st.sidebar:
    st.markdown("### ⚙️ Quiz Settings")
    num_mcq = st.slider("Multiple choice questions", 0, MAX_QUESTIONS_PER_TYPE, DEFAULT_NUM_MCQ)
    num_short = st.slider("Short answer questions", 0, MAX_QUESTIONS_PER_TYPE, DEFAULT_NUM_SHORT)

# --- Header and upload ---
render_hero()

uploaded_file = st.file_uploader(
    "Upload your document",
    type=["pdf", "docx"],
    help="PDF or Word (.docx) files work best. Aim for 10-20 pages for fastest results.",
)

generate_clicked = st.button(
    "✨ Generate Quiz", use_container_width=True, disabled=uploaded_file is None
)

# --- Generate ---
if generate_clicked and uploaded_file is not None:
    if num_mcq == 0 and num_short == 0:
        st.warning("Select at least one question type in the sidebar.")
    else:
        try:
            placeholder = st.empty()

            with placeholder.container():
                render_loader("📖 Reading your document...")
            text = extract_text(uploaded_file)

            with placeholder.container():
                render_loader("🧠 Generating questions with AI... this can take a moment")
            quiz = generate_questions(text, num_mcq, num_short)

            placeholder.empty()

            st.session_state.quiz = quiz
            st.session_state.source_filename = uploaded_file.name
            st.session_state.chars_processed = len(text)
            st.success("Quiz generated successfully!")

        except (UnsupportedFileError, EmptyDocumentError, QuestionGenerationError) as e:
            st.error(str(e))
        except Exception as e:
            st.error(f"Something went wrong: {e}")

# --- Results ---
if st.session_state.quiz is not None:
    quiz = st.session_state.quiz

    st.markdown("---")
    render_stats(
        len(quiz.mcqs),
        len(quiz.short_answers),
        st.session_state.chars_processed,
    )

    render_quiz(quiz)

    st.markdown("---")
    st.markdown("### 📥 Download this quiz")

    title = f"Quiz - {st.session_state.source_filename}"
    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            "⬇️ Download as Word (.docx)",
            data=build_docx(quiz, title=title),
            file_name="generated_quiz.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            use_container_width=True,
        )

    with col2:
        st.download_button(
            "⬇️ Download as PDF",
            data=build_pdf(quiz, title=title),
            file_name="generated_quiz.pdf",
            mime="application/pdf",
            use_container_width=True,
        )