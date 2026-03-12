import streamlit as st
import materials.linear_algebra.quiz.q1_basics as q1

def display_quiz():
    quiz_map = {
        "Topic 1: Basics": q1
    }
    
    choice = st.selectbox("📝 Select Quiz:", list(quiz_map.keys()), key="linear_algebra_quiz")
    st.divider()
    quiz_map[choice].run()
