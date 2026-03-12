import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def run():
    st.header("Chapter 1: Introduction to Discrete Mathematics")
    st.write("Welcome to the first chapter of Discrete Mathematics.")
    st.info("This is a placeholder. You can edit this file in 'materials/discrete_math/content/ch1_intro.py'")
    
    # Generic Graph
    st.subheader("Topic Visualization")
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    st.line_chart(y)
