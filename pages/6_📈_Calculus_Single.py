import streamlit as st

# --- IMPORT FROM YOUR MATERIALS FOLDER ---
import materials.calculus_single.content.manager as content_mgr
import materials.calculus_single.quiz.manager as quiz_mgr
import materials.calculus_single.slides.manager as slides_mgr

# --- PAGE SETUP ---
TOPIC_NAME = "Single-Variable Calculus"
TOPIC_ICON = "📈"

st.set_page_config(page_title=TOPIC_NAME, page_icon=TOPIC_ICON, layout="wide")
st.title(f"{TOPIC_ICON} {TOPIC_NAME}")

# --- THE 3 TABS ---
tab1, tab2, tab3 = st.tabs(["📚 Content", "📝 Practice", "👨‍🏫 Slides"])

with tab1:
    content_mgr.display_content()

with tab2:
    quiz_mgr.display_quiz()

with tab3:
    slides_mgr.display_slides()




