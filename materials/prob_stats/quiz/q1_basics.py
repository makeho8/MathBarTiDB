import streamlit as st

def run():
    st.subheader("📝 Quiz: Basics of Probability & Statistics")
    st.write("Question 1: Is this topic interesting?")
    if st.button("Yes", key="prob_stats_q1_y"):
        st.success("Correct! +10 XP (Prob & Stats)")
        if 'xp' not in st.session_state: 
            st.session_state.xp = 0
        st.session_state.xp["Prob & Stats"] += 10
    if st.button("No", key="prob_stats_q1_n"):
        st.error("Wrong answer!")
