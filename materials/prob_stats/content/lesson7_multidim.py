import streamlit as st
import pandas as pd
import numpy as np


def run():
    st.header("Bài 7: Biến ngẫu nhiên nhiều chiều")
    st.markdown("---")

    # --- PHẦN 1: LUẬT PHÂN PHỐI ---
    st.subheader("1. Luật phân phối của Biến ngẫu nhiên 2 chiều")

    st.write("""
    Khi xét đồng thời hai biến ngẫu nhiên $X$ và $Y$ trên cùng một phép thử, ta có một **biến ngẫu nhiên hai chiều** $(X, Y)$.
    """)

    tab1, tab2 = st.tabs(["Trường hợp Rời rạc", "Trường hợp Liên tục"])

    with tab1:
        st.markdown("**Bảng phân phối xác suất đồng thời:**")
        st.write("Dùng để mô tả xác suất $P(X = x_i, Y = y_j) = p_{ij}$.")
        st.latex(r"\sum_{i} \sum_{j} p_{ij} = 1")

        st.info(
            "💡 **Phân phối lề:** Để tìm phân phối riêng của $X$ (hoặc $Y$), ta cộng tổng các xác suất theo hàng (hoặc cột).")
        st.latex(r"P(X = x_i) = \sum_{j} p_{ij}")

    with tab2:
        st.markdown("**Hàm mật độ đồng thời $f(x, y)$:**")
        st.write("Xác suất để điểm $(X, Y)$ rơi vào miền $D$:")
        st.latex(r"P((X, Y) \in D) = \iint_D f(x, y) dx dy")
        st.markdown("""
        **Tính chất:**
        - $f(x, y) \\geq 0$
        - $\\int_{-\\infty}^{+\\infty} \\int_{-\\infty}^{+\\infty} f(x, y) dx dy = 1$
        """)

    # --- PHẦN 2: CÁC THAM SỐ ĐẶC TRƯNG ---
    st.divider()
    st.subheader("2. Các tham số đặc trưng")

    with st.expander("📊 Kỳ vọng và Phương sai lề"):
        st.write("""
        Các tham số $E(X), E(Y), V(X), V(Y)$ được tính dựa trên phân phối lề tương ứng của chúng. 
        Chúng phản ánh trung tâm và độ phân tán của từng biến khi đứng riêng lẻ.
        """)

    with st.expander("🔗 Hiệp phương sai (Covariance)"):
        st.write("""
        **Hiệp phương sai** $Cov(X, Y)$ dùng để đo lường mối quan hệ tuyến tính giữa $X$ và $Y$.
        """)
        st.latex(r"Cov(X, Y) = E[(X - E(X))(Y - E(Y))] = E(XY) - E(X)E(Y)")
        st.markdown("""
        - $Cov(X, Y) > 0$: $X$ và $Y$ đồng biến.
        - $Cov(X, Y) < 0$: $X$ và $Y$ nghịch biến.
        - $Cov(X, Y) = 0$: $X$ và $Y$ không có tương quan tuyến tính (Nếu $X, Y$ độc lập thì $Cov(X, Y) = 0$).
        """)

    with st.expander("📏 Hệ số tương quan (Correlation Coefficient)"):
        st.write("""
        Để chuẩn hóa độ mạnh yếu của mối quan hệ mà không phụ thuộc vào đơn vị đo, ta dùng **Hệ số tương quan** $\rho_{XY}$.
        """)
        st.latex(r"\rho_{XY} = \frac{Cov(X, Y)}{\sigma_X \cdot \sigma_Y}")
        st.warning(
            "⚠️ **Tính chất:** $-1 \\leq \\rho_{XY} \\leq 1$. Nếu $|\\rho_{XY}|$ càng gần 1, mối quan hệ tuyến tính càng chặt chẽ.")

    # --- PHẦN 3: CÔNG CỤ TÍNH TOÁN TƯƠNG TÁC ---
    st.divider()
    st.subheader("🛠️ Máy tính Tương quan (Bảng 2x2)")
    st.write("Nhập xác suất đồng thời cho bảng 2x2 dưới đây:")

    col1, col2, col3 = st.columns([1, 1, 1])
    p11 = col1.number_input("P(X1, Y1)", 0.0, 1.0, 0.2)
    p12 = col2.number_input("P(X1, Y2)", 0.0, 1.0, 0.1)
    p21 = col1.number_input("P(X2, Y1)", 0.0, 1.0, 0.3)
    p22 = col2.number_input("P(X2, Y2)", 0.0, 1.0, 0.4)

    x1, x2 = 10, 20
    y1, y2 = 5, 15

    total_p = p11 + p12 + p21 + p22

    if st.button("Phân tích mối quan hệ"):
        if abs(total_p - 1.0) > 1e-9:
            st.error(f"Tổng xác suất phải bằng 1.0 (Hiện là {total_p:.2f})")
        else:
            # Tính phân phối lề
            px1, px2 = p11 + p12, p21 + p22
            py1, py2 = p11 + p21, p12 + p22

            # Tính Kỳ vọng
            ex = x1 * px1 + x2 * px2
            ey = y1 * py1 + y2 * py2
            exy = (x1 * y1 * p11) + (x1 * y2 * p12) + (x2 * y1 * p21) + (x2 * y2 * p22)

            # Tính Hiệp phương sai và Tương quan
            cov = exy - (ex * ey)
            vx = (x1 ** 2 * px1 + x2 ** 2 * px2) - ex ** 2
            vy = (y1 ** 2 * py1 + y2 ** 2 * py2) - ey ** 2
            corr = cov / (np.sqrt(vx) * np.sqrt(vy))

            c1, c2 = st.columns(2)
            c1.metric("Hiệp phương sai (Cov)", f"{cov:.2f}")
            c2.metric("Hệ số tương quan (ρ)", f"{corr:.4f}")

            if abs(corr) > 0.7:
                st.success("Kết luận: Mối quan hệ tuyến tính rất mạnh.")
            elif abs(corr) < 0.3:
                st.info("Kết luận: Mối quan hệ tuyến tính yếu.")
            else:
                st.warning("Kết luận: Mối quan hệ tuyến tính trung bình.")

    # --- FOOTNOTE ---
    st.sidebar.markdown("---")
    st.sidebar.info("""
    **Ghi chú:** 
    Trong thực tế, khi đo lường các chỉ số như "Chiều cao" và "Cân nặng" của cùng một đối tượng, chúng ta đang làm việc với biến ngẫu nhiên 2 chiều.
    """)