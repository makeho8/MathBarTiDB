import streamlit as st
import materials.prob_stats.slides.s1_lecture as s1

def display_slides():
    slide_map = {
        "Lecture 1: Basics": s1
    }
    
    choice = st.selectbox("📽️ Select Lecture:", list(slide_map.keys()), key="prob_stats_slide")
    st.divider()
    slide_map[choice].run()
