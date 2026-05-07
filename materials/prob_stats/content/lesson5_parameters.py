import streamlit as st
import numpy as np
import pandas as pd


def run():
    st.header("Bài 5: Các tham số đặc trưng")
    st.markdown("---")

    # --- PHẦN 1: KỲ VỌNG (EXPECTATION) ---
    st.subheader("1. Kỳ vọng của Biến ngẫu nhiên")

    with st.expander("📖 Định nghĩa và Ý nghĩa"):
        st.write("""
        **Kỳ vọng** (ký hiệu là $E(X)$ hoặc $\\mu$) đại diện cho giá trị trung bình mà biến ngẫu nhiên nhận được trong rất nhiều phép thử.
        """)

        st.markdown("**Công thức tính:**")
        st.write("- **Rời rạc:** $E(X) = \\sum x_i p_i$")
        st.write("- **Liên tục:** $E(X) = \\int_{-\\infty}^{+\\infty} x f(x) dx$")

        st.info(
            "💡 **Ý nghĩa thực tế:** Trong các bài toán thực tế, kỳ vọng thường là mục tiêu cần kiểm định, chẳng hạn như trọng lượng trung bình của sản phẩm hay năng suất trung bình của giống mới.")

    with st.expander("⚙️ Tính chất của Kỳ vọng"):
        st.markdown("""
        - $E(C) = C$ (với $C$ là hằng số).
        - $E(CX) = C \\cdot E(X)$.
        - $E(X + Y) = E(X) + E(Y)$.
        - $E(X \\cdot Y) = E(X) \\cdot E(Y)$ (nếu $X, Y$ độc lập).
        """)

    # --- PHẦN 2: PHƯƠNG SAI VÀ ĐỘ LỆCH CHUẨN ---
    st.divider()
    st.subheader("2. Phương sai và Độ lệch chuẩn")

    with st.expander("📐 Phương sai (Variance)"):
        st.write("""
        **Phương sai** (ký hiệu là $V(X), Var(X)$ hoặc $\\sigma^2$) dùng để đo mức độ phân tán (độ tập trung) của các giá trị của biến ngẫu nhiên quanh giá trị kỳ vọng.
        """)
        st.latex(r"V(X) = E[X - E(X)]^2 = E(X^2) - [E(X)]^2")
        st.write("- Nếu $V(X)$ nhỏ: Các giá trị tập trung gần kỳ vọng (máy móc hoạt động ổn định).")
        st.write("- Nếu $V(X)$ lớn: Các giá trị phân tán xa kỳ vọng (sai số nhiều).")

    with st.expander("📏 Độ lệch chuẩn (Standard Deviation)"):
        st.write("""
        Vì phương sai có đơn vị là bình phương của đơn vị gốc, nên ta dùng **Độ lệch chuẩn** ($\\sigma$) để đưa về cùng đơn vị với biến ngẫu nhiên.
        """)
        st.latex(r"\sigma = \sqrt{V(X)}")
        st.info("Ví dụ: Nếu đơn vị của $X$ là 'gam' thì đơn vị của $\\sigma$ cũng là 'gam'.")

    # --- PHẦN 3: CÁC THAM SỐ KHÁC ---
    st.divider()
    st.subheader("3. Một số tham số đặc trưng khác")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Giá trị yếu vị (Mode):**")
        st.write("Giá trị có xác suất lớn nhất (rời rạc) hoặc tại đó hàm mật độ đạt cực đại (liên tục).")
    with col2:
        st.markdown("**Trung vị (Median):**")
        st.write("Giá trị chia phân phối thành hai phần có xác suất bằng nhau ($0.5$).")

    # --- PHẦN 4: MÁY TÍNH THAM SỐ TƯƠNG TÁC ---
    st.divider()
    st.subheader("🛠️ Máy tính Kỳ vọng và Phương sai (Rời rạc)")
    st.write("Nhập bảng phân phối bên dưới:")

    df_data = pd.DataFrame({
        "x_i (Giá trị)": [1.0, 2.0, 3.0, 4.0],
        "p_i (Xác suất)": [0.1, 0.4, 0.3, 0.2]
    })

    edited_df = st.data_editor(df_data, num_rows="dynamic")

    if st.button("Tính toán thông số"):
        x = edited_df["x_i (Giá trị)"].values
        p = edited_df["p_i (Xác suất)"].values

        if abs(np.sum(p) - 1.0) > 1e-9:
            st.error(f"Tổng xác suất phải bằng 1.0 (Hiện tại là: {np.sum(p):.4f})")
        else:
            ev = np.sum(x * p)
            var = np.sum((x ** 2) * p) - (ev ** 2)
            std = np.sqrt(var)

            c1, c2, c3 = st.columns(3)
            c1.metric("Kỳ vọng E(X)", f"{ev:.4f}")
            c2.metric("Phương sai V(X)", f"{var:.4f}")
            c3.metric("Độ lệch chuẩn σ", f"{std:.4f}")

    # --- FOOTNOTE ---
    st.sidebar.markdown("---")
    st.sidebar.info("""
    **💡 Bạn có biết?**
    Trong kiểm định giả thuyết, chúng ta thường so sánh kỳ vọng thực tế của mẫu ($\\overline{X}$) với kỳ vọng giả thuyết ($\\mu_0$) để đưa ra kết luận về chất lượng sản phẩm.
    """)