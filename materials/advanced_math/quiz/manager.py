import streamlit as st
import materials.advanced_math.quiz.q1_matrices as q1
import materials.advanced_math.quiz.q2_series as q2
import materials.advanced_math.quiz.q3_multivar as q3
import materials.advanced_math.quiz.q4_diffeq as q4

def display_quiz():
    st.sidebar.markdown("## 📝 Practice Quizzes")
    quiz_map = {
        "Topic 1: Matrices": q1,
        "Topic 2: Series": q2,
        "Topic 3: Multi-Var": q3,
        "Topic 4: Diff Eq": q4
    }
    choice = st.selectbox("Select Quiz:", list(quiz_map.keys()), key="adv_quiz_sel")
    st.divider()
    quiz_map[choice].run()