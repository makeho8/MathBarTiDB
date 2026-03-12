import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def run():
    st.header("Chapter 1: Introduction to Probability & Statistics")
    st.write("Welcome to the first chapter of Probability & Statistics.")
    st.info("This is a placeholder. You can edit this file in 'materials/prob_stats/content/ch1_intro.py'")
    
    # Generic Graph
    st.subheader("Topic Visualization")
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    st.line_chart(y)
