import streamlit as st
import materials.linear_algebra.content.ch1_intro as ch1

def display_content():
    st.sidebar.info("Select a Chapter below 👇")
    
    chapter_map = {
        "Chapter 1: Intro": ch1
    }
    
    choice = st.selectbox("📖 Select Chapter:", list(chapter_map.keys()), key="linear_algebra_cont")
    st.divider()
    chapter_map[choice].run()
