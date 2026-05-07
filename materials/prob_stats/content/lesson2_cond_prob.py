import streamlit as st


def run():
    st.header("Bài 2: Xác suất có điều kiện")
    st.markdown("---")

    # --- PHẦN 1: ĐỊNH NGHĨA VÀ TÍNH CHẤT ---
    st.subheader("1. Định nghĩa và Tính chất")

    with st.expander("📖 Định nghĩa Xác suất có điều kiện"):
        st.write("""
        Cho hai biến cố $A$ và $B$. Xác suất của biến cố $A$ với điều kiện biến cố $B$ đã xảy ra được gọi là **xác suất có điều kiện**, ký hiệu là $P(A|B)$.
        """)
        st.latex(r"P(A|B) = \frac{P(A \cap B)}{P(B)} \quad (\text{với } P(B) > 0)")
        st.info(
            "💡 **Giải thích:** Chúng ta đang thu hẹp không gian mẫu từ $\\Omega$ xuống chỉ còn các kết quả nằm trong $B$.")

    with st.expander("⚙️ Công thức nhân xác suất"):
        st.write("Từ định nghĩa trên, ta suy ra công thức nhân để tính xác suất của một tích các biến cố:")
        st.latex(r"P(A \cap B) = P(B) \cdot P(A|B) = P(A) \cdot P(B|A)")
        st.write("Đối với nhiều biến cố $A_1, A_2, \\dots, A_n$:")
        st.latex(r"P(A_1 A_2 \dots A_n) = P(A_1) \cdot P(A_2|A_1) \dots P(A_n|A_1 A_2 \dots A_{n-1})")

    # --- PHẦN 2: ĐỘC LẬP VÀ PHỤ THUỘC ---
    st.subheader("2. Sự độc lập và Phụ thuộc")

    st.markdown("""
    Việc xác định hai biến cố có "liên quan" đến nhau hay không là cực kỳ quan trọng trong thống kê:
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.success("**Biến cố Độc lập**")
        st.write("""
        Việc $B$ xảy ra không ảnh hưởng đến xác suất của $A$.
        - $P(A|B) = P(A)$
        - $P(B|A) = P(B)$
        - **Công thức:** $P(A \\cap B) = P(A) \\cdot P(B)$
        """)
    with col2:
        st.error("**Biến cố Phụ thuộc**")
        st.write("""
        Việc $B$ xảy ra làm thay đổi khả năng xảy ra của $A$.
        - $P(A|B) \\neq P(A)$
        - **Công thức:** $P(A \\cap B) = P(B) \\cdot P(A|B)$
        """)

    # --- PHẦN 3: VÍ DỤ CỤ THỂ ---
    st.divider()
    st.subheader("🔍 Ví dụ minh họa")

    # Ví dụ 1: Lấy bi (Phụ thuộc)
    st.markdown("### Ví dụ 1: Lấy bi không hoàn lại (Phụ thuộc)")
    st.write("Một hộp có **3 bi đỏ** và **2 bi xanh**. Lấy ngẫu nhiên lần lượt 2 viên bi không hoàn lại.")

    if st.checkbox("Xem lời giải Ví dụ 1"):
        st.write("- Xác suất lấy được bi đỏ ở lần 1: $P(R1) = 3/5$.")
        st.write(
            "- Nếu lần 1 đã lấy bi đỏ, trong hộp còn 2 đỏ, 2 xanh. Xác suất lần 2 lấy bi xanh: $P(B2|R1) = 2/4 = 0.5$.")
        st.write("- Xác suất cả hai lần lấy được (Đỏ, Xanh): $P(R1 \\cap B2) = (3/5) \\times (2/4) = 0.3$.")
        st.info("Ở đây, biến cố lần 2 phụ thuộc vào kết quả lần 1.")

    # Ví dụ 2: Tung đồng xu (Độc lập)
    st.markdown("### Ví dụ 2: Tung đồng xu và xúc xắc (Độc lập)")
    st.write("Tung một đồng xu và gieo một con xúc xắc. Tính xác suất đồng xu ngửa và xúc xắc ra mặt 6.")

    if st.checkbox("Xem lời giải Ví dụ 2"):
        st.write("- Xác suất đồng xu ngửa: $P(A) = 1/2$.")
        st.write("- Xác suất xúc xắc ra mặt 6: $P(B) = 1/6$.")
        st.write("- Vì hai hành động này không liên quan: $P(A \\cap B) = (1/2) \\times (1/6) = 1/12$.")

    # --- PHẦN 4: CÔNG CỤ TÍNH NHANH ---
    st.sidebar.markdown("---")
    st.sidebar.subheader("🛠️ Kiểm tra tính Độc lập")
    pa = st.sidebar.number_input("P(A)", 0.0, 1.0, 0.5)
    pb = st.sidebar.number_input("P(B)", 0.0, 1.0, 0.4)
    pab = st.sidebar.number_input("P(A ∩ B)", 0.0, 1.0, 0.2)

    if st.sidebar.button("Kiểm tra"):
        if abs(pab - (pa * pb)) < 1e-9:
            st.sidebar.success("A và B Độc lập!")
        else:
            st.sidebar.error("A và B Phụ thuộc!")
            st.sidebar.write(f"P(A|B) thực tế = {pab / pb:.4f}")

    # --- PHẦN 5: ỨNG DỤNG TRONG Y KHOA ---
    st.divider()
    st.subheader("3. Ứng dụng trong Chẩn đoán Y khoa")

    st.write("""
    Trong y khoa, các bác sĩ thường phải đối mặt với các sai lầm trong xét nghiệm. Đây là minh chứng rõ nhất cho xác suất có điều kiện:
    """)

    with st.expander("🔬 Các loại sai lầm trong xét nghiệm"):
        st.markdown("""
        Dựa trên nguyên lý xác suất, chúng ta có hai tình huống sai lầm cơ bản:
        - **Sai lầm loại I (Dương tính giả):** Người không có bệnh nhưng kết quả xét nghiệm lại kết luận là có bệnh (yêu cầu nhập viện).
        - **Sai lầm loại II (Âm tính giả):** Người thực sự có bệnh nhưng kết quả xét nghiệm lại kết luận là bình thường.
        """)
        st.info(
            "💡 Việc xem xét sai lầm nào quan trọng hơn sẽ giúp bác sĩ đưa ra quyết định lâm sàng phù hợp.")

    # --- VÍ DỤ TỰ ĐỘNG HÓA ---
    st.subheader("🧮 Máy tính xác suất chẩn đoán")
    st.write("Hãy thử nhập các thông số sau để thấy sự 'nghịch lý' của xác suất:")

    col_y1, col_y2, col_y3 = st.columns(3)
    prevalence = col_y1.number_input("Tỉ lệ mắc bệnh trong cộng đồng (P(D))", 0.001, 0.5, 0.01, format="%.3f")
    sensitivity = col_y2.number_input("Độ nhạy - P(T+|D)", 0.5, 1.0, 0.99)
    specificity = col_y3.number_input("Độ đặc hiệu - P(T-|no D)", 0.5, 1.0, 0.95)

    # Tính toán theo công thức Bayes (sẽ học kỹ ở bài 3, nhưng ứng dụng ở đây)
    # P(T+) = P(T+|D)P(D) + P(T+|no D)P(no D)
    p_pos_if_no_disease = 1 - specificity
    p_test_positive = (sensitivity * prevalence) + (p_pos_if_no_disease * (1 - prevalence))

    # P(D|T+) = P(T+|D)P(D) / P(T+)
    p_disease_given_pos = (sensitivity * prevalence) / p_test_positive

    st.markdown(f"**Kết quả phân tích:**")
    if st.button("Phân tích kết quả dương tính"):
        st.warning(
            f"Nếu một người có kết quả **Dương tính**, xác suất thực sự họ có bệnh chỉ là: **{p_disease_given_pos * 100:.2f}%**")

        with st.expander("Tại sao con số này lại thấp?"):
            st.write(f"""
            Mặc dù xét nghiệm có độ nhạy rất cao ({sensitivity * 100}%), nhưng vì căn bệnh này hiếm ({prevalence * 100}% dân số), 
            số người **khỏe mạnh nhưng bị dương tính giả** vẫn áp đảo số người thực sự mắc bệnh.

            Đây là lý do tại sao trong y khoa, khi có kết quả dương tính với bệnh hiếm, bác sĩ luôn yêu cầu **xét nghiệm lại lần 2**.
            """)

    # Ví dụ minh họa từ tài liệu
    st.info(
        "📌 **Ghi chú từ bài giảng:** Trong thực tế, bác sĩ phải cân nhắc sai lầm nào gây tổn thất lớn hơn (ví dụ: bỏ lót người bệnh nặng) để điều chỉnh mức ý nghĩa chẩn đoán.")