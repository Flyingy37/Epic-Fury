import streamlit as st
from pathlib import Path
import re

base_dir = Path(__file__).parent
html_path = base_dir / "paste.txt"

sheet_url = "https://docs.google.com/spreadsheets/d/1iGQU60BabjpVZbn7-P7expQ_c4C58vJSvBrriszExOw/edit?usp=sharing"
embed_url = "https://docs.google.com/spreadsheets/d/1iGQU60BabjpVZbn7-P7expQ_c4C58vJSvBrriszExOw/preview"

st.set_page_config(page_title="תרגול DATEDIF", layout="wide")

st.markdown("""
<style>
html, body, [class*="css"] {
    direction: rtl;
    text-align: right;
}

.block-container {
    max-width: 1240px;
    padding-top: 1.25rem;
    padding-bottom: 2rem;
}

.title-wrap {
    width: 100%;
    text-align: right;
    margin-bottom: 1rem;
}

.main-title {
    font-size: 2.6rem;
    font-weight: 800;
    color: #1f2937;
    line-height: 1.1;
    margin-bottom: 0.35rem;
}

.sub-title {
    font-size: 1.04rem;
    color: #6b7280;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 1.25rem;
}

.stTabs [data-baseweb="tab"] {
    font-size: 1.02rem;
}

iframe {
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="title-wrap">
    <div class="main-title">תרגול DATEDIF</div>
    <div class="sub-title">מצגת ההסבר וגישה ישירה לגיליון התרגול</div>
</div>
""", unsafe_allow_html=True)

presentation_tab, sheet_tab = st.tabs(["מצגת", "Google Sheet"])

with presentation_tab:
    if html_path.exists():
        html_text = html_path.read_text(encoding="utf-8", errors="ignore")
        html_text = re.sub(r'<img[^>]*alt="מגמת מידע ונתונים"[^>]*>', '', html_text, flags=re.IGNORECASE)
        html_text = re.sub(r'<img[^>]*alt="שאגת האריה"[^>]*>', '', html_text, flags=re.IGNORECASE)

        injected_css = """
        <style>
        html, body {
            direction: rtl !important;
            text-align: right !important;
            margin: 0 !important;
            padding: 0 !important;
            overflow-x: hidden !important;
        }

        header img {
            display: none !important;
        }

        header .flex.items-center.gap-3 {
            justify-content: flex-end !important;
            width: 100% !important;
        }

        header h1,
        header div,
        main,
        section,
        p,
        span,
        h2,
        h3 {
            text-align: right !important;
            direction: rtl !important;
        }

        .max-w-5xl {
            max-width: 96% !important;
        }

        nav#tab-nav {
            justify-content: flex-start !important;
        }
        </style>
        """

        st.components.v1.html(injected_css + html_text, height=930, scrolling=True)
    else:
        st.error("paste.txt לא נמצא")

with sheet_tab:
    st.link_button("פתיחת הגיליון ב-Google Sheets", sheet_url)
    st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)
    st.components.v1.iframe(embed_url, height=900, scrolling=True)
