import streamlit as st

def run():
    st.subheader("Quiz: Series")
    st.write("If limits of $|u_{n+1}/u_n| < 1$, the series...")
    if st.button("Converges"): 
        st.success("Correct! +10 XP (Advanced Math)"); 
        st.session_state.xp["Advanced Math"] += 10
    if st.button("Diverges"): 
        st.error("Incorrect.")