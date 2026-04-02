import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.header("Chapter 4: Phương trình vi phân")
    st.write("Trọng tâm: Các phương trình tuyến tính bậc 2 với các hệ số hằng.")

    st.subheader("Phương trình vi phân tuyến tính (bậc 2, các hệ số hằng)")
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