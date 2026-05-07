import streamlit as st
import math


def run():
    st.header("Bài 1: Sự kiện ngẫu nhiên và Xác suất")
    st.markdown("---")

    # --- PHẦN 1: GIẢI TÍCH TỔ HỢP ---
    st.subheader("1. Sự kiện ngẫu nhiên và Giải tích tổ hợp")

    with st.expander("📝 Lý thuyết Giải tích tổ hợp"):
        st.write("Trước khi tính xác suất, ta cần nắm vững các cách đếm mẫu:")
        st.markdown("""
        - **Hoán vị ($P_n$):** Sắp xếp $n$ phần tử theo một thứ tự.
        """)
        st.latex(r"P_n = n!")

        st.markdown("- **Chỉnh hợp ($A_n^k$):** Chọn $k$ phần tử từ $n$ phần tử và **có sắp xếp** thứ tự.")
        st.latex(r"A_n^k = \frac{n!}{(n-k)!}")

        st.markdown("- **Tổ hợp ($C_n^k$):** Chọn $k$ phần tử từ $n$ phần tử và **không quan tâm** thứ tự.")
        st.latex(r"C_n^k = \frac{n!}{k!(n-k)!}")

        st.info(
            "💡 **Mẹo:** Nếu bài toán chọn người vào các chức vụ khác nhau (Trưởng phòng, thư ký) -> dùng Chỉnh hợp. Nếu chỉ chọn một nhóm đi chơi -> dùng Tổ hợp.")

    # --- PHẦN 2: SỰ KIỆN NGẪU NHIÊN ---
    with st.expander("🔍 Sự kiện ngẫu nhiên (Biến cố)"):
        st.write("""
        - **Phép thử:** Một hành động mà kết quả không đoán trước được (Gieo xúc xắc, tung đồng xu).
        - **Không gian mẫu ($\\Omega$):** Tập hợp tất cả các kết quả có thể xảy ra.
        - **Biến cố (Event):** Một tập con của không gian mẫu.
        """)

        st.markdown("**Phân loại biến cố:**")
        st.write("- **Biến cố chắc chắn ($\\Omega$):** Luôn luôn xảy ra.")
        st.write("- **Biến cố không thể ($\\varnothing$):** Không bao giờ xảy ra.")
        st.write("- **Biến cố đối ($\\overline{A}$):** Xảy ra khi $A$ không xảy ra.")

    # --- PHẦN 3: ĐỊNH NGHĨA XÁC SUẤT ---
    st.subheader("2. Định nghĩa Xác suất")

    tab1, tab2, tab3 = st.tabs(["Cổ điển", "Thống kê", "Hình học"])

    with tab1:
        st.markdown("**Định nghĩa của Laplace:**")
        st.latex(r"P(A) = \frac{m}{n}")
        st.write("- $m$: Số kết quả thuận lợi cho $A$.")
        st.write("- $n$: Tổng số kết quả đồng khả năng.")
        st.success("Ví dụ: Gieo xúc xắc 6 mặt, xác suất hiện mặt chẵn là $3/6 = 0.5$.")

    with tab2:
        st.markdown("**Định nghĩa thực nghiệm:**")
        st.write(
            "Khi số phép thử $n$ tiến ra vô cùng, tần suất xuất hiện biến cố $A$ sẽ ổn định quanh một hằng số, đó là xác suất.")
        st.latex(r"P(A) \approx \frac{k}{n} \quad (\text{với } n \text{ lớn})")

    with tab3:
        st.markdown("**Xác suất hình học:**")
        st.write("Dùng khi kết quả phép thử lấp đầy một miền hình học (độ dài, diện tích, thể tích).")
        st.latex(r"P(A) = \frac{\text{Độ đo}(g)}{\text{Độ đo}(G)}")

    # --- PHẦN 4: NGUYÊN LÝ XÁC SUẤT ---
    st.subheader("3. Nguyên lý xác suất lớn và xác suất nhỏ")

    col1, col2 = st.columns(2)
    with col1:
        st.info("**Nguyên lý xác suất nhỏ**")
        st.write("""
        Nếu một biến cố có xác suất rất bé ($\\approx 0$), ta có thể coi như nó **sẽ không xảy ra** trong một lần thử.
        """)
    with col2:
        st.info("**Nguyên lý xác suất lớn**")
        st.write("""
        Nếu một biến cố có xác suất rất lớn ($\\approx 1$), ta có thể coi như nó **chắc chắn xảy ra** trong một lần thử.
        """)

    # --- PHẦN 5: CÔNG CỤ TÍNH TOÁN ---
    st.divider()
    st.subheader("🛠️ Máy tính tổ hợp & Xác suất cổ điển")

    c1, c2 = st.columns(2)
    n_input = c1.number_input("Tổng số phần tử (n)", value=10, min_value=1)
    k_input = c2.number_input("Số phần tử chọn ra (k)", value=2, min_value=0, max_value=n_input)

    calc_type = st.radio("Loại tính toán:", ["Tổ hợp (C_n^k)", "Chỉnh hợp (A_n^k)", "Hoán vị (n!)"])

    if st.button("Tính toán"):
        if calc_type == "Tổ hợp (C_n^k)":
            res = math.comb(n_input, k_input)
            st.code(f"Kết quả: {res}")
        elif calc_type == "Chỉnh hợp (A_n^k)":
            res = math.perm(n_input, k_input)
            st.code(f"Kết quả: {res}")
        else:
            res = math.factorial(n_input)
            st.code(f"Kết quả: {res}")