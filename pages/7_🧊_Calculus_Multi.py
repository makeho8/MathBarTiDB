import streamlit as st

# --- IMPORT FROM YOUR MATERIALS FOLDER ---
# Change this import for each of your 7 pages
import materials.calculus_multi.content.manager as content_mgr
import materials.calculus_multi.quiz.manager as quiz_mgr
import materials.calculus_multi.slides.manager as slides_mgr

# --- PAGE SETUP ---
TOPIC_NAME = "Multi-Variable Calculus"
TOPIC_ICON = "🧊"

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





