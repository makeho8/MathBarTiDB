import streamlit as st

def run():
    st.subheader("📝 Quiz: Basics of Specialized Mathematics")
    st.write("Question 1: Is this topic interesting?")
    if st.button("Yes", key="specialized_math_q1_y"):
        st.success("Correct! +10 XP (Specialized Math)")
        if 'xp' not in st.session_state: 
            st.session_state.xp = 0
        st.session_state.xp["Specialized Math"] += 10
    if st.button("No", key="specialized_math_q1_n"):
        st.error("Wrong answer!")
