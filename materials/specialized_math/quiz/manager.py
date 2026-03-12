import streamlit as st
import materials.specialized_math.quiz.q1_basics as q1

def display_quiz():
    quiz_map = {
        "Topic 1: Basics": q1
    }
    
    choice = st.selectbox("📝 Select Quiz:", list(quiz_map.keys()), key="specialized_math_quiz")
    st.divider()
    quiz_map[choice].run()
