import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson, norm, expon, uniform


def run():
    st.header("Bài 6: Một số phân phối xác suất thường gặp")
    st.markdown("---")

    # --- PHẦN 1: CÁC PHÂN PHỐI RỜI RẠC ---
    st.subheader("I. Các phân phối rời rạc")

    # 1. Phân phối Nhị thức
    with st.expander("1. Phân phối Nhị thức B(n, p)"):
        st.write("""
        Dùng cho dãy thử nghiệm Bernoulli độc lập. Đây là cơ sở để kiểm định tỉ lệ ($p$) trong các bài toán thực tế.
        """)
        st.latex(r"P(X=k) = C_n^k \cdot p^k \cdot (1-p)^{n-k}")
        st.markdown("""
        - **Kỳ vọng:** $E(X) = np$
        - **Phương sai:** $V(X) = npq$
        """)
        st.info("Ví dụ: Kiểm tra 500 sản phẩm để tìm số phế phẩm trong một lô hàng.")

    # 2. Phân phối Poisson
    with st.expander("2. Phân phối Poisson P(λ)"):
        st.write("""
        Dùng để mô tả số lần xảy ra của một sự kiện hiếm trong một khoảng thời gian hoặc không gian xác định.
        """)
        st.latex(r"P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}")
        st.write("- **Kỳ vọng và Phương sai:** $E(X) = V(X) = \\lambda$")

    # --- PHẦN 2: CÁC PHÂN PHỐI LIÊN TỤC ---
    st.divider()
    st.subheader("II. Các phân phối liên tục")

    # 3. Phân phối Chuẩn - Quan trọng nhất
    with st.expander("3. Phân phối Chuẩn N(μ, σ²) - Trọng tâm"):
        st.write("""
        Đây là phân phối quan trọng nhất trong thống kê. Nhiều đại lượng trong tự nhiên và kỹ thuật tuân theo quy luật này:
        """)
        st.markdown("""
        * **Năng suất giống cây trồng:** Là một biến ngẫu nhiên có phân bố chuẩn.
        * **Độ dày sản phẩm:** Như độ dày của các tấm chất dẻo.
        * **Kích thước chi tiết máy:** Các chi tiết do máy sản xuất thường có kích thước tuân theo quy luật chuẩn.
        """)
        st.latex(r"f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}")
        st.info(
            "💡 Khi $\\mu=0$ và $\\sigma=1$, ta có phân phối chuẩn tắc $N(0,1)$ với biến số thường ký hiệu là $U$ hoặc $Z$.")

    # 4. Phân phối Đều và Phân phối Mũ
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Phân phối Đều U(a, b)**")
        st.write("Xác suất như nhau trên mọi khoảng có cùng độ dài.")
        st.latex(r"f(x) = \frac{1}{b-a} \text{ với } x \in [a, b]")
    with col2:
        st.markdown("**Phân phối Mũ Exp(λ)**")
        st.write("Thường dùng mô tả thời gian chờ đợi giữa các sự kiện.")
        st.latex(r"f(x) = \lambda e^{-\lambda x} \text{ với } x > 0")

    # --- PHẦN 3: MINH HỌA TRỰC QUAN ---
    st.divider()
    st.subheader("🛠️ Mô phỏng hình dạng phân phối")

    dist_type = st.selectbox("Chọn loại phân phối để xem đồ thị:",
                             ["Chuẩn (Normal)", "Nhị thức (Binomial)", "Poisson"])

    fig, ax = plt.subplots()

    if dist_type == "Chuẩn (Normal)":
        mu = st.slider("Kỳ vọng (μ)", -10.0, 10.0, 0.0)
        sigma = st.slider("Độ lệch chuẩn (σ)", 0.1, 5.0, 1.0)
        x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 100)
        ax.plot(x, norm.pdf(x, mu, sigma), color='red', lw=2)
        ax.set_title(f"Phân phối Chuẩn N({mu}, {sigma}²)")
        st.caption("Hình dáng 'quả chuông' đối xứng qua giá trị trung bình μ.")

    elif dist_type == "Nhị thức (Binomial)":
        n_val = st.slider("Số phép thử (n)", 1, 100, 20)
        p_val = st.slider("Xác suất thành công (p)", 0.0, 1.0, 0.5)
        x = np.arange(0, n_val + 1)
        ax.bar(x, binom.pmf(x, n_val, p_val), color='skyblue')
        ax.set_title(f"Phân phối Nhị thức B({n_val}, {p_val})")

    elif dist_type == "Poisson":
        lam = st.slider("Hệ số λ (Kỳ vọng)", 0.1, 20.0, 5.0)
        x = np.arange(0, 40)
        ax.bar(x, poisson.pmf(x, lam), color='green')
        ax.set_title(f"Phân phối Poisson (λ={lam})")

    st.pyplot(fig)

    # --- FOOTNOTE ---
    st.sidebar.info("""
    **Ghi chú kiểm định:** 
    Trong thực tế, khi kiểm tra máy móc hay năng suất, ta thường giả định dữ liệu có phân phối chuẩn để sử dụng các tiêu chuẩn kiểm định $U$ hoặc $t$.
    """)