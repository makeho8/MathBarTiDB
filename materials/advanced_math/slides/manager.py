import streamlit as st
import materials.advanced_math.slides.s1_matrices as s1
import materials.advanced_math.slides.s2_series as s2
import materials.advanced_math.slides.s3_multivar as s3
import materials.advanced_math.slides.s4_diffeq as s4

def display_slides():
    st.sidebar.markdown("## 📽️ Lecture Slides")
    slide_map = {
        "L1: Matrices": s1,
        "L2: Series": s2,
        "L3: Multi-Var": s3,
        "L4: Diff Eq": s4
    }
    choice = st.selectbox("Select Slide Deck:", list(slide_map.keys()), key="adv_slide_sel")
    st.divider()
    slide_map[choice].run()