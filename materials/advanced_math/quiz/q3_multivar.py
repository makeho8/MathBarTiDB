import streamlit as st

def run():
    st.subheader("Quiz: Partial Derivatives")
    st.latex(r"f(x,y) = x^2y. \quad \text{Find } \frac{\partial f}{\partial x}")
    ans = st.radio("Choose:", ["2xy", "x^2", "2x"], key="q3_multi")
    if st.button("Check", key="btn_q3"):
        if ans == "2xy": 
            st.success("Correct! +10 XP (Advanced Math)"); 
            st.session_state.xp["Advanced Math"] += 10
        else: st.error("Treat y as a constant number.")