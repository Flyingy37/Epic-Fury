import streamlit as st
from pathlib import Path

base_dir = Path(__file__).parent
logo_png = base_dir / "logo.png"
logo_gif = base_dir / "logo.gif"
logo_file = logo_png if logo_png.exists() else logo_gif

sheet_url = "https://docs.google.com/spreadsheets/d/1iGQU60BabjpVZbn7-P7expQ_c4C58vJSvBrriszExOw/edit?usp=sharing"

st.set_page_config(page_title="תרגול DATEDIF", layout="centered")

st.markdown("""
<style>
html, body, [class*="css"] {
    direction: rtl;
    text-align: right;
}

.block-container {
    max-width: 800px;
    padding-top: 3rem;
}

.main-title {
    font-size: 2rem;
    font-weight: 700;
    color: #1f2937;
    margin-bottom: 0.5rem;
}

.sub-title {
    color: #6b7280;
    margin-bottom: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

if logo_file.exists():
    st.image(str(logo_file), width=180)

st.markdown('<div class="main-title">תרגול DATEDIF</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">גישה ישירה לגיליון התרגול</div>', unsafe_allow_html=True)

st.link_button("פתיחת הגיליון", sheet_url, use_container_width=True)
