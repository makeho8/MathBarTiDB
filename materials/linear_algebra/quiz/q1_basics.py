import streamlit as st

def run():
    st.subheader("📝 Quiz: Basics of Linear Algebra")
    st.write("Question 1: Is this topic interesting?")
    if st.button("Yes", key="linear_algebra_q1_y"):
        st.success("Correct! +10 XP (Linear Algebra)")
        if 'xp' not in st.session_state: 
            st.session_state.xp = 0
        st.session_state.xp["Linear Algebra"] += 10
    if st.button("No", key="linear_algebra_q1_n"):
        st.error("Wrong answer!")
