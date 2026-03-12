import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def run():
    st.header("Chapter 3: Functions of Several Variables")
    st.write("Focus: Partial Derivatives and 3D Surfaces.")
    
    st.write("Functions like $z = f(x, y)$ map pairs of (x,y) to a height z, creating surfaces.")
    
    st.subheader("Partial Derivatives")
    st.latex(r"\frac{\partial z}{\partial x} \quad \text{and} \quad \frac{\partial z}{\partial y}")
    st.write("Treat one variable as a constant while differentiating the other.")

    # 3D Surface Visualization
    st.subheader("Interactive 3D Surface")
    func_type = st.selectbox("Choose Function:", ["Paraboloid (Bowl)", "Saddle (Hyperbolic)", "Sin Wave"])
    
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    
    if func_type == "Paraboloid (Bowl)":
        Z = X**2 + Y**2
    elif func_type == "Saddle (Hyperbolic)":
        Z = X**2 - Y**2
    else:
        Z = np.sin(np.sqrt(X**2 + Y**2))
        
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    surf = ax.plot_surface(X, Y, Z, cmap=cm.viridis, alpha=0.8)
    fig.colorbar(surf)
    st.pyplot(fig)