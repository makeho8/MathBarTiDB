import streamlit as st
import materials.calculus_single.content.ch1_intro as ch1

def display_content():
    st.sidebar.info("Select a Chapter below 👇")
    
    chapter_map = {
        "Chapter 1: Intro": ch1
    }
    
    choice = st.selectbox("📖 Select Chapter:", list(chapter_map.keys()), key="calculus_single_cont")
    st.divider()
    chapter_map[choice].run()
