import streamlit as st
import numpy as np
import numpy.linalg as la
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def run():
    st.header("Chapter 1: Determinants, Matrices, Systems")

    st.markdown("---")
    st.subheader("Part 1. Determinants")

    with st.expander("ℹ️. Concept of Matrices"):
        st.latex(r'''
            \textbf{A} = [a_{ij}]_{m \times n} = \begin{bmatrix}
            a_{11} & a_{12} & \ldots & a_{1n} \\
            a_{21} & a_{22} & \ldots & a_{2n} \\
            \vdots & \vdots & \ddots & \vdots \\
            a_{m1} & a_{m2} & \ldots & a_{mn}
            \end{bmatrix}
            ''')
        st.latex(r'''
            \textbf{A} = [a_{ij}]_{m \times n} = \begin{bmatrix}
            a_{11} & a_{12} & \ldots & a_{1n} \\
            a_{21} & a_{22} & \ldots & a_{2n} \\
            \vdots & \vdots & \ddots & \vdots \\
            a_{m1} & a_{m2} & \ldots & a_{mn}
            \end{bmatrix}
            ''')
        st.markdown(r'''
            * The set of all $m \times n$ matrices is denoted by $\mathcal{M}_{m \times n}$
            * The set of all square matrices of oder $n$ is denoted by $\mathcal{M}_n$
            * Zero matrix $\textbf{0} = [0]_{m \times n}$
            * $\textbf{A} = [a_{ij}]_{m \times n} = \textbf{B} = [b_{ij}]_{m \times n} \Leftrightarrow a_{ij} = b_{ij}$ for all $i = \overline{1, m};\; j = \overline{1, m}$
            ''')
        st.markdown(r''' *Example:*
            $$\textbf{A} = \begin{bmatrix}
            1 & 2 & 3 \\
            2 & 3 & 4 \\
            1 & 5 & 7
            \end{bmatrix}$$
            $$\textbf{B} = \begin{bmatrix}
            1 & 1 & 1 \\
            0 & 1 & 1 \\
            0 & 0 & 1
            \end{bmatrix}$$
            ''')


    with st.expander("ℹ️ℹ️. Definition of Determinant"):
        st.markdown('''
            The determinant of a **square** matrix is the *sum* of all terms
            (each term is the product of elements
            (taking exactly one element from each row and one element from each column)).
            ''')
        st.markdown(r"$A \in M_n$")
        st.latex(r"\det A := |A| = a_{i1}A_{i1} + a_{i2}A_{i2} + \cdots + a_{in}A_{in}; \rightarrow i \text{ row }")
        st.latex(r"\det A := |A| = a_{1i}A_{1i} + a_{2i}A_{2i} + \cdots + a_{ni}A_{ni}; \rightarrow i \text{ column }")
        st.markdown(r"$A_{ij} = (-1)^{i+j}M_{ij}$")
        st.write('''**Example:** For a 2x2 matrix,
        the determinant is $ad - bc$.''')
        c1, c2 = st.columns(2)
        with c1:
            a1 = st.number_input("a1", value=2)
            b1 = st.number_input("b1", value=1)
        with c2:
            a2 = st.number_input("a2", value=5)
            b2 = st.number_input("b2", value=3)
        B = np.array([[a1,a2],
                      [b1,b2]])
        detB = la.det(B)
        st.metric("Determinant", detB)

    with st.expander("ℹ️ℹ️ℹ️. Determinant of a 3x3 square matrix (Sarrus' rule)"):
        st.markdown('''
        * Copy the first 2 columns to the rigth side of the matrix
        * Sum of (products of elements on diagonals from top-left to bottom-rigth)
        * Subtract (products of elements on diagonal from top-rigth to bottom-left)''')
        st.markdown(r''' **Example:** For a 3x3 matrix:''')
        st.latex(r'''\begin{bmatrix}
        a_{11} & a_{12} & a_{13} \\
        b_{11} & b_{12} & b_{13} \\
        c_{11} & c_{12} & c_{13} \end{bmatrix} \begin{matrix}
        a_{11} & a_{12}  \\
        b_{11} & b_{12}  \\
        c_{11} & c_{12} \end{matrix}''')
        c1, c2, c3 = st.columns(3)
        with c1:
            a11 = st.number_input("a11", value=2)
            b11 = st.number_input("b11", value=1)
            c11 = st.number_input("c11", value=1)
        with c2:
            a12 = st.number_input("a12", value=5)
            b12 = st.number_input("b12", value=3)
            c12 = st.number_input("c12", value=1)
        with c3:
            a13 = st.number_input("a13", value=5)
            b13 = st.number_input("b13", value=3)
            c13 = st.number_input("c13", value=1)
        A = np.array([[a11,a12,a13],
                      [b11,b12,b13],
                      [c11,c12,c13]])
        detA = la.det(A)
        st.metric("Determinant", detA)

    with st.expander("ℹ️✋🏻. Properties of determinants"):
        st.markdown(r'''
        * Swapping two rows of a matrix changes the sign of the determinant. (1)
        * The determinant is linear with respect to each row. (2)
        * From (1) and (2) $\Rightarrow$ if a matrix has two proportional rows, its determinant is 0. (3)
        * Adding a linear compination of other rows to one row does not change the determinant. (4)
        * $\det \textbf{A}^t = \det \textbf{A}$. (5) $\Rightarrow$ the properties of determinant that hold for rows also hold for columns and vice versa.
        * The determinant of any linear dependent system of vectors is 0. (6)
        * For square matrices $\textbf{A, B}$ of the same oder, we always have $\det (\textbf{AB}) = \det \textbf{A} \cdot \det \textbf{B}$. (7)
        ''')

    with st.expander("✋🏻. Calculating determinant using elementary operations"):
        st.markdown(r"""
        * Use row operations to transform matrix $A$ into matrix $U$ (upper triangular matrix).
        * The determinant of matrix $U$ is the product of the elements on its main diagonal.
        * $\det(A) = (-1)^k \times$ (product of the elements on the main diagonal of $U$).
        + $k$ is the number of row swaps.
        + If a row is multiplied by $\alpha$, we must divide the determinant by $\alpha$.
        + Adding a multiple of one row to another row does not change the determinant.
        + $\begin{bmatrix}
    	    a_{11}  & a_{12} & a_{13} \\
            0       & a_{22} & a_{23} \\
            0       & 0      & a_{33}
    	    \end{bmatrix}$
        """)

    st.markdown("---")
    st.subheader("Part 2. Matrices")

    with st.expander("ℹ️. Matrix operations"):
        st.markdown(r"""
        * $[a_{ij}]_{m \times n} + [b_{ij}]_{m \times n} = [a_{ij} + b_{ij}]_{m \times n}$
        * $k[a_{ij}]_{m \times n} = [ka_{ij}]_{m \times n}$
        * $[a_{ij}]_{m \times p} [b_{ij}]_{p \times n} = [c_{ij}]_{m \times n}$ with $c_{ij} = \sum_{k = 1}^p a_{ik}b_{kj}$ (row $i$ of $\textbf{A}$ times column $j$ of $\textbf{B}$).
        * $\textbf{I}_n \in \mathcal{M}_n$, for all $\textbf{A}_{m \times n} \in \mathcal{M}_{m \times n}$ we have $\textbf{I}_m \textbf{A}_{m \times n} = \textbf{A}_{m \times n} = \textbf{A}_{m \times n}\textbf{I}_n$
        * If $\textbf{A} = [a_{ij}]_{m \times n}$ then its transpose is $\textbf{A}^t = [a_{ji}]_{n \times m}$
        """)

    with st.expander("ℹ️ℹ️. Inverse matrix"):
        st.markdown(r"""
        * A square matrix $\textbf{A}$ is called **invertible** is there exists a square matrix $\textbf{B}$ of the same order such that $\textbf{AB = BA = I}$. If $\textbf{B}$ exists, it is unique and called the inverse of $\textbf{A}$, denoted as $\textbf{A}^{-1}$.
        * $\textbf{A}$ is invertible if and only if $\det \textbf{A} \neq 0$
        * $\textbf{A}^{-1} = \frac{1}{\det \textbf{A}} \textbf{C}^t$, where $\textbf{C} = [A_{ij}]_{n \times n}$, and $A_{ij}$ is the **cofactor** of $a_{ij}$, $\textbf{C}$ is called the adjugate matrix of $\textbf{A}$.
        """)
        st.info("Finding the inverse matrix using the Gauss-Jordan method (elementary row operations)")
        st.markdown(r"""
        * Write the identity matrix $\textbf{I}$ of the same order to the rigth of $\textbf{A}$: $\textbf{A}|\; \textbf{I}$
        * Perform elementary row operations simutaneouly on $\textbf{A}|\; \textbf{I}$ to transform $\textbf{A}$ into the identity matrix.
        * When the left side becomes identity matrix, the right side is $\textbf{A}^{-1}$;
        * $$\textbf{A}|\; \textbf{I} \to \ldots \ldots \to \textbf{I}|\; \textbf{A}^{-1}$$
        """)

    with st.expander("ℹ️ℹ️ℹ️. Rank of a matrix"):
        st.markdown(r"""
        - Suppose $\textbf{A} = [a_{ij}]_{m \times n}$, if there exists a non-zero sub-determinant (minor) of order $p$ and all sub-determinant of order $p + 1$ are zero, then $r(A) = p$.
        - **Finding the rank using elementary operations:**
        - Use elementary row operations to transform the matrix into row echelon form. The rank is the number of non-zero rows.
        """)
        with st.expander("🧮 View rank calculation algorithm in Python"):
            st.write("In practice, we use the `numpy` library for high-speed computation:")
            st.code("""
            import numpy as np

            A = np.array([
                [1, 2, 1, 1],
                [2, 4, 2, 2],
                [3, 6, 3, 15]
                ])

                rank = np.linalg.matrix_rank(A)
                print(f"The rank of the matrix is: {rank}")
                """, language='python')

            # Direct result illustration
            A = np.array([[1, 2, 1, 1], [2, 4, 2, 2], [3, 6, 3, 15]])
            st.warning(f"Calculation result: r(A) = {np.linalg.matrix_rank(A)}")

    st.markdown("---")
    st.subheader("Part 3. Systems of linear equations")

    with st.expander("ℹ️. Concept of linear systems"):
        #Definition, examples
        with st.expander("🥱 Definition and examples"):
            st.markdown(r"""
            **General form of $m$ equations with $n$ variables**
            $\begin{cases}
            a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1 \\
            a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2 \\
            \ldots  \\
            a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m
            \end{cases}$
            where $x_1, \ldots , x_n$ are the $n$ variables, $a_{ij}$ is the coefficient of the $j$-th variable in the $i$-th equation, and $b_i$ is the right-hand side of the $i$-th equation; $i = 1, \ldots , m; \; j =
            1, \ldots , n$.
            """)
            st.info("Examples")
            # Create three columns for the examples
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(r"**$3 \times 3$ system:**")
                st.latex(r"""
                \begin{cases}
                    9x_1 + x_2 + 4x_3 = 1 \\
                    2x_1 + 2x_2 + 3x_3 = 5 \\
                    7x_1 + x_2 + 6x_3 = 7
                \end{cases}
                """)
            with col2:
                st.markdown(r"**$3 \times 4$ system:**")
                st.latex(r"""
                \begin{cases}
                    9x_1 + x_2 + 4x_3 + x_4 = 1 \\
                    2x_1 + 2x_2 + 3x_3 + x_4 = 5 \\
                    7x_1 + x_2 + 6x_3 + x_4 = 7
                \end{cases}
                """)
            with col3:
                st.markdown(r"**$4 \times 3$ system:**")
                st.latex(r"""
                \begin{cases}
                    9x_1 + x_2 + 4x_3 = 1 \\
                    2x_1 + 2x_2 + 3x_3 = 5 \\
                    7x_1 + x_2 + 6x_3 = 7 \\
                    x_1 + x_2 + x_3 = 3
                \end{cases}
                """)

        # Matrix reprecentation
        with st.expander("#### 🧮 Matrix representation of systems of lilear equations"):
            # Display matrix definitions A, b, x
            st.latex(r"""
            \textbf{A} = \begin{bmatrix}
                a_{11} & a_{12} & \ldots & a_{1n} \\
                a_{21} & a_{22} & \ldots & a_{2n} \\
                \vdots & \vdots & \ddots & \vdots \\
                a_{m1} & a_{m2} & \ldots & a_{mn}
            \end{bmatrix},\;
            \textbf{b} = \begin{bmatrix}
                b_1 \\
                b_2 \\
                \vdots \\
                b_m
            \end{bmatrix},\;
            \textbf{x} = \begin{bmatrix}
                x_1 \\
                x_2 \\
                \vdots \\
                x_n
            \end{bmatrix}
            """)
            # compact matrix equation
            st.markdown("Then, the system of equations can be written compactly as:")
            st.latex(r"\textbf{Ax} = \textbf{b}")

        #Vector representation
        with st.expander("#### 🏹 Vector representation of systems of linear equations"):
            st.markdown(r"""
            If we denote the $j$-th column vector of the matrix as $\textbf{v}_j = (a_{1j},\ldots, a_{mj})^T \in \mathbb{R}^m$
            and the rigth-hand side vector as $\textbf{b} = (b_1, \ldots, b_m)^T \in \mathbb{R}^m$,
            then the general system of linear equations can be written as:
            """)
            # Linear combination equation
            st.latex(r"x_1\textbf{v}_1 + x_2\textbf{v}_2 + \cdots + x_n\textbf{v}_n = \textbf{b}")
            st.info("💡 **Meaning:** Solving a system of linear equations is essentially finding away to 'blend' (linearly combine) the column vectors of matrix $A$ with proportions $x_i$ to obtain the resultant vector $b$.")

        with st.expander("#### 🏹 Visualizing linear combinations"):
            # 1. Input data
            c1, c2 = st.columns(2)
            with c1:
                v1 = [st.number_input("v1_x", value=1.0), st.number_input("v1_y", value=2.0)]
            with c2:
                v2 = [st.number_input("v2_x", value=3.0), st.number_input("v2_y", value=1.0)]
            x1 = st.slider("Coefficient x1", -5.0, 5.0, 1.0)
            x2 = st.slider("Coefficient x2", -5.0, 5.0, 1.0)
            # Calculate resultant vector b = x1*v1 + x2*v2
            b = [x1*v1[0] + x2*v2[0], x1*v1[1] + x2*v2[1]]
            # 2. create plot
            fig = go.Figure()
            # Function to draw vectors using annotations
            def draw_vector(x, y, name, color):
                fig.add_annotation(
                    x=x, y=y,
                    ax=0, ay=0,
                    xref='x', yref='y',
                    axref='x', ayref='y',
                    text='', # No text at the arrowhead
                    showarrow=True,
                    arrowhead=3,
                    arrowsize=1,
                    arrowwidth=3,
                    arrowcolor=color )
                # Add an invisible trace to show the legend
                fig.add_trace(go.Scatter(
                    x=[x], y=[y],
                    name=name,
                    mode='markers',
                    marker=dict(color=color, size=0),)) # Size=0 to hide the marker
            # Draw vectors
            draw_vector(v1[0]*x1, v1[1]*x1, f"{x1}*v1 (Blue)", "blue")
            draw_vector(v2[0]*x2, v2[1]*x2, f"{x2}*v2 (Green)", "green")
            draw_vector(b[0], b[1], "Vector b (Red)", "red")
            # Configure layout
            limit = 10
            fig.update_layout(
                xaxis=dict(range=[-limit, limit], zeroline=True, zerolinewidth=2, zerolinecolor='black'),
                yaxis=dict(range=[-limit, limit], zeroline=True, zerolinewidth=2, zerolinecolor='black'),
                width=600, height=600,
                title="Illustration: x1*v1 + x2*v2 = b")
            if st.checkbox("Show Parallelogram Rule"):
                # Draw dashed line from x1*v1 to b
                fig.add_trace(go.Scatter(
                    x=[v1[0]*x1, b[0]], y=[v1[1]*x1, b[1]],
                    mode='lines', line=dict(dash='dash', color='gray'),
                    showlegend=False
                ))
                # Draw dashed line from x2*v2 to b
                fig.add_trace(go.Scatter(
                    x=[v2[0]*x2, b[0]], y=[v2[1]*x2, b[1]],
                    mode='lines', line=dict(dash='dash', color='gray'),
                    showlegend=False
                ))
            st.plotly_chart(fig)

    # II) Cramer system
    with st.expander("ℹ️ℹ️. Cramer's system"):
        # concept
        with st.expander("🟰 Concept "):
            st.markdown(r"""
            **Cramer's system** is a square system of linear equations ($n \times n$)
            where the coefficient matrix $\textbf{A}$ is non-singular ($\det \textbf{A} \neq 0$).

            > **Theorem:** Every Cramer's system has unique solution.
             """)
            st.latex(r"x_1\textbf{v}_1 + x_2\textbf{v}_2 + \cdots + x_n\textbf{v}_n = \textbf{b}")
            st.markdown("The solution of the system is calculated using the fomula:")
            st.latex(r"x_i = \frac{D_i}{D}, \quad i = 1,\ldots, n")
            st.markdown("**Where:**")
            st.latex(r"""
            \begin{aligned}
                D = \det A = \det(v_1, \ldots, v_i, \ldots, v_n) \\
                D_i = \det(v_1, \ldots, b, \ldots, v_n)
            \end{aligned}
            """)
            st.info("""💡 **Explanation:** $D_i$ is the determinant of the matrix obtained by replacing
                        the $i$-th column of matrix $A$ with the right-hand side column vector $b$.""")

        # Small-scale experiment
        with st.expander("🧮 Experiment with a 2x2 system"):
            st.write("Solve the system: $ax + by = e$ and $cx + dy = f$")

            col1, col2 = st.columns(2)
            with col1:
                a = st.number_input("a", value=1)
                b = st.number_input("b", value=2)
                e = st.number_input("e (right-hand side 1)", value=5)
            with col2:
                c = st.number_input("c", value=3)
                d = st.number_input("d", value=4)
                f = st.number_input("f (right-hand side 2)", value=11)
            D = a*d - b*c
            if D != 0:
                D1 = e*d - b*f
                D2 = a*f - e*c
                st.info(f"D = {D}, D1 = {D1}, D2 = {D2}")
                st.latex(rf"x = \frac{{{D1}}}{{{D}}} = {D1/D}, \quad y = \frac{{{D2}}}{{{D}}} = {D2/D}")
            else:
                st.error("D = 0: This is not a Cramer's system!")

        # 2. Illustrative example
        with st.expander("📚 Illustrative example (3x3 system)"):
            st.latex(r"""
            \begin{cases}
                9x_1 + x_2 + 4x_3 = 1 \\
                2x_1 + 2x_2 + 3x_3 = 5 \\
                7x_1 + x_2 + 6x_3 = 7
            \end{cases}
            """)
            st.info("Try solving this system using Cramer's method!")

        # Kronecker-Kapelli
        with st.expander("©️. Rouche-Kapelli theorem"):
            st.markdown(r"""
            A general system of linear equations $\textbf{Ax} = \textbf{b}$ has a solution if and only if the rank of coefficient matrix equals the rank of the augmented matrix:
            """)
            st.latex(r"r(\textbf{A}) = r(\widetilde{\textbf{A}})")
            st.info(r"📝 View augmented matrix structure $\widetilde{\textbf{A}}$")
            st.markdown(r"The augmented matrix is created by appending the right-hand side column vector $\textbf{b}$ to the right of matrix $\textbf{A}$:")
            st.latex(r"""
                \widetilde{\textbf{A}} = \left[ \begin{array}{ccc|c}
                a_{11} & \ldots & a_{1n} & b_1 \\
                \vdots & \ddots & \vdots & \vdots \\
                a_{m1} & \ldots & a_{mn} & b_m
                \end{array} \right]
            """)
            st.warning("📊 Analyzing the number of solutions")
            st.markdown("Suppose the system has $n$ variables:")
            # Inconsistent case
            st.success(r"1. **Inconsistent (No solution):** if $r(\textbf{A}) < r(\widetilde{\textbf{A}})$")
            # Consistent case
            st.error(r"2. **Consistent (Has solution):** if $r(\textbf{A}) = r(\widetilde{\textbf{A}}) = r$")
            st.write("    * If $r = n$: The system has **unique solution**.")
            st.write("    * If $r < n$: The system has **infinitely many solutions** (depending on $n-r$ free variables).")

    # III Homogeneous linear systems
    with st.expander("ℹ️ℹ️ℹ️. Homogeneous linear systems"):
        st.latex(r'''
        \textbf{A} = \begin{bmatrix}
	    a_{11} & a_{12} & \ldots & a_{1n} \\
        a_{21} & a_{22} & \ldots & a_{2n} \\
        \vdots & \vdots & \ddots & \vdots \\
        a_{m1} & a_{m2} & \ldots & a_{mn}
        \end{bmatrix},\; \textbf{b} = \begin{bmatrix}
            0 \\
            0 \\
            \vdots \\
            0
        \end{bmatrix},\; \textbf{x} = \begin{bmatrix}
            x_1 \\
            x_2 \\
            \vdots \\
            x_n
        \end{bmatrix}
    \textbf{Ax} = \textbf{0}
                 ''')
        st.write(r"For a homogeneous Cramer system, there is only the unique trivial solution $x_i = 0, \forall i = 1,\ldots, n$.")

    # IV Solving systems using the Gauss method
    with st.expander("ℹ️✋🏻. Solving systems of linear equation using Gaussian elimination method"):
        st.markdown("""
        Perform the following elementary row operations on the equations:
        - Swap the positions of two equations;
        - Multiply or divide both sides of an equations by a non-zero number;
        - Add a linear combination of other equations to an equation.\\
        To transform the given system into an equivalent system where the augmented matrix is in row echelon form.
                    """)
        st.latex(r"""
        \begin{bmatrix}
        a_{11} & a_{12} & \ldots & a_{1p} &\ldots& | & b_1 \\
        0      & a_{22} & \ldots & a_{2p} &\ldots& | & b_2 \\
        \ddots & \ddots & \ddots & \ddots &\ldots& | & \vdots \\
        0      & 0      & \ldots & a_{pp} &\ldots& | & b_p
        \end{bmatrix}
        """)

