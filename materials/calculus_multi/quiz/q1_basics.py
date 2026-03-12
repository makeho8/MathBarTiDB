import streamlit as st

def run():
    st.subheader("📝 Quiz: Basics of Multi-Variable Calculus")
    st.write("Question 1: Is this topic interesting?")
    if st.button("Yes", key="calculus_multi_q1_y"):
        st.success("Correct! +10 XP (Calculus 2)")
        if 'xp' not in st.session_state: 
            st.session_state.xp = 0
        st.session_state.xp["Calculus 2"] += 10
    if st.button("No", key="calculus_multi_q1_n"):
        st.error("Wrong answer!")
