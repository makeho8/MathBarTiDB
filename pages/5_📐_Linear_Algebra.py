import streamlit as st

# --- IMPORTS (THE 3 MANAGERS) ---
import materials.linear_algebra.content.manager as content_mgr
import materials.linear_algebra.quiz.manager as quiz_mgr
import materials.linear_algebra.slides.manager as slides_mgr

# --- PAGE SETUP ---
TOPIC_NAME = "Linear Algebra"
TOPIC_ICON = "📐"

st.set_page_config(page_title=TOPIC_NAME, page_icon=TOPIC_ICON, layout="wide")
st.title(f"{TOPIC_ICON} {TOPIC_NAME}")

# --- THE 3 TABS ---
tab1, tab2, tab3 = st.tabs(["📚 Content", "📝 Practice", "👨‍🏫 Slides"])

with tab1:
    # The Content Manager handles the chapters
    content_mgr.display_content()

with tab2:
    # The Quiz Manager handles the topics
    quiz_mgr.display_quiz()

with tab3:
    # The Slide Manager handles the lectures
    slides_mgr.display_slides()