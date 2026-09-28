CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* --- Animated gradient header --- */
.hero-container {
    text-align: center;
    padding: 2.5rem 1rem 2rem 1rem;
    animation: fadeInDown 0.8s ease-out;
}

.hero-title {
    font-family: 'Poppins', sans-serif;
    font-weight: 700;
    font-size: 2.8rem;
    background: linear-gradient(270deg, #6366f1, #8b5cf6, #ec4899, #6366f1);
    background-size: 800% 800%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: gradientShift 6s ease infinite;
    margin-bottom: 0.3rem;
}

.hero-subtitle {
    font-size: 1.05rem;
    color: #9ca3af;
    font-weight: 500;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}

/* --- Question cards --- */
.question-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 1.3rem 1.5rem;
    margin-bottom: 1rem;
    animation: fadeInUp 0.5s ease-out backwards;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.question-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.15);
}

.question-badge {
    display: inline-block;
    padding: 0.2rem 0.7rem;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.03em;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
}

.badge-mcq {
    background: rgba(99, 102, 241, 0.15);
    color: #a5b4fc;
}

.badge-short {
    background: rgba(236, 72, 153, 0.15);
    color: #f9a8d4;
}

.question-text {
    font-weight: 600;
    font-size: 1.02rem;
    margin-bottom: 0.6rem;
    color: #f3f4f6;
}

.option-row {
    padding: 0.45rem 0.8rem;
    border-radius: 8px;
    margin-bottom: 0.35rem;
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.06);
    font-size: 0.93rem;
}

.correct-answer-box {
    margin-top: 0.7rem;
    padding: 0.6rem 0.9rem;
    border-radius: 8px;
    background: rgba(34, 197, 94, 0.1);
    border-left: 3px solid #22c55e;
    font-size: 0.9rem;
}

.explanation-box {
    margin-top: 0.4rem;
    padding: 0.5rem 0.9rem;
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.02);
    font-size: 0.85rem;
    color: #9ca3af;
    font-style: italic;
}

/* --- Stat pills --- */
.stat-pill {
    display: inline-block;
    padding: 0.5rem 1.1rem;
    border-radius: 999px;
    background: linear-gradient(135deg, rgba(99,102,241,0.15), rgba(236,72,153,0.15));
    border: 1px solid rgba(139, 92, 246, 0.25);
    font-weight: 600;
    font-size: 0.9rem;
    margin-right: 0.6rem;
    animation: fadeInUp 0.5s ease-out;
}

/* --- Buttons --- */
.stButton>button, .stDownloadButton>button {
    border-radius: 10px;
    font-weight: 600;
    transition: all 0.25s ease;
    border: none;
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: white;
}

.stButton>button:hover, .stDownloadButton>button:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 18px rgba(99, 102, 241, 0.35);
}

/* --- Sidebar --- */
section[data-testid="stSidebar"] {
    border-right: 1px solid rgba(255,255,255,0.06);
}
</style>
"""


def question_card_delay(index: int) -> str:
    delay = min(index * 0.08, 0.6)
    return f"animation-delay: {delay}s;"