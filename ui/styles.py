CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;1,600;1,700&family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* --- Doodle background --- */
.stApp {
    background-color: #f4f7e8;
    background-image:
        radial-gradient(circle at 10% 20%, rgba(103, 6, 38, 0.06) 0px, transparent 40px),
        radial-gradient(circle at 80% 15%, rgba(186, 215, 151, 0.5) 0px, transparent 50px),
        radial-gradient(circle at 60% 70%, rgba(103, 6, 38, 0.05) 0px, transparent 45px),
        radial-gradient(circle at 25% 85%, rgba(186, 215, 151, 0.5) 0px, transparent 40px),
        radial-gradient(circle at 90% 60%, rgba(103, 6, 38, 0.05) 0px, transparent 35px),
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160' viewBox='0 0 160 160'%3E%3Cg fill='none' stroke='%23670626' stroke-width='2' stroke-linecap='round' opacity='0.10'%3E%3Cpath d='M20 30 Q30 10 45 25 T70 20'/%3E%3Ccircle cx='120' cy='40' r='6'/%3E%3Cpath d='M100 100 q10 -15 20 0 q10 15 20 0'/%3E%3Cpath d='M30 120 l10 10 m-10 0 l10 -10'/%3E%3Ccircle cx='140' cy='130' r='4'/%3E%3Cpath d='M60 140 Q75 125 90 140'/%3E%3Ccircle cx='15' cy='90' r='3'/%3E%3C/g%3E%3C/svg%3E");
    background-repeat: repeat;
    background-size: auto, auto, auto, auto, auto, 160px 160px;
}

/* --- Hero header --- */
.hero-container {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem 1rem;
    animation: fadeInDown 0.8s ease-out;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-weight: 700;
    font-size: 3rem;
    color: #670626;
    margin-bottom: 0.3rem;
}

.hero-subtitle {
    font-size: 1.05rem;
    color: #4a5a38;
    font-weight: 500;
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
    background: #ffffff;
    border: 1px solid rgba(103, 6, 38, 0.12);
    border-radius: 14px;
    padding: 0;
    margin-bottom: 1.2rem;
    overflow: hidden;
    animation: fadeInUp 0.5s ease-out backwards;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    box-shadow: 0 2px 10px rgba(103, 6, 38, 0.05);
}

.question-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 24px rgba(103, 6, 38, 0.15);
}

.card-strip-mcq {
    background: #670626;
    padding: 0.9rem 1.4rem 0.7rem 1.4rem;
}

.card-strip-short {
    background: #bad797;
    padding: 0.9rem 1.4rem 0.7rem 1.4rem;
}

.card-body {
    padding: 1.1rem 1.4rem 1.3rem 1.4rem;
}

.question-badge {
    display: inline-block;
    padding: 0.15rem 0.6rem;
    border-radius: 999px;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

.badge-mcq {
    background: rgba(255, 255, 255, 0.15);
    color: #f2d9df;
}

.badge-short {
    background: rgba(103, 6, 38, 0.12);
    color: #670626;
}

.question-text-mcq {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-weight: 600;
    font-size: 1.15rem;
    color: #fdf6f8;
}

.question-text-short {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-weight: 600;
    font-size: 1.15rem;
    color: #4a1220;
}

.option-row {
    padding: 0.5rem 0.9rem;
    border-radius: 8px;
    margin-bottom: 0.4rem;
    background: #f7f4ea;
    border: 1px solid rgba(103, 6, 38, 0.08);
    font-size: 0.93rem;
    color: #3a3a2f;
}

.correct-answer-box {
    margin-top: 0.8rem;
    padding: 0.6rem 0.9rem;
    border-radius: 8px;
    background: rgba(186, 215, 151, 0.35);
    border-left: 3px solid #6b8f4e;
    font-size: 0.9rem;
    color: #33421f;
}

.explanation-box {
    margin-top: 0.5rem;
    padding: 0.5rem 0.9rem;
    border-radius: 8px;
    background: #f7f4ea;
    font-size: 0.85rem;
    color: #6b6b5c;
    font-style: italic;
}

/* --- Stat pills --- */
.stat-pill {
    display: inline-block;
    padding: 0.5rem 1.1rem;
    border-radius: 999px;
    background: #fdf6f8;
    border: 1px solid rgba(103, 6, 38, 0.2);
    color: #670626;
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
    background: #670626;
    color: #fdf6f8;
}

.stButton>button:hover, .stDownloadButton>button:hover {
    transform: translateY(-1px);
    background: #7d0a30;
    box-shadow: 0 6px 18px rgba(103, 6, 38, 0.3);
}

/* --- Sidebar --- */
section[data-testid="stSidebar"] {
    background: #670626;
    border-right: 1px solid rgba(103, 6, 38, 0.4);
}

section[data-testid="stSidebar"] * {
    color: #fdf6f8 !important;
}

section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] .stMarkdown p {
    font-family: 'Playfair Display', serif;
}

/* Slider track and handle */
section[data-testid="stSidebar"] [data-baseweb="slider"] div[role="slider"] {
    background-color: #bad797 !important;
    border-color: #bad797 !important;
}

section[data-testid="stSidebar"] [data-testid="stTickBarMin"],
section[data-testid="stSidebar"] [data-testid="stTickBarMax"] {
    color: #f2d9df !important;
}

/* Slider filled track */
section[data-testid="stSidebar"] div[data-baseweb="slider"] > div > div {
    background: #bad797 !important;
}
</style>
"""


def question_card_delay(index: int) -> str:
    delay = min(index * 0.08, 0.6)
    return f"animation-delay: {delay}s;"