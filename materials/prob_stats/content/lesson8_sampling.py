import streamlit as st
import pandas as pd
import numpy as np

def run():
    st.header("Bài 8: Mẫu ngẫu nhiên")
    st.markdown("---")

    # --- PHẦN 1: KHÁI NIỆM MẪU NGẪU NHIÊN ---
    st.subheader("1. Khái niệm về Mẫu ngẫu nhiên")

    with st.expander("📝 Tổng thể và Mẫu"):
        st.write("""
        - **Tổng thể (Population):** Tập hợp tất cả các phần tử cùng quan tâm về một dấu hiệu nghiên cứu $X$ nào đó.
        - **Mẫu ngẫu nhiên (Random Sample):** Một tập hợp gồm $n$ phần tử được chọn ra từ tổng thể theo nguyên tắc ngẫu nhiên.
        - **Kích thước mẫu ($n$):** Số lượng phần tử có trong mẫu.
        """)
        st.info("💡 Mục tiêu của thống kê là dùng các đặc trưng của mẫu để suy diễn về các đặc trưng của tổng thể.")

    with st.expander("📊 Các dạng biểu diễn mẫu"):
        st.markdown("**1. Mẫu cụ thể (Mẫu thực nghiệm):**")
        st.write("Là tập hợp các giá trị số cụ thể thu được sau khi quan sát: $x_1, x_2, \\dots, x_n$.")

        st.markdown("**2. Bảng tần số (Mẫu rút gọn):**")
        st.write(
            "Khi các giá trị lặp lại, ta lập bảng gồm các giá trị khác nhau $x_i$ và số lần xuất hiện $n_i$ của chúng.")
        st.latex(r"\sum n_i = n")

    # --- PHẦN 2: CÁC ĐẶC TRƯNG CỦA MẪU ---
    st.divider()
    st.subheader("2. Các đặc trưng của mẫu (Thống kê mẫu)")
    st.write("Các đại lượng này được tính toán từ mẫu để ước lượng cho các tham số tương ứng của tổng thể.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔹 Trung bình mẫu ($\\overline{X}$)")
        st.write("Dùng để ước lượng cho kỳ vọng $\\mu$ của tổng thể.")
        st.latex(r"\overline{x} = \frac{1}{n} \sum_{i=1}^k n_i x_i")

        st.markdown("### 🔹 Tỉ lệ mẫu ($f$)")
        st.write("Dùng để ước lượng cho tỉ lệ $p$ của tổng thể.")
        st.latex(r"f = \frac{m}{n}")
        st.caption("(với $m$ là số phần tử có tính chất cần nghiên cứu)")

    with col2:
        st.markdown("### 🔹 Phương sai mẫu ($S^2$)")
        st.write("Đặc trưng cho độ phân tán của mẫu.")
        st.latex(r"s^2 = \frac{1}{n} \sum n_i (x_i - \overline{x})^2")

        st.markdown("### 🔹 Phương sai mẫu hiệu chỉnh ($S^2_{hc}$)")
        st.write("Là ước lượng không chệch cho phương sai $\\sigma^2$ của tổng thể.")
        st.latex(r"s^2_{hc} = \frac{n}{n-1} s^2")
        st.info("💡 Khi $n$ lớn, $s^2 \\approx s^2_{hc}$.")

    # --- PHẦN 3: CÔNG CỤ TÍNH TOÁN MẪU ---
    st.divider()
    st.subheader("🛠️ Máy tính đặc trưng mẫu tự động")
    st.write("Nhập dãy số liệu mẫu (cách nhau bằng dấu phẩy):")

    sample_input = st.text_input("Ví dụ: 5, 7, 8, 5, 6, 9, 7", "10, 12, 11, 10, 13, 11, 10, 12")

    if sample_input:
        try:
            data = [float(x.strip()) for x in sample_input.split(",")]
            n = len(data)
            x_bar = np.mean(data)
            s2 = np.var(data)  # Phương sai mẫu
            s2_hc = np.var(data, ddof=1)  # Phương sai mẫu hiệu chỉnh

            # Hiển thị kết quả
            res_col1, res_col2, res_col3 = st.columns(3)
            res_col1.metric("Kích thước mẫu (n)", n)
            res_col2.metric("Trung bình mẫu (x̄)", f"{x_bar:.4f}")
            res_col3.metric("Phương sai hiệu chỉnh (s_hc²)", f"{s2_hc:.4f}")

            # Tạo bảng tần số tự động
            st.write("**Bảng tần số tự động:**")
            unique, counts = np.unique(data, return_counts=True)
            freq_df = pd.DataFrame({"Giá trị (xi)": unique, "Tần số (ni)": counts})
            st.table(freq_df.T)

        except ValueError:
            st.error("Vui lòng chỉ nhập số và ngăn cách bởi dấu phẩy.")

    # --- FOOTNOTE ---
    st.sidebar.markdown("---")
    st.sidebar.info("""
    **💡 Lưu ý quan trọng:** 
    Trong các công thức kiểm định ở Bài 10, chúng ta sẽ sử dụng chủ yếu là **Trung bình mẫu** và **Độ lệch chuẩn hiệu chỉnh** ($s_{hc}$) để tính toán giá trị quan sát.
    """)