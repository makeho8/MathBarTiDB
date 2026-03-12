import streamlit as st

def run():
    st.subheader("Quiz: Diff Eq")
    st.write("For $y'' - 3y' + 2y = 0$, what are the roots of $k^2 - 3k + 2 = 0$?")
    ans = st.radio("Roots:", ["1 and 2", "3 and 2", "0 and 0"], key="q4_diff")
    if st.button("Check", key="btn_q4"):
        if ans == "1 and 2": 
            st.success("Correct! +10 XP (Advanced Math)"); 
            st.session_state.xp["Advanced Math"] += 10
        else: st.error("Factorize the quadratic.")