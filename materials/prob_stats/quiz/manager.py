import streamlit as st
import materials.prob_stats.quiz.q1_basics as q1

def display_quiz():
    quiz_map = {
        "Topic 1: Basics": q1
    }
    
    choice = st.selectbox("📝 Select Quiz:", list(quiz_map.keys()), key="prob_stats_quiz")
    st.divider()
    quiz_map[choice].run()
