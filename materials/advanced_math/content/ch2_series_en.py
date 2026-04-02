import streamlit as st
import numpy as np
import numpy.linalg as la
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go


def run():
    # Chuong 2: Ly thuyet chuoi
    st.header("Chapter 2: Series Theory")

    # Bai 4. Chuoi so
    st.markdown("---")
    st.subheader("Part 4. Numerical Series")

    # I: Khai niem
    with st.expander("ℹ️. Numerical Series Definition"):
        st.markdown(r"""
        Cho dãy số thực $(a_n),\; a_n \in \mathbb{R}$ với mọi $n$, gọi $a_1 + a_2 + \cdots + a_n + \cdots = \sum_{k = 1}^{\infty}a_k$ là
        một chuỗi số thực. Số thực $a_k$ với $k$ xác định gọi là số hạng thứ $k$, với $k$ không xác định gọi là số hạng tổng quát của
        chuỗi.

        ---
        **Một vài chuỗi số đặc biệt:**

        $\sum_{n = 1}^{\infty}(-1)^{n-1}\dfrac{1}{n};\; \sum_{n = 1}^{\infty}(-1)^{n-1}$;

        $\sum_{n = 0}^{\infty}\dfrac{1}{2^n} \textrm{ chuỗi cấp số nhân có công bội là 1/2}$;

        $\sum_{n = 1}^{\infty}\dfrac{1}{n} \textrm{ chuỗi điều hòa}$;

        $\sum_{n = 1}^{\infty}\dfrac{1}{n^{\alpha}} \textrm{ chuỗi Riemann với tham số } \alpha$.
        """)

        st.markdown("---")
        st.markdown(r"""
        **∑ Dãy tổng riêng**

        Cho chuỗi $a_1 + a_2 + \cdots + a_n + \cdots = \sum_{k = 1}^{\infty}a_k$

        $$S_n = \sum_{i = 1}^{n}a_i$$
        gọi là tổng riêng thứ $n$ của chuỗi.

        Nếu dãy $(S_n)$ hội tụ, tức $\displaystyle \lim_{n \to \infty}S_n = S$ (hữu hạn) thì ta nói chuỗi hội tụ và có tổng là
        $\displaystyle S = \sum_{i = 1}^{\infty}a_i$. $R_n = S - S_n$ gọi là phần dư thứ $n$ của chuỗi (hội tụ về 0). Nếu dãy $(S_n)$
        không hội tụ ta nói chuỗi phân kỳ.
        """)

        with st.expander("🎯 Điều kiện hội tụ của chuỗi số"):

            # --- ĐỊNH LÝ 1: CAUCHY ---
            st.info("1️⃣ Định lý 1: Tiêu chuẩn Cauchy (Điều kiện cần và đủ)")
            st.markdown("**Nội dung định lý:**")
            st.markdown(r"""
            Để chuỗi số $\displaystyle \sum_{n = 1}^{\infty}a_n$ hội tụ, điều kiện cần và đủ là:
            """)
            st.latex(r"""\forall \epsilon > 0,\; \exists n_0 :\; \forall n > n_0, \forall p \in \mathbb{N}^* \Rightarrow |a_n + a_{n+1}
            + \cdots + a_{n+p}| < \epsilon""")

            st.warning("""
            💡 **Giải thích đơn giản:** Điều này có nghĩa là nếu lấy một đoạn bất kỳ các số hạng nằm ở "phần đuôi" của chuỗi (khi
            $n$ đủ lớn), thì tổng của đoạn đó phải nhỏ tùy ý (tiến về 0).
            """)

            # --- ĐỊNH LÝ 2: ĐIỀU KIỆN CẦN ---
            st.info("2️⃣ Định lý 2: Điều kiện cần (Rất quan trọng)")
            st.markdown("**Nội dung định lý:**")
            st.markdown(r"""
            Điều kiện cần để chuỗi $\displaystyle \sum_{n = 1}^{\infty}a_n$ hội tụ là số hạng tổng quát phải tiến về 0:
            """)
            st.latex(r"\lim_{n \to \infty}a_n = 0")

            # Cảnh báo quan trọng cho sinh viên
            st.warning(r"""
            ⚠️ **Lưu ý:**
            * Nếu $\lim_{n \to \infty}a_n \neq 0$ $\Rightarrow$ Chuỗi chắc chắn **PHÂN KỲ**.
            * Nếu $\lim_{n \to \infty}a_n = 0$ $\Rightarrow$ Chưa thể kết luận gì cả (có thể hội tụ hoặc phân kỳ).
            """)

            st.markdown("---")
            st.markdown("#### 🧪 Ví dụ phản chứng:")
            col1, col2 = st.columns(2)

            with col1:
                st.write(r"**Chuỗi phân kỳ:** $\sum \frac{1}{n}$")
                st.latex(r"\lim_{n \to \infty} \frac{1}{n} = 0")
                st.write("(Thỏa mãn điều kiện cần, nhưng vẫn phân kỳ)")

            with col2:
                st.write(r"**Chuỗi hội tụ:** $\sum \frac{1}{2^n}$")
                st.latex(r"\lim_{n \to \infty} \frac{1}{2^n} = 0")
                st.write("(Thỏa mãn điều kiện cần và hội tụ)")

        # --- MINH HỌA TRỰC QUAN (OPTIONAL) ---
        if st.checkbox("Hiển thị biểu đồ minh họa Định lý 2"):
            n_vals = np.arange(1, 21)

            # Dữ liệu
            a_n_harmonic = 1/n_vals
            a_n_geometric = 1/(2**n_vals)
            a_n_div = (n_vals)/(n_vals + 1) # Lim -> 1

            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(n_vals, a_n_harmonic, 'o--', label=r'$1/n \to 0$ (Phân kỳ)', color='orange')
            ax.plot(n_vals, a_n_geometric, 'o--', label=r'$1/2^n \to 0$ (Hội tụ)', color='green')
            ax.plot(n_vals, a_n_div, 'x-', label=r'$n/(n+1) \to 1$ (Phân kỳ rõ ràng)', color='red')

            ax.axhline(0, color='black', linewidth=1)
            ax.set_title("So sánh giới hạn của số hạng tổng quát $a_n$")
            ax.legend()
            st.pyplot(fig)

        st.markdown("___")
        st.info("💡 Các tính chất cơ bản của Chuỗi số hội tụ")

        # --- TÍNH CHẤT 1: HỮU HẠN SỐ HẠNG ĐẦU ---
        st.warning("1. Ảnh hưởng của các số hạng đầu tiên")
        st.markdown("""
        > **Tính chất:** Tính chất hội tụ hay phân kỳ của chuỗi **vẫn giữ nguyên** khi thay đổi hữu hạn số hạng đầu tiên của chuỗi.
        """)
        with st.expander("🧪 Ví dụ minh họa"):
            st.write(r"Xét chuỗi hội tụ (Cấp số nhân công bội 1/2): $S = 1 + 1/2 + 1/4 + \cdots = 2$")
            # Cho phép người dùng thay đổi 3 số hạng đầu
            col1, col2, col3 = st.columns(3)
            new_a0 = col1.number_input("Sửa số hạng 1 ($a_0$)", value=1.0)
            new_a1 = col2.number_input("Sửa số hạng 2 ($a_1$)", value=0.5)
            new_a2 = col3.number_input("Sửa số hạng 3 ($a_2$)", value=0.25)
            # Tính tổng lý thuyết ban đầu (từ n=3 trở đi)
            # Tổng vô hạn ban đầu = 2. Tổng 3 số đầu ban đầu = 1 + 0.5 + 0.25 = 1.75
            # Phần đuôi (tail) = 2 - 1.75 = 0.25
            tail_sum = 0.25
            # Tổng mới
            new_sum = new_a0 + new_a1 + new_a2 + tail_sum
            st.success(f"Tổng mới của chuỗi là: **{new_sum}**")
            st.success("""
            ✅ **Kết luận:** Mặc dù giá trị tổng thay đổi, nhưng chuỗi **VẪN HỘI TỤ** vì phần đuôi (vô hạn số hạng phía sau) không bị
            ảnh hưởng.
            """)

        st.markdown("___")
        # --- TÍNH CHẤT 2 & 3: TÍNH TUYẾN TÍNH ---
        st.warning("2. Tính tuyến tính")
        st.markdown(r"Nếu các chuỗi $\sum a_n$ và $\sum b_n$ hội tụ:")
        # Sử dụng Columns để trình bày song song 2 tính chất
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Nhân với hằng số:**")
            st.latex(r"\sum_{n = 1}^{\infty}\lambda a_n = \lambda S")
            st.caption("Nếu chuỗi hội tụ về $S$, nhân mọi số hạng với $\lambda$ thì tổng mới là $\lambda S$.")
        with c2:
            st.markdown("**Tổng hai chuỗi:**")
            st.latex(r"\sum_{n = 1}^{\infty}(a_n + b_n) = A + B")
            st.caption("Tổng của hai chuỗi hội tụ là một chuỗi hội tụ.")

        # --- CẢNH BÁO (RẤT QUAN TRỌNG CHO SINH VIÊN) ---
        with st.expander("⚠️ Cảnh báo bẫy tư duy thường gặp"):
            st.success("**Lưu ý về chiều ngược lại:**")
            st.markdown(r"""
            * Nếu $\sum (a_n + b_n)$ hội tụ, **KHÔNG** suy ra được $\sum a_n$ và $\sum b_n$ cũng hội tụ.
            * **Ví dụ:** $a_n = 1/n$ (phân kỳ) và $b_n = -1/n$ (phân kỳ).
            * Nhưng tổng $a_n + b_n = 0$ (chuỗi số 0 hội tụ về 0).
            """)

        st.markdown("___")
        st.error("#### ✨ Ví dụ minh họa: Sự hội tụ & Phân kỳ")
        # Chia màn hình thành 2 tab để không gian rộng rãi hơn cho đồ thị
        tab1, tab2, tab3 = st.tabs(["1️⃣ Chuỗi Cấp số nhân", "2️⃣ Chuỗi Điều hòa", "3️⃣ Chuỗi Riemann"])

        # --- TAB 1: CHUỖI CẤP SỐ NHÂN ---
        with tab1:
            st.success("Chuỗi hình học (Geometric Series)")
            st.latex(r"\sum_{i = 1}^{\infty}q^i = q + q^2 + q^3 + \cdots")
            col1, col2 = st.columns([1, 2])
            with col1:
                st.write("### 🎛️ Điều khiển")
                # Slider cho phép chọn q âm hoặc dương
                q = st.slider("Chọn công bội q", -1.5, 1.5, 0.5, step=0.1)
                num_terms = st.slider("Số lượng số hạng (N)", 10, 100, 50)
            # Biện luận lý thuyết
            st.markdown("---")
            if abs(q) < 1:
                st.success(f"**Kết luận:** $|{q}| < 1$ → Chuỗi **Hội tụ**.")
                limit_sum = q / (1 - q) # Công thức tổng lùi vô hạn với i bắt đầu từ 1
                st.latex(rf"S = \frac{{q}}{{1-q}} = {limit_sum:.4f}")
            else:
                st.error(f"**Kết luận:** $|{q}| \ge 1$ → Chuỗi **Phân kỳ**.")

            with col2:
                # Tính toán dữ liệu
                n_vals = np.arange(1, num_terms + 1)
                terms = q ** n_vals
                partial_sums = np.cumsum(terms) # Tổng riêng thứ n
                # Vẽ đồ thị bằng Plotly
                fig1 = go.Figure()
                # Đường tổng riêng
                fig1.add_trace(go.Scatter(x=n_vals, y=partial_sums,
                                          mode='lines+markers', name='Tổng riêng Sn',
                                          line=dict(color='blue')
                                         ))
                # Đường giới hạn (nếu hội tụ)
                if abs(q) < 1:
                    fig1.add_hline(y=limit_sum, line_dash="dash", line_color="green", annotation_text="Giới hạn S")
                fig1.update_layout(title=f"Đồ thị Tổng riêng với q = {q}", xaxis_title="n", yaxis_title="Sn")
                st.plotly_chart(fig1, use_container_width=True)

        # --- TAB 2: CHUỖI ĐIỀU HÒA ---
        with tab2:
            st.success("Chuỗi Điều hòa (Harmonic Series)")
            st.latex(r"\sum_{n = 1}^{\infty}\dfrac{1}{n} = 1 + \frac{1}{2} + \frac{1}{3} + \cdots")

            with st.expander("🤔 Tại sao chuỗi này thú vị?"):
                st.write("""
                Đây là ví dụ điển hình cho thấy: **Điều kiện $a_n \\to 0$ là chưa đủ để hội tụ.**
                - Số hạng thứ 1 triệu là $1/1.000.000$ (rất nhỏ).
                - Nhưng tổng của chuỗi vẫn tiến ra vô cùng (dù rất chậm).
                """)

            # Minh họa sự tăng trưởng chậm
            n_harmonic = st.slider("Chọn số lượng số hạng để cộng thử", 100, 10000, 1000)
            n_vals_h = np.arange(1, n_harmonic + 1)
            partial_sums_h = np.cumsum(1 / n_vals_h)

            # So sánh với hàm Logarit (ln(n))
            ln_vals = np.log(n_vals_h)
            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(x=n_vals_h, y=partial_sums_h, name='Tổng chuỗi (Sn)', line=dict(color='red')))
            fig2.add_trace(go.Scatter(x=n_vals_h, y=ln_vals, name='Hàm Logarit (ln n)', line=dict(dash='dash', color='gray')))
            fig2.update_layout(
            title="Sự phân kỳ chậm chạp của chuỗi điều hòa",
            xaxis_title="Số hạng n", yaxis_title="Giá trị",
            annotations=[dict(x=n_harmonic, y=partial_sums_h[-1], text=f"S({n_harmonic}) ≈ {partial_sums_h[-1]:.2f}", showarrow=True,
                              arrowhead=1)]
            )
            st.plotly_chart(fig2, use_container_width=True)
            st.success(r"""💡 **Ghi nhớ:** Tổng của chuỗi điều hòa xấp xỉ hàm Logarit tự nhiên: $S_n \approx \ln(n) + \gamma$ (Hằng
            số Euler). Vì $\ln(n) \to \infty$, nên chuỗi phân kỳ.""")

        # --- Tab 3: CHUỖI RIEMANN ---
        with tab3:
            st.success("Chuỗi Riemann (p-series)")
            st.latex(r"\sum_{n=1}^{\infty} \dfrac{1}{n^{\alpha}}")

            col_riemann1, col_riemann2 = st.columns([1,2])
            with col_riemann1:
                st.write("#### 🔢 Điều khiển")
                # Slider cho tham số alpha
                alpha = st.slider("Chọn tham số α", 0.5, 3.0, 1.0, step=0.1, key="alpha_riemann")
                num_terms_riem = st.slider("Số lượng số hạng (N)", 10, 500, 100, key="num_terms_riemann")

                st.markdown("---")
                if alpha > 1:
                    st.info(f"**Kết luận:** $\\alpha = {alpha} > 1$ nên Chuỗi **hội tụ**")
                    #st.warning("Giá trị hội tụ có thể là hàm Zeta Riemann, không có dạng đóng đơn giản.")
                else:
                    st.error(f"**Kết luận:** $\\alpha = {alpha} \le 1$ nên chuỗi **Phân kỳ**")

            with col_riemann2:
                n_vals_riem = np.arange(1, num_terms_riem + 1)
                #Tránh lỗi chia cho 0 nếu n = 0, dù chuỗi bắt đầu từ n = 1
                terms_riem = 1/(n_vals_riem**alpha)
                partial_sums_riem = np.cumsum(terms_riem)

                fig3 = go.Figure()
                fig3.add_trace(go.Scatter(x=n_vals_riem, y=partial_sums_riem,
                mode='lines + markers', name=f'Tổng riêng Sn (α = {alpha})',
                line=dict(color='purple')
                ))
                fig3.update_layout(
                title = f'Đồ thị Tổng riêng của Chuỗi Riemann (α = {alpha})',
                xaxis_title = 'Số hạng n', yaxis_title = 'Sn',
                yaxis_range = [0, partial_sums_riem[-1]*1.2 if alpha <= 1 else partial_sums_riem[-1]*1.5]
                )
                st.plotly_chart(fig3, use_container_width = True)


