import streamlit as st
import matplotlib.pyplot as plt

def run():
    st.header("Chapter 1: Introduction to Vectors")
    st.write("A vector is an object that has both a magnitude and a direction.")
    st.info("Imagine an arrow pointing in space.")
    
    # Chapter 1 specific graph
    st.write("### Vector Visualization")
    fig, ax = plt.subplots()
    ax.arrow(0, 0, 2, 3, head_width=0.3, color='blue')
    ax.set_xlim(-1, 5); ax.set_ylim(-1, 5)
    st.pyplot(fig)