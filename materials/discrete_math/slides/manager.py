import streamlit as st
import materials.discrete_math.slides.s1_lecture as s1

def display_slides():
    slide_map = {
        "Lecture 1: Basics": s1
    }
    
    choice = st.selectbox("📽️ Select Lecture:", list(slide_map.keys()), key="discrete_math_slide")
    st.divider()
    slide_map[choice].run()
