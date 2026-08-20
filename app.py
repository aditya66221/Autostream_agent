import streamlit as st
from agent import Agent

# ──────────────────────────────────────────────
# PAGE CONFIG
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="AutoStream AI",
    page_icon="🎥",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────
# GLOBAL STYLING (Apple / iOS Dark Glass Theme)
# ──────────────────────────────────────────────
st.markdown(
    """
<style>
/* ── Font Import ─────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* ── Base Theme Overrides ────────────────────── */
html, body, [data-testid="stAppViewContainer"],
[data-testid="stMain"], [data-testid="stMainBlockContainer"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    background-color: #0c0d12 !important;
    color: #e4e4e9 !important;
}

/* ── Hide Default Streamlit Chrome ───────────── */
#MainMenu, footer, [data-testid="stDecoration"], [data-testid="stStatusWidget"] {
    display: none !important;
}

header[data-testid="stHeader"] {
    background: transparent !important;
}

/* ── Custom Scrollbar ────────────────────────── */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}
::-webkit-scrollbar-track {
    background: transparent;
}
::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.12);
    border-radius: 999px;
}
::-webkit-scrollbar-thumb:hover {
    background: rgba(255, 255, 255, 0.2);
}

/* ── Main Container Spacing ──────────────────── */
[data-testid="stMainBlockContainer"] {
    max-width: 820px !important;
    padding-top: 1.2rem !important;
    padding-bottom: 7rem !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
}

/* ══════════════════════════════════════════════
   SIDEBAR STYLING
══════════════════════════════════════════════ */
[data-testid="stSidebar"] {
    background-color: rgba(14, 15, 22, 0.96) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
}
[data-testid="stSidebarContent"] {
    padding: 1.5rem 1rem !important;
}

.sb-header {
    display: flex;
    align-items: center;
    gap: 12px;
    padding-bottom: 1.25rem;
    margin-bottom: 1.25rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.07);
}
.sb-logo-box {
    width: 38px;
    height: 38px;
    border-radius: 10px;
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    box-shadow: 0 4px 14px rgba(99, 102, 241, 0.35);
}
.sb-title-group h2 {
    margin: 0;
    font-size: 16px;
    font-weight: 700;
    letter-spacing: -0.3px;
    color: #ffffff;
}
.sb-title-group p {
    margin: 0;
    font-size: 11px;
    color: rgba(255, 255, 255, 0.45);
}

.sb-section-label {
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: rgba(255, 255, 255, 0.35);
    margin: 1.2rem 0 0.6rem 0.2rem;
}

.sb-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 12px;
    padding: 14px;
    margin-bottom: 1rem;
}

.sb-meta-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 12px;
    padding: 6px 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.04);
}
.sb-meta-row:last-child {
    border-bottom: none;
    padding-bottom: 0;
}
.sb-meta-label {
    color: rgba(255, 255, 255, 0.45);
}
.sb-meta-val {
    color: #e2e8f0;
    font-weight: 500;
}
.sb-status-badge {
    background: rgba(16, 185, 129, 0.15);
    border: 1px solid rgba(16, 185, 129, 0.3);
    color: #34d399;
    font-size: 11px;
    font-weight: 500;
    padding: 2px 8px;
    border-radius: 6px;
}

/* Sidebar Button Styling */
[data-testid="stSidebar"] button {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 10px !important;
    color: #e2e8f0 !important;
    font-weight: 500 !important;
    font-size: 13px !important;
    padding: 0.55rem 1rem !important;
    transition: all 0.2s ease !important;
    width: 100% !important;
}
[data-testid="stSidebar"] button:hover {
    background: rgba(99, 102, 241, 0.15) !important;
    border-color: rgba(99, 102, 241, 0.4) !important;
    color: #c7d2fe !important;
    box-shadow: 0 4px 12px rgba(99, 102, 241, 0.15) !important;
}

/* ══════════════════════════════════════════════
   TOP HEADER
══════════════════════════════════════════════ */
.top-nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 20px;
    background: rgba(20, 21, 30, 0.7);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 18px;
    margin-bottom: 24px;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.35);
}
.nav-left {
    display: flex;
    align-items: center;
    gap: 12px;
}
.nav-icon {
    width: 36px;
    height: 36px;
    border-radius: 10px;
    background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    box-shadow: 0 2px 10px rgba(99, 102, 241, 0.3);
}
.nav-title {
    font-size: 15px;
    font-weight: 700;
    letter-spacing: -0.3px;
    color: #ffffff;
    margin: 0;
    line-height: 1.2;
}
.nav-subtitle {
    font-size: 11px;
    color: rgba(255, 255, 255, 0.42);
    margin: 0;
}
.online-pill {
    display: flex;
    align-items: center;
    gap: 6px;
    background: rgba(16, 185, 129, 0.1);
    border: 1px solid rgba(16, 185, 129, 0.25);
    border-radius: 20px;
    padding: 5px 12px;
    font-size: 11px;
    font-weight: 500;
    color: #34d399;
}
.online-dot {
    width: 6px;
    height: 6px;
    background: #34d399;
    border-radius: 50%;
    box-shadow: 0 0 8px rgba(52, 211, 153, 0.8);
    animation: statusPulse 2.5s infinite;
}
@keyframes statusPulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.4; transform: scale(0.9); }
}

/* ══════════════════════════════════════════════
   HERO / EMPTY STATE
══════════════════════════════════════════════ */
.hero-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 40px 16px 24px;
}
.hero-badge-icon {
    width: 64px;
    height: 64px;
    border-radius: 18px;
    background: linear-gradient(135deg, #6366f1 0%, #9333ea 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 30px;
    box-shadow: 0 8px 30px rgba(99, 102, 241, 0.35);
    margin-bottom: 20px;
}
.hero-heading {
    font-size: 28px;
    font-weight: 700;
    letter-spacing: -0.6px;
    color: #ffffff;
    margin: 0 0 8px 0;
}
.hero-heading span {
    background: linear-gradient(135deg, #818cf8 0%, #c084fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-desc {
    font-size: 13.5px;
    color: rgba(255, 255, 255, 0.45);
    max-width: 440px;
    line-height: 1.6;
    margin: 0 0 32px 0;
}
.hero-suggestions {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    width: 100%;
    max-width: 520px;
}
.suggestion-chip {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 12px;
    padding: 12px 16px;
    text-align: left;
    transition: all 0.2s ease;
    backdrop-filter: blur(10px);
}
.suggestion-chip:hover {
    background: rgba(99, 102, 241, 0.08);
    border-color: rgba(99, 102, 241, 0.3);
    transform: translateY(-1px);
}
.chip-emoji {
    font-size: 14px;
    margin-right: 6px;
}
.chip-title {
    font-size: 12.5px;
    font-weight: 500;
    color: rgba(255, 255, 255, 0.8);
}

/* ══════════════════════════════════════════════
   CHAT MESSAGES
══════════════════════════════════════════════ */
.chat-container {
    display: flex;
    flex-direction: column;
    gap: 16px;
    margin-bottom: 20px;
}

.msg-wrapper {
    display: flex;
    align-items: flex-end;
    gap: 10px;
    width: 100%;
}

.msg-user {
    justify-content: flex-end;
}

.msg-assistant {
    justify-content: flex-start;
}

.bot-avatar {
    width: 32px;
    height: 32px;
    border-radius: 9px;
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 15px;
    flex-shrink: 0;
    box-shadow: 0 2px 8px rgba(99, 102, 241, 0.3);
}

.bubble-content {
    max-width: 76%;
    padding: 12px 18px;
    font-size: 13.5px;
    line-height: 1.6;
    letter-spacing: -0.1px;
    word-break: break-word;
}

.user-bubble {
    background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
    color: #ffffff;
    border-radius: 18px 18px 4px 18px;
    box-shadow: 0 4px 16px rgba(99, 102, 241, 0.25);
    border: 1px solid rgba(255, 255, 255, 0.1);
}

.bot-bubble {
    background: rgba(255, 255, 255, 0.04);
    color: #eaeaf0;
    border-radius: 18px 18px 18px 4px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}

/* ══════════════════════════════════════════════
   FLOATING CHAT INPUT
══════════════════════════════════════════════ */
[data-testid="stChatInput"] {
    position: fixed !important;
    bottom: 24px !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    width: 100% !important;
    max-width: 820px !important;
    padding: 0 1.5rem !important;
    z-index: 99999 !important;
    background: transparent !important;
}

[data-testid="stChatInputContainer"] {
    background: rgba(22, 23, 34, 0.75) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 18px !important;
    backdrop-filter: blur(24px) !important;
    -webkit-backdrop-filter: blur(24px) !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
    transition: all 0.25s ease !important;
    padding: 4px 6px !important;
}

[data-testid="stChatInputContainer"]:focus-within {
    border-color: rgba(99, 102, 241, 0.6) !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6), 0 0 0 3px rgba(99, 102, 241, 0.2), inset 0 1px 0 rgba(255, 255, 255, 0.15) !important;
}

[data-testid="stChatInputContainer"] textarea {
    color: #f1f5f9 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 13.5px !important;
}

[data-testid="stChatInputContainer"] textarea::placeholder {
    color: rgba(255, 255, 255, 0.3) !important;
}

[data-testid="stChatInputSubmitButton"] {
    background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
    border-radius: 12px !important;
    color: white !important;
    transition: transform 0.15s ease, opacity 0.15s ease !important;
}

[data-testid="stChatInputSubmitButton"]:hover {
    transform: scale(1.05) !important;
    opacity: 0.95 !important;
}

@media (max-width: 768px) {
    .hero-suggestions {
        grid-template-columns: 1fr;
    }
    .bubble-content {
        max-width: 88%;
    }
}
</style>
""",
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────
# STATE INITIALIZATION (Preserved exactly)
# ──────────────────────────────────────────────
if "bot" not in st.session_state:
    st.session_state.bot = Agent()

if "chat" not in st.session_state:
    st.session_state.chat = []

# ──────────────────────────────────────────────
# SIDEBAR
# ──────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        """
<div class="sb-header">
    <div class="sb-logo-box">🎥</div>
    <div class="sb-title-group">
        <h2>AutoStream</h2>
        <p>AI Video Assistant</p>
    </div>
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown('<div class="sb-section-label">Session</div>', unsafe_allow_html=True)
    if st.button("＋ New Conversation", use_container_width=True):
        st.session_state.bot = Agent()
        st.session_state.chat = []
        st.rerun()

    total_msgs = len(st.session_state.chat)
    exchanges = total_msgs // 2

    st.markdown('<div class="sb-section-label">Information</div>', unsafe_allow_html=True)
    st.markdown(
        f"""
<div class="sb-card">
    <div class="sb-meta-row">
        <span class="sb-meta-label">Total Messages</span>
        <span class="sb-meta-val">{total_msgs}</span>
    </div>
    <div class="sb-meta-row">
        <span class="sb-meta-label">Exchanges</span>
        <span class="sb-meta-val">{exchanges}</span>
    </div>
    <div class="sb-meta-row">
        <span class="sb-meta-label">AI Model</span>
        <span class="sb-meta-val">GPT-OSS 20B</span>
    </div>
    <div class="sb-meta-row">
        <span class="sb-meta-label">Knowledge Base</span>
        <span class="sb-status-badge">● Online</span>
    </div>
</div>
""",
        unsafe_allow_html=True,
    )

# ──────────────────────────────────────────────
# TOP HEADER
# ──────────────────────────────────────────────
st.markdown(
    """
<div class="top-nav">
    <div class="nav-left">
        <div class="nav-icon">🎥</div>
        <div>
            <div class="nav-title">AutoStream</div>
            <div class="nav-subtitle">AI Video Assistant</div>
        </div>
    </div>
    <div class="online-pill">
        <div class="online-dot"></div>
        <span>AI Online</span>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────
# HERO / EMPTY STATE vs CONVERSATION VIEW
# ──────────────────────────────────────────────
if not st.session_state.chat:
    st.markdown(
        """
<div class="hero-wrapper">
    <div class="hero-badge-icon">🎥</div>
    <h1 class="hero-heading">AutoStream <span>AI</span></h1>
    <p class="hero-desc">
        Your intelligent video workflow assistant. Ask about pricing, features, supported platforms, or get started with AutoStream.
    </p>
    <div class="hero-suggestions">
        <div class="suggestion-chip">
            <span class="chip-emoji">💳</span>
            <span class="chip-title">View pricing</span>
        </div>
        <div class="suggestion-chip">
            <span class="chip-emoji">✨</span>
            <span class="chip-title">What features do you offer?</span>
        </div>
        <div class="suggestion-chip">
            <span class="chip-emoji">🚀</span>
            <span class="chip-title">I want to get started</span>
        </div>
        <div class="suggestion-chip">
            <span class="chip-emoji">📱</span>
            <span class="chip-title">What platforms are supported?</span>
        </div>
    </div>
</div>
""",
        unsafe_allow_html=True,
    )
else:
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for sender, message in st.session_state.chat:
        safe_message = (
            message.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace("\n", "<br>")
        )

        if sender == "You":
            st.markdown(
                f"""
<div class="msg-wrapper msg-user">
    <div class="bubble-content user-bubble">{safe_message}</div>
</div>
""",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
<div class="msg-wrapper msg-assistant">
    <div class="bot-avatar">🎥</div>
    <div class="bubble-content bot-bubble">{safe_message}</div>
</div>
""",
                unsafe_allow_html=True,
            )
    st.markdown("</div>", unsafe_allow_html=True)

# ──────────────────────────────────────────────
# CHAT INPUT & HANDLER (Preserved exactly)
# ──────────────────────────────────────────────
user_input = st.chat_input("Ask AutoStream something...")

if user_input:
    response = st.session_state.bot.handle_input(user_input)

    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Bot", response))

    st.rerun()