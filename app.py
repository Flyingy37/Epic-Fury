import streamlit as st
from pathlib import Path

base_dir = Path(__file__).parent
html_path = base_dir / "paste.txt"
logo_png = base_dir / "logo.png"
logo_gif = base_dir / "logo.gif"
logo_file = logo_png if logo_png.exists() else logo_gif

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
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.main-title {
    font-size: 2.2rem;
    font-weight: 700;
    color: #1f2937;
    margin-bottom: 0.4rem;
}

.sub-title {
    font-size: 1.02rem;
    color: #6b7280;
    margin-bottom: 1.5rem;
}

iframe {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

top_col1, top_col2 = st.columns([4, 1])

with top_col1:
    st.markdown('<div class="main-title">תרגול DATEDIF</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">מצגת ההסבר וגישה ישירה לגיליון התרגול</div>', unsafe_allow_html=True)

with top_col2:
    if logo_file.exists():
        st.image(str(logo_file), width=170)

tab1, tab2 = st.tabs(["מצגת", "Google Sheet"])

with tab1:
    if html_path.exists():
        html_text = html_path.read_text(encoding="utf-8", errors="ignore")
        st.components.v1.html(html_text, height=900, scrolling=True)
    else:
        st.error("paste.txt לא נמצא")

with tab2:
    st.link_button("פתיחת הגיליון ב-Google Sheets", sheet_url, use_container_width=True)
    st.markdown("### תצוגת הגיליון")
    st.components.v1.iframe(embed_url, height=850, scrolling=True)
