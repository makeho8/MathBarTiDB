import streamlit as st

def run():
    st.header("🎓 Discrete Math: FINAL EXAM")
    st.error("⚠️ This is the end of the program. Worth 500 XP.")
    
    st.write("**Q1: Eigenvalues**")
    st.write("If Av = 3v, what is the eigenvalue?")
    ans = st.number_input("Enter value:", step=1, key="fin_q1")
    
    if st.button("Finish Course"):
        if ans == 3:
            st.success("Correct! You have mastered Discrete Math. +500 XP")
            st.session_state.xp["Discrete Math"] += 500
        else:
            st.error("Incorrect.")