import streamlit as st

def run():
    st.header("Chapter 2: The Matrix")
    st.write("A matrix is a rectangular array of numbers.")
    st.latex(r"A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}")
    st.warning("Don't confuse matrices with determinants!")