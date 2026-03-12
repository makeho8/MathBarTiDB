import streamlit as st

def run():
    st.subheader("📝 Quiz: Vectors")
    st.write("Question 1: What is the magnitude of vector [3, 4]?")
    if st.button("Check Answer", key="q1_vec"):
        st.success("The answer is 5 (Pythagoras Theorem). +10 XP (Linear Algebra)")
        if 'xp' not in st.session_state: 
            st.session_state.xp = 0
        st.session_state.xp["Linear Algebra"] += 10