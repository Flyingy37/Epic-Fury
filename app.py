import streamlit as st
from pathlib import Path

base_dir = Path(__file__).parent
html_path = base_dir / "paste.txt"
student_file = base_dir / "תרגול_DATEDIF_משופר_למשתתפים.xlsx"
teacher_file = base_dir / "תרגול_DATEDIF_משופר_למרצה.xlsx"
logo_file = base_dir / "logo.gif"

page_icon_val = str(logo_file) if logo_file.exists() else None
st.set_page_config(page_title="תרגול DATEDIF", page_icon=page_icon_val, layout="wide")

st.markdown("""
<style>
html, body, [class*="css"] {
    direction: rtl;
    text-align: right;
}
.block-container {
    padding-top: 1.5rem;
}
.hero-box {
    background: linear-gradient(135deg, #fff7ed 0%, #ffffff 100%);
    border: 1px solid #fed7aa;
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.05);
}
.hero-title {
    font-size: 2.1rem;
    font-weight: 800;
    color: #374151;
    margin-bottom: 6px;
}
.hero-sub {
    color: #6b7280;
    font-size: 1.02rem;
    line-height: 1.7;
}
.card-box {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 16px;
    padding: 18px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.04);
}
.small-note {
    color: #6b7280;
    font-size: 0.92rem;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    if logo_file.exists():
        st.image(str(logo_file), use_container_width=True)
    st.markdown("### מגמת מידע ונתונים")
    st.caption("תרגול DATEDIF והורדת קבצים")
    st.divider()
    st.markdown("**ניווט מהיר**")
    st.markdown("- מצגת והסבר")
    st.markdown("- קבצי תרגול")
    st.markdown("- Google Sheet")

hero_col1, hero_col2 = st.columns([1, 3])
with hero_col1:
    if logo_file.exists():
        st.image(str(logo_file), width=230)
with hero_col2:
    st.markdown('<div class="hero-box">', unsafe_allow_html=True)
    st.markdown('<div class="hero-title">תרגול DATEDIF - מגמת מידע ונתונים</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">כל חומרי התרגול במקום אחד: מצגת ההסבר, קבצי העבודה להורדה וגישה ישירה אל גיליון Google Sheets.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

info_col1, info_col2, info_col3 = st.columns(3)
with info_col1:
    st.metric("קבצי תרגול", "2")
with info_col2:
    st.metric("תצוגות באפליקציה", "3")
with info_col3:
    st.metric("גישה לגיליון", "ישירה")

st.divider()

tab1, tab2, tab3 = st.tabs(["מצגת והסבר", "קבצי תרגול", "הטמעת Google Sheet"])

with tab1:
    st.subheader("מצגת והסבר")
    st.markdown('<div class="small-note">התוכן נטען מתוך הקובץ paste.txt ומוצג ישירות בתוך האפליקציה.</div>', unsafe_allow_html=True)
    if html_path.exists():
        html_text = html_path.read_text(encoding="utf-8", errors="ignore")
        st.components.v1.html(html_text, height=900, scrolling=True)
    else:
        st.error("paste.txt לא נמצא")

with tab2:
    st.subheader("קבצי תרגול להורדה")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.markdown("#### קובץ למשתתפים")
        st.markdown("גרסה לעבודה עצמאית במהלך התרגול.")
        if student_file.exists():
            st.download_button(
                label="הורדת קובץ משתתפים",
                data=student_file.read_bytes(),
                file_name=student_file.name,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )
        else:
            st.error("קובץ המשתתפים לא נמצא")
        st.markdown('</div>', unsafe_allow_html=True)
    with col_b:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.markdown("#### קובץ למרצה")
        st.markdown("גרסה הכוללת את הפתרון והנחיה להוראה.")
        if teacher_file.exists():
            st.download_button(
                label="הורדת קובץ מרצה",
                data=teacher_file.read_bytes(),
                file_name=teacher_file.name,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )
        else:
            st.error("קובץ המרצה לא נמצא")
        st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.subheader("Google Sheet")
    sheet_url = "https://docs.google.com/spreadsheets/d/1iGQU60BabjpVZbn7-P7expQ_c4C58vJSvBrriszExOw/edit?usp=sharing"
    embed_url = "https://docs.google.com/spreadsheets/d/1iGQU60BabjpVZbn7-P7expQ_c4C58vJSvBrriszExOw/preview"
    st.markdown("פתיחה ישירה של הגיליון:")
    st.code(sheet_url)
    st.components.v1.iframe(embed_url, height=720, scrolling=True)
    st.info("אם ההטמעה לא מוצגת, יש לוודא שההרשאה של הקובץ מוגדרת לצפייה באמצעות קישור.")
