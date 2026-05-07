import streamlit as st
import pandas as pd
#import numpy as np


def run():
    st.header("Bài 4: Biến ngẫu nhiên và Hàm phân phối")
    st.markdown("---")

    # --- PHẦN 1: KHÁI NIỆM BIẾN NGẪU NHIÊN ---
    st.subheader("1. Khái niệm Biến ngẫu nhiên (ĐLNN)")

    with st.expander("📖 Định nghĩa"):
        st.write("""
        **Biến ngẫu nhiên** (hay Đại lượng ngẫu nhiên - ĐLNN) là một đại lượng nhận các giá trị số tùy thuộc vào kết quả của phép thử ngẫu nhiên.
        """)
        st.info("💡 Nói cách khác, nó là một hàm số đi từ không gian mẫu $\\Omega$ vào tập số thực $\\mathbb{R}$.")

    with st.expander("🗂️ Phân loại Biến ngẫu nhiên"):
        st.markdown("""
        - **Biến ngẫu nhiên rời rạc:** Các giá trị có thể liệt kê được (ví dụ: số sản phẩm lỗi, số lần bắn trúng).
        - **Biến ngẫu nhiên liên tục:** Các giá trị lấp đầy một khoảng trên trục số (ví dụ: năng suất cây trồng, độ dày tấm chất dẻo).
        """)

    # --- PHẦN 2: PHÂN PHỐI XÁC SUẤT ---
    st.subheader("2. Phân phối xác suất")

    tab1, tab2, tab3 = st.tabs(["BNN Rời rạc", "BNN Liên tục", "Hàm phân phối (CDF)"])

    with tab1:
        st.markdown("**Bảng phân phối xác suất:**")
        st.write("Dùng để liệt kê các giá trị $x_i$ và xác suất tương ứng $p_i = P(X = x_i)$.")
        st.latex(r"\sum_{i} p_i = 1")

        st.markdown("#### 🔍 Ví dụ 1: Số mặt ngửa")
        st.write("Tung 2 đồng xu, gọi $X$ là số mặt ngửa.")
        data = {"X": [0, 1, 2], "P(X)": [0.25, 0.50, 0.25]}
        st.table(pd.DataFrame(data).set_index("X"))

    with tab2:
        st.markdown("**Hàm mật độ xác suất $f(x)$:**")
        st.write(
            "Dùng cho biến liên tục. Xác suất tại một điểm bằng 0, chúng ta chỉ tính xác suất trên một khoảng $[a, b]$.")
        st.latex(r"P(a \leq X \leq b) = \int_{a}^{b} f(x) dx")
        st.latex(r"\int_{-\infty}^{+\infty} f(x) dx = 1")

        st.markdown("#### 🔍 Ví dụ thực tế")
        st.write("""
        Trong thực tế kỹ thuật, các đại lượng như:
        - **Năng suất giống cây trồng**.
        - **Độ dày của các tấm chất dẻo**.
        - **Kích thước các chi tiết máy**.

        Thường được coi là các biến ngẫu nhiên liên tục có **phân phối chuẩn**.
        """)

    with tab3:
        st.markdown("**Hàm phân phối xác suất $F(x)$:**")
        st.write("Định nghĩa chung cho cả rời rạc và liên tục:")
        st.latex(r"F(x) = P(X < x)")
        st.markdown("""
        **Tính chất:**
        - $0 \\leq F(x) \\leq 1$.
        - $F(x)$ là hàm không giảm.
        - $P(a \\leq X < b) = F(b) - F(a)$.
        """)

    # --- PHẦN 3: CÔNG CỤ MINH HỌA ---
    st.divider()
    st.subheader("🛠️ Kiểm tra tính hợp lệ của Bảng phân phối")
    st.write("Nhập các xác suất $p_i$ (cách nhau bởi dấu phẩy) để kiểm tra tổng có bằng 1 hay không.")

    user_input = st.text_input("Ví dụ: 0.2, 0.5, 0.3", "0.2, 0.5, 0.3")
    try:
        probs = [float(p.strip()) for p in user_input.split(",")]
        total = sum(probs)
        if abs(total - 1.0) < 1e-9:
            st.success(f"Tổng bằng {total:.1f} ✅ Đây là bảng phân phối hợp lệ!")
        else:
            st.error(f"Tổng bằng {total:.4f} ❌ Không hợp lệ (Phải bằng 1.0)")
    except ValueError:
        st.warning("Vui lòng chỉ nhập số thực.")

    # --- SIDEBAR: PHỤ LỤC ---
    st.sidebar.info("""
    **💡 Ghi chú:** 
    Trong các bài toán thực tế ở chương sau, chúng ta thường giả định biến ngẫu nhiên tuân theo quy luật chuẩn $N(\\mu, \\sigma^2)$.
    """)