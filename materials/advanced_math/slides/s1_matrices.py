import streamlit as st
import numpy as np
import numpy.linalg as la
import pandas as pd
import matplotlib.pyplot as plt

def run():
    def slide_1():
        st.header("👋 Subject Introduction")
        st.write("### Welcome to Class!")
        st.write("Content in detail:")
        st.info("Chapter 1: Determinant, Matrix, Equations")
        st.warning("Chapter 2: Series Theory")
        st.info("Chapter 3: Multi-Variable Funtions")
        st.warning("Chương 4: Differentiation equation")
        
    def slide_2():
        st.header("🛑 Chapter 1: Determinant, Matrix, Equations")
        st.subheader("Part 1. Determinant")
        st.info("#### I. Matrix Deffinition")
        st.latex(r'''
        \textbf{A} = [a_{ij}]_{m \times n} = \begin{bmatrix}
        a_{11} & a_{12} & \ldots & a_{1n} \\
        a_{21} & a_{22} & \ldots & a_{2n} \\
        \vdots & \vdots & \ddots & \vdots \\
        a_{m1} & a_{m2} & \ldots & a_{mn}
        \end{bmatrix}
        ''')
        st.markdown(r"""
        ##### 📋 Some keys
        * Set of all matrices size $m \times n$ : $\mathcal{M}_{m \times n}$
        * Set of all square matrices size $n$ : $\mathcal{M}_n$
        * Zero matric $\mathbf{0} = [0]_{m \times n}$
        * $\textbf{A} = [a_{ij}]_{m \times n} = \textbf{B} = [b_{ij}]_{m \times n} \Leftrightarrow a_{ij} = b_{ij}$ for all $i = \overline{1, m};\; j = \overline{1, n}$
        """)
        
    def slide_3():
        st.header("🛑 Chapter 1: Determinant, Matrix, Equations")
        st.subheader("Part 1. Determinant")
        st.info("#### I. Matrix Deffinition")
        st.latex(r'''
        \textbf{A} = [a_{ij}]_{3 \times 4} = \begin{bmatrix}
        1 & 2 & 3 & 4 \\
        2 & a_{22} & a_{23} & a_{24} \\
        3 & a_{32} & a_{33} & a_{34} 
        \end{bmatrix}
        ''')
        st.latex(r'''
        \textbf{B} = [b_{ij}]_{4 \times 3} = \begin{bmatrix}
        1 & 2 & 3 & \\
        2 & a_{22} & a_{23} \\
        3 & a_{32} & a_{33} \\
        4 & a_{42} & a_{43}
        \end{bmatrix}
        ''')
        
    def slide_4():
        st.header("🛑 Chapter 1: Determinant, Matrix, Equations")
        st.subheader("Part 1. Determinant")
        st.info("#### II. Determinant Deffinition")
        st.markdown('''
            * The Determinant of a matrix is a special number that can be
            calculated from square matrices
            * What is the Determinant used for?
            - The determinant helps us find the inverse matrix (which we
            will cover later)
            - The Determinant will give us useful information when dealing
            with Systems of Linear Equations (which we will cover later)
            - Used in advanced Control Engineering theory
            ''')
        st.markdown(r"$A \in M_n$")
        st.latex(r"\det A := |A| = a_{i1}A_{i1} + a_{i2}A_{i2} + \cdots + a_{in}A_{in}; \rightarrow i \text{ row }")
        st.latex(r"\det A := |A| = a_{1i}A_{1i} + a_{2i}A_{2i} + \cdots + a_{ni}A_{ni}; \rightarrow i \text{ column }")
        st.markdown(r"$A_{ij} = (-1)^{i+j}M_{ij}$")
        
    def slide_5():
        st.header("🛑 Chapter 1: Determinant, Matrix, Equations")
        st.subheader("Part 1. Determinant")
        st.info("#### II. Determinant Deffinition")
        st.write("**Ex:** Matrix size 2x2: determinant $(a1*b2) - (a2*b1)$.")
        st.latex(r'''
            \begin{bmatrix}
            2 & 3 \\
            4 & 5
            \end{bmatrix}
                ''')
        B = np.array([[2,3],
                      [4,5]])
        detB = la.det(B)
        st.metric("Determinant", detB)
        
    def slide_6():
        st.header("🛑 Chapter 1: Determinant, Matrix, Equations")
        st.subheader("Part 1. Determinant")
        st.info("#### III. Start rule")
        st.markdown(r"""
        * Imagine copying the first two columns and placing them to the right of the matrix.
        * Multiply the diagonals going from top-left to bottom-right (Add these).
        * Multiply the diagonals going from top-right to bottom-left (Subtract these).
        """)
        st.write("**Ex:** Matrix size 3x3.")
    
        st.latex(r'''
            \begin{bmatrix}
            2 & 3 & 4 \\
            5 & 6 & 7 \\
            8 & 9 & 10
            \end{bmatrix}
                ''')
        
        A = np.array([[2,3,4],
                      [5,6,7],
                      [8,9,10]])
        detA = la.det(A)
        st.metric("Determinant", detA)
    
    def slide_7():
        st.header("🛑 Chapter 1: Determinant, Matrix, Equations")
        st.subheader("Part 1. Determinant")
        st.info("#### IV. Properties of Determinant")
        st.markdown(r"""
        + Swapping 2 rows reverses the sign.
        + Linear property per row.
        + Proportional rows => determinant is 0.
        + Adding linear combination of rows => determinant unchanged.
        + $\det(A^T) = \det(A)$.
        + Linearly dependent vectors => determinant is 0.
        + $\det(AB) = \det(A)\det(B)$.
        """)
    
    def slide_8():
        st.header("🛑 Chapter 1: Determinant, Matrix, Equations")
        st.subheader("Part 1. Determinant")
        st.info("#### V. Determinant by elementary row operations")

        st.latex(r"""
        \text{If $A$ is upper triangular matrix:}\\
        \det(A) = (-1)^k \cdot \prod a_{ii}.\\
        k \text{ is number of row swaps.}\\
        \begin{bmatrix}
	    a_{11}  & a_{12} & a_{13} \\
        0       & a_{22} & a_{23} \\
        0       & 0      & a_{33}
	    \end{bmatrix}
        """)

    def slide_9():
        st.header("🛑 Chapter 1: Determinant, Matrix, Equations")
        st.subheader("Part 2. Matrix")
        st.info("#### I. Matrix Calculators")
        st.markdown(r"""
        * $[a_{ij}]_{m \times n} + [b_{ij}]_{m \times n} = [a_{ij} + b_{ij}]_{m \times n}$
        * $k[a_{ij}]_{m \times n} = [ka_{ij}]_{m \times n}$
        * $[a_{ij}]_{m \times p} [b_{ij}]_{p \times n} = [c_{ij}]_{m \times n}$; $c_{ij} = \sum_{k = 1}^p a_{ik}b_{kj}$ (row $i$ of $\textbf{A}$ multiply column $j$ of $\textbf{B}$).
        * $\textbf{I}_n \in \mathcal{M}_n$, for all $\textbf{A}_{m \times n} \in \mathcal{M}_{m \times n}$ we have $\textbf{I}_m \textbf{A}_{m \times n} = \textbf{A}_{m \times n} = \textbf{A}_{m \times n}\textbf{I}_n$
        * If $\textbf{A} = [a_{ij}]_{m \times n}$ then $\textbf{A}^t = [a_{ji}]_{n \times m}$
        """)

    def slide_10():
        st.header("🛑 Chapter 1: Determinant, Matrix, Equations")
        st.subheader("Part 2. Matrix")
        st.info("#### II. Inverse Matrix")
        st.markdown(r"""
        * Square matrix **A** called **inverse** if there is the same size square matrix **B** such that $\textbf{AB = BA = I}$. If $\exists \textbf{B}$ then $\textbf{B}$ is unique and we call $\textbf{B}$ the inverse of $\textbf{A}$, denoted $\textbf{A}^{-1}$.
        * $\textbf{A}$ is invertible if and only if $\det \textbf{A} \neq 0$ 
        * $\textbf{A}^{-1} = \frac{1}{\det \textbf{A}} \textbf{C}^t$, with $\textbf{C} = [A_{ij}]_{n \times n}$, $A_{ij}$ is **algebraic complement** of $a_{ij}$, $\textbf{C}$ is called the **adjugate matrix** of $\textbf{A}$.
        """)
            
    def slide_end():
        st.header("🏁 Class Dismissed")
        st.write("### Homework:")
        st.write("1. Complete the Quiz on Page 5")
        st.write("2. Join the Leaderboard")
        st.balloons()
    # List of your slides in order
    slides = [ slide_1, slide_2, slide_3, slide_4, slide_5, slide_6, slide_7, slide_8, slide_9, slide_10, slide_end ]

    # 3. NAVIGATION LOGIC
    if 'slide_index' not in st.session_state:
        st.session_state.slide_index = 0

    # --- 3. NAVIGATION & RESOURCES (Sidebar) ---
    with st.sidebar:
        st.title("🔧 Controls")
        # A. NAVIGATION
        st.subheader("Jump to Slide")
        slide_names = [f"Slide {i+1}" for i in range(len(slides))]
        selected_slide = st.radio("Go to:", range(len(slides)), format_func=lambda x: slide_names[x], index=st.session_state.slide_index)

        if selected_slide != st.session_state.slide_index:
            st.session_state.slide_index = selected_slide
            st.rerun()
    
        st.divider()
        # B. DIGITAL LIBRARY (Multiple Books)
        st.subheader("📚 Digital Library")
    
        # 1. DEFINE YOUR BOOKS HERE
        # Format: "Button Name": "ExactFilename.pdf"
        book_list = {
            "📘 Advanced Math Slide": "SlideToanCaoCap.pdf",
            "📕 Specialized Math Slide": "SlideToanChuyenDe.pdf",
            "📗 Formula Cheat Sheet": "formulas.pdf",
            "📄 Homework Set 1": "homework1.pdf"
        }

        # 2. GENERATE BUTTONS AUTOMATICALLY
        for display_name, file_name in book_list.items():
            try:
                with open(file_name, "rb") as pdf_file:
                    st.download_button(
                        label=display_name,
                        data=pdf_file,
                        file_name=file_name,
                        mime="application/pdf",
                        use_container_width=True
                    )
            except FileNotFoundError:
                # If you haven't uploaded the file yet, we show a helpful error
                st.warning(f"⚠️ Missing file: {file_name}")

        st.divider()

        # C. PRINT INSTRUCTIONS
        with st.expander("🖨️ How to Print Slides"):
            st.write("1. Press **Ctrl + P**.")
            st.write("2. Select **'Save as PDF'**.")
            st.write("3. Click **Save**.")
        
    # 4. RENDER THE CURRENT SLIDE
    # Create a container for the slide content
    with st.container():
        st.markdown("---") # Top line
        # CALL THE FUNCTION FOR THE CURRENT SLIDE
        slides[st.session_state.slide_index]()
        st.markdown("---") # Bottom line
    # 5. FOOTER BUTTONS (Prev / Next)
    col1, col2, col3 = st.columns([1, 4, 1])

    with col1:
        if st.button("⬅️ Previous"):
            if st.session_state.slide_index > 0:
                st.session_state.slide_index -= 1
                st.rerun()

    with col2:
        # Display "Slide X of Y" in the center
        st.markdown(f"<div style='text-align: center; color: gray;'>Slide {st.session_state.slide_index + 1} of {len(slides)}</div>", unsafe_allow_html=True)

    with col3:
        if st.button("Next ➡️"):
            if st.session_state.slide_index < len(slides) - 1:
                st.session_state.slide_index += 1
                st.rerun()
        

    