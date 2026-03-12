import streamlit as st
import numpy as np
import numpy.linalg as la
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def run():
    st.header("Chương 1: Định thức, Ma trận, Hệ PTTT")

    st.markdown("---")
    st.subheader("Phần 1. Định thức")

    with st.expander("ℹ️. Khái niệm về ma trận"):
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
            * Tập hợp tất cả các ma trận cỡ $m \times n$ được ký hiệu $\mathcal{M}_{m \times n}$
            * Tập hợp tất cả các ma trận vuông cấp $n$ được ký hiệu $\mathcal{M}_n$
            * Ma trận không $\textbf{0} = [0]_{m \times n}$
            * $\textbf{A} = [a_{ij}]_{m \times n} = \textbf{B} = [b_{ij}]_{m \times n} \Leftrightarrow a_{ij} = b_{ij}$ với mọi $i = \overline{1, m};\; j = \overline{1, m}$
            ''')
        st.markdown(r''' *Ví dụ:*
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


    with st.expander("ℹ️ℹ️. Định nghĩa định thức"):
        st.markdown('''
            Định thức của một ma trận **vuông** bằng *Tổng* của tất cả
            các số hạng (mỗi số hạng là tích của các phần tử
            (mỗi hàng lấy 1 phần tử mỗi cột lấy một phần tử)).
            ''')
        st.markdown(r"$A \in M_n$")
        st.latex(r"\det A := |A| = a_{i1}A_{i1} + a_{i2}A_{i2} + \cdots + a_{in}A_{in}; \rightarrow i \text{ row }")
        st.latex(r"\det A := |A| = a_{1i}A_{1i} + a_{2i}A_{2i} + \cdots + a_{ni}A_{ni}; \rightarrow i \text{ column }")
        st.markdown(r"$A_{ij} = (-1)^{i+j}M_{ij}$")
        st.write('''**Ví dụ:** Cho một ma trận cỡ 2x2,
        định thức là $ad - bc$.''')
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
        st.metric("Định thức", detB)

    with st.expander("ℹ️ℹ️ℹ️. Định thức của ma trận vuông cấp 3 (quy tắc hình sao)"):
        st.markdown('''
        * Sao chép 2 cột đầu tiên vào bên phải ma trận
        * Tổng của (tích các phần tử trên đường chéo trên-trái tới dưới phải)
        * Trừ đi (tích các phần tử trên đường chéo trên-phải tới dưới-trái)''')
        st.markdown(r''' **Ví dụ:** Cho một ma trận cỡ 3x3:''')
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
        st.metric("Định thức", detA)

    with st.expander("ℹ️✋🏻. Các tính chất của định thức"):
        st.markdown(r'''
        * Đổi chỗ 2 hàng của ma trận thì định thức đổi dấu. (1)
        * Định thức có tính chất tuyến tính đối với mỗi hàng. (2)
        * Từ (1) và (2) $\Rightarrow$ ma trận có 2 hàng tỷ lệ thì định thức bằng 0. (3)
        * (Một hàng) + (tổ hợp tuyến tính các hàng khác) thì định thức không thay đổi. (4)
        * $\det \textbf{A}^t = \det \textbf{A}$. (5) $\Rightarrow$ các tính chất của định thức đúng với hàng thì cũng đúng với cột và ngược lại.
        * Định thức của mọi hệ vector phụ thuộc tuyến tính đều bằng 0. (6)
        * Với $\textbf{A, B}$ vuông cùng cấp, luôn có $\det (\textbf{AB}) = \det \textbf{A} \cdot \det \textbf{B}$. (7)
        ''')

    with st.expander("✋🏻. Cách tính định thức bằng biến đổi sơ cấp"):
        st.markdown(r"""
        * Sử dụng các phép toán theo hàng để chuyển ma trận $A$ thành ma trận $U$ (ma trận tam giác trên).
        * Định thức của ma trận $U$ là tích của các phần tử trên đường chéo chính của $U$.
        * $\det(A) = (-1)^k \times$ (tích các phần tử trên đường chéo chính của $U$).
        + $k$ là số lần hoán đổi hàng.
        + Nếu hàng được nhân với $\alpha$, chia kết quả cho $\alpha$.
        + Thêm bội của hàng vào hàng khác không thay đổi định thức.
        + $\begin{bmatrix}
    	    a_{11}  & a_{12} & a_{13} \\
            0       & a_{22} & a_{23} \\
            0       & 0      & a_{33}
    	    \end{bmatrix}$
        """)

    st.markdown("---")
    st.subheader("Phần 2. Ma trận")

    with st.expander("ℹ️. Các phép toán trên ma trận"):
        st.markdown(r"""
        * $[a_{ij}]_{m \times n} + [b_{ij}]_{m \times n} = [a_{ij} + b_{ij}]_{m \times n}$
        * $k[a_{ij}]_{m \times n} = [ka_{ij}]_{m \times n}$
        * $[a_{ij}]_{m \times p} [b_{ij}]_{p \times n} = [c_{ij}]_{m \times n}$ với $c_{ij} = \sum_{k = 1}^p a_{ik}b_{kj}$ (hàng $i$ của $\textbf{A}$ nhân cột $j$ của $\textbf{B}$).
        * $\textbf{I}_n \in \mathcal{M}_n$, với mọi $\textbf{A}_{m \times n} \in \mathcal{M}_{m \times n}$ ta có $\textbf{I}_m \textbf{A}_{m \times n} = \textbf{A}_{m \times n} = \textbf{A}_{m \times n}\textbf{I}_n$
        * Với $\textbf{A} = [a_{ij}]_{m \times n}$ thì $\textbf{A}^t = [a_{ji}]_{n \times m}$
        """)

    with st.expander("ℹ️ℹ️. Ma trận nghịch đảo"):
        st.markdown(r"""
        * Ma trận vuông $\textbf{A}$ dgl **khả nghịch** nếu tồn tại ma trận vuông cùng cấp $\textbf{B}$ sao cho $\textbf{AB = BA = I}$. Nếu $\exists \textbf{ ma trận B}$ thì duy nhất và ta gọi là ma trận nghịc đảo của $\textbf{A}$, ký hiệu $\textbf{A}^{-1}$.
        * $\textbf{A}$ khả nghịch khi và chỉ khi $\det \textbf{A} \neq 0$
        * $\textbf{A}^{-1} = \frac{1}{\det \textbf{A}} \textbf{C}^t$, với $\textbf{C} = [A_{ij}]_{n \times n}$, trong đó $A_{ij}$ là **phần bù đại số** của $a_{ij}$, $\textbf{C}$ được gọi là ma trận phụ hợp của $\textbf{A}$.
        """)
        st.info("Tìm ma trận nghịch đảo bằng phương pháp Gauss-Jordan (hay biến đổi sơ cấp)")
        st.markdown(r"""
        * Viết ma trận đơn vị cùng cấp $\textbf{I}$ bên phải ma trận $\textbf{A}$: $\textbf{A}|\; \textbf{I}$
        * Thực hiện các phép biến đổi sơ cấp đồng thời lên các hàng của $\textbf{A}|\; \textbf{I}$ để đưa $\textbf{A}$ về ma trận đơn vị.
        * Khi vế trái trở thành ma trận đơn vị thì vế phải là $\textbf{A}^{-1}$;
        * $$\textbf{A}|\; \textbf{I} \to \ldots \ldots \to \textbf{I}|\; \textbf{A}^{-1}$$
        """)

    with st.expander("ℹ️ℹ️ℹ️. Hạng của ma trận"):
        st.markdown(r"""
        - Giả sử $\textbf{A} = [a_{ij}]_{m \times n}$, nếu có định thức con cấp $p$ khác 0 và mọi định thức con cấp $p + 1$ đều bằng 0 thì $r(A) = p$.
        - **Tìm hạng của ma trận theo phương pháp biến đổi sơ cấp:**
        - Dùng các phép biến đổi sơ cấp về hàng, đưa ma trận về dạng bậc thang, hạng của ma trận là số hàng khác $\textbf{0}$.
        """)
        with st.expander("🧮 Xem giải thuật tìm hạng bằng Python"):
            st.write("Trong thực tế, ta dùng thư viện `numpy` để tính toán cực nhanh:")
            st.code("""
            import numpy as np

            A = np.array([
                [1, 2, 1, 1],
                [2, 4, 2, 2],
                [3, 6, 3, 15]
                ])

                rank = np.linalg.matrix_rank(A)
                print(f"Hạng của ma trận là: {rank}")
                """, language='python')

            # Minh họa kết quả trực tiếp
            A = np.array([[1, 2, 1, 1], [2, 4, 2, 2], [3, 6, 3, 15]])
            st.warning(f"Kết quả tính toán: r(A) = {np.linalg.matrix_rank(A)}")

    st.markdown("---")
    st.subheader("Phần 3. Hệ PTTT")

    with st.expander("ℹ️. Khái niệm HPT-TT"):
        #Định nghĩa, ví dụ
        with st.expander("🥱 Định nghĩa và ví dụ"):
            st.markdown(r"""
            **Dạng tổng quát $m$ phương trình $n$ ẩn**
            $\begin{cases}
            a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1 \\
            a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2 \\
            \ldots  \\
            a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m
            \end{cases}$
            trong đó $x_1, \ldots , x_n$ là $n$ ẩn, $a_{ij}$ là hệ số của ẩn thứ $j$ trong phương trình thứ $i$, $b_i$ là vế phải của phương trình thứ $i$; $i = 1, \ldots , m; \; j =
            1, \ldots , n$.
            """)
            st.info("Ví dụ về Hệ phương trình tuyến tính")
            # Create three columns for the examples
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(r"**Hệ $3 \times 3$:**")
                st.latex(r"""
                \begin{cases}
                    9x_1 + x_2 + 4x_3 = 1 \\
                    2x_1 + 2x_2 + 3x_3 = 5 \\
                    7x_1 + x_2 + 6x_3 = 7
                \end{cases}
                """)
            with col2:
                st.markdown(r"**Hệ $3 \times 4$:**")
                st.latex(r"""
                \begin{cases}
                    9x_1 + x_2 + 4x_3 + x_4 = 1 \\
                    2x_1 + 2x_2 + 3x_3 + x_4 = 5 \\
                    7x_1 + x_2 + 6x_3 + x_4 = 7
                \end{cases}
                """)
            with col3:
                st.markdown(r"**Hệ $4 \times 3$:**")
                st.latex(r"""
                \begin{cases}
                    9x_1 + x_2 + 4x_3 = 1 \\
                    2x_1 + 2x_2 + 3x_3 = 5 \\
                    7x_1 + x_2 + 6x_3 = 7 \\
                    x_1 + x_2 + x_3 = 3
                \end{cases}
                """)

        # Biễu diễn hệ dạng ma trận
        with st.expander("#### 🧮 Biểu diễn hệ phương trình dưới dạng ma trận"):
            # Hiển thị định nghĩa các ma trận A, b, x
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
            # Hiển thị phương trình ma trận rút gọn
            st.markdown("Khi đó, hệ phương trình có thể viết gọn lại thành:")
            st.latex(r"\textbf{Ax} = \textbf{b}")

        #Biểu diễn dạng vector
        with st.expander("#### 🏹 Biểu diễn hệ phương trình dưới dạng Vector"):
            st.markdown(r"""
            Nếu ta ký hiệu vector cột thứ $j$ của ma trận là $\textbf{v}_j = (a_{1j},\ldots, a_{mj})^T \in \mathbb{R}^m$
            và vector vế phải là $\textbf{b} = (b_1, \ldots, b_m)^T \in \mathbb{R}^m$,
            thì hệ phương trình tuyến tính tổng quát được viết dưới dạng:
            """)
            # Hiển thị phương trình tổ hợp tuyến tính
            st.latex(r"x_1\textbf{v}_1 + x_2\textbf{v}_2 + \cdots + x_n\textbf{v}_n = \textbf{b}")
            st.info("💡 **Ý nghĩa:** Giải hệ phương trình thực chất là tìm cách 'pha trộn' các vector cột của ma trận $A$ theo các tỉ lệ $x_i$ để thu được vector kết quả $b$.")

        with st.expander("#### 🏹 Trực quan hóa Tổ hợp tuyến tính"):
            # 1. Nhập dữ liệu
            c1, c2 = st.columns(2)
            with c1:
                v1 = [st.number_input("v1_x", value=1.0), st.number_input("v1_y", value=2.0)]
            with c2:
                v2 = [st.number_input("v2_x", value=3.0), st.number_input("v2_y", value=1.0)]
            x1 = st.slider("Hệ số x1", -5.0, 5.0, 1.0)
            x2 = st.slider("Hệ số x2", -5.0, 5.0, 1.0)
            # Tính toán vector kết quả b = x1*v1 + x2*v2
            b = [x1*v1[0] + x2*v2[0], x1*v1[1] + x2*v2[1]]
            # 2. Tạo đồ thị
            fig = go.Figure()
            # Hàm vẽ mũi tên bằng annotations
            def draw_vector(x, y, name, color):
                fig.add_annotation(
                    x=x, y=y,
                    ax=0, ay=0,
                    xref='x', yref='y',
                    axref='x', ayref='y',
                    text='', # Không để chữ tại đầu mũi tên
                    showarrow=True,
                    arrowhead=3,
                    arrowsize=1,
                    arrowwidth=3,
                    arrowcolor=color )
                # Thêm một trace ẩn để hiển thị chú thích (Legend)
                fig.add_trace(go.Scatter(
                    x=[x], y=[y],
                    name=name,
                    mode='markers',
                    marker=dict(color=color, size=0),)) # Size=0 để ẩn chấm tròn
            # Vẽ các vector
            draw_vector(v1[0]*x1, v1[1]*x1, f"{x1}*v1 (Xanh)", "blue")
            draw_vector(v2[0]*x2, v2[1]*x2, f"{x2}*v2 (Lục)", "green")
            draw_vector(b[0], b[1], "Vector b (Đỏ)", "red")
            # Cấu hình khung nhìn
            limit = 10
            fig.update_layout(
                xaxis=dict(range=[-limit, limit], zeroline=True, zerolinewidth=2, zerolinecolor='black'),
                yaxis=dict(range=[-limit, limit], zeroline=True, zerolinewidth=2, zerolinecolor='black'),
                width=600, height=600,
                title="Minh họa: x1*v1 + x2*v2 = b")
            if st.checkbox("Hiển thị quy tắc hình bình hành"):
                # Vẽ đường đứt đoạn từ x1*v1 đến b
                fig.add_trace(go.Scatter(
                    x=[v1[0]*x1, b[0]], y=[v1[1]*x1, b[1]],
                    mode='lines', line=dict(dash='dash', color='gray'),
                    showlegend=False
                ))
                # Vẽ đường đứt đoạn từ x2*v2 đến b
                fig.add_trace(go.Scatter(
                    x=[v2[0]*x2, b[0]], y=[v2[1]*x2, b[1]],
                    mode='lines', line=dict(dash='dash', color='gray'),
                    showlegend=False
                ))
            st.plotly_chart(fig)

    # II Hệ Cramer
    with st.expander("ℹ️ℹ️. Hệ Cramer"):
        # Khái niệm
        with st.expander("🟰 Khái niệm "):
            st.markdown(r"""
            **Hệ Cramer** là hệ phương trình tuyến tính vuông (số phương trình bằng số ẩn, $n \times n$)
            có ma trận hệ số $\textbf{A}$ không suy biến ($\det \textbf{A} \neq 0$).

            > **Định lý:** Mọi hệ Cramer đều có một nghiệm duy nhất.
             """)
            st.latex(r"x_1\textbf{v}_1 + x_2\textbf{v}_2 + \cdots + x_n\textbf{v}_n = \textbf{b}")
            st.markdown("Nghiệm của hệ được tính theo công thức:")
            st.latex(r"x_i = \frac{D_i}{D}, \quad i = 1,\ldots, n")
            st.markdown("**Trong đó:**")
            st.latex(r"""
            \begin{aligned}
                D = \det A = \det(v_1, \ldots, v_i, \ldots, v_n) \\
                D_i = \det(v_1, \ldots, b, \ldots, v_n)
            \end{aligned}
            """)
            st.info("""💡 **Giải thích:** $D_i$ là định thức của ma trận có được bằng cách thay
                        cột thứ $i$ của ma trận $A$ bằng vector cột vế phải $b$.""")

        # Thực nghiệm với hệ cỡ nhỏ
        with st.expander("🧮 Thực nghiệm với hệ 2x2"):
            st.write("Giải hệ: $ax + by = e$ và $cx + dy = f$")

            col1, col2 = st.columns(2)
            with col1:
                a = st.number_input("a", value=1)
                b = st.number_input("b", value=2)
                e = st.number_input("e (vế phải 1)", value=5)
            with col2:
                c = st.number_input("c", value=3)
                d = st.number_input("d", value=4)
                f = st.number_input("f (vế phải 2)", value=11)
            D = a*d - b*c
            if D != 0:
                D1 = e*d - b*f
                D2 = a*f - e*c
                st.info(f"D = {D}, D1 = {D1}, D2 = {D2}")
                st.latex(rf"x = \frac{{{D1}}}{{{D}}} = {D1/D}, \quad y = \frac{{{D2}}}{{{D}}} = {D2/D}")
            else:
                st.error("D = 0: Đây không phải là hệ Cramer!")

        # 2. Dùng expander để ẩn các ví dụ phức tạp
        with st.expander("📚 Ví dụ minh họa (Hệ 3 phương trình)"):
            st.latex(r"""
            \begin{cases}
                9x_1 + x_2 + 4x_3 = 1 \\
                2x_1 + 2x_2 + 3x_3 = 5 \\
                7x_1 + x_2 + 6x_3 = 7
            \end{cases}
            """)
            st.info("Thử giải hệ này bằng phương pháp Cramer ở phía dưới!")

        # Kronecker-Kapelli
        with st.expander("©️. Định lý Kronecker-Kapelli"):
            st.markdown(r"""
            Hệ phương trình tuyến tính tổng quát $\textbf{Ax} = \textbf{b}$ có nghiệm khi và chỉ khi hạng của ma trận hệ số bằng hạng của ma trận bổ sung:
            """)
            st.latex(r"r(\textbf{A}) = r(\widetilde{\textbf{A}})")
            st.info(r"📝 Xem cấu trúc Ma trận bổ sung $\widetilde{\textbf{A}}$")
            st.markdown(r"Ma trận bổ sung được tạo ra bằng cách ghép thêm cột vector vế phải $\textbf{b}$ vào bên phải ma trận $\textbf{A}$:")
            st.latex(r"""
                \widetilde{\textbf{A}} = \left[ \begin{array}{ccc|c}
                a_{11} & \ldots & a_{1n} & b_1 \\
                \vdots & \ddots & \vdots & \vdots \\
                a_{m1} & \ldots & a_{mn} & b_m
                \end{array} \right]
            """)
            st.warning("📊 Biện luận số nghiệm của hệ")
            st.markdown("Giả sử hệ có $n$ ẩn số:")
            # Trường hợp vô nghiệm
            st.success(r"1. **Vô nghiệm:** Nếu $r(\textbf{A}) < r(\widetilde{\textbf{A}})$")
            # Trường hợp có nghiệm
            st.error(r"2. **Có nghiệm:** Nếu $r(\textbf{A}) = r(\widetilde{\textbf{A}}) = r$")
            st.write("    * Nếu $r = n$: Hệ có **nghiệm duy nhất**.")
            st.write("    * Nếu $r < n$: Hệ có **vô số nghiệm** (phụ thuộc vào $n-r$ ẩn tự do).")

    # III Hệ thuần nhất
    with st.expander("ℹ️ℹ️ℹ️. Hệ PTTT-Thuần nhất"):
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
        st.write(r"Hệ Cramer, thuần nhất thì có duy nhất nghiệm tầm thường $x_i = 0, \forall i = 1,\ldots, n$.")

    # IV Giải hệ bằng phương pháp Gauss
    with st.expander("ℹ️✋🏻. Giải HPTTT bằng PP Gauss"):
        st.markdown("""
        Thực hiện các phép biến đổi sơ cấp sau lên các phương trình:
        - Đổi chỗ hai phương trình;
        - Nhân, chia một số khác 0 vào cả 2 vế của một phương trình;
        - Cộng vào một phương trình một tổ hợp tuyến tính các PT khác.\\
        Để đưa HPT đã cho về hệ tương đương mà ma trận bổ sung có dạng bậc thang.
                    """)
        st.latex(r"""
        \begin{bmatrix}
        a_{11} & a_{12} & \ldots & a_{1p} &\ldots& | & b_1 \\
        0      & a_{22} & \ldots & a_{2p} &\ldots& | & b_2 \\
        \ddots & \ddots & \ddots & \ddots &\ldots& | & \vdots \\
        0      & 0      & \ldots & a_{pp} &\ldots& | & b_p
        \end{bmatrix}
        """)

