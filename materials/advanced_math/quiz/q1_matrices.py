import streamlit as st
import numpy as np
import numpy.linalg as la
import pandas as pd
import matplotlib.pyplot as plt

def run():
    st.subheader("Quiz: Matrices")
    st.write("Calculate determinant of: [[2, 0], [0, 5]]")
    ans = st.number_input("Answer:", key="q1_mat")
    if st.button("Check", key="btn_q1"):
        if ans == 10: 
            st.success("Correct! +10 XP (Advanced Math)")
            st.session_state.xp["Advanced Math"] += 10
        else: st.error("Wrong.")