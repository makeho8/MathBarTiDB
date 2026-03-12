import streamlit as st

def run():
    st.subheader("📝 Quiz: Basics of Discrete Mathematics")
    st.write("Question 1: Is this topic interesting?")
    if st.button("Yes", key="discrete_math_q1_y"):
        st.success("Correct! +10 XP (Discrete Math)")
        if 'xp' not in st.session_state: 
            st.session_state.xp = 0
        st.session_state.xp["Discrete Math"] += 10
    if st.button("No", key="discrete_math_q1_n"):
        st.error("Wrong answer!")
