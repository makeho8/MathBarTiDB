import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.header("Chapter 4: Differential Equations")
    st.write("Focus: Second Order Linear Equations with Constant Coefficients.")

    st.subheader("Linear Diff Eq (Order 2, Constant Coeffs)")
    st.latex(r"y'' + py' + qy = 0")
    
    st.write("We solve the characteristic equation: $k^2 + pk + q = 0$.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Case 1: $\Delta > 0$**")
        st.latex(r"y = C_1 e^{k_1 x} + C_2 e^{k_2 x}")
    with col2:
        st.write("**Case 2: $\Delta < 0$ (Complex)**")
        st.latex(r"y = e^{\alpha x}(C_1 \cos \beta x + C_2 \sin \beta x)")
        
    st.success("Example from PDF: $y'' - 4y' + 3y = 3e^{2x}$")